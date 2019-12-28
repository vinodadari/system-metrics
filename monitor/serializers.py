from rest_framework import serializers

from . import models

class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Metrics
        fields = '_all_'