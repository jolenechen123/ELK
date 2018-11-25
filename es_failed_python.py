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
												"password"
												]

										}
									}
								]
								
							}
						}
					}
				)
	num_j = 0
	num_y = 0
	num_l = 0
	num_d = 0
	for resp in response_suc:

		#doc_keys = resp["_source"].keys()

#print (doc_keys)

		#doc_values = resp["_source"].values()

		#doc_items = resp["_source"].items()

#print (doc_items)



		acct = resp['_source']['acct']
		if acct == "jocelyn":
			num_j +=1
		elif acct == "yuhan":
			num_y +=1
		elif acct == "leon":
			num_l +=1
		elif acct == "daniel":
			num_d +=1

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
	num_js = str(num_j)
	num_ys = str(num_y)
	num_ls = str(num_l)
	num_ds = str(num_d)
	print("[")
	print('{"name":"jocelyn","amount":' + num_js + '},{"name":"yuhan","amount":' + num_ys + '},{"name":"leon","amount":' + num_ls + '},{"name":"daniel","amount":'+ num_ds + '}')
	print("]")
	
