from rest_framework import serializers
from odsay_api.models import Gpsdata

class GpsdataSerializer(serializers.Serializer):
  
  sx = serializers.CharField(max_length=50)
  sy = serializers.CharField(max_length=50)
  ex = serializers.CharField(max_length=50)
  ey = serializers.CharField(max_length=50)
  opt = serializers.CharField(max_length=50)
  SearchType = serializers.CharField(max_length=50)
  SearchPathType = serializers.CharField(max_length=50)

  def create(self, validated_data):
    """
    Create and return a new `Snippet` instance, given the validated data.
    """
    return Gpsdata.objects.create(**validated_data)

  def update(self, instance, validated_data):
    """
    Update and return an existing `Snippet` instance, given the validated data.
    """
    instance.sx = validated_data.get('sx', instance.sx)
    instance.sy = validated_data.get('sy', instance.sy)
    instance.ex = validated_data.get('ex', instance.ex)
    instance.ey = validated_data.get('ey', instance.ey)
    instance.opt = validated_data.get('opt', instance.style)
    instance.SearchType = validated_data.get('SearchType', instance.style)
    instance.SearchPathType = validated_data.get('SearchPathType', instance.style)
    instance.save()
    return instance