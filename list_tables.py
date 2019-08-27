#!/usr/bin/env python3
import copy
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
URL= 'https://192.168.33.3:8445/'
HEADERS= {'Content-Type':'application/json', 'Authorization': 'Basic YWRtaW46YWRtaW4='}

def get_classifier_context(cl_table_name):
    if cl_table_name=='None':
        return '-1'
    #print("getting classifier context")
    url=URL+'restconf/operational/vpp-classifier-context:vpp-classifier-context/classify-table-context/{}'.format(cl_table_name)
    req=requests.get(url,headers=HEADERS,verify=False)
    #print(req.status_code)
    #print(json.dumps(response,indent=4, sort_keys=True))
    if req.status_code==200:
        cl_context = json.loads(req.content)
        table_id=cl_context['classify-table-context'][0]['index']
        return str(table_id)
    else:
        #print("No classify context found for ",cl_table_name)
        return '-1'

def get_next_table(table_name):
    url=URL+'restconf/operational/vpp-classifier:vpp-classifier-state/classify-table/{}'.format(table_name)
    req=requests.get(url,headers=HEADERS,verify=False)
    #print(req.status_code)
    #print(json.dumps(response,indent=4, sort_keys=True))
    if req.status_code==200:
        response = json.loads(req.content)
        if 'next_table' in response['classify-table'][0]:
            return response['classify-table'][0]['next_table']
        else :
            return 'None'

def list_tables(table_name):
    #table4-src-32
    table=table_name
    while get_next_table(table) is not None :
        next_table=get_next_table(table)
        print(table+" ["+get_classifier_context(table)+"] => "+next_table+" ["+get_classifier_context(next_table)+"]")
        table=next_table 


    #printint the classify table along with their next tables
def main():
    print("Listing tables")
    #list_tables('table4-src-29')
    table='table4-src-29'
    next_table=get_next_table(table)
    print(table+" ["+get_classifier_context(table)+"] => "+next_table+" ["+get_classifier_context(next_table)+"]")
    
    table='table4-src-30'
    next_table=get_next_table(table)
    print(table+" ["+get_classifier_context(table)+"] => "+next_table+" ["+get_classifier_context(next_table)+"]")

    table='table4-src-32'
    next_table=get_next_table(table)
    print(table+" ["+get_classifier_context(table)+"] => "+next_table+" ["+get_classifier_context(next_table)+"]")
     


if __name__ == '__main__':
    main()



