from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models

class messageViewSet(viewsets.ModelViewSet):

    queryset = models.messageModel.objects.all()
    serializer_class = serializers.messageSerializer