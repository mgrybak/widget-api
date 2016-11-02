__author__ = 'Matthew'

'''
Set custom preferences here for new partners
'''


#------------------Registration------------------#

PUBLISHER_NAME = 'RE_DEMO'


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

options_dict = {"wid":"kWnjaJNcFed",
"type":"card",
"title":"",
"dir_name":"",
"dir_url":"",
"publisher_id":"386",
"amazon_id":"",
"w":600,
"h":974,
"limit":100,
"field":"",
"fields":[],
"link_color":"",
"ids":["144389036"],
"filters":[],
"filter_by":[],
"autogeo":False,
"autohide_info":False,
"initial_slide":True,
"rcq":False,
"sort_field":"",
"sort_dir":"",
"app_id":4561,
"source":"Card Editor",
"single_widget_mode":True,
"card_id":3517,
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
elif


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


json_options = json.dumps(options_dict)