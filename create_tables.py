#!/usr/bin/env python3
import copy
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
URL= 'https://192.168.33.3:8445/'
CL_TABLE_MEM="104857600"
HEADERS= {'Content-Type':'application/json', 'Authorization': 'Basic YWRtaW46YWRtaW4='}
masks={        
        "table4-src-32":"00:00:00:00:00:00:00:00:00:00:ff:ff:ff:ff:00:00",
        "table4-src-30":"00:00:00:00:00:00:00:00:00:00:ff:ff:ff:fc:00:00",
        "table4-src-29":"00:00:00:00:00:00:00:00:00:00:ff:ff:ff:f8:00:00",
        }
classify_table_dict= {
    "classify-table": [
        {
            "name": "",
            "nbuckets": "2",
            "memory_size": "104857600",
            "miss_next": "permit",
            "skip_n_vectors": "0",
            "mask": ""
        }
    ]
}

def create_classify_table(table_name,next_table=None):
    classify_table=copy.deepcopy(classify_table_dict)
    if next_table is not None:
        classify_table["classify-table"][0]["next_table"]=next_table
    add_classify_table_url=URL+"restconf/config/vpp-classifier:vpp-classifier/classify-table/{0}".format(table_name)
    classify_table["classify-table"][0]["name"]=table_name
    classify_table["classify-table"][0]["memory_size"]=CL_TABLE_MEM
    classify_table["classify-table"][0]["mask"]=masks[table_name]
    classify_table["classify-table"][0]["skip_n_vectors"]=0
    #print("The mask is:"+masks[table_name])
    post_url=add_classify_table_url
    req=requests.put(post_url,headers=HEADERS,verify=False,data=json.dumps(classify_table))
    #print(req.status_code)
    if str(req.status_code) in ['200','201']:
        msg="Created {}".format(table_name)
        if next_table is not None:
            msg+=" with next_table "+next_table
        print(msg)

#print("TEST")
print("Connecting to URL "+URL+"..")
create_classify_table('table4-src-32')
create_classify_table('table4-src-30','table4-src-32')
create_classify_table('table4-src-29','table4-src-30')
    
