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
	num = 0
	
	for resp in response_suc:

		#doc_keys = resp["_source"].keys()

#print (doc_keys)

		#doc_values = resp["_source"].values()

		#doc_items = resp["_source"].items()

#print (doc_items)



		res = resp['_source']['res']
		if res == "failed":
			num +=1


		# num_info = {
		# 	{"name":"jocelyn","amount":num_j},
		# 	{"name":"yuhan","amount":num_y},
		# 	{"name":"leon","amount":num_l},
		# 	{"name":"daniel","amount":num_d}
		# }

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
	num_s = str(num)
	
	print(num_s)
	# print('{"name":"jocelyn","amount":' + num_js + '},{"name":"yuhan","amount":' + num_ys + '},{"name":"leon","amount":' + num_ls + '},{"name":"daniel","amount":'+ num_ds + '}')
	# print("]")
	
