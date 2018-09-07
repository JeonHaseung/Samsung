import re, json, datetime, string, random

from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.core import serializers
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404, HttpResponseRedirect
from django.http.response import HttpResponse, JsonResponse
from django.http.request import QueryDict
from django.shortcuts import get_object_or_404, render, redirect
from django.middleware.csrf import get_token
from django.utils.timezone import make_aware
from django.template import Context
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt


def index(request, template="index.html"):
    coinoneList = [
        "ltc",
        "bch",
        "zrx",
        "qtum",
        "knc",
        "eos",
        "etc",
        "btg",
        "btc",
        "omg",
        "eth",
        "zil",
        "xrp"
    ]
    bithumbList = [
        "LTC",
        "BCH",
        "ZRX",
        "QTUM",
        "KNC",
        "EOS",
        "ETC",
        "BTG",
        "BTC",
        "OMG",
        "ETH",
        "ZIL",
        "XRP"
    ]
    context = {
        "button" : bithumbList,
    }
    return render(request, template, context)

@csrf_exempt
def coin(request):
    context = {}
    c = request.POST.get("which")
    
    f1 = random.random() + random.randrange(-1,1)
    f2 = random.random() + random.randrange(-2,2)
    f3 = random.random() + random.randrange(-4,4)
    f4 = random.random() + random.randrange(-8,8)
    f5 = random.random() + random.randrange(-9,9)
    f6 = random.random() + random.randrange(-10,10)
    
    context["f1"] = f1
    context["f2"] = f2
    context["f3"] = f3
    context["f4"] = f4
    context["f5"] = f5
    context["f6"] = f6
    
    if f1 > 0 :
        context["f1c"] = True
    else:
        context["f1c"] = False
    
    if f2 > 0 :
        context["f2c"] = True
    else:
        context["f2c"] = False
        
    if f3 > 0 :
        context["f3c"] = True
    else:
        context["f3c"] = False
        
    if f4 > 0 :
        context["f4c"] = True
    else:
        context["f4c"] = False
        
    if f5 > 0 :
        context["f5c"] = True
    else:
        context["f5c"] = False
        
    if f6 > 0 :
        context["f6c"] = True
    else:
        context["f6c"] = False
    return JsonResponse(context)

@csrf_exempt
def realtime(request):
    context = {}
    bithumbList = [
        "LTC",
        "BCH",
        "ZRX",
        "QTUM",
        "KNC",
        "EOS",
        "ETC",
        "BTG",
        "BTC",
        "OMG",
        "ETH",
        "ZIL",
        "XRP"
    ]
    n = random.randrange(0,13)
    context["first"] = bithumbList[n%13]
    context["second"] = bithumbList[(n+1)%13]
    context["third"] = bithumbList[(n+2)%13]
    
    return JsonResponse(context)
