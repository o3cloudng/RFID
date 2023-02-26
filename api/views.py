from django.shortcuts import render
# from rest_framework.generics import CreateAPIView
from rest_framework import mixins
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from api.models import ApiData
from api.serializers import ApiCreateSerializer
from member.models import Member
from device.models import Device
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes


class ApiCreateApiView(ListCreateAPIView):
    serializer_class = ApiCreateSerializer
    queryset = ApiData.objects.all()
    authentication_classes = []

    def post(self, request):
        try:
            member = Member.objects.get(tag_id=request.data["tag_id"])
            request.data["tag_id"] = member.id
        except Member.DoesNotExist:
            return Response({'error': 'Member does not exists'})
        try:
            device = Device.objects.get(device_id=request.data["device_id"])
            request.data["device_id"] = device.id
        except Device.DoesNotExist:
            return Response({'error': 'Device does not exists'})

        timestamp = request.POST.get("timestamp")

        print(f"MEMBER: {member.firstname}, DEVICE: {device.location} - TIME: {timestamp}")
        serializer = ApiCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()


        print("REQUEST DATA: ", request.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        data =  ApiData.objects.all()
        return self.list(request, data)


# @api_view(["POST", "GET"])
# @authentication_classes("")
# # @permission_classes("")
# def apidata_view(request):
#     if request.method == "POST":
        
#         try:
#             member = Member.objects.get(tag_id=request.data["tag_id"])
#             request.data["tag_id"] = member.id
#         except Member.DoesNotExist:
#             return Response({'error': 'Member does not exists'})
#         try:
#             device = Device.objects.get(device_id=request.data["device_id"])
#             request.data["device_id"] = device.id
#         except Device.DoesNotExist:
#             return Response({'error': 'Device does not exists'})

#         timestamp = request.POST.get("timestamp")
#         print(f"MEMBER: {member.firstname}, DEVICE: {device.location} - TIME: {timestamp}")
#         serializer = ApiCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#     if request.method == "GET":
#         apidata = ApiData.objects.all()
#         # serializer = ApiCreateSerializer(data=apidata, many=True)
#         # serializer.is_valid(raise_exception = True)
#         return Response(apidata, status=status.HTTP_200_OK)