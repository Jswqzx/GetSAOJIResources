import requests
from lxml import etree
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

def generate_items_file(fileName,items):
    file = open(fileName, mode='w', encoding='utf-8')

    for item in items:

        driver = webdriver.Edge()

        if item.download_url != "":
            driver.get(item.download_url)

            time.sleep(1)

            try:
                btn = driver.find_element(By.XPATH, "//a[@id='downloadButton']")
                item.isDownload = True

                print("%s可以下载" % item.name)
            except NoSuchElementException:
                print("%s不存在" % item.name)

            driver.quit()

        file.write("名称: %s\n" % item.name)
        file.write("图片数: %s\n" % item.p_count)
        file.write("视频数: %s\n" % item.v_count)
        file.write("文件大小: %s\n" % item.f_size)
        file.write("是否可下载: %s\n" % item.isDownload)
        file.write("下载链接: %s\n" % item.download_url)
        file.write("\n")

    file.close()

def send_request(_url):
    return requests.get(url=_url,headers=header).content.decode()

def get_xml(_url):
    return etree.HTML(send_request(_url))

def get_element_by_xpath(xml,_xpath):
    return xml.xpath(_xpath)