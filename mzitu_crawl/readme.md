

# 爬虫使用手册



![](<https://img.shields.io/badge/python-3-brightgreen.svg>)![](<https://img.shields.io/badge/redis-support-green.svg>)![](<https://img.shields.io/badge/random-proxy-yellow.svg>)![](<https://img.shields.io/badge/python-crawler-orange.svg>)![](<https://img.shields.io/badge/python-requests-red.svg>)![](<https://img.shields.io/badge/python-requests__html-blue.svg>)





有两个爬虫版本，一个是有随机IP的，一个没有随机IP



## 技术实现

- 随机请求头
- URL去重，将爬过的图片地址放入redis数据库中，爬虫停止后，不会从头开始爬。
- 程序有大量IO，使用多线程提高效率
- （可选）随机代理IP







## 运行条件

​	

```
python3 
安装有Redis数据库
安装requests.txt
pip install -r requirements.txt
```



### 无代理的版本

- redis-server 开启redis服务
- 运行mzitu_cr

我的电脑上有G盘，在这里报错的记得改个盘符

```
32 行         base_dir = 'G:\meizi'  # 存放的文件夹 

```



### 有爬虫的版本运行流程

- redis-server 要先启动
- 命令行下 cd  到 /proxy_pool/run    文件夹 
- python main.py
- 运行mzitu_proxy



代理IP也是从别的地方抓取来的代理的质量不是很好，运行这个版本的爬虫的时候能速度有些慢



​	

