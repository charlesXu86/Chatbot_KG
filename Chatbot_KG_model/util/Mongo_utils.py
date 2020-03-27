# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     Mongo_utils.py
   Description :  连接mongoDB
   Author :       charl
   date：          2018/9/3
-------------------------------------------------
   Change Activity: 2018/9/3:
-------------------------------------------------
"""

import pprint
from pymongo import MongoClient

uri = 'mongodb://fuwuqi2019:falvtuandui@106.13.137.219:27017/'
class Mongo():

	def __init__(self):
		self.host = '106.13.137.219'
		self.username = ''
		self.passwd = ''

		self.uri = 'mongodb://' + 'fuwuqi2019' + ':' + 'falvtuandui' + '@' + '106.13.137.219' + ':' + '27017' +'/'
		self.client = MongoClient(self.host, 27017)
		self.db = self.client['admin']
		self.db.authenticate('fuwuqi219', 'falvtuandui', mechanism='SCRAM-SHA-1')

	def get_count(self):
		'''

		:return:
		'''
		data = self.client['wenshu']
		count = data.chongqing_origin.count()
		print(count)

	def get_one(self):
		'''

		:return:
		'''
		pass

	def insert_data(self):
		'''
		插入数据
		:return:
		'''


db = Mongo()
# def find_MONGO_one(ids):
# 	'''
# 	查询一条数据
# 	:param ids:
# 	:return:
# 	'''
# 	db = db.client.wusong
# 	collection = db.chongqing_origin
# 	datas = collection.find_one({'judgementId':ids})
# 	pprint.pprint(datas)
# host = '106.13.137.219'
# client = MongoClient(host, 27017)
# db = client.admin
# db.authenticate('fuwuqi219', 'falvtuandui', mechanism='SCRAM-SHA-1')
# collection = db.wenshu
# print(collection)


if __name__ == '__main__':
	#
	#
	# judgementId = '0d5ce792-69cb-494a-8eca-2725b5eea1de'
	# find_MONGO_one(judgementId)
	db.get_count()

