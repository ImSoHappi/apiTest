from . import models
from rest_framework import serializers

class messageSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.messageModel
        fields = (
            'messages',
        )

