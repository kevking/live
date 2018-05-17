from scrapy import cmdline
import os

os.system("scrapy crawl douyu_overwatch -o database/douyu_overwatch.json")
os.system("scrapy crawl douyu_LOL -o database/douyu_LOL.json")
os.system("scrapy crawl douyu_jdqs -o database/douyu_jdqs.json")
os.system("scrapy crawl douyu_jdqscjzc -o database/douyu_jdqscjzc.json")
os.system("scrapy crawl douyu_wzry -o database/douyu_wzry.json")
os.system("scrapy crawl douyu_TVgame -o database/douyu_TVgame.json")
os.system("scrapy crawl douyu_blzy -o database/douyu_blzy.json")
