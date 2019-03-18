from scrut_api import *
import json


# initiate Scurtinizer client. 
client = scrut_api_client(
         hostname="scrutinizer.plxr.local", 
         authToken="BI5NGMrqd3ZsAvWPHekHmPUT")
#set up report JSON. 

report_object = scrut_json(filters = {'sdfDips_0': 'in_GROUP_ALL'})
report_format = scrut_data_requested()


#load up params to be passed to request
request = scrut_request(
    client=client,
    json_data = report_object.report_json,
    data_requested=report_format.format

)

response = request.send()


#print out the data formatted. 
for ip_address in response.data['report']['table']['inbound']['rows']:
    print('Source IP Address: ' + ip_address[1]['label'])

