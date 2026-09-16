# SDAIA Academy RAG Application - Quick Start Guide

**Program:** Modern Data Engineering for Advanced AI Systems  
**Reference:** Day 3 Advanced RAG Implementation

---

## 📋 Prerequisites

Before starting, ensure you have:

- **Python 3.9+** installed
- **Docker & Docker Compose** (for infrastructure)
- **Git** for version control
- **API Keys** (optional, for LLM providers):
  - OpenAI API Key (if using GPT models)
  - Anthropic API Key (if using Claude)
  - Hugging Face Token (for Sentence Transformers)

---

## 🚀 Quick Setup (5 minutes)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rag-application.git
cd rag-application
```

### 2. Create Virtual Environment

```bash
# Create
python -m venv venv

# Activate
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your settings
# nano .env  (or use your editor)
```

**Minimal .env example:**
```
# LLM Configuration
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=your-api-key-here

# Vector Database
VECTOR_DB_TYPE=faiss

# Kafka (if using local)
KAFKA_BOOTSTRAP_SERVERS=localhost:9092

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
```

### 5. Start Infrastructure (Optional - for full pipeline)

```bash
# Start Kafka, Zookeeper, and other services
docker-compose up -d

# Verify services are running
docker-compose ps
```

---

## 🏃 Running the RAG Application

### Option A: Minimal Setup (File-based, No Infrastructure)

Perfect for testing locally without Kafka/Docker:

```bash
# Run the Day 3 reference implementation
python DAY3_CODE_REFERENCE.py
```

**Output:**
```
================================================================================
SDAIA Academy - Modern Data Engineering for Advanced AI Systems
Day 3: Advanced RAG Implementation
================================================================================

Query: What is hybrid search?
--------------------------------------------------------------------------------
Confidence: 0.85

Answer:
Based on the provided context, modern data engineering is a critical discipline...

Top Retrieved Documents:
  [1] Hybrid Search Architecture
      Retrieval Score: 0.80
      Rerank Score: 0.85
  [2] Cross-Encoder Reranking
      Retrieval Score: 0.75
      Rerank Score: 0.78
```

### Option B: Start RAG API Server

```bash
# Start FastAPI server
python app/main.py

# Server starts at http://localhost:8000
```

**Test the API:**

```bash
# Query the RAG application
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is modern data engineering?",
    "top_k": 5,
    "retrieval_method": "hybrid"
  }'
```

**Response:**
```json
{
  "query": "What is modern data engineering?",
  "answer": "Based on the provided context...",
  "confidence": 0.87,
  "retrieved_docs": [
    {
      "doc_id": "doc_001",
      "title": "Modern Data Engineering Fundamentals",
      "retrieval_score": 0.82,
      "rerank_score": 0.87,
      "final_rank": 1
    }
  ],
  "metadata": {
    "retrieval_method": "hybrid",
    "reranking_method": "cross_encoder",
    "num_retrieved": 5,
    "avg_rerank_score": 0.87
  }
}
```

### Option C: Interactive Gradio Interface

```bash
# Start Gradio web UI
python app/gradio_app.py

# Open browser to http://localhost:7860
```

### Option D: Full Pipeline with Airflow

```bash
# Initialize Airflow
airflow db init

# Start Airflow webserver
airflow webserver --port 8080

# In another terminal, start the scheduler
airflow scheduler

# Access Airflow UI at http://localhost:8080
# Trigger DAGs through the UI
```

---

## 📚 Next Steps

### 1. Explore the Code Reference

```bash
# Read the Day 3 implementation
cat DAY3_CODE_REFERENCE.py

# Key classes to understand:
# - HybridRetriever: Combining BM25 + semantic search
# - CrossEncoderReranker: Two-stage ranking
# - RAGPipeline: End-to-end orchestration
```

### 2. Load Your Own Documents

```python
from app.pipeline import RAGPipeline

# Load your documents
my_docs = [
    {
        "doc_id": "doc_001",
        "title": "Your Title",
        "content": "Your content here...",
        "metadata": {}
    }
]

# Initialize pipeline
rag = RAGPipeline(documents=my_docs)

# Query
response = rag.query("Your question here")
print(response.answer)
```

### 3. Evaluate Your RAG System

```bash
# Run evaluation notebook
jupyter notebook notebooks/04_rag_evaluation.ipynb

# Key metrics to evaluate:
# - Faithfulness (answer grounded in context)
# - Answer Relevance (answer addresses query)
# - Context Relevance (retrieved docs are relevant)
```

### 4. Configure Embedding Models

Edit `config/embedding_models.yaml`:
```yaml
models:
  default: "sentence-transformers/all-MiniLM-L6-v2"
  options:
    - name: "sentence-transformers/all-mpnet-base-v2"
      dimension: 768
      speed: "slow"
      quality: "high"
```

### 5. Configure LLM Provider

Edit `config/llm.yaml`:
```yaml
provider: "anthropic"
model: "claude-3-sonnet-20240229"
temperature: 0.7
max_tokens: 2048
```

---

## 🧪 Testing

### Run All Tests

```bash
# Run complete test suite
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html
```

### Run Specific Tests

```bash
# Test retrieval components
pytest tests/test_rag.py::TestHybridRetriever -v

# Test storage layer
pytest tests/test_storage.py -v

# Test integration
pytest tests/test_integration.py -v
```

---

## 🐛 Troubleshooting

### Issue: "No module named 'pyspark'"

**Solution:**
```bash
pip install pyspark
```

### Issue: "FAISS IndexFlatL2 error"

**Solution:**
```bash
pip install --upgrade faiss-cpu
# or for GPU:
pip install --upgrade faiss-gpu
```

### Issue: "Kafka connection error"

**Solution:**
```bash
# Check if Docker containers are running
docker-compose ps

# Restart services
docker-compose restart
```

### Issue: "API Key not found"

**Solution:**
```bash
# Verify .env file exists and contains your key
cat .env

# Set via environment variable
export ANTHROPIC_API_KEY="your-key"
```

### Issue: "Port 8000 already in use"

**Solution:**
```bash
# Use different port
python app/main.py --port 8001

# Or kill existing process
lsof -ti:8000 | xargs kill -9
```

---

## 📊 Project Structure Quick Reference

```
rag-application/
├── app/
│   ├── main.py              # Start here: API entry point
│   ├── pipeline.py          # Core RAG pipeline
│   └── rag/
│       ├── retriever.py     # Hybrid search logic
│       ├── reranker.py      # Cross-encoder reranking
│       └── llm_client.py    # LLM integration
├── notebooks/
│   └── 04_rag_evaluation.ipynb  # See notebook for full flow
├── tests/
│   └── test_rag.py          # Example tests
├── DAY3_CODE_REFERENCE.py   # Start here: Reference implementation
├── README.md                # Full documentation
└── requirements.txt         # Dependencies
```

---

## 🎯 Common Commands Cheat Sheet

```bash
# Environment management
source venv/bin/activate          # Activate virtual env
deactivate                        # Deactivate

# Installation
pip install -r requirements.txt   # Install dependencies
pip freeze > requirements.txt     # Update requirements

# Running code
python DAY3_CODE_REFERENCE.py    # Run reference implementation
python app/main.py               # Start API server
jupyter notebook                 # Start Jupyter

# Testing
pytest tests/ -v                 # Run all tests
pytest tests/ -k "test_hybrid"   # Run specific test

# Docker
docker-compose up -d             # Start services
docker-compose down              # Stop services
docker-compose logs -f           # View logs

# Git
git status                       # Check status
git add .                        # Stage changes
git commit -m "message"          # Commit
git push origin main             # Push to remote
```

---

## 📖 Learning Path

1. **Start Here**: Run `python DAY3_CODE_REFERENCE.py`
   - Understand basic RAG flow
   - See hybrid search + reranking in action

2. **Explore**: Read `README.md`
   - Architecture overview
   - Component descriptions
   - Best practices

3. **Experiment**: Modify `DAY3_CODE_REFERENCE.py`
   - Change BM25 weights
   - Try different embedding models
   - Adjust reranking strategy

4. **Implement**: Build `app/main.py`
   - Add your documents
   - Set up API endpoints
   - Deploy with Docker

5. **Evaluate**: Run `notebooks/04_rag_evaluation.ipynb`
   - Measure retrieval quality
   - Assess generation quality
   - Identify improvements

---

## 🚀 Deployment

### Deploy with Docker

```bash
# Build Docker image
docker build -t rag-app:latest .

# Run container
docker run -p 8000:8000 \
  -e ANTHROPIC_API_KEY="your-key" \
  rag-app:latest

# Push to registry
docker tag rag-app:latest your-registry/rag-app:latest
docker push your-registry/rag-app:latest
```

### Deploy to Cloud

```bash
# Kubernetes
kubectl apply -f k8s-deployment.yaml

# AWS Lambda (with modifications)
# GCP Cloud Run
# Azure Container Instances
```

---

## 📞 Getting Help

- **Issues**: Open GitHub issue with details
- **Discussion**: Use GitHub Discussions
- **SDAIA Academy**: Contact Academy@sdaia.gov.sa
- **Documentation**: Read README.md

---

## ✅ Checklist

Before submitting:

- [ ] Code follows PEP 8 style guide
- [ ] Tests pass: `pytest tests/ -v`
- [ ] README includes SDAIA Academy reference
- [ ] Include #SDAIAAcademy hashtag in commits
- [ ] Documentation is complete
- [ ] Example usage in README
- [ ] Docker setup works
- [ ] Environment variables are documented
- [ ] API has proper error handling
- [ ] Logging is comprehensive

---

## 🎓 SDAIA Academy Reference

- **Program**: Modern Data Engineering for Advanced AI Systems
- **Website**: https://sdaia.gov.sa
- **GitHub**: https://github.com/SDAIAAcademy
- **Contact**: Academy@sdaia.gov.sa

#SDAIAAcademy

---

*Last Updated: September 2026*
