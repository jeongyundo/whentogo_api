from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from odsay_api.models import Gpsdata
from odsay_api.serializers import GpsdataSerializer
from odsay_api import useodsayapi
from odsay_api import refinedata
import json
@csrf_exempt
def getGpsdata(request):
    if request.method == 'POST':
        print(request)
        data = JSONParser().parse(request)
        print(data)
        # serializer = GpsdataSerializer(data=data)
        # if serializer.is_valid():
            
        #     serializer.save()
            
        sx = data['sx']
        sy = data['sy']
        ex = data['ex']
        ey = data['ey']
        opt = data['opt']
        SearchType = data['SearchType']
        SearchPathType = data['SearchPathType']
        datafromapi = useodsayapi.findway(sx,sy,ex,ey,opt,SearchType,SearchPathType)
        refindeddata= refinedata.refinedata(json.loads(datafromapi.text))
        print(refindeddata)

        return JsonResponse(refindeddata, status=201)
        return JsonResponse(serializer.errors, status=400)
        


  