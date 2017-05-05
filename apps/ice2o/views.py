from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import (viewsets, decorators)
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

from django.contrib.auth.models import User
from apps.ice2o.models import Modern

from apps.ice2o.serializers import UserSerializer
from apps.ice2o.serializers import ModernSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
@decorators.permission_classes((AllowAny,))
def modern_list(request):
    """
    List all modern
    """
    if request.method == 'GET':
        id_str = request.GET['ids']
        id_list = [int(id) for id in id_str.split(',')]
        print(id_list)
        modern = Modern.objects.filter(modernid__in=id_list)
        serializer = ModernSerializer(modern, many=True)
        return JsonResponse(serializer.data, safe=False)
