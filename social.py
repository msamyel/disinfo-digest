from dotenv import load_dotenv
from datetime import datetime, timezone
import requests, os, json, re

load_dotenv()


def create_bsky_connection():
    if not os.getenv("BLUESKY_ENABLED", False):
        return None
    BLUESKY_HANDLE = os.getenv("BLUESKY_HANDLE")
    BLUESKY_APP_PASSWORD = os.getenv("BLUESKY_APP_PASSWORD")

    print(f"Logging in as {BLUESKY_HANDLE}...")

    resp = requests.post(
        "https://bsky.social/xrpc/com.atproto.server.createSession",
        json={"identifier": BLUESKY_HANDLE, "password": BLUESKY_APP_PASSWORD},
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
    #link length is not counted towards used characters over 31 chars
    if url_len > 31:
        url_len = 31

    if len(article_title) > (299-url_len):
        article_title = article_title[:296-url_len]+"..."

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