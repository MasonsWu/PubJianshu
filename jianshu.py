#  _*_ coding:utf-8 _*_
#  QQ: 2457179751
__author__ = 'xmduke'
from selenium import webdriver
import time
from PubJianshu.jianshu import authorize
from selenium.webdriver.support.wait import WebDriverWait
from PubJianshu.jianshu import main






class JianShu(object):
    @classmethod
    def post(self,main,timeout,self_timeout):
        driver = webdriver.Chrome()
        driver.get("https://www.jianshu.com/sign_in")

        # 窗口最大化
        driver.maximize_window()

        # 使用QQ授权登录
        driver.find_element_by_xpath(".//*[@id='qq']/i").click()
        time.sleep(6)
        driver.close()
        authorize.LoginQQ(driver)
        time.sleep(3)

        # 点击发布文章

        write_blog = WebDriverWait(driver, 10).until(
            lambda d: d.find_element_by_xpath("html/body/nav/div/a[2]")).click()
        driver.close()

        # 获取所有句柄
        window_handles = driver.window_handles
        # driver.switch_to_window(window_handles[-1])
        driver.switch_to.window(window_handles[-1])

        # 点击指定分类

        classify = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_class_name("_3DM7w"))

        html = classify.get_attribute('innerHTML')

        if main.category in html:
            classify.click()
        else:
            # 如果分类不存在，还可以直接新建分类
            pass

        # 点击' 新建文章'
        time.sleep(self_timeout)
        new_article = WebDriverWait(driver, 10).until(
            lambda d: d.find_element_by_css_selector(".fa.fa-plus-circle")).click()

        # 填写标题, 内容
        time.sleep(self_timeout)
        title = driver.find_element_by_class_name("_24i7u")
        title.clear()
        # title.send_keys("前端开发需要哪些技能？")
        title.send_keys(main.title)
        content = driver.find_element_by_id("arthur-editor")
        content.clear()
        # content.send_keys("厦门前端开发待遇如何,10k有不")
        content.send_keys(main.content)

        time.sleep(10)
        # 保存草稿
        # driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div[2]/div/div/div/div/ul/li[9]/a").click()

        # 发布文章
        driver.find_element_by_xpath(".//*[@id='root']/div/div[2]/div[2]/div/div/div/div/ul/li[1]/a").click()

        time.sleep(10)










