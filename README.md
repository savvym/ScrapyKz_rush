# 爬取kz_rush网站每张kz图的Screenshots和Shortcuts图
## 关于
基于scrapy框架，爬取类似https://kz-rush.ru/en/maps/cs16/4k_hb_sofiaFTW页面的screenshots和shortcuts
## 文件介绍
- ###  item.py
```
map_title = scrapy.Field() /**地图名称**/
map_screenshots = scrapy.Field() /**screenshots名**/
ss_num = scrapy.Field() /**screenshots数量**/
map_shortcuts = scrapy.Field() /**shortcuts名**/
sc_num = scrapy.Field() /**shortcuts数量**/
screenshots = scrapy.Field() /**screenshots图片url**/
shortcuts = scrapy.Field() /**shortcuts图片url**/
img_path = scrapy.Field() /**图片分类路径**/
```
- ### pipelines.py
```
1.  def process_item(self, item, spider)
    将地图名和对应的screenshots或shortcuts数量写入screenshots.txt或shotcuts.txt
2.  class ImgPipeline(ImagesPipeline)
    处理每个页面要下载的图片及分类
```
- ### settings.py
```
开启相应模块
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
BOT_NAME = 'kz'

SPIDER_MODULES = ['kz.spiders']
NEWSPIDER_MODULE = 'kz.spiders'

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1
COOKIES_ENABLED = False

DOWNLOADER_MIDDLEWARES = {
    'kz.middlewares.KzDownloaderMiddleware': 1,
}

IMAGES_URLS_FIELD = "screenshots"
IMAGES_STORE = '../imgaes' 
ITEM_PIPELINES = {
    'kz.pipelines.ImgPipeline':1,
    'kz.pipelines.KzPipeline': 2,
}

```
- ### kz.py(爬虫文件)
1. 通过txt文件导入url
2. 对每个页面通过selector对所需内容进行选取，其中xpath路径可以通过网页右键检查之后，对相应位置复制xpath路径即可。