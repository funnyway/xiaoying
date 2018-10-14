# xiaoying
python爬虫框架scrapy练手项目

定时爬取小盈理财项目列表，并把抓取的项目数据存入数据库
运行项目之前创建数据表，xiaoying.sql

## 单次执行任务
cd 到xiaoying目录

<code>scrapy crawl xiaoying</code>

## 定时执行
在unix/linux系统执行
crontab -e
添加下面一行，实现每5秒抓一次项目列表 path_to_xiaoying为项目在unix/linux 系统中的绝对路径

<code>* * * * * path_to_xiaoying/time_task.sh</code>
