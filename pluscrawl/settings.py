# Scrapy settings for pluscrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'pspider'

SPIDER_MODULES = ['pluscrawl.spiders']
NEWSPIDER_MODULE = 'pluscrawl.spiders'
ITEM_PIPELINES = ['pluscrawl.pipelines.PluscrawlPipeline',]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pluscrawl (+http://www.yourdomain.com)'
import MySQLdb
#USER_AGENT = 'myspace (+http://www.yourdomain.com)'
# in
MONGODB_SERVER = '10.1.1.111'
#out
#MONGODB_SERVER = ''
MONGODB_PORT = 12345
# MONGODB_SERVER = 'localhost'
# MONGODB_PORT = 27017
MONGODB_DB = 'lastfm'
MONGODB_COLLECTION = 'profiles'
MONGODB_UNIQ_KEY = '_id'
##########

# Set your own download folder
# DOWNLOAD_FILE_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "download_file")

USER_AGENT = "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)"
AUTOTHROTTLE_ENABLED= True
#database connectivity

# conn=db = MySQLdb.connect(host="localhost",user="root",passwd="passme", db="cubator")
# cursor=db.cursor()
