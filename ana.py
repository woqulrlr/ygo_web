import json
with open('/home/lirui/ygo_web/ygo_card_info.txt') as f:
    lines = f.readlines()
    lines = json.loads(lines[0])['data']

key_name = set()
for one_card in lines:
    key_name = set(one_card.keys()) | key_name

print(123)

    # {'level', 'type', 'def', 'card_sets', 'card_prices', 'atk', 'name', 'archetype', 'linkmarkers', 
    # 'race', 'id', 'card_images', 'linkval', 'desc', 'scale', 'attribute', 'banlist_info'}

# import sqlite3

# conn = sqlite3.connect('test.db')

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
# VALUES (1, 'Paul', 32, 'California', 20000.00 )");

# conn.commit()

# conn.close()

# for line_key,line_val in enumerate(lines):


# 'card_images' line['card_images'][0]['image_url']
# 'linkmarkers'

import sqlite3
conn = sqlite3.connect('/home/lirui/ygo_web/mysite/db.sqlite3')

def insert_data(col_name_list, row_val_list):
    # conn.execute("INSERT INTO ygo_card (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )");
    col_name_str = ','.join(col_name_list)
    row_val_str = ','.join(row_val_list)
    sql = 'INSERT INTO ygo_card (' + col_name_str + ') VALUES (' + row_val_str + ')'
    conn.execute(sql)
    conn.commit()

def process_int(row_val):
    # int_value_list = {'level', 'def', 'atk', 'id', 'linkval', 'scale'}
    return str(row_val)

def process_str(row_val):
    # int_value_list = {'type', 'name', 'archetype', 'race', 'desc', 'attribute'}
    row_val = "'" + row_val + "'"
    return row_val

def process_card_images(images_url):
    images_url = images_url[0]['image_url']
    row_val = "'" + images_url + "'"
    return row_val

def process_linkmarkers(row_val):
    return str(row_val)

err_dic = {}
crr_dic = []

for line in lines:
    col_name_list = []
    row_val_list = []
    for key in line:
        col_name = key
        row_val = line[key]
        # col_name_list.append('card_' + col_name)
        if col_name in {'level', 'def', 'atk', 'id', 'linkval', 'scale'}:
            col_name_list.append('card_' + col_name)
            row_val_list.append(process_int(row_val))
        # if col_name in {'type', 'name', 'archetype', 'race', 'desc', 'attribute'}:
        # desc 导致很多导入失败，暂时不导入
        if col_name in {'type', 'name', 'archetype', 'race', 'attribute'}:
            col_name_list.append('card_' + col_name)
            row_val_list.append(process_str(row_val))
        if col_name == 'card_images':
            col_name_list.append(col_name)
            row_val_list.append(process_card_images(row_val))
        if process_linkmarkers == 'linkmarkers':
            col_name_list.append('card_' + col_name)
            row_val_list.append(process_linkmarkers(row_val))
    try:
        insert_data(col_name_list, row_val_list)
        # print(line['id'])
        crr_dic.append(line['id'])
    except:
        err_id = line['id']
        col_name_str = ','.join(col_name_list)
        row_val_str = ','.join(row_val_list)
        sql = 'INSERT INTO ygo_card (' + col_name_str + ') VALUES (' + row_val_str + ')'
        err_dic[err_id] = sql
        print(line['id'])
        # print(col_name_list)
        # print(row_val_list)
        # insert_data(col_name_list, row_val_list)
print(123)