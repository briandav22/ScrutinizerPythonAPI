from scrut_api import *



# initiate Scurtinizer client. 
client = scrut_api_client(
         hostname="some_scrutinizer_ip", 
         authToken="some_auth_token")
#set up report JSON. 

report_object = scrut_json()
report_format = scrut_data_requested()

#load up params to be passed to request
params = scrut_params(
    client=client,
    json_data = report_object.report_json,
    data_requested=report_format.format

)

response = scrut_request(params)


#print out the data formatted. 
scrut_print(response.data)
