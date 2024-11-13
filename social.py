from dotenv import load_dotenv
from datetime import datetime, timezone
from config import Config
import requests, os, json, re
import urllib
from urllib.parse import urlparse


# get second level and top level domain from url
def get_sld_tld(url):
    if not url.startswith("http"):
        url = "http://" + url
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    domain_parts = domain.split('.')
    if len(domain_parts) >= 2:
        sld = domain_parts[-2]
        tld = domain_parts[-1]
        return f"{sld}.{tld}"
    else:
        return None


class BskyPostData:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.hostname = get_sld_tld(url)

    def get_bytes_to_hostname_start(self):
        return len(self.title.encode("UTF-8")) + 2  # +2 is for space and parentheses

    def get_bytes_to_hostname_end(self):
        return self.get_bytes_to_hostname_start() + len(self.hostname.encode("UTF-8"))

    def get_post_string(self):
        return f"{self.title} ({self.hostname})"

    def get_length(self):
        return len(self.get_post_string())


class BskyPostPublisher:
    def __init__(self):
        self.session = None

    def connect(self, handle, app_password):
        print(f"Logging in as {handle}...")

        resp = requests.post(
            "https://bsky.social/xrpc/com.atproto.server.createSession",
            json={"identifier": handle, "password": app_password},
        )
        resp.raise_for_status()
        session = resp.json()
        self.session = session

    def publish_bsky_post(self, post):
        if not self.session:
            print(post)
            return
        requests.post(
            "https://bsky.social/xrpc/com.atproto.repo.createRecord",
            headers={"Authorization": "Bearer " + self.session["accessJwt"]},
            json={
                "repo": self.session["did"],
                "collection": "app.bsky.feed.post",
                "record": post,
            },
        )


class BskyPostJoiner:
    def __init__(self):
        self.posts = []
        self.total_length = 0

    def add_post(self, post: BskyPostData, publisher: BskyPostPublisher):
        BSKY_MAX_LENGTH = 300
        new_length = post.get_length()
        if (self.total_length + new_length + 1) > BSKY_MAX_LENGTH:
            # newly added post cannot fit into currently crafted post, publish all present posts and reset
            self.create_joined_posts_and_publish(publisher)
            self.posts = []
            self.total_length = 0

        self.posts.append(post)
        self.total_length += post.get_length()

    def create_joined_posts_and_publish(self, publisher: BskyPostPublisher):
        if len(self.posts) == 0:
            return
        post = self.create_post_from_articles()
        if not publisher:
            print(post)
            return
        publisher.publish_bsky_post(post)

    def create_post_from_articles(self):
        if len(self.posts) == 0:
            return None

        now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        post_text = "\n".join([post.get_post_string() for post in self.posts])

        url_facets = []
        last_byte = 0

        for post in self.posts:
            url_facets.append({
                "index": {
                    "byteStart": last_byte + post.get_bytes_to_hostname_start(),
                    "byteEnd": last_byte + post.get_bytes_to_hostname_end(),
                },
                "features": [
                    {
                        "$type": "app.bsky.richtext.facet#link",
                        "uri": post.url,
                    }
                ]
            })
            last_byte += post.get_bytes_to_hostname_end() + 2  # add 2 for closing parentheses and space

        post = {
            "$type": "app.bsky.feed.post",
            "text": post_text,
            "createdAt": now,
            "langs": ["cs", "sk"],
            "facets": url_facets
        }

        return post

    def get_posts(self):
        return self.posts

    def get_total_length(self):
        return self.total_length


def create_threads_media_container(text, article_link, user_id, headers):
    url = f'https://graph.threads.net/v1.0/{user_id}/threads?media_type=TEXT&text={text}'
    response = requests.post(url, headers=headers, data=f"link_attachment={article_link}")
    if response.status_code == 200 and 'id' in response.json():
        media_container_id = response.json()['id']
        return media_container_id

    return None


def publish_threads_media_container(media_container_id, user_id, headers):
    url = f'https://graph.threads.net/v1.0/{user_id}/threads_publish?creation_id={media_container_id}'
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        return True

    return False


def create_threads_post(text, article_url, user_id, api_key):
    # Headers for authentication
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    escaped_text = escape_text_for_url(text)
    media_container_id = create_threads_media_container(escaped_text, article_url, user_id, headers)

    if media_container_id is None:
        print('Failed to create media container')
        return

    if publish_threads_media_container(media_container_id, user_id, headers):
        print('Thread published successfully')


def escape_text_for_url(text):
    return urllib.parse.quote(text, safe='')


def create_mastodon_status(status_text, url, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    data = {
        "status": status_text,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("Mastodon status posted successfully")


def publish_articles_to_social_media(articles):
    if len(articles) == 0:
        return

    config = Config()

    bsky_post_joiner = None
    bsky_publisher = None
    if config.BLUESKY_ENABLED:
        bsky_publisher = BskyPostPublisher()
        bsky_publisher.connect(config.BLUESKY_HANDLE, config.BLUESKY_APP_PASSWORD)
        bsky_post_joiner = BskyPostJoiner()

    for article in articles:
        article_url = article['link']
        article_title = article['title']
        post_content_concatenated = f'{article_title} {article_url}'
        print(f"Posting article to social media... {article_url}")

        if bsky_post_joiner:
            bsky_post_joiner.add_post(BskyPostData(article_title, article_url), publisher=bsky_publisher)

        if config.THREADS_ENABLED:
            create_threads_post(post_content_concatenated, article_url, config.THREADS_USER_ID, config.THREADS_API_KEY)

        if config.MASTODON_ENABLED:
            create_mastodon_status(post_content_concatenated, config.MASTODON_URL, config.MASTODON_ACCESS_TOKEN)

    if bsky_post_joiner:
        bsky_post_joiner.create_joined_posts_and_publish(publisher=bsky_publisher)
