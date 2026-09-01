# FISI Calculator

> Food Inflammation Scores of Individuals Calculator

A web-based FISI calculator designed to help users assess the inflammatory potential of their diet. It supports fuzzy searching across 9,931 food items, real-time calculation of FISI values, and automatic classification of pro-inflammatory or anti-inflammatory status.

## 🌟 Online Demo

- **GitHub Pages**: https://forelsketmax.github.io/FISI-calculator/

## ✨ Features

- 🔍 **Fuzzy Search**: Quickly search among 9,931 food items using Fuse.js
- 📊 **Real-Time Calculation**: Calculates FISI in real time using the formula `FISI = Σ(Intake/100 × FII)`
- 🎯 **Inflammatory Status Classification**:
  - FISI ≥ -6.76: Pro-inflammatory status (displayed in red)
  - FISI < -6.76: Anti-inflammatory status (displayed in green)
- 📱 **Responsive Design**: Fully compatible with both desktop and mobile devices
- 🎨 **Medical Research Style**: Professional, clean, and intuitive user interface
- ⚡ **No Build Tools Required**: Pure HTML/Python/JavaScript, with no need for npm or webpack

## 📦 Project Structure

```text
fisi-calculator/
├── index.html              # Main page
├── data/
│   └── foods.json          # Data for 9,931 food items
├── convert-csv-to-json.js  # Data conversion script
├── README.md               # Project documentation
└── .gitignore              # Git ignore file
```

## 🚀 Quick Start

### Method 1: Run Locally

1. Clone or download this project.
2. Start a local server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve

# Using PHP
php -S localhost:8000
```

3. Open `http://localhost:8000` in your browser.

### Method 2: Deploy to GitHub Pages

1. Fork this project or create a new repository.
2. Upload all project files to the repository.
3. Enable GitHub Pages in the repository settings.
4. Select the deployment branch, usually `main`, and the root directory.
5. Visit https://forelsketmax.github.io/FISI-calculator/

### Method 3: Deploy to Vercel

1. Visit [Vercel](https://vercel.com).
2. Import the GitHub repository or directly drag and drop the project folder.
3. Deployment will be completed automatically.
4. A free HTTPS domain will be provided.

## 📖 Instructions for Use

### 1. Search for Foods

- Enter a food name or food code in the search box.
- English fuzzy search is supported, such as `milk`, `chicken`, or `rice`.
- The top 10 best-matching results will be displayed automatically.

### 2. Add Foods

- Click a food item in the search results.
- Enter the intake amount in grams.
- Click the "Add to Recipe" button.

### 3. View Results

- **Total FISI Score**: Calculated and displayed in real time
- **Inflammatory Status**: Automatically classified as pro-inflammatory or anti-inflammatory
- **Recipe List**: Displays all food items that have been added

### 4. Manage the Recipe

- Click ❌ to remove an individual food item.
- Click "Clear All" to remove all food items.

## 🧮 Calculation Formula

```text
FISI = Σ(Intake/100 × FII)
```

**Example Calculation**:

- Milk, whole - 200 g, FII = -0.0775
- Chicken, breast - 150 g, FII = -0.0520

```text
Contribution of Food 1 = 200/100 × (-0.0775) = -0.155
Contribution of Food 2 = 150/100 × (-0.0520) = -0.078
Total FISI Score = -0.155 + (-0.078) = -0.233
```

Result: FISI = -0.233 > -6.76, therefore classified as **pro-inflammatory**.

## 🛠️ Technology Stack

- **Frontend**: Pure HTML/CSS/JavaScript
- **UI Framework**: Tailwind CSS (CDN)
- **Search Engine**: Fuse.js (CDN)
- **Data Format**: JSON
- **Deployment**: Static website hosting

## 📊 Data Description

### Data Source

- Includes FII data for 9,931 food items
- Data are derived from FNDDS (Food and Nutrient Database for Dietary Studies)

### Data Fields

- **Food_code**: Food code (8-digit number)
- **Main_food_description**: Food description in English
- **FII**: Food Inflammation Index
- **FII score**: FII score

## 🔧 Development Guide

### Regenerate the JSON Data

If the dataset needs to be updated, run the conversion script:

```bash
node convert-csv-to-json.js
```

This will generate `data/foods.json` from `9231种食物的FII值.csv`.

### Modify the Calculation Formula

Locate the `handleAddFood` function in [`index.html`](index.html:245):

```javascript
// Current formula: FISI = Σ(Intake/100 × FII)
const contribution = (amount / 100) * selectedFood.FII;
```

### Modify the Classification Threshold

Locate the `updateDashboard` function in [`index.html`](index.html:295):

```javascript
const threshold = -6.76;  // Modify this value
```

## 🌐 Browser Compatibility

- ✅ Chrome/Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Mobile browsers

## 📝 Frequently Asked Questions

### Q: Why are there no search results?

A: Please make sure that:

- At least 2 characters are entered
- English keywords are used, as the database is in English
- More general keywords are tried

### Q: What should I do if the data fail to load?

A: Please check:

- Whether the `data/foods.json` file exists
- Whether the project is being run through a local server instead of opening the HTML file directly
- Whether there are any error messages in the browser console

### Q: Can I save my recipe?

A: The current version supports data persistence and can display historical FISI records.

## 🚧 Future Plans

- [ ] Export functionality (PDF/CSV)
- [ ] Multi-day dietary records and trend analysis
- [ ] Nutrient composition analysis
- [ ] PWA support for offline use

## 📄 License

This project is intended for educational and research purposes only. Food data are derived from publicly available databases.

## 📧 Contact

If you have any questions or suggestions, please contact us through one of the following methods:

- Submit an [Issue](https://github.com/Forelsketmax/FISI-calculator/issues)
- Send an email to 2545010438@stu.ahmu.edu.cn

## 🙏 Acknowledgements

- [Tailwind CSS](https://tailwindcss.com/) - UI framework
- [Fuse.js](https://fusejs.io/) - Fuzzy search library
- [FNDDS](https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/food-surveys-research-group/docs/fndds/) - Food data source

---

⭐ If you find this project useful, please give it a Star!
