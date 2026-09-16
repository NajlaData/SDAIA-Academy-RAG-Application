# أوامر GitHub السريعة - نسخ ولصق مباشرة 📋

**ملاحظة**: استبدل `YOUR_USERNAME` بـ اسم المستخدم GitHub الفعلي

---

## 🚀 الأوامر الأساسية (نسخ ولصق)

### الخطوة 1️⃣: اعمل مجلد المشروع

```bash
mkdir SDAIA-Academy-RAG-Application
cd SDAIA-Academy-RAG-Application
git init
```

### الخطوة 2️⃣: اضف الملفات

```bash
# انسخ كل الملفات اللي أنا أعطيتك في هذا المجلد:
# - README.md
# - DAY3_CODE_REFERENCE.py
# - requirements.txt
# - QUICKSTART.md
# - PROJECT_REQUIREMENTS_SUMMARY.md
# - INDEX.md
# - GITHUB_UPLOAD_GUIDE.md

# تأكد من وجود كل الملفات
ls -la
```

### الخطوة 3️⃣: إعداد Git

```bash
# إذا لم تعمل هذا قبل
git config --global user.name "اسمك الكامل"
git config --global user.email "بريدك الإلكتروني"
```

### الخطوة 4️⃣: أول Commit

```bash
# أضف كل الملفات
git add .

# اعمل commit
git commit -m "Initial commit: Full RAG Application for SDAIA Academy

- Day 3 reference implementation with hybrid search and reranking
- Delta Lake Bronze/Silver/Gold storage layers  
- Comprehensive documentation and setup guides
- Requirements and project structure templates
- SDAIA Academy attribution and links

#SDAIAAcademy"
```

### الخطوة 5️⃣: اربط مع GitHub

```bash
# استبدل YOUR_USERNAME
git remote add origin https://github.com/YOUR_USERNAME/SDAIA-Academy-RAG-Application.git

# غير اسم البرانش من master إلى main
git branch -M main

# ارفع الملفات
git push -u origin main
```

---

## ✅ التحقق من كل شي

```bash
# شيف الملفات المرفوعة
git log --oneline

# شيف الـ remote
git remote -v

# شيف الـ status
git status
```

---

## 📝 أوامر مهمة بعد الرفع

### إذا أضفت ملف جديد:

```bash
git add filename.py
git commit -m "Add filename.py description

#SDAIAAcademy"
git push origin main
```

### إذا عدّلت ملف:

```bash
git add .
git commit -m "Update documentation and add new features

#SDAIAAcademy"
git push origin main
```

### إذا حذفت ملف:

```bash
git rm filename.py
git commit -m "Remove unnecessary file

#SDAIAAcademy"
git push origin main
```

---

## 🔄 Commits نموذجية مع #SDAIAAcademy

```bash
# مثال 1: إضافة feature
git commit -m "Add hybrid search implementation

- Combine BM25 keyword search with semantic similarity
- Implement score normalization and merging
- Add configurable weights for BM25 and semantic search

#SDAIAAcademy"

# مثال 2: إضافة tests
git commit -m "Add comprehensive test suite

- Unit tests for retriever components
- Integration tests for full pipeline
- Test coverage >80%

#SDAIAAcademy"

# مثال 3: تحديث documentation
git commit -m "Update README with evaluation results

- Add RAGAS metrics and results
- Update architecture diagrams
- Add usage examples

#SDAIAAcademy"

# مثال 4: Bug fix
git commit -m "Fix: Handle empty retrieval results gracefully

- Add null checks in reranker
- Improve error messages
- Add logging for debugging

#SDAIAAcademy"
```

---

## 🎯 أوامر يومية أثناء التطوير

```bash
# في بداية اليوم: أحدث الملفات
git pull origin main

# أثناء اليوم: حفظ التغييرات
git add .
git commit -m "Working on: [feature name] description

#SDAIAAcademy"
git push origin main

# نهاية اليوم: التحقق من الحالة
git status
git log --oneline -5
```

---

## 🧪 اختبار الكود قبل الرفع

```bash
# تأكد من أن الكود يشتغل
python DAY3_CODE_REFERENCE.py

# تأكد من المتطلبات
pip install -r requirements.txt

# لما تعمل tests (بعدين)
pytest tests/ -v
```

---

## 🔍 التحقق من Repository على الويب

بعد الرفع، روح:
```
https://github.com/YOUR_USERNAME/SDAIA-Academy-RAG-Application
```

وتفقد:
- [ ] ✅ الملفات موجودة
- [ ] ✅ README يظهر صح
- [ ] ✅ يقول `#SDAIAAcademy`
- [ ] ✅ فيه link لـ SDAIA Academy
- [ ] ✅ الـ License Apache 2.0

---

## 🚨 مشاكل شائعة والحل

### مشكلة 1: `fatal: repository not found`

```bash
# الحل: تأكد من اسم المستخدم صحيح
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME_CORRECT/SDAIA-Academy-RAG-Application.git
git push -u origin main
```

### مشكلة 2: `error: src refspec main does not match any`

```bash
# الحل: أول commit أولاً
git add .
git commit -m "Initial commit"
git push -u origin main
```

### مشكلة 3: `Permission denied`

```bash
# الحل: استخدم SSH أو Personal Access Token
# أو استخدم HTTPS مع token بدل password
git remote set-url origin https://YOUR_USERNAME:YOUR_TOKEN@github.com/YOUR_USERNAME/SDAIA-Academy-RAG-Application.git
```

---

## 📊 Workflow النهائي (كل مرة)

```bash
# 1. شيف الحالة
git status

# 2. أضف التغييرات
git add .

# 3. اعمل commit مع الهاشتاج
git commit -m "Your description here

#SDAIAAcademy"

# 4. ارفع
git push origin main

# 5. تفقد على الويب
# https://github.com/YOUR_USERNAME/SDAIA-Academy-RAG-Application
```

---

## 🎓 أوامر متقدمة (اختيارية)

### اعمل branches للـ features:

```bash
# اعمل branch جديد
git checkout -b feature/hybrid-search

# اشتغل عليه
# ثم ارفعه
git push origin feature/hybrid-search

# وقدم Pull Request في GitHub
```

### اعمل release tag:

```bash
# اعمل tag
git tag -a v1.0.0 -m "First release for SDAIA Academy"

# ارفعه
git push origin v1.0.0
```

### شيف السجل بشكل احترافي:

```bash
# شيف آخر 10 commits
git log --oneline -10

# شيف commits في سطر واحد مع التاريخ
git log --oneline --date=short --format="%h %ad %s"

# شيف commits مع الـ author
git log --oneline --author="Your Name"
```

---

## ✨ نصائح ذهبية

1. ✅ **اكتب رسائل commit واضحة**: "Add X feature" أفضل من "fix"

2. ✅ **أضف #SDAIAAcademy في كل commit**: عشان SDAIA Academy يشوف المشروع

3. ✅ **اعمل commits صغيرة**: كل feature في commit منفصل

4. ✅ **اختبر الكود قبل push**: تجنب breaking changes

5. ✅ **اعمل README حلو**: أول شي يشوفه الناس

6. ✅ **استخدم .gitignore**: ما تنسخ ملفات ما تحتاج

7. ✅ **أضف license**: Apache 2.0 إذا SDAIA Academy

8. ✅ **اعمل documentation**: comments و docstrings

---

## 📋 الملفات اللي تحتاج تنسخها:

```
من الملفات اللي أنا أعطيتك:
✅ README.md
✅ DAY3_CODE_REFERENCE.py
✅ requirements.txt
✅ QUICKSTART.md
✅ PROJECT_REQUIREMENTS_SUMMARY.md
✅ INDEX.md
✅ GITHUB_UPLOAD_GUIDE.md (هذا الملف)
```

وأنت اللي تسوي:
```
📁 app/ (مجلد)
   - main.py
   - config.py
   - ingestion/
   - quality/
   - storage/
   - rag/

📁 tests/ (مجلد)
   - test_rag.py

📁 .github/workflows/ (اختياري)
   - tests.yml

📄 .env.example (file)
📄 .gitignore (من GitHub auto)
📄 LICENSE (من GitHub auto - Apache 2.0)
```

---

## 🎉 بعد الرفع الناجح:

```
✅ Repository created
✅ All files uploaded
✅ README visible
✅ #SDAIAAcademy in commits
✅ SDAIA Academy link present
✅ Tests passing (لما تعمل tests)
✅ Documentation complete
✅ Ready for SDAIA Academy review
```

---

## 🔗 الروابط المهمة:

- **GitHub**: https://github.com/YOUR_USERNAME
- **SDAIA Academy**: https://github.com/SDAIAAcademy
- **SDAIA Website**: https://sdaia.gov.sa
- **Your Repo**: https://github.com/YOUR_USERNAME/SDAIA-Academy-RAG-Application

---

## 💡 اسم Repository الموصى به:

```
أختر واحد:
✅ SDAIA-Academy-RAG-Application
✅ Modern-Data-Engineering-RAG
✅ Masar-RAG-Application
✅ SDAIA-Capstone-RAG-Project

الأهم: في README و commits اكتب #SDAIAAcademy
```

---

**الحمد الله! أنت جاهز الآن! 🚀**

استخدم هذه الأوامر ومشروعك يكون على GitHub في دقائق!

#SDAIAAcademy

---

*نسخ ولصق سريع - September 2026*
