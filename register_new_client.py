__author__ = 'Matthew'

import json

'''
Set custom preferences here for new partners
'''


#------------------Registration------------------#

PUBLISHER_NAME = 'RE_DEMO'

DOMAIN = 'www.kabyr.com'

COLOR_THEME = '#3d3d3d'

GMAPS_API_KEY = 'xxxx-xxxxx-xx'


#-----------------Customizations-----------------#

#VIZ TITLE (HEADER) [True/False]
TITLE = False

#DISABLE OUTBOUND LINKS [True/False]
DISABLE_ALL_LINKS = True

#VIZ DESTINATION LINK [NONE/VLP/SEO]
VIZ_DESTINATION_LINK = "NONE"

#NATIVE [True/False]
NATIVE = True

#FOOTER [True/False]
FOOTER = False

#SOURCES [True/False]
SOURCES = False

#SHARE [True/False]
SHARE = False

#COLORS [#HEXCODE]
COLOR_THEME = '#3d3d3d'

#-------------------------------------------------#

#DEFAULT WIDGET OPTIONS

options_dict = {"wid":"kWnjaJNcFed", #Edit viz ID
"type":"card",
"title":"",
"dir_name":"",
"dir_url":"",
"publisher_id":"386", #Edit publisher ID
"amazon_id":"",
"w":600,
"h":600,
"limit":100,
"field":"",
"fields":[],
"link_color":"",
"ids":["144389036"], #Edit listing ID
"filters":[],
"filter_by":[],
"autogeo":False,
"autohide_info":False,
"initial_slide":True,
"rcq":False,
"sort_field":"",
"sort_dir":"",
"app_id":4561, #Edit App ID
"source":"Card Editor",
"single_widget_mode":True,
"card_id":3517, #Edit Card ID
"context":"SINGLE",
"freeze_frequency":"",
"freeze_date":"",
"backlink":False,
"global_no_links":True,
"theme":"native",
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
elif VIZ_DESTINATION_LINK == "SEO"::
    options_dict.pop('global_no_links')

#NATIVE [True/False]
if NATIVE == False:
    options_dict['native'] = False

#FOOTER [True/False]
if FOOTER == true:
    options_dict['show_footer'] = True

#SOURCES [True/False]
if SOURCES == True:
    options_dict['show_sources'] = True

#SHARE [True/False]
if SHARE = True:
    options_dict['no_share'] = False


json_options = json.dumps(options_dict)
