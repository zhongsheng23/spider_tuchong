#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 网页输出器,输出爬取的结果
import os

class HtmlOutputer(object):
    def __init__(self):
        self.urls = []
        os.mkdir('page')

    def collect_data(self,url):
        if url is None:
            return
        self.urls += url

    def output_html(self,title):
        fout = open('page/' + title+'.html','w')
        fout.write('<!doctype html> <html> <head> <meta charset="UTF-8"> <title>图虫网</title> <style> .container{-webkit-column-width:160px; -moz-column-width:160px; -webkit-column-gap:5px; -moz-column-gap:5px;} .container div{width:160px;margin:4px 0;} </style> </head> <body> <div class="container">')

        for url in self.urls:
            fout.write('<div><img src="%s"></div>' % url)

        fout.write('</div> </body> </html>')
        fout.close()
        self.urls = []
        