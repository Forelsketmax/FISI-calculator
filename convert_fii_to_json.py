#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FII数据CSV转JSON预处理脚本
将9229种食物的FII值CSV转换为精简的JSON文件
"""

import pandas as pd
import json
import os


# 配置常量
INPUT_CSV = '9229种食物的FII值.csv'
OUTPUT_JSON = 'fisi-calculator/public/data/foods.json'


def get_file_size(filepath):
    """获取文件大小（KB）"""
    size_bytes = os.path.getsize(filepath)
    return size_bytes / 1024


def convert_csv_to_json():
    """主转换函数"""
    try:
        # 1. 读取CSV文件
        print(f'正在读取CSV文件: {INPUT_CSV}')
        df = pd.read_csv(INPUT_CSV, encoding='utf-8')
        
        # 2. 数据清理 - 只保留前4列
        df = df.iloc[:, :4]
        
        # 重命名列
        df.columns = ['Food_code', 'Main_food_description', 'FII', 'FII_score']
        
        # 3. 数据类型转换
        df['Food_code'] = df['Food_code'].astype(str)
        df['Main_food_description'] = df['Main_food_description'].astype(str)
        df['FII'] = pd.to_numeric(df['FII'], errors='coerce')
        df['FII_score'] = pd.to_numeric(df['FII_score'], errors='coerce')
        
        # 移除可能的空值行
        df = df.dropna()
        
        print(f'数据行数: {len(df)}')
        
        # 4. 转换为字典列表
        data_list = df.to_dict(orient='records')
        
        # 5. 创建输出目录
        os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
        
        # 6. 保存为JSON文件（紧凑格式）
        print(f'正在转换为JSON...')
        with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
            json.dump(
                data_list,
                f,
                ensure_ascii=False,
                separators=(',', ':')
            )
        
        print(f'✓ JSON文件已保存: {OUTPUT_JSON}')
        
        # 7. 显示文件大小对比
        csv_size = get_file_size(INPUT_CSV)
        json_size = get_file_size(OUTPUT_JSON)
        compression_rate = (1 - json_size / csv_size) * 100
        
        print('\n文件大小对比:')
        print(f'  CSV:  {csv_size:.2f} KB')
        print(f'  JSON: {json_size:.2f} KB')
        print(f'  压缩率: {compression_rate:.1f}%')
        
        # 8. 显示数据示例
        print('\n数据示例（前3条）:')
        for i, item in enumerate(data_list[:3], 1):
            print(f'  {i}. {item}')
        
        return True
        
    except FileNotFoundError:
        print(f'错误: 找不到文件 {INPUT_CSV}')
        print(f'请确保文件位于当前目录: {os.getcwd()}')
        return False
        
    except Exception as e:
        print(f'错误: {type(e).__name__}: {e}')
        return False


def main():
    """主函数"""
    print('=' * 60)
    print('FII数据CSV转JSON预处理脚本')
    print('=' * 60)
    print()
    
    success = convert_csv_to_json()
    
    print()
    print('=' * 60)
    if success:
        print('✓ 转换完成！')
    else:
        print('✗ 转换失败')
    print('=' * 60)


if __name__ == '__main__':
    main()
