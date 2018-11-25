import re
import os
import sys
import json
import datetime
import elasticsearch.helpers
from elasticsearch import Elasticsearch, helpers

today = datetime.date.today()
today_s = str(today)
today1 = today_s.replace("-",".")

es = Elasticsearch("http://localhost:9200")
for tmpindex in es.indices.get('audit-{}'.format(today1)):

	rawIndiceName = tmpindex
	response_suc = helpers.scan(es,
				scroll= "10m",
				index=rawIndiceName,
				timeout="10m",
				size=8000,
				query =
					{
					"query": {
						"bool": {
							"must": [
									{
									"terms": {
										"op.keyword": [
												"success"
												]

										}
									}
								]
								
							}
						}
					}
				)
	num = 0
	acct_list = []
	addr_list = []

	print('{"data":[')

	for resp in response_suc:

		#doc_keys = resp["_source"].keys()

#print (doc_keys)

		#doc_values = resp["_source"].values()

		#doc_items = resp["_source"].items()

#print (doc_items)

		
		
		acct = resp['_source']['acct']
		if acct == "jocelyn":
			num +=1
		elif acct == "yuhan":
			num +=1
		elif acct == "leon":
			num +=1
		elif acct == "daniel":
			num +=1

		acct_list.append(acct)

		addr = resp['_source']['addr']
		# num_info = {
		# 	{"name":"jocelyn","amount":num_j},
		# 	{"name":"yuhan","amount":num_y},
		# 	{"name":"leon","amount":num_l},
		# 	{"name":"daniel","amount":num_d}
		# }
		addr_list.append(addr)
		# num_info = {
		# 	"jocelyn":num_j,
		# 	"yuhan":num_y,
		# 	"leon":num_l,
		# 	"daniel":num_d
		# }

		#bs = resp['_source']['LNBTS']

		#moClass = resp['_source']['moClass']

		#moidFull = bs + moid

		#num +=1
	# num_js = str(num_j)
	# num_ys = str(num_y)
	# num_ls = str(num_l)
	# num_ds = str(num_d)
	x = num-1
	# print(acct_list)
	# for i in range(0,num):
	# 	print(addr_list[i])
	for i in range(0,num):
		# print(acct_list[0])
		# print(acct_list[{}].format(i))
		print('{"id":"'+acct_list[i]+'","ip":"' + addr_list[i] +'","count":1}')
		
		if i < x:
			print(",")

		
	# print('{"id":"jocelyn","ip":"' + addr +'","count":"'+ num_js +'"},{"id":"yuhan","ip":"' + addr +'","count":"'+ num_ys + '"},{"id":"leon","ip":"' + addr +'","count":"'+ num_ls +'"},{"id":"daniel","ip":"'+ addr +'","count":"'+ num_ds + '"}')
	print("]}")
	
