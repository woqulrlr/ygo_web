import json

from django.shortcuts import render, HttpResponse
from .models import Card
from django.http import HttpResponseRedirect
from django.shortcuts import render

def load_txt():
    with open('/home/lirui/ygo_web/ygo_card_info_small.txt') as f:
        lines = f.readlines()
        lines = json.loads(lines[0])['data']
    return lines

def lll(card_info):
    if 'scale' in card_info:
        card_scale = card_info['scale']
    if 'def' in card_info:
        card_def = card_info['def']
    if 'linkval' in card_info:
        card_linkval = card_info['linkval']
    if 'race' in card_info:
        card_race = card_info['race']
    if 'linkmarkers' in card_info:
        card_linkmarkers = card_info['linkmarkers']
    if 'name' in card_info:
        card_name = card_info['name']
    if 'id' in card_info:
        card_id = card_info['id']
    if 'type' in card_info:
        card_type = card_info['type']
    if 'archetype' in card_info:
        card_archetype = card_info['archetype']
    if 'atk' in card_info:
        card_atk = card_info['atk']
    if 'attribute' in card_info:
        card_attribute = card_info['attribute']
    try:
        card = Card(
            # card_scale,
            # card_def,
            card_linkval = card_linkval,
            card_race = card_race,
            card_linkmarkers = card_linkmarkers,
            card_name = card_name,
            card_id = card_id,
            card_type = card_type,
            card_archetype = card_archetype,
            # card_atk,
            card_attribute = card_attribute,
        )
    except:
        print(card_info)
    return Card(
            # card_scale,
            # card_def,
            card_linkval = card_linkval,
            card_race = card_race,
            card_linkmarkers = card_linkmarkers,
            card_name = card_name,
            card_id = card_id,
            card_type = card_type,
            card_archetype = card_archetype,
            # card_atk,
            card_attribute = card_attribute,
        )
    
def index(request):
    info = Card.objects.get(pk=1)
    
    return render(request, 'ygo/index.html')

def insert_data(request):
    lines = load_txt()
    l = []
    for i in lines:
        if i['type'] == "Link Monster":
            l.append(  lll(i) )
    Card.objects.bulk_create(l)  # 批量插入数据
    return render(request, 'ygo/index.html')

def select_data(request):
    cards = Card.objects.all()
    one_card = Card.objects.filter(card_id=86066372)[0]
    return render(request, 'ygo/selectbottom.html', {'cards':cards, 'one_card':one_card})