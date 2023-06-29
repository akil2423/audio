from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AudioSerializer
from .models import Audio
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Detail View':'/audio-detail/<str:pk>/',
		'Create':'/audio-create/',
		'Update':'/audio-update/<str:pk>/',
		'Delete':'/audio-delete/<str:pk>/',
		'Detail-start' : '/audio-detail-start/',
		}

	return Response(api_urls)


@api_view(['GET'])
def audioDetail(request, pk):
	audio = Audio.objects.get(id=pk)
	serializer = AudioSerializer(audio, many=False)
	print(serializer.data)
	context={
    "id": serializer.data["id"],
    "url": serializer.data["url"],
    "volume": serializer.data["volume"],  # High volume no overlap
    "type":  serializer.data["type"], 
    "duration": {
        "start_time":  serializer.data["start_time"], 
        "end_time":  serializer.data["end_time"], 
	}
    }

	return Response(context)


@api_view(['POST'])
def audioCreate(request):
	print(request.data)
	serializer = AudioSerializer(data=request.data)
	print(serializer)

	if serializer.is_valid():
		serializer.save()
	print(serializer.data)
	context={
    "id": serializer.data["id"],
    "url": serializer.data["url"],
    "volume": serializer.data["volume"],  # High volume no overlap
    "type":  serializer.data["type"], 
    "duration": {
        "start_time":  serializer.data["start_time"], 
        "end_time":  serializer.data["end_time"], 
	}
    }
	return Response(context)

@api_view(['POST'])
def audioUpdate(request, pk):
	audio = Audio.objects.get(id=pk)
	serializer = AudioSerializer(instance=audio, data=request.data)
	
	if serializer.is_valid():
		serializer.save()
		context={
    "id": serializer.data["id"],
    "url": serializer.data["url"],
    "volume": serializer.data["volume"],  # High volume no overlap
    "type":  serializer.data["type"], 
    "duration": {
        "start_time":  serializer.data["start_time"], 
        "end_time":  serializer.data["end_time"], 
	}
    }

	return Response(context)


@api_view(['DELETE'])
def audioDelete(request, pk):
	audio = Audio.objects.get(id=pk)
	audio.delete()

	return Response('Item succsesfully delete!') #throw error cuz delete


@api_view(['GET'])
def audioDetailWithStartTime(request):
	start_time= request.GET.get('start')
	end_time=request.GET.get('end')
	# audio = Audio.objects.filter(start_time=start_time,end_time=end_time)
	audio = Audio.objects.filter(start_time__gte=start_time).filter(end_time__lte=end_time)
	serializer = AudioSerializer(audio, many=True)
	print(serializer.data)


	return Response(serializer.data)


