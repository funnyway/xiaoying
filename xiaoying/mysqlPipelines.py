import pymysql.cursors
import time
def timetostr(timestamp):
	timeArray = time.localtime(timestamp)
	return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
class mysqlPipelines(object):
	def __init__(self):
		# 连接数据库
		self.connect = pymysql.connect(
			host='127.0.0.1',  # 数据库地址
			port=3306,  # 数据库端口
			db='python',  # 数据库名
			user='root',  # 数据库用户名
			passwd='12345678',  # 数据库密码
			charset='utf8',  # 编码方式
			use_unicode=True)
		# 通过cursor执行增删查改
		self.cursor = self.connect.cursor()
	def hasExist(self,project_id):
		sql = "select count(1) as total from xy_project where `project_id`="+str(project_id)
		try:
			self.cursor.execute(sql)
			data = self.cursor.fetchone()
			return data[0] == 1
		except:
			return True
	def process_item(self, item, spider):
		if self.hasExist(item['project_id']):
			print(item['project_id']+' hasExist')
			return item 
		item['ctime'] = str(int(time.time()))
		item['ctime_timestamp'] = timetostr(time.time())
		sql = "insert into xy_project(project_id,project_name,year_rate,total_amount,time_limit,ctime,ctime_timestamp) value('"+item['project_id']+"','"+item['project_name']+"','"+item['year_rate']+"','"+item['total_amount']+"','"+item['time_limit']+"','"+item['ctime']+"','"+item['ctime_timestamp']+"')" 
		print(sql)
		try:
			self.cursor.execute(sql)
			self.connect.commit()
		except:
			print('---------sql failed------'+sql)
			pass
		return item  # 必须实现返回

	