import re
import secrets
from arcpy import GetParameterAsText, SetParameterAsText, AddMessage
import requests

"""
Parameters
input
0 - ExportWebMapService_URL - URL to the export web map service.
(e.g. http://localhost/arcgis/rest/services/DEQEnviro/ExportWebMap/GPServer/Export%20Web%20Map)
1 - Web_Map_as_JSON - Web map JSON txt
2 - Format - e.g. PDF
3 - Layout_Template - e.g. Portrait
output
4 - Output_File - path to the generated file
"""


def switch_quad_words(json):
    match = re.search(ur'discover\.agrc\.utah\.gov\/login\/path\/(.*?)\/', json)
    if match:
        old_quad = match.groups(1)[0]
        return json.replace(old_quad, secrets.OPEN_QUAD_WORD)
    else:
        return json


def make_request(url, webmap, print_format, layout_template):
    response_json = requests.post(format_url(url), data={
        'Web_Map_as_JSON': webmap,
        'Format': print_format,
        'Layout_Template': layout_template,
        'f': 'json'
    }).json()
    if 'error' in response_json.keys():
        raise Exception(response_json['error'])
    else:
        AddMessage(response_json['results'][0]['value']['url'])
        return response_json['results'][0]['value']['url']


def format_url(url):
    if not url.startswith('http'):
        url = 'http://' + url
    return '{}/execute'.format(url)


def url_to_file(url):
    match = re.search(ur'^.*arcgisoutput', url)
    if match:
        return url.replace(match.group(0), secrets.AGS_OUTPUT_DIR).replace('/', '\\')

if __name__ == '__main__':
    # get parameters
    url = GetParameterAsText(0)
    webmap = switch_quad_words(GetParameterAsText(1))
    print_format = GetParameterAsText(2)
    layout_template = GetParameterAsText(3)

    SetParameterAsText(4, url_to_file(make_request(url, webmap, print_format, layout_template)))
