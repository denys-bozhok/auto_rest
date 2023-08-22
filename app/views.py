from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import models, serializers


def get_data(some_model, some_serializer, amount, *args):
    match amount:
        case 'singular':
            arg = args[0]
            isinstance = some_model.objects.get(id=arg)
            serialized_data = some_serializer(isinstance).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        
        case 'multi':
            isinstances = some_model.objects.all()
            serialized_data = some_serializer(isinstances, many=True).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        
        case _:
            pass
        
        
def post_data(req, some_model, some_serializer):
    some_model.objects.create(**req.data)
    return Response(some_serializer(some_model.objects.all(), many=True).data)


def put_data(req, some_model, some_serializer, arg):
    imstance = some_model.objects.get(id=arg)
    update_instance = some_serializer(imstance, data=req.data, partial=False)
    update_instance.is_valid()
    update_instance.save()
    return Response(some_serializer(some_model.objects.all(), many=True).data)
    

def patch_data(req, some_model, some_serializer, arg):
    imstance = some_model.objects.get(id=arg)
    update_instance = some_serializer(imstance, data=req.data, partial=True)
    update_instance.is_valid()
    update_instance.save()
    return Response(some_serializer(some_model.objects.all(), many=True).data)


def delete_data(some_model, some_serializer, arg):
    old_model = some_model.objects.get(id=arg)
    old_model.delete()
    return Response(some_serializer(some_model.objects.all(), many=True).data)


@api_view(['GET', 'POST'])
def autos(req):
    match(req.method):
        case 'GET':
            return get_data(models.Auto, serializers.SerializedAuto, 'multi')
        
        case 'POST':
            return post_data(req, models.Auto, serializers.SerializedAuto)
        
        case _:
            pass
        
        
@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def auto(req, arg):
    match(req.method):
        case 'GET':
            return get_data(models.Auto, serializers.SerializedAuto, 'singular', arg)
    
        case 'PUT':
            return put_data(req, models.Auto, serializers.SerializedAuto, arg)
        
        case 'PATCH':
            return patch_data(req, models.Auto, serializers.SerializedAuto, arg)
        
        case 'DELETE':
            return delete_data(models.Auto, serializers.SerializedAuto, arg)
            
        case _:
            pass
        

@api_view(['GET', 'POST'])
def owners(req):
    match(req.method):
        case 'GET':
            
            return get_data(models.Owner, serializers.SerializedOwner, 'multi')
        
        case 'POST':
            req.data['car_number'] = models.AutoPassport.objects.get(id=req.data['car_number'])
            return post_data(req, models.Owner, serializers.SerializedOwner)
        
        case _:
            pass
        

@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def owner(req, arg):
    match(req.method):
        case 'GET':
            return get_data(models.Owner, serializers.SerializedOwner, 'singular', arg)
    
        case 'PUT':
            return put_data(req, models.Owner, serializers.SerializedOwner, arg)
        
        case 'PATCH':
            return patch_data(req, models.Owner, serializers.SerializedOwner, arg)
        
        case 'DELETE':
            return delete_data(models.Owner, serializers.SerializedOwner, arg)
            
        case _:
            pass
        
        
@api_view(['GET', 'POST'])
def auto_passports(req):
    match(req.method):
        case 'GET':
            
            return get_data(models.AutoPassport, serializers.SerializedAutoPassport, 'multi')
        
        case 'POST':
            req.data['related_auto'] = models.Auto.objects.get(id=req.data['related_auto'])
            return post_data(req, models.AutoPassport, serializers.SerializedAutoPassport)
        
        case _:
            pass
        

@api_view(['GET', 'PATCH', 'PUT', 'DELETE'])
def auto_passport(req, arg):
    match(req.method):
        case 'GET':
            return get_data(models.AutoPassport, serializers.SerializedAutoPassport, 'singular', arg)
    
        case 'PUT':
            return put_data(req, models.AutoPassport, serializers.SerializedAutoPassport, arg)
        
        case 'PATCH':
            return patch_data(req, models.AutoPassport, serializers.SerializedAutoPassport, arg)
        
        case 'DELETE':
            return delete_data(models.AutoPassport, serializers.SerializedAutoPassport, arg)
            
        case _:
            pass