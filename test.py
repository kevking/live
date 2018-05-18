from scrapy import cmdline
import os
from datetime import datetime

dir_name = datetime.now().strftime("%Y%m%d_%H%M%S") 
os.rename('database',dir_name)
os.makedirs('database')
