from scrut_api import *



# initiate Scurtinizer client. 
client = scrut_api_client(
         hostname="scrutinizer.plxr.local", 
         authToken="BI5NGMrqd3ZsAvWPHekHmPUT")
#set up report JSON. 

report_object = scrut_json(filters = {"sdfDips_0": "in_10.1.1.252_ALL"},
							reportTypeLang = "applications")
report_format = scrut_data_requested()

#load up params to be passed to request
params = scrut_params(
    client=client,
    json_data = report_object.report_json,
    data_requested=report_format.format

)

# make request. Data comes with .data attribute
# response = scrut_request(params)

response = scrut_request(params)


#print out the data formatted. 
scrut_print(response.data)


# with open('data.json', 'w') as outfile:  
#     json.dump(response.data, outfile)