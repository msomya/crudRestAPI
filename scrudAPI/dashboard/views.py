from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from dashboard.models import Production
from dashboard.serializers import productionSerializer

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def product_list(request):
    
    if request.method == 'GET':
        product = Production.objects.all()
        serializer = productionSerializer(product, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = productionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def production_detail(request):

	if request.method == 'GET':
		try:
			item = request.GET.get('item', '')
			year = request.GET.get('year', '')
			param = []
			if item != '':
                        	param.append(item)
                	if year != '':
                        	param.append(year)
                	if len(param) == 2:
                        	production = Production.objects.raw("SELECT * FROM production WHERE Item = %s AND year = %s",param)
                	elif len(param) == 1 and item != '':
                        	production = Production.objects.raw("SELECT * FROM production WHERE Item = %s",param)
                	elif len(param) == 1 and year != '':
                        	production = Production.objects.raw("SELECT * FROM production WHERE year = %s",param)
		except Production.DoesNotExist:
                	return HttpResponse(status=404)
        	if len(param) == 2:
                	serializer = productionSerializer(production[0])
                	return JSONResponse(serializer.data)
        	elif len(param) == 1:
                	serializer = productionSerializer(production, many=True)
                	return JSONResponse(serializer.data)


@csrf_exempt
def production_modify(request):

	if request.method == 'PUT':
            data = JSONParser().parse(request)
            try:
                param = []
                if 'item' in data and 'year' in data:
                    param.append(data['item'])
                    param.append(data['year'])
                    production = Production.objects.raw("SELECT * FROM production WHERE Item = %s AND year = %s ",param)
            except Production.DoesNotExist:
                return HttpResponse(status=404)
            serializer = productionSerializer(production[0],data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
                try:
                        item = request.GET.get('item', '')
                        year = request.GET.get('year', '')
                        param = []
                        if item != '':
                                param.append(item)
                        if year != '':
                                param.append(year)
                        if len(param) == 2:
                                production = Production.objects.raw("SELECT * FROM production WHERE item = %s AND year = %s",param)
                                production[0].delete()
                except Production.DoesNotExist:
                        return HttpResponse(status=404)
                return HttpResponse(status=201)

