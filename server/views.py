from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from server.serializers import PersonSerializers, UserSerializer
from server.models import Person
from django.contrib.auth.models import User
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers


def index(request):
    return render(request, 'index.html')

def dm(request):
    if request.is_ajax():
        print('dmmmm')
        context = {}
        person = Person.objects.all()[:10]
        # data = Person.objects.all().values('name').distinct()[:3]
        print('minhkma')
        for id,use in enumerate(person):
            context['user_{}'.format(id)] = use.name
        json_data = json.dumps(context)
    return HttpResponse(json_data, content_type="application/json")



