from django.db import models

# class CardInfoManager(models.Manager):
#     def create_book(self, card_info):
#         if 'scale' in card_info:
#             card_scale = card_info['scale']
#         if 'def' in card_info:
#             card_def = card_info['def']
#         if 'linkval' in card_info:
#             card_linkval = card_info['linkval']
#         if 'race' in card_info:
#             card_race = card_info['race']
#         if 'linkmarkers' in card_info:
#             card_linkmarkers = card_info['linkmarkers']
#         if 'name' in card_info:
#             card_name = card_info['name']
#         if 'id' in card_info:
#             card_id = card_info['id']
#         if 'type' in card_info:
#             card_type = card_info['type']
#         if 'archetype' in card_info:
#             card_archetype = card_info['archetype']
#         if 'atk' in card_info:
#             card_atk = card_info['atk']
#         if 'attribute' in card_info:
#             card_attribute = card_info['attribute']
#         card = self.create(
#             card_scale,
#             card_def,
#             card_linkval,
#             card_race,
#             card_linkmarkers,
#             card_name,
#             card_id,
#             card_type,
#             card_archetype,
#             card_atk,
#             card_attribute,
#         )
#         return card

class Card(models.Model):
    card_scale = models.IntegerField(blank = True, null=True)#灵摆刻度
    card_def = models.IntegerField(blank = True, null=True)
    card_linkval = models.IntegerField(blank = True, null=True)
    card_race = models.CharField(max_length=20, blank = True, null=True)#种族   
    card_linkmarkers = models.CharField(max_length=50, blank = True, null=True)#连接箭头
    card_name = models.CharField(max_length=50, blank = True, null=True)
    card_id = models.IntegerField(blank = True, null=True)
    card_type = models.CharField(max_length=50, blank = True, null=True)#卡牌类型
    card_archetype = models.CharField(max_length=50, blank = True, null=True)#字段
    card_atk = models.IntegerField(blank = True, null=True)
    card_level = models.IntegerField(blank = True, null=True)
    card_attribute = models.CharField(max_length=50, blank = True, null=True)#属性
    card_images = models.CharField(max_length=500, blank = True, null=True)#字段
    card_desc = models.TextField(max_length=1000, blank = True, null=True)#字段

    def __str__(self):
        return self.card_nameclear

    # objects = CardInfoManager()

    # {'level', 'type', 'def', 'card_sets', 'card_prices', 'atk', 'name', 'archetype', 'linkmarkers', 
    # 'race', 'id', 'card_images', 'linkval', 'desc', 'scale', 'attribute', 'banlist_info'}