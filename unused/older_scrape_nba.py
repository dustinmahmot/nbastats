import requests
import json
import fileinput
from pandas import DataFrame

SITEMAP_ID = '1052816'

API_KEY = 'xygyDc821bFYMeWckcWq08SvNctFZhlOoQef4rbglGdg11ln3OPivDnDkwEy'


# sends request to 
def getScrapeJob(job_id):
	data = {}
	
	resp =  requests.get(url='https://api.webscraper.io/api/v1/scraping-job/' + str(job_id) + '/json?api_token=' + API_KEY)

	raw_data = resp.content.decode().splitlines()

	# fills 'data' with nested dict containing data
	for x in raw_data: 

		[left,data_line] = x.split('\"Player\":') 
		[key_main,value_main] = data_line.split(',\"', maxsplit=1)

		key_main = key_main.strip('\"')
		data[key_main] = {}

		value_main = value_main.replace('\"', '')[:-1]
		
		pairs = value_main.split(',')


		for pair in pairs:
			[key_nested, value_nested] = pair.split(':')
			data[key_main][key_nested] = value_nested

	return data

	


# gets all jobs
param_dict = {"sitemap": "&sitemap_id=" + SITEMAP_ID}
resp_all_jobs = requests.request(method= 'GET', url= 'https://api.webscraper.io/api/v1/scraping-jobs?api_token=' + API_KEY, params= param_dict)
dict_all_jobs = resp_all_jobs.json()

job_list = dict_all_jobs['data']

newest_job_id = job_list[-1]['id']


	
data = getScrapeJob(18519353)
stats_dataframe = DataFrame.from_dict(data, orient='index')
stats_dataframe = stats_dataframe.sort_values('REB', ascending=False)
# for x in stats_dataframe['REB']:
# 	print(type(x))
print(stats_dataframe)


# for i in stats_dataframe.keys():
# 	print(i)

# stats_dataframe['Lebron']


# scrape_specs = {
# 	"SITEMAP_ID": 1052816,
# 	"driver": "fast", 
# 	"page_load_delay": 2000,
# 	"request_interval": 2000,
# 	"custom_id": "big_ol_job"
# }

# create scaping job - NOT WORKING. 
# resp = requests.request(method= 'POST', url= 'https://api.webscraper.io/api/v1/scraping-job?api_token=' + API_KEY, json= scrape_specs)
# print(resp.content)
 