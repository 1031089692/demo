# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

# 打开无头模式
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'D:\Python233\chromedriver.exe')
cookies = driver.get_cookies()
driver.get("http://www.51job.com/")
driver.implicitly_wait(20)      # 隐式等待

# 找到城市并模拟点击（多写两层路径）
button = driver.find_element_by_xpath("//div[@class='ush top_wrap']//div[@class='el on']/p\
[@class='addbut']//input[@id='work_position_input']").click()

# 选中城市弹出框（利用句柄）
h1 = driver.current_window_handle

# 定义一个空字典。
dic = {}

# 找到城市和对应的城市编号(注意这里是elements)
find_city_elements = driver.find_elements_by_xpath("//div[@id='work_position_layer']//\
div[@id='work_position_click_center_right_list_000000']//tbody/tr/td")
for element in find_city_elements:
    number = element.find_element_by_xpath("./em").get_attribute("data-value") # 城市编号
    city = element.find_element_by_xpath("./em").text # 城市
    dic.setdefault(city,number) # 添加到字典。
print(dic)

# 保存
# json.dumps序列化时默认使用ASCII编码。想要输出真正的中文需要指定ensure_ascii=False
# 这里用文本方式读取。不用二进制。
with open('city.txt','w',encoding='utf8')as f:
    f.write(json.dumps(dic,ensure_ascii=False))
driver.quit()