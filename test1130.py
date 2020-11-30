#coding=utf-8
#1.设置字符集
from selenium import webdriver
#2.导入selenium中的浏览器驱动程序
br=webdriver.Chrome()
#3.设置需要打开的浏览器
br.get("https://www.baidu.com")
#4.打开目标网页的地址
#a.通过name定位
# br.find_element_by_name("wd").send_keys("花木兰")
#b.通过class定位
# br.find_element_by_class_name("s_ipt").send_keys("兰陵王")
#c.通过tag定位
# br.find_element_by_tag_name("input").send_keys("张飞")
#d.通过link定位
# br.find_element_by_link_text("hao123").click()
#e.通过partial link定位
# br.find_element_by_partial_link_text("闻").click()
#f.通过xpath定位
# br.find_element_by_xpath("//*[@id='kw']").send_keys("川普")
#g.通过css定位
br.find_element_by_css_selector("#kw").send_keys("拜登")