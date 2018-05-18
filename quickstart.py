from scrapy import cmdline
import os
from datetime import datetime

dir_name = datetime.now().strftime("%Y%m%d_%H%M%S") 
os.rename('database',dir_name)
os.makedirs('database')
os.system("scrapy crawl douyu_overwatch -o database/douyu_overwatch.json")
os.system("scrapy crawl douyu_LOL -o database/douyu_LOL.json")
os.system("scrapy crawl douyu_jdqs -o database/douyu_jdqs.json")
os.system("scrapy crawl douyu_jdqscjzc -o database/douyu_jdqscjzc.json")
os.system("scrapy crawl douyu_wzry -o database/douyu_wzry.json")
os.system("scrapy crawl douyu_TVgame -o database/douyu_TVgame.json")
os.system("scrapy crawl douyu_blzy -o database/douyu_blzy.json")
os.system("scrapy crawl panda_overwatch -o database/panda_overwatch.json")
os.system("scrapy crawl panda_LOL -o database/panda_LOL.json")
os.system("scrapy crawl panda_jdqs -o database/panda_jdqs.json")
os.system("scrapy crawl panda_jdqscjzc -o database/panda_jdqscjzc.json")
os.system("scrapy crawl panda_wzry -o database/panda_wzry.json")
os.system("scrapy crawl panda_TVgame -o database/panda_TVgame.json")
os.system("scrapy crawl panda_blzy -o database/panda_blzy.json")
os.system("scrapy crawl yy_jdqscjzc -o database/yy_jdqscjzc.json")
os.system("scrapy crawl yy_wzry -o database/yy_wzry.json")
os.system("scrapy crawl yy_jdqs -o database/yy_jdqs.json")
os.system("scrapy crawl yy_lol -o database/yy_lol.json")

