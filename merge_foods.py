import pandas as pd
import json

# 读取现有的9229种食物数据
with open('data/foods.json', 'r', encoding='utf-8') as f:
    existing_foods = json.load(f)

# 读取额外的702种食物
new_foods_df = pd.read_excel('额外计算702种食物FII.xlsx')

# 转换为字典列表
new_foods = []
for _, row in new_foods_df.iterrows():
    food = {
        'Food_code': str(int(row['Food_code'])),
        'Main_food_description': row['Main_food_description'],
        'FII': float(row['FII']),
        'FII_score': float(row['FII_score'])
    }
    new_foods.append(food)

# 合并数据（去重，以Food_code为准）
existing_codes = {f['Food_code'] for f in existing_foods}
merged_foods = existing_foods.copy()

for food in new_foods:
    if food['Food_code'] not in existing_codes:
        merged_foods.append(food)

# 保存合并后的数据
with open('data/foods.json', 'w', encoding='utf-8') as f:
    json.dump(merged_foods, f, ensure_ascii=False)

print(f'原有食物: {len(existing_foods)}')
print(f'新增食物: {len(merged_foods) - len(existing_foods)}')
print(f'合并后总数: {len(merged_foods)}')
