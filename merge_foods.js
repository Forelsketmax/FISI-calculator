const fs = require('fs');
const XLSX = require('xlsx');

// 读取现有的9229种食物数据
const existingFoods = JSON.parse(fs.readFileSync('data/foods.json', 'utf-8'));

// 读取额外的702种食物
const workbook = XLSX.readFile('额外计算702种食物FII.xlsx');
const sheetName = workbook.SheetNames[0];
const worksheet = workbook.Sheets[sheetName];
const newFoodsData = XLSX.utils.sheet_to_json(worksheet);

// 转换新食物数据
const newFoods = newFoodsData.map(row => ({
    Food_code: String(row.Food_code),
    Main_food_description: row.Main_food_description,
    FII: parseFloat(row.FII),
    FII_score: parseFloat(row.FII_score)
}));

// 合并数据（去重）
const existingCodes = new Set(existingFoods.map(f => f.Food_code));
const mergedFoods = [...existingFoods];

newFoods.forEach(food => {
    if (!existingCodes.has(food.Food_code)) {
        mergedFoods.push(food);
    }
});

// 保存合并后的数据
fs.writeFileSync('data/foods.json', JSON.stringify(mergedFoods, null, 0), 'utf-8');

console.log(`原有食物: ${existingFoods.length}`);
console.log(`新增食物: ${mergedFoods.length - existingFoods.length}`);
console.log(`合并后总数: ${mergedFoods.length}`);
