import sys
import re
import os
import urllib
sys.path.append('..')
from confs.conf import conf

def parseListUrl(url):
    listset = []
    url = parseIndex(url)


    patt = r'\[([0-9]+)-([0-9]+)\]'
    for i in url:
        if i==None:
            continue
        match = re.search(patt,i, re.M|re.I)
        if match:
            pagestart = match.group(1)
            pageend = match.group(2)
            urli = re.sub(patt, '<{page}>', i)
            if pagestart and pageend :
                for j in range(int(pagestart),int(pageend)+1):
                    listset.append(urli.replace('<{page}>',str(j)))
        else:
            listset.append(i)
    print len(listset)
    #os._exit(0)
    return tuple(listset)

def parseIndex(url):
    listset = []
    if conf['isindex']:
        for e in conf['index']:
            for i in conf['index'][e]:
                for u in url:
                    urli = u.replace('<{'+e+'}>',urllib.quote(str(i)))
                    listset.append(urli)
        return tuple(listset)
    else:
        return url

def urlencode(str):
    #str = str.decode('gbk')
    urllib.quote(str)