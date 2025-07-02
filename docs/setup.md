# ⚙️ Scrapy Project Setup Guide

This guide helps you quickly set up and run the Scrapy web scraping framework locally.

---

## 📦 Prerequisites

Make sure you have:

- Python 3.7 or higher
- `pip` (Python package manager)
- A terminal or command line interface
- (Optional but recommended) `virtualenv`

---

## 🧪 1. Create and Activate Virtual Environment

```bash
python -m venv env
source env/bin/activate       # For macOS/Linux
env\Scripts\activate          # For Windows
```


## 📥 2. Install Scrapy
```bash
python -m venv env
source env/bin/activate       # For macOS/Linux
env\Scripts\activate          # For Windows
```

## 🚀 3. Create a New Scrapy Project
```bash
scrapy startproject scrappy_docs
cd scrappy_docs
```
This creates
```bash
scrappy_docs/
├── scrapy.cfg
└── scrappy_docs/
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders/
```

## 🕷️ 4. Generate a Spider
```bash
cd scrappy_docs/spiders
scrapy genspider quotes quotes.toscrape.com
```

## ▶️ 5. Run the Spider
```bash
cd ../..
scrapy crawl quotes
```
To save output as a JSON file
```bash
scrapy crawl quotes -o output/quotes.json
```
Create the output/ folder first if it doesn't exist:
```bash
mkdir output
```

## 📄 6. Project Folder Structure (After Setup)
```bash
scrappy_docs/
├── scrapy.cfg
├── SETUP.md
├── output/
│   └── quotes.json
└── scrappy_docs/
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders/
        └── quotes.py
```



## ✅ You're Ready!
Now you can:

🕷️ Build more spiders

🛠️ Write custom logic for scraping anything

📤 Export to CSV, JSON, or databases

📄 Document each spider in docs/spiders/*.

PS: _Ill add more details and code on each step as needed._