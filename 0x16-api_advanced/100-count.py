#!/usr/bin/python3
"""
Module that queries the Reddit API
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    A function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces).

    Results are printed in descending order, by the count, and if
    the count is the same for separate keywords, they are sorted
    alphabetically (ascending, from A to Z). Words with no matches
    are skipped and not printed. Words are printed in lowercase.

    Results are based on the number of times a keyword appears, not titles
    it appears in. java java java counts as 3 separate occurrences of java.

    'java.' or 'java!' or 'java_' do not count as 'java'.

    If an invalid subreddit is given, the function prints nothing.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word.lower()) is None:
                    instances[word.lower()] = times
                else:
                    instances[word.lower()] += times

    if after is None:
        if len(instances) == 0:
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
