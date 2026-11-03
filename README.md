# alu-scripting

Python functions that ask the Reddit API for information about a subreddit.
Everything is in the `api_advanced` folder.

## What each file does

- `0-subs.py` - how many subscribers a subreddit has
- `1-top_ten.py` - prints the titles of the first 10 hot posts
- `2-recurse.py` - gets the titles of all the hot posts, using recursion
- `3-count.py` - counts how many times given words show up in those titles

## How to run them

Each file holds one function, so you call it from a small main script:

```
$ cat 0-main.py
#!/usr/bin/python3
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    print("{:d}".format(number_of_subscribers(sys.argv[1])))
```

```
$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0
```

## Notes

Reddit sends a redirect to its search page when a subreddit does not exist,
so the requests are made with redirects turned off. That way a bad subreddit
comes back as a 302 instead of a 200 full of search results.

Reddit also needs a User-Agent of your own, otherwise it answers with
Too Many Requests.
