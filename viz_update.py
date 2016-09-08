__author__ = 'Matthew'

'''
Takes a csv with the headers "name", and "vid" and generates a csv containing the name and a new forked widget ID with provided specifications.
Default: Title (no), Footer (no), Native (yes), Share (no), Sources (yes)


To Do:
- Change from save_widget to GIQ Widget API for forking + new widget issuance
- Use Ultron to grab information from API package topic
- Use PAPI imports to push into Prog-API topic and Onboarding Tracker topic
'''

import sys, requests, json, csv
from datetime import datetime


'''
GLOBALS
'''
SW_URL_TEMPLATE = 'https://www.graphiq.com/w/ajax/save_widget?app_id={5}&options={{"wid":"{0}","type":"card","w":{1},"h":{2},"limit":100,"ids":["{3}"],"autogeo":false,"autohide_info":false,"initial_slide":true,"rcq":false,"u_ratings":false,"show_sources":true,"u_reviews":false,"app_id":{5},"source":"Card Editor","single_widget_mode":true,"card_id":{4},"context":"SINGLE","theme":"native","no_share":true,"show_footer":false,"show_header":false,"freeze":false}}&custom_attributes={{}}&embed_type=1'
VIZ_API_URL = 'http://api.graphiq.com/visualizations/'
VIZ_API_TOKEN = '56cce9e2c44bdb48410000017f508c60058d4ff46d13216f386de51b'
VIZ_HEIGHT = 500
VIZ_WIDTH = 700
HEADERS = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
PUBLISHER = 'Onboarding-Demo'
PID = '404'
STANDARD_STYLE = 'font:14px/16px arial;color:#339933;'
STANDARD_ANCHOR = 'More Details | FindTheHome'

def openCSV(csv_file):
    with open(csv_file,'rb') as input_csv:
        csv_reader = csv.DictReader(input_csv, delimiter=',', quotechar='"')
        rows = [line for line in csv_reader]
        return rows


def sendVizRequest(viz):
    try:
        r = requests.get(SW_URL_TEMPLATE.format(viz['vid'], VIZ_WIDTH, VIZ_HEIGHT, viz['listing_id'], viz['card_id'], viz['app_id']), headers=HEADERS)
        return json.loads(r.text)
    except requests.exceptions.RequestException as e:
        print e
        sys.exit(1)



def getVizInfo(viz):
    url = VIZ_API_URL + viz['vid']
    headers = {
    'token': VIZ_API_TOKEN
    }
    try:
        response = requests.request("GET", url, headers=headers)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print e
        sys.exit(1)


    
def formatEmbedCode(embed):
    start, end = embed.index('<a'), embed.index('/a>')
    no_href_code = embed[:start] + embed[end+3:]
    return no_href_code


def sendToTracker(viz_output):


def main():
    viz_rows = openCSV(sys.argv[1])
    tracker_import = []
    for viz in viz_rows:
        if 'card_id' in getVizInfo(viz).keys():
            viz_info = getVizInfo(viz)
            viz['card_id'] = viz_info['card_id']
            viz['app_id'] = viz_info['app_id']
            viz['listing_id'] = viz_info['listing_ids'][0]
            new_widget_response = sendVizRequest(viz)
            #viz_output = [viz['name'], new_widget_response['id']]
            #print ','.join(map(lambda x: str(x),viz_output))
            to_tracker = {"title":viz['description'],"widget_name":viz['name'],"widget_id":new_widget_response['id'],"publisher":PUBLISHER,"pid":PID,"json_widget_options":'{"type":"' + viz['api_topic'] + '", "add-ad-tag":false}',"style":STANDARD_STYLE,"anchor_text":STANDARD_ANCHOR,"date_issued":datetime.now(),"status":'current'}
            tracker_import.append(to_tracker)
        else:
            continue
    print tracker_import

if __name__ == "__main__":
    main()

