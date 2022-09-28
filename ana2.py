import json
with open('/home/lirui/ygo_web/ygo_card_info.txt') as f:
    lines = f.readlines()
    lines = json.loads(lines[0])['data']

# key_name = set()
# for one_card in lines:
#     key_name = set(one_card.keys()) | key_name

# {'level', 'type', 'def', 'card_sets', 'card_prices', 'atk', 'name', 'archetype', 'linkmarkers', 
# 'race', 'id', 'card_images', 'linkval', 'desc', 'scale', 'attribute', 'banlist_info'}


import sqlite3
conn = sqlite3.connect('/home/lirui/ygo_web/mysite/db.sqlite3')

def insert_data(col_name_list, row_val_list):
    # conn.execute("INSERT INTO ygo_card (card_id,card_name,card_type,card_desc,card_race,card_archetype,card_images) VALUES (?,?,?,?,?,?,?)",(row_val_list));
    col_str = ','.join(col_name_list)
    values_zw =','.join(['?']*len(col_name_list))
    sql = "INSERT INTO ygo_card (" + col_str + ") VALUES (" + values_zw + ")"
    conn.execute(sql,(row_val_list))
    conn.commit()

def process_card_images(images_url):
    return images_url[0]['image_url']
    # row_val = "'" + images_url + "'"
    # return row_val

def process_linkmarkers(row_val):
    return str(row_val)

total_lines = len(lines)
for index, line in enumerate(lines):
    col_name_list = []
    row_val_list = []
    for key in line:
        col_name = key
        row_val = line[key]
        # derect insert
        if col_name in {'level', 'def', 'atk', 'id', 'linkval', 'scale','type', 'name', 'archetype', 'race', 'desc', 'attribute'}:
            col_name_list.append('card_' + col_name)
            row_val_list.append(row_val)
        # list -> str
        if col_name == 'card_images':
            col_name_list.append(col_name)
            row_val_list.append(process_card_images(row_val))
        # list -> str
        if process_linkmarkers == 'linkmarkers':
            col_name_list.append('card_' + col_name)
            row_val_list.append(process_linkmarkers(row_val))
    try:
        insert_data(col_name_list, row_val_list)
    except:
        print(col_name_list)
        print(row_val_list)
    print(str(index) + "/" + str(total_lines))