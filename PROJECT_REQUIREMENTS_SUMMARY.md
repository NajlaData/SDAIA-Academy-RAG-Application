# SDAIA Academy - RAG Application Project Requirements Summary

**Program**: Modern Data Engineering for Advanced AI Systems  
**Project Type**: Full RAG Application  
**Reference**: Day 3 Code Implementation  
**Date**: September 2026

---

## 📋 Executive Summary

Build a **Full Retrieval-Augmented Generation (RAG) Application** combining modern data engineering principles with advanced AI capabilities. The project must demonstrate:

1. ✅ **Data Engineering Excellence**: Kafka streaming, Delta Lake, quality gates
2. ✅ **Advanced Retrieval**: Hybrid search with cross-encoder reranking
3. ✅ **AI Integration**: LLM integration with prompt engineering
4. ✅ **Production Quality**: Orchestration, monitoring, testing, documentation

---

## 🎯 Core Project Requirements

### 1. GitHub Repository Structure

**Required:**
- [ ] Full source code in GitHub repository
- [ ] README.md with project description (see template provided)
- [ ] Day 3 reference code as example
- [ ] Requirements.txt with all dependencies
- [ ] Clear folder structure (see PROJECT_STRUCTURE.md)

**Must Include:**
```
rag-application/
├── app/
│   ├── ingestion/          # Data ingestion layer
│   ├── quality/            # Quality checks
│   ├── storage/            # Delta Lake operations
│   ├── rag/                # RAG components
│   └── main.py             # API entry point
├── dags/                   # Airflow DAGs
├── notebooks/              # Jupyter notebooks
├── tests/                  # Test suite
├── config/                 # Configuration files
├── DAY3_CODE_REFERENCE.py  # Reference implementation
├── requirements.txt        # Dependencies
├── README.md              # Documentation
└── docker-compose.yml     # Infrastructure setup
```

---

## 📚 README.md Requirements

Your README **MUST INCLUDE**:

1. **Program Attribution**
   ```markdown
   **Program**: Modern Data Engineering for Advanced AI Systems
   **Organization**: SDAIA Academy
   **Website**: https://sdaia.gov.sa
   **GitHub**: https://github.com/SDAIAAcademy
   ```

2. **Project Overview**
   - What the project does
   - Why it's relevant to data engineering
   - Key features and benefits

3. **Architecture Diagram**
   - Data flow from ingestion to generation
   - Component interactions
   - Technology stack

4. **Quick Start Guide**
   - Prerequisites
   - Installation steps
   - Running the application
   - Example queries

5. **Key Features**
   - Data ingestion (Kafka streaming)
   - Storage (Delta Lake Bronze/Silver/Gold)
   - Quality gates and validation
   - Hybrid search (BM25 + semantic)
   - Cross-encoder reranking
   - LLM integration
   - Evaluation metrics

6. **Technology Stack**
   - Apache Kafka
   - Delta Lake / Apache Spark
   - Vector databases (FAISS/Weaviate/Pinecone)
   - Embedding models (Sentence Transformers)
   - LLM providers (OpenAI/Anthropic)
   - Orchestration (Apache Airflow)
   - Framework (FastAPI/Gradio/Streamlit)

7. **Testing & Evaluation**
   - How to run tests
   - Evaluation metrics (RAGAS)
   - Example results

8. **Hashtag & Links**
   - #SDAIAAcademy in README
   - Link to SDAIA Academy
   - Contributing guidelines
   - License information

---

## 💻 Day 3 Code Requirements

Your code must demonstrate **Day 3 Advanced RAG Implementation**:

### A. Hybrid Search (Keyword + Semantic)
```python
class HybridRetriever:
    """Combine BM25 keyword search with semantic similarity"""
    
    def __init__(self, documents, bm25_weight=0.5):
        self.bm25_retriever = BM25Retriever(documents)
        self.semantic_retriever = SemanticRetriever(documents)
        self.bm25_weight = bm25_weight
    
    def retrieve(self, query, top_k=5):
        # Get BM25 results
        bm25_results = self.bm25_retriever.retrieve(query)
        
        # Get semantic results
        semantic_results = self.semantic_retriever.retrieve(query)
        
        # Combine and normalize scores
        # Return top_k merged results
```

**Key Implementation Points:**
- [ ] BM25 keyword-based retrieval
- [ ] Semantic similarity with embeddings
- [ ] Score normalization (0-1)
- [ ] Weighted combination
- [ ] Re-ranking merged results
- [ ] Configurable weights

### B. Cross-Encoder Reranking
```python
class CrossEncoderReranker:
    """Two-stage ranking for improved relevance"""
    
    def __init__(self, model_name="cross-encoder/ms-marco-TinyBERT-L-2-v2"):
        self.model = CrossEncoder(model_name)
    
    def rerank(self, query, retrieval_results, top_k=5):
        # Create (query, document) pairs
        pairs = [[query, result.content] for result in retrieval_results]
        
        # Score with cross-encoder
        scores = self.model.predict(pairs)
        
        # Sort by score
        reranked = sorted(zip(retrieval_results, scores), key=lambda x: x[1], reverse=True)
        
        # Return top_k with new scores
        return [result for result, score in reranked[:top_k]]
```

**Key Implementation Points:**
- [ ] Cross-encoder model loading
- [ ] Query-document pair scoring
- [ ] Score computation
- [ ] Result re-ranking
- [ ] Top-k selection
- [ ] Score preservation for metrics

### C. Delta Lake Quality Gates
```python
class DeltaLakeManager:
    """Bronze → Silver → Gold data layers"""
    
    def write_to_bronze(self, records):
        # Raw data ingestion
        # Preserve lineage
        # Store exactly as received
        pass
    
    def merge_to_silver(self, records, merge_key="doc_id"):
        # Deduplicate using MERGE operation
        # Enforce schema
        # MERGE INTO silver AS t
        # USING new_records AS s
        # ON t.doc_id = s.doc_id
        # WHEN MATCHED THEN UPDATE SET *
        # WHEN NOT MATCHED THEN INSERT *
        pass
    
    def publish_to_gold(self, query):
        # Optimized for BI/AI
        # Materialized views
        # Performance tuning
        pass
```

**Key Implementation Points:**
- [ ] Bronze layer (raw data)
- [ ] Silver layer (cleaned, MERGE operations)
- [ ] Gold layer (optimized outputs)
- [ ] Schema enforcement
- [ ] Deduplication logic
- [ ] ACID compliance

### D. End-to-End RAG Pipeline
```python
class RAGPipeline:
    """Complete pipeline integration"""
    
    def __init__(self, documents, llm_client, bm25_weight=0.5):
        self.delta_lake = DeltaLakeManager()
        self.retriever = HybridRetriever(documents, bm25_weight)
        self.reranker = CrossEncoderReranker()
        self.llm_client = llm_client
    
    def query(self, query, top_k=5):
        # 1. Retrieve with hybrid search
        retrieved = self.retriever.retrieve(query, top_k)
        
        # 2. Rerank with cross-encoder
        reranked = self.reranker.rerank(query, retrieved, top_k)
        
        # 3. Prompt engineering
        prompt = self.build_prompt(query, reranked)
        
        # 4. Generate with LLM
        answer = self.llm_client.generate(prompt)
        
        # 5. Return response with metrics
        return RAGResponse(
            query=query,
            answer=answer,
            confidence=compute_confidence(reranked),
            retrieved_docs=reranked
        )
```

**Key Implementation Points:**
- [ ] Component orchestration
- [ ] Error handling
- [ ] Logging at each stage
- [ ] Confidence scoring
- [ ] Metadata collection
- [ ] Response formatting

---

## 🔧 Technical Requirements

### A. Data Ingestion & Processing
- [ ] **Kafka Streaming**: confluent-kafka for resilient ingestion
- [ ] **Data Contracts**: Pydantic for validation
- [ ] **Schema Evolution**: Handle schema changes safely
- [ ] **Dead-Letter Queue**: Route invalid records with logging
- [ ] **Quality Checks**: Automated validation at each stage

### B. Storage Layer
- [ ] **Delta Lake**: ACID-compliant storage
- [ ] **Bronze Layer**: Raw data (immutable)
- [ ] **Silver Layer**: Cleaned, deduplicated data
- [ ] **Gold Layer**: Optimized for AI/BI
- [ ] **Time Travel**: Version history capabilities
- [ ] **Schema Enforcement**: Data type validation

### C. Vector Search & Retrieval
- [ ] **Embeddings**: Generate vector representations
- [ ] **Vector Store**: Store and index embeddings
- [ ] **Hybrid Search**: BM25 + semantic combination
- [ ] **Cross-Encoder Reranking**: Two-stage retrieval
- [ ] **Top-K Selection**: Efficient result filtering
- [ ] **Score Normalization**: Consistent scoring

### D. Generation & LLM
- [ ] **Prompt Engineering**: Optimized prompt templates
- [ ] **LLM Integration**: Support multiple providers
- [ ] **Context Inclusion**: Retrieve documents in prompt
- [ ] **Confidence Scoring**: Measure response quality
- [ ] **Error Handling**: Graceful API failures
- [ ] **Rate Limiting**: Handle API constraints

### E. Orchestration & Monitoring
- [ ] **Apache Airflow**: Workflow orchestration
- [ ] **DAG Definitions**: Ingestion, quality, RAG DAGs
- [ ] **Scheduling**: Regular pipeline execution
- [ ] **OpenLineage**: Data lineage tracking
- [ ] **Logging**: Structured logs throughout
- [ ] **Monitoring**: Metrics and alerts

### F. Testing & Quality
- [ ] **Unit Tests**: Individual component testing
- [ ] **Integration Tests**: End-to-end workflow
- [ ] **RAGAS Evaluation**: RAG quality metrics
- [ ] **Coverage**: >80% code coverage
- [ ] **Fixtures**: Test data and mocks
- [ ] **CI/CD**: Automated testing

---

## 📊 Evaluation Metrics

Your project will be evaluated on:

### A. Code Quality
- [ ] **Style**: Follows PEP 8
- [ ] **Documentation**: Clear docstrings
- [ ] **Modularity**: Reusable components
- [ ] **Error Handling**: Proper exception handling
- [ ] **Logging**: Comprehensive logging

### B. Functionality
- [ ] **Retrieval**: Hybrid search works correctly
- [ ] **Reranking**: Cross-encoder improves results
- [ ] **Generation**: LLM produces coherent answers
- [ ] **Pipeline**: End-to-end integration succeeds
- [ ] **Performance**: Acceptable response times

### C. Data Engineering
- [ ] **Kafka**: Resilient streaming ingestion
- [ ] **Delta Lake**: Proper layering and operations
- [ ] **Quality Gates**: Automated validation
- [ ] **Deduplication**: MERGE operations work
- [ ] **Schema**: Enforcement and evolution

### D. Documentation
- [ ] **README**: Complete and clear
- [ ] **SDAIA Attribution**: Proper acknowledgment
- [ ] **Architecture**: Diagram and explanation
- [ ] **Usage**: Clear examples
- [ ] **Evaluation**: Metrics and results

### E. Testing
- [ ] **Coverage**: >80% code coverage
- [ ] **Unit Tests**: Pass all tests
- [ ] **Integration**: End-to-end success
- [ ] **RAGAS Scores**: Document quality metrics
- [ ] **Evidence**: Test results in notebooks

---

## 📝 Submission Checklist

Before submitting, verify:

### Repository
- [ ] GitHub repository created
- [ ] Code committed with meaningful messages
- [ ] README.md follows template
- [ ] requirements.txt complete
- [ ] .gitignore includes sensitive files
- [ ] LICENSE specified (Apache 2.0 recommended)

### Documentation
- [ ] README mentions "Modern Data Engineering for Advanced AI Systems"
- [ ] SDAIA Academy link included
- [ ] #SDAIAAcademy hashtag in README
- [ ] Architecture diagram present
- [ ] Quick start guide included
- [ ] Technology stack documented

### Code
- [ ] Day 3 reference code implemented
- [ ] All required components present
- [ ] Code follows PEP 8
- [ ] Docstrings for all functions
- [ ] Comprehensive comments
- [ ] No hardcoded secrets

### Testing
- [ ] Unit tests written
- [ ] Integration tests passing
- [ ] Test coverage >80%
- [ ] Tests run successfully
- [ ] Example queries in README

### Evaluation
- [ ] RAGAS metrics computed
- [ ] Example results documented
- [ ] Evaluation notebook included
- [ ] Metrics explained
- [ ] Improvements discussed

### Deployment
- [ ] Docker setup included
- [ ] docker-compose.yml provided
- [ ] Environment variables documented
- [ ] .env.example included
- [ ] Installation instructions clear

---

## 🏆 Excellence Criteria

Projects earning top marks demonstrate:

1. **Advanced Features**
   - Multiple embedding models
   - Custom reranking strategies
   - Advanced prompt engineering
   - Monitoring and alerting

2. **Production Readiness**
   - Error handling and recovery
   - Comprehensive logging
   - Performance optimization
   - Security best practices

3. **Innovation**
   - Novel retrieval techniques
   - Custom evaluation metrics
   - Performance improvements
   - Real-world application

4. **Communication**
   - Clear documentation
   - Informative visualizations
   - Compelling README
   - Professional presentation

---

## 📚 Reference Materials

### SDAIA Academy
- Website: https://sdaia.gov.sa
- GitHub: https://github.com/SDAIAAcademy
- Academy Email: Academy@sdaia.gov.sa

### Day 3 Topics
- Hybrid search architecture
- Cross-encoder reranking
- Delta Lake operations
- Quality gates implementation
- RAG pipeline orchestration

### Technologies
- [Delta Lake Docs](https://docs.delta.io)
- [Apache Kafka](https://kafka.apache.org)
- [Apache Airflow](https://airflow.apache.org)
- [Sentence Transformers](https://www.sbert.net)
- [LangChain RAG](https://python.langchain.com/docs/use_cases/retrieval_augmented_generation/)
- [RAGAS Evaluation](https://github.com/explodinggradients/ragas)

---

## 🎯 Success Criteria

Your project successfully meets requirements if:

✅ GitHub repository contains full RAG application  
✅ README includes SDAIA Academy attribution and links  
✅ Day 3 code reference implemented (hybrid search + reranking)  
✅ All data engineering components present (Kafka, Delta Lake, Airflow)  
✅ Tests pass with >80% coverage  
✅ Documentation is comprehensive and clear  
✅ Project is deployable with Docker  
✅ RAGAS evaluation metrics computed  
✅ Code follows PEP 8 style guide  
✅ Commits include #SDAIAAcademy hashtag  

---

## 📞 Support & Questions

- **SDAIA Academy**: Academy@sdaia.gov.sa
- **GitHub Issues**: Use repository issues for questions
- **Documentation**: Refer to README.md and provided guides

---

## 📄 Final Notes

This is a **Capstone Project** demonstrating mastery of:
- Modern data engineering principles
- Advanced AI/RAG techniques
- Production-grade software development
- Professional documentation and communication

**Quality over quantity** - focus on demonstrating deep understanding of the Day 3 advanced concepts through well-implemented, thoroughly tested, and clearly documented code.

---

**Program**: Modern Data Engineering for Advanced AI Systems  
**Organization**: SDAIA Academy  
**Date**: September 2026  
**#SDAIAAcademy**

---

*Generated by SDAIA Academy Project Requirements System*
