from django.conf.urls import url, include
from server import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'person', views.PersonViewSet)


urlpatterns = [
    url('home/', views.index, name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^ajax/top/$', views.dm, name='top'),
]