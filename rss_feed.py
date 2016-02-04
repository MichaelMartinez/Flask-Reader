#import gevent
#from gevent import monkey; monkey.patch_all()
import time
from datetime import datetime, timedelta

import feedparser as fp
import pytz


subscriptions = [
    'http://feedpress.me/512pixels',
    'http://www.leancrew.com/all-this/feed/',
    'http://ihnatko.com/feed/',
    'http://blog.ashleynh.me/feed',
    'http://www.betalogue.com/feed/',
    'http://bitsplitting.org/feed/',
    'http://feedpress.me/jxpx777',
    'http://kieranhealy.org/blog/index.xml',
    'http://blueplaid.net/news?format=rss',
    'http://brett.trpstra.net/brettterpstra',
    'http://feeds.feedburner.com/NerdGap',
    'http://www.libertypages.com/clarktech/?feed=rss2',
    'http://feeds.feedburner.com/CommonplaceCartography',
    'http://kk.org/cooltools/feed',
    'http://danstan.com/blog/imHotep/files/page0.xml',
    'http://daringfireball.net/feeds/main',
    'http://david-smith.org/atom.xml',
    'http://feeds.feedburner.com/drbunsenblog',
    'http://stratechery.com/feed/',
    'http://www.gnuplotting.org/feed/',
    'http://feeds.feedburner.com/jblanton',
    'http://feeds.feedburner.com/IgnoreTheCode',
    'http://indiestack.com/feed/',
    'http://feedpress.me/inessential',
    'http://feeds.feedburner.com/JamesFallows',
    'http://feeds.feedburner.com/theendeavour',
    'http://feed.katiefloyd.me/',
    'http://www.caseyliss.com/rss',
    'http://www.macdrifter.com/feeds/all.atom.xml',
    'http://mackenab.com/feed',
    'http://hints.macworld.com/backend/osxhints.rss',
    'http://macsparky.com/blog?format=rss',
    'http://www.macstories.net/feed/',
    'http://www.marco.org/rss',
    'http://merrillmarkoe.com/feed',
    'http://mjtsai.com/blog/feed/',
    'http://feeds.feedburner.com/mygeekdaddy',
    'http://nathangrigg.net/feed.rss',
    'http://onethingwell.org/rss',
    'http://schmeiser.typepad.com/penny_wiseacre/rss.xml',
    'http://feeds.feedburner.com/PracticallyEfficient',
    'http://robjwells.com/rss',
    'http://www.red-sweater.com/blog/feed/',
    'http://feedpress.me/candlerblog',
    'http://inversesquare.wordpress.com/feed/',
    'http://high90.com/feed',
    'http://joe-steel.com/feed',
    'http://feeds.veritrope.com/',
    'http://xkcd.com/atom.xml',
    'http://doingthatwrong.com/?format=rss',
    'http://www.pydanny.com/feeds/all.atom.xml',
    'http://www.blog.pythonlibrary.org/feed/',
    'https://realpython.com/atom.xml',
    'http://www.snarky.ca/feed',
    'http://lucumr.pocoo.org/feed.atom',
    'http://planetpython.org/rss20.xml',
    'https://hackaday.com/blog/feed/',
    'http://planet.ubuntu.com/rss20.xml',
    'http://www.ianww.com/blog/rss/']

# Date and time setup. I want only posts from "today,"
# where the day lasts until 2 AM.
utc = pytz.utc
homeTZ = pytz.timezone('US/Arizona')
dt = datetime.now(homeTZ)
if dt.hour < 2:
    dt = dt - timedelta(hours=24)
start = dt.replace(hour=0, minute=0, second=0, microsecond=0)
start = start.astimezone(utc)


# Collect all of today's posts and put them in a list of tuples.
posts = []


def get_posts():
    for s in subscriptions:
        f = fp.parse(s)
        try:
            blog = f['feed']['title']
        except KeyError:
            continue
        for e in f['entries']:
            try:
                when = e['published_parsed']
            except KeyError:
                when = e['updated_parsed']
            when = utc.localize(datetime.fromtimestamp(time.mktime(when)))
            if when > start:
                title = e['title']
                try:
                    body = e['content'][0]['value']
                except KeyError:
                    body = e['summary']
                link = e['link']
                posts.append((when, blog, title, link, body))

                # Sort the posts in reverse chronological order.
                posts.sort()
                posts.reverse()
    return posts

# def get_post_gv(s):
#     f = fp.parse(s)
#     try:
#         blog = f['feed']['title']
#     except KeyError:
#         blog = "blog"
#     for e in f['entries']:
#         try:
#             when = e['published_parsed']
#         except KeyError:
#             when = e['updated_parsed']
#         when = utc.localize(datetime.fromtimestamp(time.mktime(when)))
#         if when > start:
#             title = e['title']
#             try:
#                 body = e['content'][0]['value']
#             except KeyError:
#                 body = e['summary']
#             link = e['link']
#             posts.append((when, blog, title, link, body))
#
#             # Sort the posts in reverse chronological order.
#             posts.sort()
#             posts.reverse()
#     return posts

# def get_posts_call():
#     jobs = [gevent.spawn(get_post_gv, s) for s in subscriptions]
#     gevent.wait(jobs)

def get_single_blog(feed):
    '''Feed the all_posts path an individual blog/feed to parse and display from inside the template'''
    the_feed = fp.parse(feed)
    single_blog_posts = the_feed['entries']
    return single_blog_posts


def get_subscriptions():
    '''simple method to pass the subscriptions (will improve here)'''
    s = subscriptions
    return s


# TODO: pick the most efficient option: generate html in template or in code
def get_sorted_posts(sorted_posts):
    '''
    This method returns generated html with the days posts. Contrast to the get_single_blog method that
    generates the html inside the template.'''
    listTemplate = ''' <section>
                <h2 class="page-header no-margin-top"><a href="{3}">{2}</a></h2>
                <p>{4}</p>
            <div class="panel-footer">
                        <div class="row">
                            <div class="col-md-12">
                                <i class="fa fa-clock-o"></i> {0} <i class="fa fa-user"> </i> <a href="{3}">{1}</a>.
                            </div>
                        </div>
                    </div>
            </section>'''
    litems = []
    for p in sorted_posts:
        q = [x for x in p[1:]]
        timestamp = p[0].astimezone(homeTZ)
        q.insert(0, timestamp.strftime('%b %d, %Y %I:%M %p'))
        litems.append(listTemplate.format(*q))
    myitems = '</br>'.join(litems)
    return myitems



