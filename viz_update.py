__author__ = 'Matthew'

'''
Takes a csv with the headers "name", and "vid" and generates a csv containing the name and a new forked widget ID with provided specifications.
Default: Title (no), Footer (no), Native (yes), Share (no), Sources (yes)


To Do:
- Change from save_widget to GIQ Widget API for forking + new widget issuance
- Use Ultron to grab information from API package topic
- Use PAPI delete step to
'''

import sys, requests, json, csv, time, creds


'''
GLOBALS
'''
SW_URL_TEMPLATE = 'https://www.graphiq.com/w/ajax/save_widget?app_id={5}&options={{"wid":"{0}","type":"card","title":"","dir_name":"","dir_url":"",\
"publisher_id":"","amazon_id":"","w":{1},"h":{2},"limit":100,"field":"","fields":[],"link_color":"","ids":["{3}"],"filters":[],"filter_by":[],"autogeo":false,\
"autohide_info":false,"initial_slide":true,"rcq":false,"sort_field":"","sort_dir":"","app_id":{5},"source":"Card Editor","single_widget_mode":true,"card_id":{4},\
"context":"SINGLE","freeze_frequency":"","freeze_date":"","freeze":false,"theme":"native","show_header":true,"show_footer":false,"show_sources":false,"global_no_links":true,"no_share":true,\
"backlink":false}}&custom_attributes={{}}&embed_type=1&source=api'
VIZ_API_URL = 'http://api.graphiq.com/visualizations/'
VIZ_API_TOKEN = '56cce9e2c44bdb48410000017f508c60058d4ff46d13216f386de51b'
VIZ_HEIGHT = 500
VIZ_WIDTH = '"100%"'
HEADERS = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
PROG_API_APP_ID = 6876
TRACKER_APP_ID = 11738
PUBLISHER = 'MyHeritage'
PID = '419'
STANDARD_STYLE = 'font:14px/16px arial;color:#339933;'
STANDARD_ANCHOR = 'More Details | MooseRoots'
IMPORT_URL = "https://www.findthebest.com:443/API/v1/app/{0}/import"
IMPORT_TOKEN = creds.import_token

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


def sendToTopic(import_data, app_id):
    headers = {
    'token': IMPORT_TOKEN
    }
    payload = {'data': json.dumps(import_data)}
    try:
        response = requests.request("POST", IMPORT_URL.format(app_id), data=payload, headers=headers)
        print response.text
    except requests.exceptions.RequestException as e:
        print e
        sys.exit(1)


def main():
    viz_rows = openCSV(sys.argv[1])
    tracker_import = []
    prog_api_import = []
    for viz in viz_rows:
        if 'card_id' in getVizInfo(viz).keys():
            viz_info = getVizInfo(viz)
            viz['card_id'] = viz_info['card_id']
            viz['app_id'] = viz_info['app_id']
            viz['listing_id'] = viz_info['listing_ids'][0]
            new_widget_response = sendVizRequest(viz)
            to_tracker = {"title":viz['description'],"widget_name":viz['name'],"widget_id":new_widget_response['id'],"publisher":PUBLISHER,"pid":PID,"json_widget_options":'{"type":"' + viz['api_topic'] + '", "add-ad-tag":false}',"style":STANDARD_STYLE,"anchor_text":STANDARD_ANCHOR,"date_issued":time.strftime('%Y-%m-%d %H:%M:%S'),"template_widget_id":viz['vid']}
            tracker_import.append(to_tracker)
            to_prog = {"title":viz['description'],"widget_name":viz['name'],"widget_id":new_widget_response['id'],"publisher":PUBLISHER,"pid":PID,"json_widget_options":'{"type":"' + viz['api_topic'] + '", "add-ad-tag":false}',"style":STANDARD_STYLE,"anchor_text":STANDARD_ANCHOR}
            prog_api_import.append(to_prog)
            print "Successfully added new visualization for", viz['name']
	        #print ",".join(map(lambda x: '"' + str(x) + '"', [new_widget_response['id'],viz['description'],viz['name'],viz['vid']]))
        else:
            print "Error forking visualization for", viz['name']
            continue
    sendToTopic(tracker_import,11738)
    sendToTopic(prog_api_import,6876)


if __name__ == "__main__":
    main()

