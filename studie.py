from scraper.twitter_scraper import Twitter_Scraper
from sanitize_filename import sanitize
from dotenv import load_dotenv
import os

load_dotenv()

USER_UNAME = os.getenv("TWITTER_USERNAME")
USER_PASSWORD = os.getenv("TWITTER_PASSWORD")
USER_MAIL = os.getenv("TWITTER_MAIL")

suchstrings = [
    '(js OR j%26s OR "j%26s") gmbh automotive'
]

startdate = "2020-01-01"

def run():
    scraper = Twitter_Scraper(USER_MAIL, USER_UNAME, USER_PASSWORD)
    scraper.login()
    for suchstring in suchstrings:
        suchstring_with_date = f"{suchstring} since:{startdate} -is:quote -is:retweet -is:reply -filter:retweets"
        scraper.scrape_tweets(
            max_tweets=500,
            no_tweets_limit=True,
            scrape_username=None,
            scrape_hashtag=None,
            scrape_query=suchstring_with_date,
            scrape_latest=True,
            scrape_top=False            
        )
        scraper.save_to_csv(f"tweets_{sanitize(suchstring.replace(' ', '_').lower())}")
        
    if not scraper.interrupted:
        scraper.driver.close()
        
run()