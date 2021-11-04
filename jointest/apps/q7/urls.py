from django.urls import path, include
from django.conf.urls import url
from q7 import views, serializers_viewsets
from rest_framework import routers

app_name = 'core_app'

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'alvos', serializers_viewsets.AlvoViewSet)

urlpatterns = [
    url('api/', include(router.urls)),
    path('', views.homepage, name='q7_homepage'),

    path('ajax/create_alvo', views.ajax_create_alvo, name='ajax_create'),
    path('ajax/update_alvo/<int:pk>', views.ajax_update_alvo, name='ajax_update'),
    path('ajax/delete_alvo/<int:pk>', views.ajax_delete_alvo, name='ajax_delete'),
]
