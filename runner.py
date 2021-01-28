import datetime
from csvRead import tuples
import json
import os
import re
import sys
import threading
import time
from datetime import date
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import (
    get_web_driver_options,
    get_chrome_web_driver,
    set_browser_as_incognito,
    set_ignore_certificate_error,
    set_browser_in_fullScreen,
    set_automation_as_head_less,
    URL, URL1
)
from selenium.webdriver.common.proxy import Proxy, ProxyType

import save_db
from filingTable import filing_table
from profile_file import profile_list
from test import Captcha
# import read_excel
import random
from hhub import proxylist

threadLocal = threading.local()


# lst = read_excel.lst


# pproxy = "5.61.58.211:4114:RU"


# lst = ["ASHIRVAD PIPES PRIVATE LIMITED "]


class Runner:

    def __init__(self, base_url, pproxy):
        self.base_url = base_url
        prox = Proxy()
        prox.proxy_type = ProxyType.MANUAL
        prox.http_proxy = pproxy
        # prox.socks_proxy = pproxy
        prox.ssl_proxy = pproxy
        print(pproxy)
        self.driver = getattr(threadLocal, 'driver', None)
        if self.driver is None:
            capabilities = webdriver.DesiredCapabilities.CHROME
            prox.add_to_capabilities(capabilities)

            options = get_web_driver_options()
            # set_proxy(options)
            set_ignore_certificate_error(options)

            set_browser_as_incognito(options)
            set_automation_as_head_less(options)
            # set_browser_in_fullScreen(options)

            self.driver = get_chrome_web_driver(options, capabilities)
        setattr(threadLocal, 'driver', self.driver)
        self.dictt = {}

    # def know_your_gst(self, cname):
    #     self.driver.get(self.base_url)
    #     self.driver.implicitly_wait(5)
    #     time.sleep(1)
    #     self.driver.find_element_by_id("gstnumber").send_keys(cname + Keys.ENTER)
    #
    #     # self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/form/div[2]/input').click()
    #     # time.sleep(2)
    #     gst = self.driver.find_element_by_xpath('//*[@id="searchresult"]/span/strong[2]').text
    #     pan = gst[2:-3]
    #     print(pan)
    #     return pan

    def gst(self, pan):
        try:
            self.driver.implicitly_wait(5)
            self.driver.get(URL1)
            time.sleep(1)
            self.driver.find_element_by_id('for_gstin').send_keys(pan)
            # img()
            try:
                self.captcha()
            except NoSuchElementException:
                self.captcha()
            except TypeError:
                self.captcha()
            except IndexError:
                self.captcha()
            data = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(text(),'Enter valid letters shown in the image below')]")))

            while data:
                self.captcha()
            if data:
                return True
        except Exception as e:
            print(str(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print("line->" + str(exc_tb.tb_lineno))
            print('Exception' + str(e))

    def captcha(self):
        time.sleep(2)
        data = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="imgCaptcha"]')))

        # self.driver.find_element_by_xpath('//*[@id="imgCaptcha"]')
        data.screenshot("foo.png")
        obj = Captcha()
        captcha_answ = obj.solve()
        while len(captcha_answ) < 1:
            captcha_answ = obj.solve()
        time.sleep(1)
        # if not captcha_answ:
        #     captcha_answ = obj.solve()
        # self.driver.execute_script(f"document.getElementById('fo-captcha').value={captcha_answ}")
        self.driver.find_element_by_id('fo-captcha').send_keys(captcha_answ, Keys.ENTER)

    def ectract_gst_number(self):
        lst = []
        try:
            data = self.driver.find_element_by_xpath("//a[contains(text(),'»')]")
            if data:
                try:
                    btn = self.driver.find_elements_by_class_name('page-link')
                    ctn = len(btn) - 1
                    while True:
                        if ctn > 1:
                            self.all_gst(lst)

                            self.driver.find_element_by_xpath("//a[contains(text(),'»')]").click()
                            time.sleep(.2)
                            ctn -= 1
                        else:
                            print("no more pages")
                            break
                    # print("lst", lst)
                    return lst
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    print("line->" + str(exc_tb.tb_lineno))
                    print('Exception' + str(e))
        except Exception:
            self.all_gst(lst)

            return lst

    def all_gst(self, all_rows):
        time.sleep(.5)
        page = self.driver.page_source
        soup = BeautifulSoup(page, "html.parser")
        data = soup.find_all("div", {"class": "table-responsive"})
        body = data[0].find_all("tr")
        body_rows = body[2:]
        # all_rows = []
        for row_num in range(len(body_rows)):
            row = []
            for row_item in body_rows[row_num].find_all("td"):
                aa = re.sub("(\xa0)|(\n)|,", "", row_item.text)
                row.append(aa.strip())
            if "Active" in row:
                all_rows.append(row[1])
        # print(all_rows)

    def open_gst_number(self, lst):
        outr = {}
        for gstin in lst:
            try:
                time.sleep(1)
                inr_dict = {}
                url = f"https://services.gst.gov.in/services/api/search/goodservice?gstin={gstin}"
                page = requests.get(url)
                bzgddtls = page.text
                jsn = json.loads(bzgddtls)
                self.driver.get("https://services.gst.gov.in/services/searchtp")
                self.driver.find_element_by_id("for_gstin").send_keys(gstin)
                time.sleep(.3)
                # element = self.driver.find_element_by_xpath('//*[@id="filingTable"]')
                # self.driver.execute_script("arguments[0].scrollIntoView();", element)

                try:
                    self.captcha()
                    time.sleep(.5)
                    self.driver.find_element_by_id('filingTable').click()
                except NoSuchElementException:
                    self.captcha()
                    data = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//*[@id="filingTable"]')))
                    data.click()
                except IndexError:
                    self.captcha()
                    time.sleep(.5)
                    self.driver.find_element_by_id('filingTable').click()
                tbl, pf_list = self.extract_data(gstin[2:-3])
                inr_dict['CompanyDetails'] = pf_list
                inr_dict['gstFiling'] = tbl
                inr_dict['goodsAndServices'] = jsn
                # inr_dict['Pan'] = gstin[2:-3]
                inr_dict['Created_at'] = str(date.today())
                outr[gstin] = inr_dict
            except Exception as e:
                print(str(e))
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print("line->" + str(exc_tb.tb_lineno))
                print('Exception' + str(e))
                continue
        self.dictt = outr
        # print(self.dictt)
        return self.dictt

    def extract_data(self, pan):
        time.sleep(1)
        page = self.driver.page_source
        soup = BeautifulSoup(page, "html.parser")
        tbl = filing_table(soup)
        # print(tbl)
        divs = soup.find("div", {"class": "tbl-format"})
        data = divs.find_all("div", {"class": "row"})
        line1 = data[0].text.split("\n")
        line2 = data[2].text.split("\n")
        pf_list = profile_list(line1, line2, pan)
        return tbl, pf_list

    def close_driver(self):
        self.driver.close()


def main(lstt):
    # for x in lstt:
    proxy_list = proxylist()
    pproxy = random.choice(proxy_list)
    run_obj = Runner(URL, pproxy)
    cname = {}
    try:
        # pan = run_obj.know_your_gst(x[1][2:-3])
        # print("pan", pan)
        data = run_obj.gst(lstt[1][2:-3])
        cnt = 0
        if data:
            while cnt < 2:
                run_obj.gst(lstt[1][2:-3])
                cnt += 1
        else:

            num = run_obj.ectract_gst_number()
            print("lst", num)
            print("len", len(num))

            res = run_obj.open_gst_number(num)
            # print(res)
            cname[lstt[0]] = res
            # print("cname[x]",cname[x[0]])
            # for i in num:
            #     if i not in cname[x].keys():
            #         res = run_obj.open_gst_number(num)
            #         cname[x] = res
            # print(cname)
            # import save_db
            # save_db.insertData(cname)

    except Exception as e:
        print(str(e))
        run_obj.close_driver()
        # continue
    finally:
        # print(cname)
        if cname[lstt[0]]:
            # print(type(cname))
            save_db.insertData(cname)

        # run_obj.close_driver()
        # print(cname)
        # with open("data_file.json", "w") as write_file:
        #     json.dump(cname, write_file)


if __name__ == '__main__':
    lst = tuples[:20]
    main(lst)
