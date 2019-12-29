from rest_framework.serializers import ModelSerializer

from . import models
 
class SubscriberSerializer(ModelSerializer):
    class Meta:
        model = models.Subscriber
        fields = '_all_'

    