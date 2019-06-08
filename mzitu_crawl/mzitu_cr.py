import os
from concurrent.futures import ThreadPoolExecutor
import pysnooper
import requests
from requests_html import HTMLSession
import common
threadpool = ThreadPoolExecutor(max_workers=10)



session = HTMLSession()
pages = session.get("https://www.mzitu.com/all/")


class Meizutu():

    # @pysnooper.snoop('log/log.log')
    def parse(self):
        # 网站有新旧两个目录，这里只爬取比较新的一部分。
        url_list_new = pages.html.xpath("/html/body/div[2]/div[1]/div[2]//a[@href]")[1:]  # 分类中比较新的
        url_list_old = pages.html.xpath("/html/body/div[2]/div[1]/div[2]//a[@href]")[0]
        for i in url_list_new:
            url = i.attrs['href']
            title = i.text
            url_md5 = common.md_url(url)
            flag = common.exist_or_not(url_md5)
            if flag:
                self.mkdir(title, url)

    def mkdir(self, title, url):
        base_dir = 'G:\meizi'  # 存放的文件夹
        img_dir = os.path.join(base_dir, title)  # 套图的路径
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)  # 创建图片文件夹
        self.parse_page(img_dir, url)


    def parse_page(self, img_dir, url):
        page = session.get(url)  # 获取详情页
        try:
            max_url = page.html.xpath('/html/body/div[2]/div[1]/div[4]/a[5]')  # 获取最大的图片张数
            max_page = max_url[0].full_text
            for i in range(1, int(max_page) + 1):
                img_page = url + '/' + str(i)
                print(img_page)
                page_d5 = common.md_url(img_page)
                not_exist = common.exist_or_not(page_d5)
                if not_exist:
                    self.save_img(img_page, img_dir)
                    print(img_dir)
                    print(img_page)
        except Exception as e:
            print(e)

    def save_img(self, img_page, img_dir):
        page = session.get(img_page)
        img_link = page.html.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src')[0]
        img_bytes = requests.get(img_link, headers=common.get_ua())
        img = img_bytes.content
        img_names = str(img_link).rsplit('/')[-1]
        file_name = os.path.join(img_dir, img_names)
        print(file_name)

        with open(file_name, 'wb') as f:
            f.write(img)


if __name__ == '__main__':
    meizi = Meizutu()
    meizi.parse()
    threadpool.submit(meizi.parse)
