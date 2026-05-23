from rest_framework import serializers
from .models import Blessing

class BlessingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blessing
        fields = '__all__'