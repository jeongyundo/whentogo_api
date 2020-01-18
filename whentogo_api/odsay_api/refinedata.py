

def refinedata(data) :
    c=data['result']
    f3 = dict()
    l2 = list()
    for i in range(0,len(c['path'])):
        f2 = dict()
        t = c['path'][i]['info']['totalTime']

        l = list()
        k = 0
        for j in range(0, len(c['path'][i]['subPath'])):
            f=dict()
            if k == 0 : 
                if c['path'][i]['subPath'][j]['trafficType'] == 3 :
                    name='걷기'#이용 공공수단
                    sectionTime=c['path'][i]['subPath'][j]['sectionTime']
                    startName='현위치'
                    endName=c['path'][i]['subPath'][j+1]['startName']
                elif c['path'][i]['subPath'][j]['trafficType'] == 2 :
                    name='버스' + str(c['path'][i]['subPath'][j]['lane'][0]['busNo'])+'번'#이용 공공수단
                    startName=c['path'][i]['subPath'][j]['startName']
                    endName=c['path'][i]['subPath'][j]['endName']
                    sectionTime=c['path'][i]['subPath'][1]['sectionTime']#걸리는 시간
                elif c['path'][i]['subPath'][j]['trafficType'] == 1 :
                    name='지하철 '+c['path'][i]['subPath'][j]['lane'][0]['name']
                    startName=c['path'][i]['subPath'][j]['startName']
                    endName=c['path'][i]['subPath'][j]['endName']
                    sectionTime=c['path'][i]['subPath'][j]['sectionTime']#걸리는 시간
            elif k+1 == len(c['path'][i]['subPath']) :
                if c['path'][i]['subPath'][j]['trafficType'] == 3 :
                    name='걷기'#이용 공공수단
                    sectionTime=c['path'][i]['subPath'][j]['sectionTime']
                    startName=c['path'][i]['subPath'][j-1]['endName']
                    endName='도착지'
                elif c['path'][i]['subPath'][j]['trafficType'] == 2 :
                    name='버스' + str(c['path'][i]['subPath'][j]['lane'][0]['busNo'])+'번'#이용 공공수단
                    startName=c['path'][i]['subPath'][j]['startName']
                    endName=c['path'][i]['subPath'][j]['endName']
                    sectionTime=c['path'][i]['subPath'][1]['sectionTime']#걸리는 시간
                elif c['path'][i]['subPath'][j]['trafficType'] == 1 :
                    name='지하철 '+c['path'][i]['subPath'][j]['lane'][0]['name']
                    startName=c['path'][i]['subPath'][j]['startName']
                    endName=c['path'][i]['subPath'][j]['endName']
                    sectionTime=c['path'][i]['subPath'][j]['sectionTime']#걸리는 시간
            else :
                if c['path'][i]['subPath'][j]['trafficType'] == 3 :
                    name='걷기'#이용 공공수단
                    sectionTime=c['path'][i]['subPath'][j]['sectionTime']
                    startName=c['path'][i]['subPath'][j-1]['endName']
                    endName=c['path'][i]['subPath'][j+1]['startName']
                elif c['path'][i]['subPath'][j]['trafficType'] == 2 :
                    name='버스' + str(c['path'][i]['subPath'][j]['lane'][0]['busNo'])+'번'#이용 공공수단
                    startName=c['path'][i]['subPath'][j]['startName']
                    endName=c['path'][i]['subPath'][j]['endName']
                    sectionTime=c['path'][i]['subPath'][1]['sectionTime']#걸리는 시간
                elif c['path'][i]['subPath'][j]['trafficType'] == 1 :
                    name='지하철 '+c['path'][i]['subPath'][j]['lane'][0]['name']
                    startName=c['path'][i]['subPath'][j]['startName']
                    endName=c['path'][i]['subPath'][j]['endName']
                    sectionTime=c['path'][i]['subPath'][j]['sectionTime']#걸리는 시간
            if sectionTime != 0 :
                f['name']=name
                f['sectionTime']=sectionTime
                f['startName']=startName
                f['endName']=endName
                l.append(f)
            else :
                f['name']=name
                f['sectionTime']=sectionTime
                f['startName']=startName
                f['endName']=endName
                l.append(f)
            k=k+1
        f2['subpath']=l
        f2['totaltime'] = t
        l2.append(f2)
    f3['result']=l2
    return f3