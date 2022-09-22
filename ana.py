import json
with open('E:\workspace\code\ygo_card\ygo_card_info_small.txt') as f:
    lines = f.readlines()
    lines = json.loads(lines[0])['data']

key_name = set()
for one_card in lines:
    key_name = set(one_card.keys()) | key_name

print(123)