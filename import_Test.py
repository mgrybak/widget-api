__author__ = 'Matthew'


import requests,json

url = "https://www.findthebest.com:443/API/v1/app/6876/import"

data  = [{"anchor_text": "More Details | FindTheHome", "publisher": "br360", "style": "font:14px/16px arial;color:#339933;", "title": "Demographic Overview", "json_widget_options": "{\"type\":\"places\", \"add-ad-tag\":false}", "pid": "405", "widget_name": "demographic_overview", "widget_id": "ctj1M22NUTr"}, {"anchor_text": "More Details | FindTheHome", "publisher": "br360", "style": "font:14px/16px arial;color:#339933;", "title": "Age Distribution", "json_widget_options": "{\"type\":\"places\", \"add-ad-tag\":false}", "pid": "405", "widget_name": "age_distribution", "widget_id": "9IYf4MphDcp"}]
payload = {'data': json.dumps(data)}

headers = {
    'token': "a815742ae8012732856fb231f0591899",
    }


response = requests.post(url, data=payload, headers=headers)
print(response.text)
