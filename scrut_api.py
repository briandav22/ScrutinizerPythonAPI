import requests
import requests.packages.urllib3
import json

requests.packages.urllib3.disable_warnings()


class scrut_api_client:
    #class used to initiated the Scrutinizer client
    def __init__(
            self,
            verify=False,
            hostname="",
            authToken=""):
        if hostname == "Scrutinizer Hostname or IP Here":
            raise ValueError(
                "You need to put in Scrutinizer host IP in settings.json")
        if authToken == "API KEY HERE":
            raise ValueError(
                "You need an authentication token in settings.json")

        self.url = "https://{}/fcgi/scrut_fcgi.fcgi".format(hostname)
        self.verify = verify
        self.authToken = authToken

class scrut_json:
    '''
    Used to generate JSON data that will be posted to scrutinizers API. All arguments that are passed have default sets, you can modify any of them you choose. 

    If you want to add in other JSON calls to api you would need to add property with that json and reference it when you send the data into the scrut_params class. 

    self.status_json is an example of this. 
    
    
    '''
    def __init__(
        self,
        reportTypeLang="conversationsApp",
        reportDirections={"selected": "inbound"},
        dataGranularity={"selected": "auto"},
        orderBy="sum_octetdeltacount",
        times={"dateRange": "LastTenMinutes"},
        filters={
            "sdfDips_0": "in_GROUP_ALL"
        },
        rateTotal={"selected": "rate"},
        dataFormat={"selected": "normal"},
        bbp={"selected": "percent"},
        view="topInterfaces",
        unit="percent"):

        self.report_json = {

            "reportTypeLang": reportTypeLang,
            "reportDirections": reportDirections,
            "dataGranularity": dataGranularity,
            "orderBy": orderBy,
            "times": times,
            "filters": filters,
            "rateTotal": rateTotal,
            "dataFormat": dataFormat,
            "bbp": bbp
        }

        self.status_json = {
            "view": view,
            "unit": unit
        }


class scrut_data_requested:
    ''' Currently this class is only used when your using the report_json property. The scrut_params class is what will receive this data, it has error checking to make sure the .format property is passed if the user is sending report_json, if the user is sending status_json the then this data will be ignored (as it is not needed)'''
    def __init__(self,
                 data_requested={"inbound": {
                     "table": {
                         "query_limit": {"offset": 0, "max_num_rows": 10}
                     }
                 }
                 }):
        self.format = data_requested


class scrut_request:
    '''This class binds together the client, with the json_data, and the data_requested. whatever variable you use to initate this class will be passted into scrut_request'''
    def __init__(self,
                 run_mode="report_api",
                 action="get",
                 json_data="",
                 data_requested=None,
                 client=""):
                try:
                    if json_data['view'] == "topInterfaces":
                        self.data_for_req = {
                                "rm": "status",
                                "action": action,
                                "rpt_json": json.dumps(json_data),
                                "authToken": client.authToken
                                }
                except:
                     if isinstance(data_requested, scrut_data_requested):
                         raise ValueError('Make sure the instance of scrut_data_requested is passed with the .format property')
                     else:
                        self.data_for_req = {
                            "rm": run_mode,
                            "action": action,
                            "rpt_json": json.dumps(json_data),
                            "data_requested": json.dumps(data_requested),
                            "authToken": client.authToken
                                }


                self.url = client.url
                self.verify = client.verify
    
    def send(self):
        response = requests.get(
            self.url, params=self.data_for_req, verify=self.verify)
        #we should really do something to verify the response...
        return scrut_response(response)

class scrut_response:
    '''Handles the redsponse portion of the api call. This uses the requests library from python.
       The .resp property holds the request object and the .data property holds it converted to JSON'''
    def __init__(self, response):
        self.resp = response
        self.data = self.resp.json()

    def get_data(self):
        return self.data


class scrut_print:
    '''Most used for error check and seeing the data Scrutinizer is returning. It prints the JSON data out in a nicely formatted way to make it easier to read.'''
    def __init__(self, data_to_print):
        self.scrut_class = data_to_print
        if isinstance(data_to_print, dict):
            print(json.dumps(data_to_print, indent=4, sort_keys=True))
        else:
            for attribute in self.scrut_class.__dict__:
                print(attribute + ' : ' +
                      str(self.scrut_class.__dict__[attribute]))
