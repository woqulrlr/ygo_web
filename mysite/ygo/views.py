import wget
import os

from django.shortcuts import render
from  django.forms import model_to_dict

from .models import Card

def index(request):
    # render , parm1 request, parm2 template path
    return render(request, 'ygo/index.html') 


def create(request):
    pass

def read(request):
    # request.POST.get('card_name')
    card_name = request.POST.get('card_name')
    card_info = Card.objects.filter(card_name=card_name)[0]
    card_info = model_to_dict(card_info)
    # dawnload_path = wget.download(card_info['card_images'],'/home/lirui/ygo_web/mysite/static/images')
    # card_info['card_images'] = os.path.join('images', os.path.basename (dawnload_path))
    return render(request, 'ygo/read.html', {'card_info' : card_info}) 

def update(request):
    pass

def delete(request):
    pass