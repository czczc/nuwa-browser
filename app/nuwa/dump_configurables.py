#!/usr/bin/env python
import sys, json

info = []

def nuwabase(root, offset):
    p = root.find("NuWa-trunk")
    if p>0:
        return root[p+offset:]
    else:
        print "cannot find nuwa:", root
        sys.exit(0)

def dump():
    from GaudiKernel.ConfigurableDb import cfgDb
    for key, item in cfgDb.items():
        comp = getConfigurable(key)
        props = sorted(comp._properties.keys())
        prop_list = []
        for prop_name in props:
            prop = comp._properties[prop_name]
            try:
                default = str(prop.getDefault())
            except AttributeError:
                default = "unknown"
            doc = prop.__doc__
            if doc == None: doc = ''
            prop_list.append({'name': prop_name, 'value': default, 'doc': doc})
        info.append({
            'name' : key,
            'pkg' : item['package'],
            # 'prop' : prop_list,
        })
        print 'dumping', key
        f = open('configurables/'+key+'.json', 'w')
        f.write(json.dumps(prop_list))
        f.close()

    # from pprint import pprint
    # pprint(info)
    f = open('configurables.json', 'w')
    f.write(json.dumps(info))
    f.close()

if __name__ == '__main__':
    from GaudiKernel.ConfigurableDb import loadConfigurableDb, getConfigurable
    loadConfigurableDb()
    dump()