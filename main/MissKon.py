import Tool as tool
import File as cosplayFile
import re

url = "https://misskon.com/page/{}/?s=Nekokoyoshi"

def getMissKonItems():
    # 页数
    pageNumber = len(tool.get_element_by_xpath(tool.get_xml(url.format(1)),"//div[@class='pagination']/*"))
    # 获取URL
    items = []
    for i in range(1,pageNumber,1):
        tempUrl = url.format(i) # 获取要访问的URL

        # 获取文件链接
        links = tool.get_element_by_xpath(tool.get_xml(tempUrl), "//article/div[@class='post-thumbnail']/a/@href")
        # 遍历链接进入获取文件信息
        for link in links:
            # 文件信息
            detail_page = tool.get_xml(link)
            info_titles = tool.get_element_by_xpath(detail_page, "//div[@class='box-inner-block']/strong/text()")
            info_values = [i for i in tool.get_element_by_xpath(detail_page, "//div[@class='box-inner-block']/text()") if ("\n" not in i)]

            # 获取标题
            title = tool.get_element_by_xpath(detail_page,"//h1/span/text()")

            # 获取下载链接
            download_url = tool.get_element_by_xpath(detail_page,"//a[contains(@href,'ouo.io')]/@href")

            # 获取图片与视频数量
            p_v_count = re.findall(r'\d+',str(info_values[info_titles.index("Number of items:")]))
            p_count = p_v_count[0]
            v_count = 0
            if len(p_v_count) == 2:
                v_count = p_v_count[1]

            # 获取文件大小
            f_size = info_values[info_titles.index("File size:")]

            # 封装文件信息
            item = cosplayFile.CosPlayFile(title,p_count,v_count,f_size,download_url).__setIsDownLoad__(True)
            items.append(item)
            # print("文件名称：%s" %title)
            # print("图片数：%s" %p_count)
            # print("视频数: %s" %v_count)
            # print("文件大小: %s" %f_size)
            # print("下载链接: %s" %download_url)

    # 返回
    return items
