#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 爬虫总调度程序
import url_manager,html_downloader,html_parser,html_outputer
from bs4 import BeautifulSoup
import urllib2

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self,root_url):
        # 解析root_url获取每个题材的的标题和url
        response = urllib2.urlopen(root_url)
        html_cont = response.read()
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        title_nodes = soup.find_all('li',class_="tag-square-base")
        for title_node in title_nodes:
            title_url = title_node.find('a')
            # 爬取单个题材
            self.urls.add_new_url(title_url['href'])
            while self.urls.has_new_url():
                try:
                    new_url = self.urls.get_new_url()
                    print '%s url:%s '% (title_url['title'],new_url)
                    html_cont = self.downloader.download(new_url)
                    new_urls,new_data = self.parser.parse(new_url,html_cont)
                    self.urls.add_new_urls(new_urls)
                    self.outputer.collect_data(new_data)

                except:
                    print 'craw failed'

            self.outputer.output_html(title_url['title'])  

if __name__ == '__main__':
    root_url = "https://tuchong.com/explore/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)