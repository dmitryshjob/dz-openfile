cook_book = {}

with open('cook_book.txt', 'rt', encoding='utf-8') as file:
    
    for i in file:
        dish_name = i.strip()
        ingredients = []
        dish = {dish_name:ingredients}
        ingredients_count = file.readline()
        
        for i in range(int(ingredients_count)):            
            ing = file.readline()
            ingredient_name, quantity, measure = ing.strip().split(' | ')
            ingredients.append({'ingredient_name':ingredient_name,'quantity':quantity,'measure':measure})
       
        line = file.readline() 
        cook_book.update(dish)
print(cook_book)

       
def get_shop_list_by_dishes(dishes, person_count):

    dishes_list = {}
    for dish in dishes:
        for x in cook_book[dish]:
            person = int(x['quantity']) * person_count
            ingredient = {x['ingredient_name']: {'measure': x['measure'], 'quantity': person}}
            dishes_list.update(ingredient)
    return dishes_list       
     
print(get_shop_list_by_dishes(['Запеченный картофель','Утка по-пекински'], 200)) 
    

import os

line_1 = {}
for file in os.listdir('files'):
    with open(os.path.join('files', file), encoding = 'utf8') as f:
        text = f.readlines()   
        line_1[file] = text

line_2 = {} 
for x in sorted(line_1, key = line_1.get, reverse=True):         
    line_2[x] = line_1[x]

for key, value in line_2.items():    
    with open('new_file.txt', 'a', encoding = 'utf8') as f:
        y = len(value)
        f.writelines(f'{key}\n{y}\n')      
        f.writelines(value)
        f.writelines('\n\n')

  
  