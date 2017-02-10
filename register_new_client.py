__author__ = 'Matthew'

import json, sys
from add_vizzes_api import *

'''
Set custom preferences here for new partners
'''

with open(sys.argv[1]) as preferences_file:    
    preferences = json.load(preferences_file)['data'][0]


#------------------Client Data------------------#

PUBLISHER_NAME = preferences['publisher_name']

PID = preferences['pid']


#-----------------Customizations-----------------#


#VIZ TITLE (HEADER) [True/False]
if preferences['title'] == 'true':
	TITLE = True
else:
	TITLE = False

#DISABLE OUTBOUND LINKS [True/False]
if preferences['disable_links'] == 'true':
	DISABLE_ALL_LINKS = True
else:
	DISABLE_ALL_LINKS = False

#VIZ DESTINATION LINK [NONE/VLP/SEO]
VIZ_DESTINATION_LINK = preferences['destination_link']

#NATIVE [True/False]
if preferences['native'] == 'true':
	NATIVE = True
else:
	NATIVE = False

#FOOTER [True/False]
if preferences['show_footer'] == 'true':
	FOOTER = True
else:
	FOOTER = False

#SOURCES [True/False]
if preferences['show_sources'] == 'true':
	SOURCES = True
else:
	SOURCES = False

#SHARE [True/False]
if preferences['show_share'] == 'true':
	SHARE = True
else:
	SHARE = False

#-------------------------------------------------#

#DEFAULT WIDGET OPTIONS

options_dict = {"wid":"", #Edit viz ID
"type":"card",
"title":"",
"dir_name":"",
"dir_url":"",
"publisher_id":"", #Edit publisher ID
"amazon_id":"",
"w":"100%",
"h":500,
"limit":100,
"field":"",
"fields":[],
"link_color":"",
"ids":[], #Edit listing ID
"filters":[],
"filter_by":[],
"autogeo":False,
"autohide_info":False,
"initial_slide":True,
"rcq":False,
"sort_field":"",
"sort_dir":"",
"app_id":"", #Edit App ID
"source":"api",
"single_widget_mode":True,
"card_id":"", #Edit Card ID
"context":"SINGLE",
"freeze_frequency":"",
"freeze_date":"",
"backlink":False,
"global_no_links":True,
"theme":"native",
"theme_dombo":"null",
"show_header":False,
"show_footer":False,
"show_sources":False,
"no_share":True}

#VIZ TITLE (HEADER) [True/False]
if TITLE == True:
    options_dict['show_header'] = True

#DISABLE OUTBOUND LINKS [True/False]
if DISABLE_ALL_LINKS == False:
    options_dict.pop('global_no_links')

#VIZ DESTINATION LINK [NONE/VLP/SEO]
if VIZ_DESTINATION_LINK == "VLP":
    options_dict['wlp'] = True
elif VIZ_DESTINATION_LINK == "SEO":
    options_dict.pop('global_no_links')

#NATIVE [True/False]
if NATIVE == False:
    options_dict['native'] = False

#FOOTER [True/False]
if FOOTER == True:
    options_dict['show_footer'] = True

#SOURCES [True/False]
if SOURCES == True:
    options_dict['show_sources'] = True

#SHARE [True/False]
if SHARE == True:
    options_dict['no_share'] = False

#Publisher ID
options_dict['publisher_id'] = PID

#Theme Combo
options_dict['theme_combo'] = PUBLISHER_NAME

#-------------------------------------------------#

package_csv = sys.argv[2]


if __name__ == "__main__":
	viz_rows = openCSV(package_csv)
	tracker_import = []
	prog_api_import = []
	for viz in viz_rows:
	    if 'card_id' in getVizInfo(viz).keys():
	        viz_info = getVizInfo(viz)
	        
			#Input new details into options_dict
	        options_dict['card_id'] = viz_info['card_id']
	        options_dict['app_id'] = viz_info['app_id']
	        options_dict['ids'] = [viz_info['listing_ids'][0]]
	        options_dict['wid'] = viz['vid']

	        	
	        new_widget_response = sendVizRequest(viz_info['app_id'],json.dumps(options_dict))
	        to_tracker = {"title":viz['description'],"widget_name":viz['name'],"widget_id":new_widget_response['id'],"publisher":PUBLISHER_NAME,"pid":PID,"json_widget_options":'{"type":"' + viz['api_topic'] + '", "add-ad-tag":false}',"style":'font:14px/16px arial;color:#339933;',"anchor_text":'More Details | FindTheHome',"date_issued":time.strftime('%Y-%m-%d %H:%M:%S'),"template_widget_id":viz['vid']}
	        tracker_import.append(to_tracker)
	        to_prog = {"title":viz['description'],"widget_name":viz['name'],"widget_id":new_widget_response['id'],"publisher":PUBLISHER_NAME,"pid":PID,"json_widget_options":'{"type":"' + viz['api_topic'] + '", "add-ad-tag":false}',"style":'font:14px/16px arial;color:#339933;',"anchor_text":'More Details | FindTheHome'}
	        prog_api_import.append(to_prog)
	        print "Successfully added new visualization {} for {}".format(new_widget_response['id'],viz['name'])
	        print ",".join(map(lambda x: '"' + str(x) + '"', [new_widget_response['id'],viz['description'],viz['name'],viz['vid']]))
	    else:
	        print "Error forking visualization {} for {}".format(new_widget_response['id'],viz['name'])
	        sys.exit(1)
	#sendToTopic(tracker_import,11738)
	#sendToTopic(prog_api_import,6876)


