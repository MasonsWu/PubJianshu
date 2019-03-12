#  _*_ coding:utf-8 _*_
#  QQ: 2457179751
__author__ = 'xmduke'

from selenium.webdriver.support.wait import WebDriverWait


# 使用QQ授权登录，使用前提是QQ客户端登录在线

def LoginQQ(driver):
    #获取多有句柄
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])

    #print("QQ 授权标题是: ",driver.title)

    # 切换到iframe
    iframe = WebDriverWait(driver,5).until(lambda d:d.find_element_by_id("ptlogin_iframe"))
    driver.switch_to_frame(iframe)

    # 点击头像进行授权登录
    login = WebDriverWait(driver,5).until(lambda d:d.find_element_by_xpath(".//*[@id='qlogin_list']/a[1]")).click()