#  _*_ coding:utf-8 _*_
#  QQ: 2457179751
__author__ = 'xmduke'

import linecache,re
from jianshu import jianshu
from jianshu.csv import random_r_title,random_r_content
import os

class Main(object):
    def __init__(self):
    	
        self.title = random_r_title.r_title.getrandomline("D:\\csv\\title.csv")
        self.content = random_r_content.r_content.getrandomline("D:\\csv\\content.csv")
        self.category = ''
        # 简书系统分类，设置个默认值
        self.jian_sys_category = '日记本'
        self.article_category = '原创'
        self.blog_category = '编程语言'


    # def read_file(self,markdown_file):
    #     self.title = linecache.getline(markdown_file,2).split('title: ')[1].strip('\n')
    #     with open(markdown_file,'r',encoding='UTF-8') as f:
    #         self.content = f.read().split('-->\n')[1]
    #         # 重置文件指针偏移量
    #         f.seek(0)
    #         for line in f.readlines():
    #             if re.search('self_category: ',line) is not None:
    #                 self.category = line.split('self_category: ')[1].strip('\n')
    #             elif re.search('self_tags: ',line) is not None:
    #                 self.tags = line.split('self_tags: ')[1].strip('\n')
    #             elif re.search('jianshu_sys_category: ',line) is not None:
    #                 self.jian_sys_category = line.split('jianshu_sys_category: ')[1].strip('\n')
    #             elif re.search('article_category: ',line) is not None:
    #                 self.article_category = line.split('article_category: ')[1].strip('\n')
    #             elif re.search('blog_category: ',line) is not None:
    #                 self.blog_categroy = line.split('blog_category: ')[1].strip('\n')




if __name__ == "__main__":
    #md_file = 'auto.md'
    #print("Markdown File is ",md_file)

    timeout = 10
    main = Main()
    Jian_s = jianshu.JianShu()
    Jian_s.post(main,timeout,self_timeout=3)











