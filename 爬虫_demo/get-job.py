# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lianxijob.mylog import MyLog as mylog
import json
import time
import urllib.request
import lxml.html
etree = lxml.html.etree

class Item(object):
    job_name = None  # 岗位名
    company_name = None  # 公司名
    work_place = None  # 工作地点
    salary = None  # 薪资
    release_time = None  # 发布时间
    job_recruitment_details = None  # 招聘岗位详细
    job_number_details = None  # 招聘人数详细
    company_treatment_details = None  # 福利待遇详细
    practice_mode = None  # 联系方式


class GetJobInfo(object):
    """
    所有数据来自前程无忧招聘网
    """
    def __init__(self):
        self.log = mylog()  # 实例化mylog类,用于记录日志
        self.startUrl = 'https://www.51job.com/'  # 爬取的目标网站
        self.browser = self.getBrowser()  # 设置chrome
        self.browser_input = self.userInput(self.browser)  # 模拟用户输入搜索
        self.getPageNext(self.browser_input)   # 找到下个页面

    def getBrowser(self):
        """
        设置selenium使用chrome的无头模式
        打开目标网站 https://www.51job.com/
        :return: browser
        """
        try:
            # 创建chrome参数对象
            chrome_options = Options()
            # 把chrome设置成无界面模式,不论windows还是linux都可以，自动适配对应参数
            chrome_options.add_argument('--headless')
            # 创建chrome无界面对象,设置成无头
            browser = webdriver.Chrome(chrome_options=chrome_options,
                    executable_path=r'D:\PY\Scripts\chromedriver.exe')
            # 利用selenium打开网站
            browser.get(self.startUrl)
            # 等待网站js代码加载完毕
            browser.implicitly_wait(20)
        except Exception as e:
            # 记录错误日志
            self.log.error('打开目标网站失败:{},错误代码:{}'.format(self.startUrl, e))
        else:
            # 记录成功日志
            self.log.info('打开目标网站成功:{}'.format(self.startUrl))
            # 返回实例化selenium对象
            return browser

    def userInput(self, browser):
        """
        北京 上海 广州 深圳 武汉 西安 杭州
        南京  成都 重庆 东莞 大连 沈阳 苏州
        昆明 长沙 合肥 宁波 郑州 天津 青岛
        济南 哈尔滨 长春 福州
        只支持以上城市,输入其它则无效
        最多可选5个城市,每个城市用 , 隔开(英文逗号)
        :return:browser
        """
        time.sleep(1)
        # 用户输入关键字搜索
        search_for_jobs = input("请输入职位搜索关键字:")
        # 用户输入城市
        print(self.userInput.__doc__)
        select_city = input("输入城市信息,最多可输入5个,多个城市以逗号隔开:")
        # 找到51job首页上关键字输入框
        textElement = browser.find_element_by_id('kwdselectid')
        # 模拟用户输入关键字
        textElement.send_keys(search_for_jobs)

        # 找到城市选择弹出框，模拟选择"北京,上海,广州,深圳,杭州"
        button = browser.find_element_by_xpath("//div[@class='ush top_wrap']\
        //div[@class='el on']/p[@class='addbut']//input[@id='jobarea']")

        # 打开城市对应编号文件
        with open("city.txt", 'r', encoding='utf8') as f:
            city_number = f.read()
            # 使用json解析文件
            city_number = json.loads(city_number)

        new_list = []
        # 判断是否输入多值
        if len(select_city.split(',')) > 1:
            for i in select_city.split(','):
                if i in city_number.keys():
                    # 把城市替换成对应的城市编号
                    i = city_number.get(i)
                    new_list.append(i)
                    # 把用户输入的城市替换成城市编号
            select_city = ','.join(new_list)
        else:
            for i in select_city.split(','):
                i = city_number.get(i)
                new_list.append(i)
            select_city = ','.join(new_list)

        # 执行js代码
        browser.execute_script("arguments[0].value = '{}';".format(select_city), button)

        # 模拟点击搜索
        browser.find_element_by_xpath("//div[@class='ush top_wrap']/button").click()
        self.log.info("模拟搜索输入成功,获取目标爬取title信息:{}".format(browser.title))
        return browser

    def getPageNext(self, browser):
        # 找到总页数
        str_sumPage = browser.find_element_by_xpath("//div[@class='dw_page']/div//\
        span[@class='td'][1]").text
        sumpage = ''
        for i in str_sumPage:
            if i.isdigit():
                sumpage += i
        self.log.info("获取总页数:{}".format(sumpage))
        s = 1
        while s <= int(sumpage):
            urls = self.getUrl(self.browser)
            # 获取每个岗位的详情
            self.items = self.spider(urls)
            # 数据下载
            self.pipelines(self.items)
            # 清空urls列表,获取后面的url(去重,防止数据重复爬取)
            urls.clear()
            s += 1
            self.log.info('开始爬取第%d页' % s)
            # 找到下一页的按钮点击
            NextTag = browser.find_element_by_partial_link_text("下一页").click()
            # 等待加载js代码
            browser.implicitly_wait(20)
            time.sleep(3)
        self.log.info('获取所有岗位成功')
        browser.quit()

    def getUrl(self, browser):
        # 创建一个空列表,用来存放所有岗位详情的url
        urls = []

        # 创建一个特殊招聘空列表
        job_urls = []

        # 获取所有岗位详情url
        Elements = browser.find_elements_by_xpath("//div[@class='dw_table']//div[@class='el']")
        for element in Elements:
            try:
                url = element.find_element_by_xpath("./p/span/a").get_attribute("href")
                title = element.find_element_by_xpath('./span[@class="t2"]/a').get_attribute('title')
            except Exception as e:
                self.log.error("获取岗位详情失败,错误代码:{}".format(e))
            else:
                # 排除特殊的url，可单独处理
                src_url = url.split('/')[3]
                if src_url == 'sc':
                    job_urls.append(url)
                    self.log.info("获取不符合爬取规则的详情成功:{},添加到job_urls".format(url))
                else:
                    urls.append(url)
                    self.log.info("获取详情成功:{},添加到urls".format(url))
        return urls

    def spider(self, urls):
        # 数据过滤,爬取需要的数据,返回items列表
        items = []
        for url in urls:
            htmlcontent = self.getreponsecontent(url)
            html_xpath = etree.HTML(htmlcontent)
            item = Item()
            # 岗位名
            item.job_name = html_xpath.xpath("normalize-space(//div[@class='cn']/h1/text())")
            # 公司名
            item.company_name = html_xpath.xpath("normalize-space(//div[@class='cn']\
            /p[@class='cname']/a/text())")
            # 工作地点
            item.work_place = html_xpath.xpath("normalize-space(//div[@class='cn']\
            //p[@class='msg ltype']/text())").split('|')[0].strip()
            # 薪资
            item.salary = html_xpath.xpath("normalize-space(//div[@class='cn']/strong/text())")
            # 发布时间
            item.release_time = html_xpath.xpath("normalize-space(//div[@class='cn']\
            //p[@class='msg ltype']/text())").split('|')[-1].strip()
            # 招聘岗位详细
            job_recruitment_details_tmp = html_xpath.xpath("//div[@class='bmsg job_msg inbox']//text()")
            item.job_recruitment_details = ''
            ss = job_recruitment_details_tmp.index("职能类别：")
            ceshi = job_recruitment_details_tmp[:ss - 1]
            for i in ceshi:
                item.job_recruitment_details = item.job_recruitment_details + i.strip() + '\n'
            # 招聘人数详细
            job_number_details_tmp = html_xpath.xpath("normalize-space(//div[@class='cn']\
            //p[@class='msg ltype']/text())").split('|')
            item.job_number_details = ''
            for i in job_number_details_tmp:
                item.job_number_details = item.job_number_details + ' ' + i.strip()
            # 福利待遇详细
            company_treatment_details_tmp = html_xpath.xpath("//div[@class='t1']//text()")
            item.company_treatment_details = ''
            for i in company_treatment_details_tmp:
                item.company_treatment_details = item.company_treatment_details + ' ' + i.strip()
            # 联系方式
            practice_mode_tmp = html_xpath.xpath("//div[@class='bmsg inbox']/p//text()")
            item.practice_mode = ''
            for i in practice_mode_tmp:
                item.practice_mode = item.practice_mode + ' ' + i.strip()
            items.append(item)
        return items

    def getreponsecontent(self, url):
        # 接收url,打开目标网站,返回html
        fakeHeaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
        try:
            request = urllib.request.Request(url, headers=fakeHeaders)
            response = urllib.request.urlopen(request)
            html = response.read().decode('gbk')
        except Exception as e:
            self.log.error(u'Python 返回 url:{} 数据失败\n错误代码:{}\n'.format(url, e))
        else:
            self.log.info(u'Python 返回 url:{} 数据成功\n'.format(url))
            time.sleep(1)  # 1秒返回一个结果  手动设置延迟防止被封
            return html

    def pipelines(self, items):  # 接收一个items列表
        # 数据下载
        filename = u'51job.txt'
        with open(filename, 'a', encoding='utf-8') as fp:
            for item in items:
                fp.write('job_name:{}\ncompany_name:{}\nwork_place:{}\nsalary:\
                {}\nrelease_time:{}\njob_recruitment_details:{}\njob_number_details:\
                {}\ncompany_treatment_details:\{}\n\
                practice_mode:{}\n\n\n\n' \
                         .format(item.job_name, item.company_name, item.work_place,
                                 item.salary, item.release_time,item.job_recruitment_details,
                                 item.job_number_details, item.company_treatment_details,
                                 item.practice_mode))
                self.log.info(u'岗位{}保存到{}成功'.format(item.job_name, filename))


if __name__ == '__main__':
    st = GetJobInfo()