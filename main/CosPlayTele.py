import Tool as tool
import File as cosplayFile
import re
url = "https://cosplaytele.com/category/nekokoyoshi/"

def getCosPlayTeleItems():
    # 获取页码
    pageNumber = tool.get_element_by_xpath(tool.get_xml(url),"//ul[@class='page-numbers nav-pagination links text-center']/li")

    items = []

    # 获取下载链接
    for i in range(1,len(pageNumber)+1,1):
        tempUrl = url + "page/{0}/".format(i) # 页数的链接
        currentPageXML = tool.get_xml(tempUrl) # 当前页
        #获取当前页中的每个元素的链接
        linkList = tool.get_element_by_xpath(currentPageXML,"//h5[@class='post-title is-large ']/a/@href")

        # 遍历每个文件的链接
        for link in linkList:
            detailXML = tool.get_xml(link)

            # 获取文件名
            name = tool.get_element_by_xpath(detailXML,"//h1[@class='entry-title']/text()")

            # 获取图片与视频数
            pCountAndVCount = tool.get_element_by_xpath(detailXML,"//blockquote/p[2]/strong[1]/text()")
            if len(pCountAndVCount) == 0:
                pCountAndVCount = tool.get_element_by_xpath(detailXML,"//blockquote/p[2]/s-[1]/text()")
            pCountAndVCount = re.sub(r"\s+","",str(pCountAndVCount[0]))
            # 获取文件大小
            fSize = tool.get_element_by_xpath(detailXML,"//blockquote/p[2]/strong[2]/text()")
            if len(fSize) == 0:
                fSize = tool.get_element_by_xpath(detailXML,"//blockquote/p[2]/s-[2]/text()")

            # 获取下载链接
            downloadLink =  tool.get_element_by_xpath(detailXML,"//a[contains(@href,'mediafire')]/@href")
            if len(downloadLink) == 0:
                downloadLink = [""]

            name = str(name).replace("\\xa0","") # 文件名
            pCountAndVCount = re.findall(r'\d+',str(pCountAndVCount)) # 图片数与视频数
            if len(pCountAndVCount) == 1:
                pCountAndVCount.append(0)

            fSize = (str(fSize)
                     .replace("'","")
                     .replace("[","")
                     .replace("]","")
                     .replace("\\xa0","")
                     .replace("File Size: ","")
                     ) # 文件大小

            item = cosplayFile.CosPlayFile(name,pCountAndVCount[0],pCountAndVCount[1],fSize,downloadLink[0])
            items.append(item)

    return items