from rest_framework import serializers
from django.contrib.auth.models import User
from apps.ice2o.models import Modern


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ModernSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modern
        fields = ('modernid', 'rgiid',
                  'glimsid', 'rgiflag', 'bgndate',
                  'enddate', 'cenlon', 'cenlat',
                  'o1region', 'o2region', 'area',
                  'glactype', 'name', 'geom')