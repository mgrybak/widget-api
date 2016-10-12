__author__ = 'Matthew'

'''
Takes a csv with the headers "name", and "vid" and generates a csv containing the name and a new forked widget ID with provided specifications.
Default: Title (no), Footer (no), Native (yes), Share (no), Sources (no), any links (no)
'''

import sys, requests, json, csv, time


'''
GLOBALS
'''
SW_URL_TEMPLATE = 'https://www.graphiq.com/w/ajax/save_widget?app_id={5}&options={{"wid":"{0}","type":"card","title":"","dir_name":"","dir_url":"",\
"publisher_id":"","amazon_id":"","w":{1},"h":{2},"limit":100,"field":"","fields":[],"link_color":"","ids":["{3}"],"filters":[],"filter_by":[],"autogeo":false,\
"autohide_info":false,"initial_slide":true,"rcq":false,"sort_field":"","sort_dir":"","app_id":{5},"source":"Card Editor","single_widget_mode":true,"card_id":{4},\
"context":"SINGLE","freeze_frequency":"","freeze_date":"","theme":"native","show_header":false,"show_footer":false,"show_sources":false,"global_no_links":true,"no_share":true,\
"backlink":false}}&custom_attributes={{}}&embed_type=1&source=api'
VIZ_API_URL = 'http://api.graphiq.com/visualizations/'
VIZ_API_TOKEN = '56cce9e2c44bdb48410000017f508c60058d4ff46d13216f386de51b'
VIZ_HEIGHT = 500
VIZ_WIDTH = 700
HEADERS = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}


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


def main():
    viz_rows = openCSV(sys.argv[1])
    for viz in viz_rows:
        if 'card_id' in getVizInfo(viz).keys():
            viz_info = getVizInfo(viz)
            viz['card_id'] = viz_info['card_id']
            viz['app_id'] = viz_info['app_id']
            viz['listing_id'] = viz_info['listing_ids'][0]
            new_widget_response = sendVizRequest(viz)
            output_list = [viz['name'],new_widget_response['status'],new_widget_response['embed']['code'],new_widget_response['id']]
            print ",".join(map(lambda x: '"' + str(x) + '"', output_list))
        else:
            print "Error forking visualization for {0} using viz ID {1}".format(viz['name'], viz['vid'])
            continue


if __name__ == "__main__":
    main()


