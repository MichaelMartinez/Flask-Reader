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
1. Add database layer
2. Form to insert/delete feeds with validation
3. Add granularity to check individual feeds and more

## Whats installed

* flask-bootstrap
* flask-moment
* flask-mail
* flask-sqlalchemy
* flask-migrate
* flask-script
* feedparser
* pytz



