"""
Django Rest Framework functions
Serializers and Viewsets for each model
"""
from rest_framework import serializers, viewsets, permissions
from q7.models import Alvo


# Serializers define the API representation..
class AlvoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Alvo
        fields = ['nome', 'latitude', 'longitude', 'expiration_date', 'pk']


# ViewSets define the view behavior.
class AlvoViewSet(viewsets.ModelViewSet):
    queryset = Alvo.objects.all()
    serializer_class = AlvoSerializer
    permission_classes = [permissions.IsAuthenticated]