export PATH=$PATH:/usr/local/bin
cd ~/python/spider/xiaoying


step=5 #间隔的秒数，不能大于60  
  
for (( i = 0; i < 59; i=(i+step) )); do  
    nohup scrapy crawl xiaoying --nolog >> xiaoying.log 2>&1 &
    sleep $step  
done  

