from dotenv import load_dotenv
from datetime import datetime, timezone
from config import Config
import requests, os, json, re
import urllib


def create_bsky_connection(handle, app_password):
    print(f"Logging in as {handle}...")

    resp = requests.post(
        "https://bsky.social/xrpc/com.atproto.server.createSession",
        json={"identifier": handle, "password": app_password},
    )
    resp.raise_for_status()
    session = resp.json()
    return session


def parse_url(text: str):
    # code snippet from: https://docs.bsky.app/docs/advanced-guides/posts#mentions-and-links
    # partial/naive URL regex based on: https://stackoverflow.com/a/3809435
    # tweaked to disallow some training punctuation
    url_regex = rb"[$|\W](https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*[-a-zA-Z0-9@%_\+~#//=])?)"
    text_bytes = text.encode("UTF-8")
    m = re.search(url_regex, text_bytes)
    return {
        "start": m.start(1),
        "end": m.end(1),
        "url": m.group(1).decode("UTF-8"),
    }


def create_bsky_post(session, article_title, article_url):
    if session is None:
        return
    print("Posting to bluesky..")

    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    url_len = len(article_url)
    # link length is not counted towards used characters over 31 chars
    if url_len > 31:
        url_len = 31

    if len(article_title) > (299 - url_len):
        article_title = article_title[:296 - url_len] + "..."

    post_content = article_title + " " + article_url
    parsed_url = parse_url(post_content)

    # Required fields that each post must include
    post = {
        "$type": "app.bsky.feed.post",
        "text": article_title + " " + article_url,
        "createdAt": now,
        "langs": ["cs", "sk"],
        "facets": [
            {
                "index": {
                    "byteStart": parsed_url["start"],
                    "byteEnd": parsed_url["end"],
                },
                "features": [
                    {
                        "$type": "app.bsky.richtext.facet#link",
                        "uri": article_url
                    }
                ]
            }
        ]
    }

    requests.post(
        "https://bsky.social/xrpc/com.atproto.repo.createRecord",
        headers={"Authorization": "Bearer " + session["accessJwt"]},
        json={
            "repo": session["did"],
            "collection": "app.bsky.feed.post",
            "record": post,
        },
    )


def create_threads_media_container(text, user_id, headers):
    url = f'https://graph.threads.net/v1.0/{user_id}/threads?media_type=TEXT&text={text}'
    response = requests.post(url, headers=headers)
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


def create_threads_post(text, user_id, api_key):
    # Headers for authentication
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    escaped_text = escape_text_for_url(text)
    media_container_id = create_threads_media_container(escaped_text, user_id, headers)

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

    if config.BLUESKY_ENABLED:
        bsky_connection = create_bsky_connection(config.BLUESKY_HANDLE, config.BLUESKY_APP_PASSWORD)
    else:
        bsky_connection = None

    for article in articles:
        article_url = article['link']
        article_title = article['title']
        post_content_concatenated = f'{article.title} {article.url}'
        print(f"Posting article to social media... {article_url}")

        if bsky_connection:
            create_bsky_post(bsky_connection, article_title, article_url)

        if config.THREADS_ENABLED:
            create_threads_post(post_content_concatenated, config.THREADS_USER_ID, config.THREADS_API_KEY)

        if config.MASTODON_ENABLED:
            create_mastodon_status(post_content_concatenated, config.MASTODON_URL, config.MASTODON_ACCESS_TOKEN)
