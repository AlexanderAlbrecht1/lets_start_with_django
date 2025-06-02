from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.utils.text import slugify

from .dummy_data import gadgets

# Create your views here.

def start_page_view(request):
    return HttpResponse('It works!')

def test_page(request):
    return HttpResponse('Test works!')

def single_gadget_view(request, gadget_id):
    return JsonResponse({"result": slugify(gadgets[gadget_id]['name'])})

def single_gadget_slug_view(request, gadget_slug):
    gadget_match = {"resukt": "nothing"}

    for gadget in gadgets:
        if slugify(gadget['name']) == gadget_slug:
            gadget_match = gadget

    return JsonResponse(gadget_match)