from django.shortcuts import render

import json

from django.views.generic.base import View
# from search.models import LagouType
from django.http import HttpResponse
# from elasticsearch import Elasticsearch
from datetime import datetime
# import redis


# Create your views here.

class IndexView(View):
    def get(self,request):
        return render(request, "index.html")