class RssFeed:
    def __init__(self, url, save_all_articles=False, tag_to_enforce=None):
        # url to fetch the feed from
        self.url = url
        # do not filter articles if set to true
        self.save_all_articles = save_all_articles
        # use this tag for all articles, unless set to None
        self.tag_to_enforce = tag_to_enforce

