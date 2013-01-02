#!/usr/bin/env python
import os, sys, json

info = []

def nuwabase(root, offset):
    p = root.find("NuWa-trunk")
    if p>0:
        return root[p+offset:]
    else:
        print "cannot find nuwa:", root
        sys.exit(0)

def dump():
    packages = [key for key in os.environ.keys() if key.endswith("ROOT")]

    for package in packages:
        location = os.environ[package]
        if location.find("NuWa-trunk") == -1: continue
        if not location.find("../") == -1: continue
        location = nuwabase(location, 11)
        if location == "": continue
        info.append({
            'name' : location.split("/")[-1],
            'location' : location,
        })
    # from pprint import pprint
    # pprint(info)
    print json.dumps(info)

if __name__ == '__main__':
    dump()