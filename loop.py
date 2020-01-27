#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml

def get_config(*args):
 with open('test-repo.yml', 'r') as f:
     conf = yaml.safe_load(f) 
 
     # get section
     section = args[0]

     # check if Config file has Section
#     if not conf.has_key(section):
     if not section in conf:
         print ("key missing")
         quit()

     # get values
     argList = list(args) # convert tuple to list
     argList.pop(0) # remove Section from list
 
     # create lookup path
     parsepath = "conf['" + section + "']"
 
     for arg in argList:
         parsepath = parsepath + "['" + arg + "']"
     return eval(parsepath)
 f.close()
scans = list(get_config('project','organization'))
for i in range(0,len(scans)):
    scans1=list(get_config('project','organization',scans[i]))
    for j in range(0,len(scans1)):
        scans2=list(get_config('project','organization',scans[i],scans1[j]))
        for k in range(0,len(scans2)):
            scan3=list(get_config('project','organization',scans[i],scans1[j]))
            # print (scans[i],scans1[j],*scan3)
            # print (" ")
            git_url="https://github.developer.io/"+scans[i]+"/"+scans1[j]
            print (git_url)
            print (*scan3)
