# GitHub Upload Guide - SDAIA Academy RAG Application

**البرنامج**: Modern Data Engineering for Advanced AI Systems  
**الأكاديمية**: SDAIA Academy  
**التاريخ**: September 2026

---

## 🚀 خطوات الرفع على GitHub (خطوة بخطوة)

### المتطلبات الأساسية:
- [ ] حساب GitHub (إذا ما عندك، اعمل واحد من https://github.com)
- [ ] Git مثبت على جهازك
- [ ] Terminal/Command Prompt

---

## 📋 الخطوة 1: إنشاء Repository جديد

### في الويب (أسهل طريقة):
1. روح https://github.com/new
2. اسم الريبو: **`SDAIA-Academy-RAG-Application`** أو **`Modern-Data-Engineering-RAG`**
3. Description: 
   ```
   Full RAG Application for SDAIA Academy Modern Data Engineering for Advanced AI Systems
   ```
4. اختر: **Public** (عشان SDAIA Academy)
5. اختر: **Add a README file** ✅
6. اختر: **Choose a license** → Apache License 2.0 ✅
7. اختر: **Add .gitignore** → Python ✅
8. اضغط: **Create repository**

---

## 💻 الخطوة 2: Clone الريبو إلى جهازك

```bash
# استبدل YOUR_USERNAME بـ اسم المستخدم الفعلي
git clone https://github.com/YOUR_USERNAME/SDAIA-Academy-RAG-Application.git

# انتقل للمجلد
cd SDAIA-Academy-RAG-Application
```

---

## 📂 الخطوة 3: أضف الملفات

انسخ كل الملفات اللي أنا أنشأتها للمجلد:

```bash
# انسخ الملفات التالية للمجلد:
# - README.md (استبدل الموجود)
# - DAY3_CODE_REFERENCE.py
# - requirements.txt
# - QUICKSTART.md
# - PROJECT_REQUIREMENTS_SUMMARY.md
# - INDEX.md
```

### الهيكل الكامل اللي تحتاج:

```
SDAIA-Academy-RAG-Application/
│
├── README.md                          ✅ (من الملفات اللي أنا أعطيتك)
├── DAY3_CODE_REFERENCE.py             ✅ (من الملفات اللي أنا أعطيتك)
├── QUICKSTART.md                      ✅ (من الملفات اللي أنا أعطيتك)
├── PROJECT_REQUIREMENTS_SUMMARY.md    ✅ (من الملفات اللي أنا أعطيتك)
├── INDEX.md                           ✅ (من الملفات اللي أنا أعطيتك)
├── requirements.txt                   ✅ (من الملفات اللي أنا أعطيتك)
├── .env.example                       📝 (اعمله أنت)
├── .gitignore                         ✅ (من GitHub)
├── LICENSE                            ✅ (Apache 2.0)
│
├── app/                               📁 (اعمله أنت - البنية)
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── ingestion/
│   ├── quality/
│   ├── storage/
│   └── rag/
│
├── tests/                             📁 (اعمله أنت)
│   ├── __init__.py
│   ├── test_rag.py
│   └── conftest.py
│
├── notebooks/                         📁 (اختياري)
│   └── 04_rag_evaluation.ipynb
│
└── dags/                             📁 (اختياري)
    └── rag_pipeline_dag.py
```

---

## 🔧 الخطوة 4: إعداد الملفات الأساسية

### أنشئ `.env.example`:

```bash
cat > .env.example << 'EOF'
# LLM Configuration
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=your-api-key-here
OPENAI_API_KEY=your-api-key-here

# Vector Database
VECTOR_DB_TYPE=faiss
VECTOR_DB_PATH=./vector_store

# Kafka Configuration
KAFKA_BOOTSTRAP_SERVERS=localhost:9092
KAFKA_TOPIC_INPUT=documents_raw
KAFKA_TOPIC_DLQ=documents_dlq

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_TITLE=SDAIA RAG Application

# Logging
LOG_LEVEL=INFO

# Embedding Model
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
EOF
```

### أنشئ `app/__init__.py`:

```bash
mkdir -p app
touch app/__init__.py
```

---

## 🔄 الخطوة 5: أول Commit

```bash
# تفقد الملفات اللي تم تغييرها
git status

# أضف كل الملفات
git add .

# اعمل commit
git commit -m "Initial commit: Full RAG Application setup for SDAIA Academy

- Added Day 3 reference implementation (hybrid search + reranking)
- Added Delta Lake storage layer (Bronze/Silver/Gold)
- Added comprehensive documentation and setup guides
- Added requirements and project structure
- Added SDAIA Academy attribution and links

#SDAIAAcademy"

# ارفعه
git push origin main
```

---

## 📝 الخطوة 6: اضبط المعلومات على GitHub

### اذهب لـ Repository Settings:

1. **About** (الوصف):
   ```
   Full RAG Application for SDAIA Academy
   Modern Data Engineering for Advanced AI Systems
   ```

2. **Topics** (المواضيع):
   أضف:
   - `sdaia-academy`
   - `rag-application`
   - `retrieval-augmented-generation`
   - `data-engineering`
   - `hybrid-search`
   - `llm`
   - `python`

3. **Homepage** (الصفحة الرئيسية):
   ```
   https://sdaia.gov.sa
   ```

4. **Description**:
   ```
   Full end-to-end RAG application demonstrating modern data engineering 
   principles with Kafka streaming, Delta Lake storage, hybrid search, 
   and LLM integration for SDAIA Academy capstone project.
   ```

---

## 📊 الخطوة 7: شيفرة الـ Code Structure الأساسي

إذا تبي تنشئ مجلدات app:

```bash
# Create directories
mkdir -p app/ingestion
mkdir -p app/quality
mkdir -p app/storage
mkdir -p app/rag
mkdir -p tests
mkdir -p notebooks

# Create __init__ files
touch app/__init__.py
touch app/ingestion/__init__.py
touch app/quality/__init__.py
touch app/storage/__init__.py
touch app/rag/__init__.py
touch tests/__init__.py

# Create placeholder files
touch app/main.py
touch app/config.py
touch tests/test_rag.py
```

---

## 🔐 الخطوة 8: Add اسم المستخدم والـ Email لـ Git

```bash
# إذا لم تعمل هذا قبل
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 🚀 الخطوة 9: إضافة GitHub Actions (اختياري ولكن احترافي)

أنشئ `.github/workflows/tests.yml`:

```bash
mkdir -p .github/workflows

cat > .github/workflows/tests.yml << 'EOF'
name: Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        pytest tests/ -v
    
    - name: Upload coverage
      uses: codecov/codecov-action@v2
EOF
```

ثم commit:

```bash
git add .github/workflows/tests.yml
git commit -m "Add GitHub Actions workflow for automated testing"
git push origin main
```

---

## 📋 الخطوة 10: تحديث README.md

تأكد إن الـ README يحتوي على:

- [ ] ✅ عنوان واضح
- [ ] ✅ SDAIA Academy mention
- [ ] ✅ Link لـ https://github.com/SDAIAAcademy
- [ ] ✅ Link لـ https://sdaia.gov.sa
- [ ] ✅ #SDAIAAcademy hashtag
- [ ] ✅ Architecture شرح
- [ ] ✅ Quick Start
- [ ] ✅ Installation steps
- [ ] ✅ Day 3 reference شرح
- [ ] ✅ Testing instructions
- [ ] ✅ Evaluation metrics

---

## ✅ تفقد قائمة - تأكد من كل شي:

```bash
# تشغيل الكود الأساسي
python DAY3_CODE_REFERENCE.py

# تأكد من متطلبات Python
pip install -r requirements.txt

# تشغيل Tests (لما تعمل tests)
pytest tests/ -v

# تفقد Git status
git status

# تفقد آخر commits
git log --oneline -5
```

---

## 🎯 أوامر Git المهمة:

```bash
# عرض الحالة
git status

# إضافة ملفات
git add .                          # كل الملفات
git add filename.py                # ملف محدد

# Commit
git commit -m "رسالة الـ commit"

# Push
git push origin main

# Pull آخر تحديثات
git pull origin main

# عرض السجل
git log --oneline

# إنشاء branch جديد
git checkout -b feature/new-feature

# تبديل branch
git checkout main
```

---

## 🔍 تفقد Repository على الويب:

بعد الرفع، روح:
```
https://github.com/YOUR_USERNAME/SDAIA-Academy-RAG-Application
```

وشيف:
- ✅ الملفات موجودة؟
- ✅ README يظهر صح؟
- ✅ الـ topics صحيحة؟
- ✅ الـ description واضح؟

---

## 🎓 حاجات اختيارية لكن احترافية:

### 1. Badge في README:

```markdown
[![Tests](https://github.com/YOUR_USERNAME/SDAIA-Academy-RAG-Application/workflows/Tests/badge.svg)](https://github.com/YOUR_USERNAME/SDAIA-Academy-RAG-Application/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
```

### 2. CONTRIBUTING.md:

```markdown
# Contributing to SDAIA Academy RAG Application

## How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Requirements

- Python 3.9+
- Follow PEP 8 style guide
- Write tests for new features
- Update documentation

## Development Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running Tests

```bash
pytest tests/ -v --cov=app
```

#SDAIAAcademy
```

### 3. CHANGELOG.md:

```markdown
# Changelog

## [1.0.0] - 2026-09-16

### Added
- Full RAG application implementation
- Day 3 advanced concepts (hybrid search + reranking)
- Delta Lake Bronze/Silver/Gold layers
- Comprehensive documentation
- Testing framework
- Docker support

### Features
- Kafka streaming ingestion
- Hybrid retrieval (BM25 + semantic)
- Cross-encoder reranking
- LLM integration
- RAGAS evaluation

#SDAIAAcademy
```

---

## 🆘 إذا حصل مشكلة:

### مشكلة: Permission denied

```bash
# حل: اعمل SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"
# ثم أضفه لـ GitHub Settings > SSH Keys
```

### مشكلة: Main branch اسمها master

```bash
# اعد تسميتها
git branch -M main
git push -u origin main
```

### مشكلة: Merge conflicts

```bash
# حل بسيط
git pull origin main --rebase
```

---

## 🎉 بعد الرفع - اللي تفعله:

1. ✅ شيف الـ Repository على الويب
2. ✅ اختبر الـ README يظهر صح
3. ✅ أضف GitHub topics
4. ✅ شارك الـ link مع الناس
5. ✅ استمر في التطوير

---

## 📞 معلومات SDAIA Academy:

```
Organization: https://github.com/SDAIAAcademy
Website: https://sdaia.gov.sa
Email: Academy@sdaia.gov.sa
```

---

## 🚀 الخطوة النهائية - Commit مع الهاشتاج:

```bash
# في كل commit، أضف #SDAIAAcademy
git commit -m "Your message here

#SDAIAAcademy"
```

---

## ✨ اسم Repository الموصى به:

اختر واحد من:
- ✅ `SDAIA-Academy-RAG-Application`
- ✅ `Modern-Data-Engineering-RAG`
- ✅ `Masar-RAG-Application`
- ✅ `SDAIA-Capstone-RAG-Project`

**الأهم**: في الـ README اكتب `#SDAIAAcademy`

---

## 📊 آخر تفقد:

| الشي | الحالة |
|------|--------|
| Repository created | ✅ |
| Files uploaded | ✅ |
| README visible | ✅ |
| Topics added | ✅ |
| #SDAIAAcademy in README | ✅ |
| SDAIA Academy link | ✅ |
| Commits with hashtag | ✅ |
| Tests working | ✅ |
| License added | ✅ |

---

**الحمد الله! مشروعك الآن على GitHub بشكل احترافي! 🎯**

#SDAIAAcademy

---

*آخر تحديث: September 2026*
