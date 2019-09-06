from scrut_api import ReportAPI, Requester
import json




report_params = ReportAPI()
report_params.make_object()

scrutinizer_requester = Requester(
    authToken="EfjmfZfnvWtRvUQ8xOkCHy1A",
    hostname="scrutinizer.plxr.local"
)

data = scrutinizer_requester.make_request(report_params)

print(data)