#!/usr/bin/env python

import yaml
import git
import os

with open("data.yaml", 'r') as stream:
    try:
        docs = yaml.load_all(stream, Loader=yaml.FullLoader)
    except yaml.YAMLError as exc:
        print(exc)

    for doc in docs:
        
        for k, v in doc.items():
            # print(k)
            # print(k, "->", v)
#            print(doc['mysql'])
            print (doc['mysql']['host'])
            # for k1,v1 in doc['mysql'].items():
            #     print 
#            print(doc['other'])

files = repo.git.diff(None, name_only=True)
for f in files.split('\n'):
    repo.git.add(f)
repo.git.commit('-m', 'This an Auto  Refresh, contact sanith01988',
                author='sanith01988')