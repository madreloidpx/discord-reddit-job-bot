import requests
import json
import redditpost

class PostGetter:
    def __init__(self):
        self.__posts__ = None
        f = open('subreddits_search.json')
        data = json.load(f)
        self.subreddits = data["subreddits"]
        self.tags = data["tags"]
        f.close()
    def __fetchPosts__(self):
        allPosts = None
        for key in self.subreddits:
            comm = "https://api.pushshift.io/reddit/search/submission/?subreddit="+key+"&sort=desc&sort_type=created_utc&size=50"
            response = requests.get(comm)
            if allPosts == None:
                allPosts = response.json()["data"]
            else:
                allPosts = allPosts + response.json()["data"]
        # print("Fetched posts:", len(allPosts))
        self.__posts__ = allPosts
    def __filterPosts__(self):
        filtered = []
        for post in self.__posts__:
            rp = redditpost.RedditPost(post.get("id"), post.get("full_link"), post.get("subreddit"), post.get("title"), post.get("link_flair_text"))
            flaircheck = False
            titleTagCheck = False
            for flair in self.subreddits[rp.subreddit]["link_flair_text"]:
                if rp.flair == flair:
                    flaircheck = True
                    break
            for titletag in self.subreddits[rp.subreddit]["title_tags"]:
                if rp.checkContains(titletag):
                    titleTagCheck = True
                    break
            if flaircheck or titleTagCheck:
                for tag in self.tags:
                    if rp.checkContains(tag):
                        filtered.append(rp)
                        break
        self.__posts__ = filtered
    def fetchNewPosts(self):
        self.__fetchPosts__()
        self.__filterPosts__()
        strpost = ""
        for post in self.__posts__:
            strpost = strpost + post.printPost() + "\n"
        return strpost