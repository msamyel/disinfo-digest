from dotenv import load_dotenv
from datetime import datetime, timezone
import requests, os, json, re


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


def connect_to_threads():
    api_key = os.getenv('THREADS_API_KEY')
    # The endpoint you want to interact with

    url = 'https://graph.threads.net/v1.0/'

    # Headers for authentication
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    # Data to send in your request
    data = {
        'title': 'New Thread',
        'body': 'This is a new thread created using the Threads API.'
    }

    # Making a POST request to create a new thread
    response = requests.post(url, headers=headers, json=data)

    print(response)
    # Checking the response
    if response.status_code == 201:
        print('Thread created successfully:', response)
    else:
        print('Failed to create thread:', response)


if __name__ == '__main__':
    load_dotenv()
    connect_to_threads()
