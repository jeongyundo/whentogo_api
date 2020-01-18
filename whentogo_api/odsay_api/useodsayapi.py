import requests
from urllib import parse
def findway(sx,sy,ex,ey,opt=0, SearchType=0, SearchPathType=0):
    url = "https://api.odsay.com/v1/api/searchPubTransPath?SX="+sx+"&SY="+sy+"&EX="+ex+"&EY="+ey+"&opt="+opt+"&SearchType="+SearchType+"&SearchPathType="+SearchPathType+"&apiKey="
    key = parse.quote("1k17H9TBEOvtjVhwJmsbl+r7Cg0BJbniUDNif/6dcW4")
    res = requests.get(url+key)
    print(res)
    return res
