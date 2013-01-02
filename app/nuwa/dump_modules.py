#!/usr/bin/env python
import os, sys, json

info = []

def nuwabase(root, offset):
    p = root.find("NuWa-trunk/dybgaudi")
    if p>0:
        return root[p+offset:]
    else:
        print "cannot find nuwa install area"
        sys.exit(0)


def process(root, dirs, files):
    if not files: return
    name = nuwabase(root, 39).replace("/", ".")
    if not name: return
    location = os.environ.get(name.split(".")[0].upper()+"ROOT", "")
    if location: 
        location = nuwabase(location, 20)
    for f in files:
        if not f.endswith(".py"): continue
        if f.endswith("_confDb.py"): continue
        if f == "__init__.py":
            info.append({"name": name, "location": location, "extra": "init"})
        elif f.endswith("Conf.py"):
            info.append({"name": name + '.' + f[:-3], "location": location, "extra": "conf"})
        else:
            info.append({"name": name + '.' + f[:-3], "location": location, "extra": ""})

def dump(top_dir):
    # print top_dir
    for root, dirs, files in os.walk(top_dir):
        process(root, dirs, files)
    print json.dumps(info)

if __name__ == '__main__':
    top_dir = os.environ['SITEROOT'] + "/dybgaudi/InstallArea/python"
    dump(top_dir)