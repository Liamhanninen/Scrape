# Superheroes of Scraping: Scrapy, Splash, and Docker

This is a Scrapy file structure with settings that allow you to scrape anything you can see on a web browser AND any Javascript (JS can be particularly evasive content for basic web scraping programs).

This is simple if you're familiar with docker and scrapy. Docker here is used to automate setting-up and running a light-weight Splash server. Scrapy performs the actual scraping.

If you're not familiar with docker you have some options:

  (1) The Docker Route (recommended) (link is for Macs) https://docs.docker.com/mac/
  
  (2) The Manual Way http://splash.readthedocs.io/en/latest/install.html#ubuntu-14-04-manual-way.
  
If you're not familiar with Scrapy you really can't do this just yet :/

  (1) Scrapy Docs http://scrapy.org/doc/

#Instructions

git clone https://github.com/Liamhanninen/Scrape.git

(( In a separate terminal execute the following command to start the splash server using docker ))
  
  sudo docker run -p 8050:8050 scrapinghub/splash

pip install -r requirements.txt

((
The spider and parsing is in: 
  - scrape_project/spiders/spidername.py 
  - When you've added your specifications (this is where your Scrapy skills are used) then execute the following command
))

scrapy runspider scrape_project/spiders/spidername.py

#Notes 
You don't need to change any of these settings. I'm just highlighting the changes.

In scrape_project/settings.py I've added:

ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
  'scrapyjs.SplashMiddleware': 725,
}

SPLASH_URL = 'http://localhost:8050/'

DUPEFILTER_CLASS = 'scrapyjs.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapyjs.SplashAwareFSCacheStorage'

Thanks to Splash https://github.com/scrapy-plugins/scrapy-splash and tutorial help from https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash/
