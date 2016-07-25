__author__ = 'Matthew'


import sys, requests, json, csv


URL_TEMPLATE = 'https://www.graphiq.com/w/ajax/save_widget?app_id={5}&options={{"wid":"{0}","type":"card","w":{1},"h":{2},"limit":100,"ids":["{3}"],"autogeo":false,"autohide_info":false,"initial_slide":true,"rcq":false,"u_ratings":false,"u_reviews":false,"app_id":{5},"source":"Card Editor","single_widget_mode":true,"card_id":{4},"context":"SINGLE","theme":"native","no_share":true,"show_footer":false,"show_header":false,"freeze":false}}&custom_attributes={{}}&embed_type=1'
VIZ_API_URL = 'http://api.graphiq.com/visualizations/'
VIZ_API_TOKEN = '56cce9e2c44bdb48410000017f508c60058d4ff46d13216f386de51b'

HEADERS = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}


def openCSV(csv_file):
    with open(csv_file,'rb') as input_csv:
        csv_reader = csv.DictReader(input_csv, delimiter=',', quotechar='"')
        rows = [line for line in csv_reader]
        return rows


def sendVizRequest(viz):
    try:
        r = requests.get(URL_TEMPLATE.format(viz['vid'], viz['width'], viz['height'], viz['listing_id'], viz['card_id'], viz['app_id']), headers=HEADERS)
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
        viz['card_id'] = getVizInfo(viz)['card_id']
        response = sendVizRequest(viz)
        no_href = formatEmbedCode(response['embed']['code'])
        viz_output = [viz['name'], no_href]
        print ','.join(map(lambda x: str(x),viz_output))

if __name__ == "__main__":
    main()

