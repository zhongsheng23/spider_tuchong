#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 网页解析器
from bs4 import BeautifulSoup
import urlparse
    
class HtmlParser(object):
    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find('div',class_="pages").find_all('a')
        for link in links:
            new_full_url = urlparse.urljoin(page_url,link['href'])
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self,page_url,soup):
        res_data = []
        img_nodes = soup.find_all('figure',class_="main-collage")
        for img_node in img_nodes:
            node = img_node.find('img')
            res_data.append(node['src'])
        return res_data


    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data