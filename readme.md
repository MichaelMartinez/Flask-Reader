#FlaRSSk - YAFRR

Yet Another Flask RSS Reader app

## Work in Progress

I am going to incrementally build this software. Its a personal project to replicate something I've missed for a while;
Google Reader. I know there are other solutions that are miles ahead of this in terms of features.

The point of programming (for me, at this point) is to scratch some itches, and to "always be learning."

## To run

1. Fill in `rss_feed.py` with the blogs/rss feeds you want to track
2. Adjust the time zone to your time zone in `rss_feed.py`
3. Run the app with: `python flask_reader.py runserver`
4. The main index page will poll the feeds and pull down the posts of the day.

## Roadmap
1. Figure out how to solve the massively IO bound nature of this beast...
- At launch, the fetch/parse cycle takes about 4 minutes before anything is shown
- This program needs to fetch the RSS feeds asynchronously/concurrently or through a task queue.
- That means I have a choice to make: Twisted, Celery, asyncio, multiprocessing, Gevent
- Perhaps I could prefetch the feeds with a GO program...
- Perhaps I could rewrite this in Go or Java...
- Situation is stalled.

2. Add database layer
3. Form to insert/delete feeds with validation
4. Add granularity to check individual feeds and more
5. Add API for voice controlled application to fetch feeds.

## Whats installed

* flask-bootstrap
* flask-moment
* flask-mail
* flask-sqlalchemy
* flask-migrate
* flask-script
* feedparser
* pytz

## License

&copy; 2015-2016 Michael Martinez

This repository is licensed under the MIT license. See `LICENSE` for
details.
