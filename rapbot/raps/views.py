# Create your views here.
from django.shortcuts import render_to_response
from raps.models import Rap

from django.http import HttpResponse

def index(request):
  rap_to_print = Rap.objects.get(pk = 1).make_rap()
  return render_to_response('raps/index.html',{'rap_to_print':rap_to_print})
