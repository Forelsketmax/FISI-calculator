// Node.js脚本：将CSV转换为JSON
const fs = require('fs');

// 读取CSV文件
const csvContent = fs.readFileSync('9229种食物的FII值.csv', 'utf-8');
const lines = csvContent.trim().split('\n');

const foods = [];

// 跳过标题行，从第2行开始
for (let i = 1; i < lines.length; i++) {
    const line = lines[i].trim();
    if (!line) continue;
    
    // 解析CSV行（处理引号）
    const matches = line.match(/(".*?"|[^,]+)(?=\s*,|\s*$)/g);
    if (!matches || matches.length < 4) continue;
    
    const foodCode = matches[0].replace(/"/g, '').trim();
    const description = matches[1].replace(/"/g, '').trim();
    const fii = parseFloat(matches[2].replace(/"/g, '').trim());
    const fiiScore = parseFloat(matches[3].replace(/"/g, '').trim());
    
    if (foodCode && description && !isNaN(fii)) {
        foods.push({
            Food_code: foodCode,
            Main_food_description: description,
            FII: fii,
            FII_score: fiiScore || 0
        });
    }
}

// 创建data目录
if (!fs.existsSync('data')) {
    fs.mkdirSync('data');
}

// 保存为JSON（紧凑格式）
fs.writeFileSync('data/foods.json', JSON.stringify(foods));

console.log(`✓ 成功转换 ${foods.length} 条食物数据`);
console.log(`✓ 文件已保存: data/foods.json`);

// 显示文件大小
const stats = fs.statSync('data/foods.json');
console.log(`✓ 文件大小: ${(stats.size / 1024).toFixed(2)} KB`);
