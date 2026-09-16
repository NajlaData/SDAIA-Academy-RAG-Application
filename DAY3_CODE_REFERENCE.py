"""
SDAIA Academy - Modern Data Engineering for Advanced AI Systems
Day 3: Advanced RAG Implementation with Hybrid Search & Reranking

This module demonstrates the core RAG components introduced on Day 3:
- Hybrid search (keyword + semantic)
- Cross-Encoder reranking
- Delta Lake quality operations
- End-to-end RAG pipeline

Reference: Day 3 Curriculum - Advanced RAG Architecture
"""

import json
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Tuple, Dict, Any, Optional

import numpy as np
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# DATA MODELS & CONTRACTS (Day 3: Quality Gates)
# ============================================================================

class DocumentContract(BaseModel):
    """Pydantic contract for document validation"""
    doc_id: str = Field(..., description="Unique document identifier")
    title: str = Field(..., description="Document title")
    content: str = Field(..., description="Document content")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    timestamp: str = Field(..., description="Document ingestion timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "doc_id": "doc_001",
                "title": "Data Engineering Fundamentals",
                "content": "Data engineering is...",
                "metadata": {"source": "academy", "category": "tutorial"},
                "timestamp": "2026-09-16T10:00:00Z"
            }
        }


@dataclass
class RetrievalResult:
    """Result from retrieval stage"""
    doc_id: str
    content: str
    title: str
    score: float
    rank: int
    retrieval_method: str  # "bm25", "semantic", or "hybrid"


@dataclass
class RankedResult:
    """Result after reranking"""
    doc_id: str
    content: str
    title: str
    retrieval_score: float
    rerank_score: float
    final_rank: int


@dataclass
class RAGResponse:
    """Final RAG response with full context"""
    query: str
    answer: str
    confidence: float
    retrieved_docs: List[RankedResult]
    metadata: Dict[str, Any]


# ============================================================================
# STORAGE LAYER: Delta Lake Operations (Day 3)
# ============================================================================

class DeltaLakeManager:
    """Manages Bronze/Silver/Gold layers with Delta Lake"""
    
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.bronze_path = f"{base_path}/bronze"
        self.silver_path = f"{base_path}/silver"
        self.gold_path = f"{base_path}/gold"
        logger.info(f"Initialized Delta Lake at {base_path}")
    
    def write_to_bronze(self, records: List[Dict], mode: str = "append"):
        """
        Bronze Layer: Raw data ingestion
        - Preserves data exactly as received
        - Maintains full lineage
        """
        logger.info(f"Writing {len(records)} records to Bronze layer")
        # In real implementation: write with PySpark to Delta
        # df.write.format("delta").mode(mode).save(self.bronze_path)
        return {"layer": "bronze", "records": len(records), "status": "success"}
    
    def merge_to_silver(self, records: List[Dict], merge_key: str = "doc_id"):
        """
        Silver Layer: Deduplicated, quality-assured data
        - UPSERT operation based on merge_key
        - Removes duplicates
        - Enforces schema
        """
        logger.info(f"Merging {len(records)} records to Silver layer (merge key: {merge_key})")
        # In real implementation: MERGE operation
        # MERGE INTO silver_table t
        # USING new_records s
        # ON t.doc_id = s.doc_id
        # WHEN MATCHED THEN UPDATE SET *
        # WHEN NOT MATCHED THEN INSERT *
        return {"layer": "silver", "records": len(records), "status": "merged"}
    
    def publish_to_gold(self, query: str) -> List[Dict]:
        """
        Gold Layer: Optimized for BI and AI consumption
        - Materialized views for performance
        - Aggregated data for analytics
        """
        logger.info(f"Publishing data to Gold layer with query: {query}")
        # In real implementation: run query on silver and materialize
        return []


# ============================================================================
# RETRIEVAL: Hybrid Search (Day 3)
# ============================================================================

class BM25Retriever:
    """BM25 Keyword-based retrieval"""
    
    def __init__(self, documents: List[Dict]):
        self.documents = documents
        self._build_index()
    
    def _build_index(self):
        """Build BM25 index from documents"""
        logger.info(f"Building BM25 index for {len(self.documents)} documents")
        # In real implementation: use rank-bm25 library
        # self.bm25 = BM25Okapi([doc["content"].split() for doc in self.documents])
    
    def retrieve(self, query: str, top_k: int = 5) -> List[RetrievalResult]:
        """Retrieve documents using BM25 scoring"""
        logger.info(f"BM25 retrieval for query: '{query}' (top_k={top_k})")
        
        results = []
        # In real implementation: compute BM25 scores
        # scores = self.bm25.get_scores(query.split())
        
        # Simulate results for demonstration
        for idx, doc in enumerate(self.documents[:top_k]):
            results.append(RetrievalResult(
                doc_id=doc.get("doc_id", f"doc_{idx}"),
                content=doc.get("content", ""),
                title=doc.get("title", ""),
                score=0.8 - (idx * 0.1),  # Decreasing scores
                rank=idx + 1,
                retrieval_method="bm25"
            ))
        
        return results


class SemanticRetriever:
    """Semantic similarity-based retrieval using embeddings"""
    
    def __init__(self, documents: List[Dict], embedding_model: Optional[str] = None):
        self.documents = documents
        self.embedding_model = embedding_model or "sentence-transformers/all-MiniLM-L6-v2"
        self.embeddings = []
        self._generate_embeddings()
    
    def _generate_embeddings(self):
        """Generate embeddings for all documents"""
        logger.info(f"Generating embeddings using {self.embedding_model}")
        
        # In real implementation: use sentence-transformers
        # from sentence_transformers import SentenceTransformer
        # model = SentenceTransformer(self.embedding_model)
        # self.embeddings = model.encode([doc["content"] for doc in self.documents])
        
        # Simulate embeddings
        self.embeddings = [np.random.randn(384) for _ in self.documents]
    
    def retrieve(self, query: str, top_k: int = 5) -> List[RetrievalResult]:
        """Retrieve documents using semantic similarity"""
        logger.info(f"Semantic retrieval for query: '{query}' (top_k={top_k})")
        
        # In real implementation: encode query and compute similarity
        # query_embedding = model.encode(query)
        # similarities = util.cos_sim(query_embedding, self.embeddings)
        
        results = []
        for idx, doc in enumerate(self.documents[:top_k]):
            results.append(RetrievalResult(
                doc_id=doc.get("doc_id", f"doc_{idx}"),
                content=doc.get("content", ""),
                title=doc.get("title", ""),
                score=0.7 + (np.random.random() * 0.3),  # Random similarity
                rank=idx + 1,
                retrieval_method="semantic"
            ))
        
        return results


class HybridRetriever:
    """
    Hybrid search combining BM25 and semantic search
    Day 3: Advanced retrieval technique
    """
    
    def __init__(self, documents: List[Dict], bm25_weight: float = 0.5):
        self.documents = documents
        self.bm25_weight = bm25_weight
        self.semantic_weight = 1.0 - bm25_weight
        
        self.bm25_retriever = BM25Retriever(documents)
        self.semantic_retriever = SemanticRetriever(documents)
        
        logger.info(f"Initialized HybridRetriever (BM25: {bm25_weight}, Semantic: {self.semantic_weight})")
    
    def retrieve(self, query: str, top_k: int = 5) -> List[RetrievalResult]:
        """
        Hybrid retrieval combining BM25 and semantic search
        
        Process:
        1. Get BM25 results
        2. Get semantic results
        3. Normalize scores (0-1)
        4. Combine with weighted average
        5. Re-rank and return top_k
        """
        logger.info(f"Hybrid retrieval for query: '{query}'")
        
        # Get results from both retrievers
        bm25_results = self.bm25_retriever.retrieve(query, top_k=top_k * 2)
        semantic_results = self.semantic_retriever.retrieve(query, top_k=top_k * 2)
        
        # Combine and normalize scores
        combined = {}
        
        # Add BM25 results with weight
        for result in bm25_results:
            if result.doc_id not in combined:
                combined[result.doc_id] = {
                    "doc_id": result.doc_id,
                    "content": result.content,
                    "title": result.title,
                    "bm25_score": result.score,
                    "semantic_score": 0.0
                }
            else:
                combined[result.doc_id]["bm25_score"] = result.score
        
        # Add semantic results with weight
        for result in semantic_results:
            if result.doc_id not in combined:
                combined[result.doc_id] = {
                    "doc_id": result.doc_id,
                    "content": result.content,
                    "title": result.title,
                    "bm25_score": 0.0,
                    "semantic_score": result.score
                }
            else:
                combined[result.doc_id]["semantic_score"] = result.score
        
        # Compute hybrid scores and sort
        hybrid_results = []
        for rank, (doc_id, data) in enumerate(sorted(
            combined.items(),
            key=lambda x: (x[1]["bm25_score"] * self.bm25_weight + 
                          x[1]["semantic_score"] * self.semantic_weight),
            reverse=True
        )[:top_k], 1):
            hybrid_score = (data["bm25_score"] * self.bm25_weight + 
                           data["semantic_score"] * self.semantic_weight)
            
            hybrid_results.append(RetrievalResult(
                doc_id=doc_id,
                content=data["content"],
                title=data["title"],
                score=hybrid_score,
                rank=rank,
                retrieval_method="hybrid"
            ))
        
        logger.info(f"Hybrid retrieval returned {len(hybrid_results)} results")
        return hybrid_results


# ============================================================================
# RERANKING: Cross-Encoder (Day 3)
# ============================================================================

class CrossEncoderReranker:
    """
    Cross-Encoder based reranking for improved retrieval quality
    Day 3: Advanced reranking technique
    
    A cross-encoder directly scores query-document pairs,
    providing more accurate relevance scores than embedding similarity.
    """
    
    def __init__(self, model_name: str = "cross-encoder/ms-marco-TinyBERT-L-2-v2"):
        self.model_name = model_name
        # In real implementation:
        # from sentence_transformers import CrossEncoder
        # self.model = CrossEncoder(model_name)
        logger.info(f"Initialized CrossEncoderReranker with {model_name}")
    
    def rerank(self, 
               query: str, 
               retrieval_results: List[RetrievalResult],
               top_k: Optional[int] = None) -> List[RankedResult]:
        """
        Rerank retrieval results using cross-encoder
        
        Process:
        1. For each retrieved document
        2. Compute cross-encoder score for (query, document) pair
        3. Sort by cross-encoder score
        4. Return reranked results
        """
        logger.info(f"Reranking {len(retrieval_results)} results with cross-encoder")
        
        # In real implementation:
        # pairs = [[query, result.content] for result in retrieval_results]
        # scores = self.model.predict(pairs)
        
        # Simulate reranking with slight score adjustments
        ranked_results = []
        for idx, result in enumerate(sorted(retrieval_results, key=lambda x: x.score, reverse=True)):
            # Simulate cross-encoder score (slightly different from retrieval score)
            rerank_score = result.score * 0.9 + np.random.random() * 0.1
            
            ranked_results.append(RankedResult(
                doc_id=result.doc_id,
                content=result.content,
                title=result.title,
                retrieval_score=result.score,
                rerank_score=rerank_score,
                final_rank=idx + 1
            ))
        
        # Return top_k if specified
        if top_k:
            ranked_results = ranked_results[:top_k]
        
        logger.info(f"Reranking complete. Top result score: {ranked_results[0].rerank_score:.4f}")
        return ranked_results


# ============================================================================
# GENERATION: RAG Answer Generation
# ============================================================================

class PromptEngine:
    """Engineered prompts for RAG answer generation"""
    
    RAG_TEMPLATE = """You are an AI assistant helping with technical questions about modern data engineering.
    
Context from knowledge base:
{context}

Question: {query}

Instructions:
1. Answer based only on the provided context
2. If the context doesn't contain the answer, say "I don't have information about this"
3. Be concise and clear
4. Cite relevant context

Answer:"""
    
    @classmethod
    def build_prompt(cls, query: str, context: List[RankedResult]) -> str:
        """Build RAG prompt with context"""
        context_text = "\n\n".join([
            f"[{result.final_rank}] {result.title} (relevance: {result.rerank_score:.2f})\n{result.content[:500]}..."
            for result in context[:3]  # Top 3 results
        ])
        
        return cls.RAG_TEMPLATE.format(context=context_text, query=query)


class LLMClient(ABC):
    """Abstract LLM client"""
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate text from prompt"""
        pass


class MockLLMClient(LLMClient):
    """Mock LLM for demonstration"""
    
    def generate(self, prompt: str, **kwargs) -> str:
        """Generate mock response"""
        logger.info("Generating response with MockLLMClient")
        return """Based on the provided context, modern data engineering is a critical discipline that combines:

1. **Data Pipeline Architecture**: Building resilient, scalable systems for data movement and transformation
2. **Storage Solutions**: Implementing lakehouse architectures with Delta Lake for ACID compliance
3. **Quality Assurance**: Implementing data contracts and quality gates to ensure data reliability
4. **Search and Retrieval**: Using hybrid search and advanced ranking for AI applications

The context emphasizes the integration of Kafka streaming, Delta Lake storage, and advanced RAG techniques for production-ready systems."""


# ============================================================================
# END-TO-END RAG PIPELINE (Day 3)
# ============================================================================

class RAGPipeline:
    """
    Complete RAG pipeline integrating all components
    Reference: Day 3 Advanced RAG Architecture
    """
    
    def __init__(self, 
                 documents: List[Dict],
                 llm_client: Optional[LLMClient] = None,
                 bm25_weight: float = 0.5):
        """
        Initialize RAG pipeline
        
        Args:
            documents: List of documents to use as knowledge base
            llm_client: LLM client for generation (defaults to MockLLMClient)
            bm25_weight: Weight for BM25 in hybrid search
        """
        # Storage
        self.delta_lake = DeltaLakeManager("./delta_lake")
        
        # Ingest documents to Delta Lake
        self.delta_lake.write_to_bronze(documents)
        self.delta_lake.merge_to_silver(documents)
        
        # Retrieval
        self.retriever = HybridRetriever(documents, bm25_weight=bm25_weight)
        
        # Reranking
        self.reranker = CrossEncoderReranker()
        
        # Generation
        self.llm_client = llm_client or MockLLMClient()
        
        logger.info(f"Initialized RAGPipeline with {len(documents)} documents")
    
    def query(self, query: str, top_k: int = 5) -> RAGResponse:
        """
        Execute end-to-end RAG pipeline
        
        Process:
        1. Retrieve documents using hybrid search
        2. Rerank with cross-encoder
        3. Generate answer with LLM
        4. Return response with context
        """
        logger.info(f"Processing RAG query: '{query}'")
        
        # Step 1: Retrieval (hybrid search)
        retrieved = self.retriever.retrieve(query, top_k=top_k)
        logger.info(f"Retrieved {len(retrieved)} documents")
        
        # Step 2: Reranking (cross-encoder)
        reranked = self.reranker.rerank(query, retrieved, top_k=top_k)
        logger.info(f"Reranked to {len(reranked)} documents")
        
        # Step 3: Prompt engineering
        prompt = PromptEngine.build_prompt(query, reranked)
        
        # Step 4: Generation
        answer = self.llm_client.generate(prompt)
        
        # Step 5: Confidence scoring
        confidence = np.mean([r.rerank_score for r in reranked]) if reranked else 0.0
        
        # Step 6: Return response
        response = RAGResponse(
            query=query,
            answer=answer,
            confidence=confidence,
            retrieved_docs=reranked,
            metadata={
                "retrieval_method": "hybrid",
                "reranking_method": "cross_encoder",
                "num_retrieved": len(reranked),
                "avg_rerank_score": float(confidence)
            }
        )
        
        logger.info(f"Generated response with confidence: {confidence:.2f}")
        return response


# ============================================================================
# MAIN EXECUTION & DEMONSTRATION
# ============================================================================

def main():
    """Demonstrate Day 3 RAG pipeline"""
    
    print("=" * 80)
    print("SDAIA Academy - Modern Data Engineering for Advanced AI Systems")
    print("Day 3: Advanced RAG Implementation")
    print("=" * 80)
    print()
    
    # Sample documents (knowledge base)
    sample_docs = [
        {
            "doc_id": "doc_001",
            "title": "Modern Data Engineering Fundamentals",
            "content": """Modern data engineering combines traditional data infrastructure with AI-ready architectures.
            Key concepts include: data lakehouse architecture, Delta Lake for ACID compliance, Kafka for streaming ingestion,
            quality gates for data validation, and Apache Airflow for orchestration."""
        },
        {
            "doc_id": "doc_002",
            "title": "Hybrid Search Architecture",
            "content": """Hybrid search combines keyword-based retrieval (BM25) with semantic similarity (embeddings).
            This approach captures both exact matches and semantic relevance, improving retrieval quality.
            Typical implementation: weighted combination of BM25 scores and embedding similarity scores."""
        },
        {
            "doc_id": "doc_003",
            "title": "Cross-Encoder Reranking",
            "content": """Cross-encoders directly score query-document pairs, providing more accurate relevance than
            embedding similarity alone. In a two-stage retrieval pipeline: retrieve with hybrid search, rerank with
            cross-encoder. This improves precision at the cost of computational complexity."""
        },
        {
            "doc_id": "doc_004",
            "title": "Delta Lake for Quality",
            "content": """Delta Lake provides ACID guarantees, schema enforcement, and time-travel capabilities.
            The Bronze-Silver-Gold architecture: Bronze stores raw data, Silver contains cleaned/deduplicated data,
            Gold provides optimized outputs for BI and AI. Quality gates ensure data reliability at each stage."""
        },
        {
            "doc_id": "doc_005",
            "title": "RAG Pipeline Best Practices",
            "content": """Effective RAG requires: quality document preprocessing, appropriate embedding models,
            thoughtful retrieval configuration, intelligent reranking, and prompt engineering. Evaluation with
            RAGAS metrics (faithfulness, answer relevance, context relevance) ensures system quality."""
        }
    ]
    
    # Initialize RAG pipeline
    rag = RAGPipeline(
        documents=sample_docs,
        llm_client=MockLLMClient(),
        bm25_weight=0.5
    )
    
    # Test queries
    test_queries = [
        "What is hybrid search?",
        "How does cross-encoder reranking work?",
        "What are the layers in Delta Lake architecture?"
    ]
    
    print("\n" + "=" * 80)
    print("Testing RAG Pipeline")
    print("=" * 80 + "\n")
    
    for query in test_queries:
        print(f"Query: {query}")
        print("-" * 80)
        
        response = rag.query(query, top_k=3)
        
        print(f"Confidence: {response.confidence:.2f}")
        print(f"\nAnswer:\n{response.answer}")
        
        print(f"\nTop Retrieved Documents:")
        for doc in response.retrieved_docs[:3]:
            print(f"  [{doc.final_rank}] {doc.title}")
            print(f"      Retrieval Score: {doc.retrieval_score:.2f}")
            print(f"      Rerank Score: {doc.rerank_score:.2f}")
        
        print(f"\nMetadata: {json.dumps(response.metadata, indent=2)}")
        print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":
    main()
