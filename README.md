# 🛒 ShopEase AI Support Agent

A production-style AI customer support system built with **RAG, LLMs, Tool Calling, Agentic Workflows, FastAPI, and Docker**.

The system can answer policy-related questions using a knowledge base and perform order-related actions using deterministic tools.

---

## 🚀 Features

* 🔎 Retrieval-Augmented Generation (RAG)
* 🧠 Semantic search using Sentence Transformers
* ⚡ FAISS vector similarity search
* 🤖 Local LLM inference using Ollama
* 🛠️ Tool-based order operations
* 🔀 Intelligent query routing
* 🤝 Combined RAG + Tool agent workflow
* 🌐 FastAPI REST API
* 🧪 Automated testing with Pytest
* 🐳 Docker containerization
* 📚 Multiple e-commerce policy documents
* 💾 JSON-based order database

---

## 🏗️ Architecture

```text
                         Customer Query
                               │
                               ▼
                         FastAPI /chat
                               │
                               ▼
                         Query Router
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
             RAG              TOOL             BOTH
              │                │                │
              ▼                ▼                ▼
        FAISS Search       Tool Executor    RAG + Tool
              │                │                │
              ▼                ▼                ▼
        Policy Context     Order Database    Combined Context
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                         LLM / Agent
                               │
                               ▼
                         Final Response
```

---

## 📁 Project Structure

```text
ecommerce-ai-support-agent/
│
├── app/
│   ├── data_loader.py
│   ├── text_splitter.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── context_builder.py
│   ├── generator.py
│   ├── rag_pipeline.py
│   ├── router.py
│   ├── tools.py
│   ├── tool_registry.py
│   ├── tool_executor.py
│   ├── tool_agent.py
│   ├── agent.py
│   ├── main.py
│   └── test_tools.py
│
├── data/
│   ├── knowledge_base/
│   │   ├── cancellation_policy.txt
│   │   ├── return_policy.txt
│   │   ├── refund_policy.txt
│   │   ├── delivery_policy.txt
│   │   └── payment_policy.txt
│   │
│   └── database/
│       └── orders.json
│
├── tests/
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

---

## 🧠 RAG Pipeline

The RAG pipeline follows these steps:

```text
Documents
   ↓
Text Splitting
   ↓
Sentence Transformer Embeddings
   ↓
FAISS Vector Store
   ↓
Similarity Search
   ↓
Relevant Context
   ↓
LLM
   ↓
Final Answer
```

The knowledge base currently contains:

* Refund Policy
* Return Policy
* Cancellation Policy
* Delivery Policy
* Payment Policy

---

## 🛠️ Available Tools

### `get_order_status`

Retrieves the current order information.

### `cancel_order`

Attempts to cancel an order according to the supported order state.

### `request_refund`

Processes a refund request for eligible delivered orders.

The tools operate on the JSON order database.

---

## 🔀 Query Routing

The router classifies incoming queries into:

```text
RAG
TOOL
BOTH
UNKNOWN
```

Examples:

```text
"Refund policy kya hai?"
→ RAG
```

```text
"Mera order 1001 kaha hai?"
→ TOOL
```

```text
"I cannot track order 1001, can I get a refund?"
→ BOTH
```

---

## 🌐 API

### Start FastAPI

```bash
uvicorn app.main:app --reload
```

API:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

## 📡 Example Request

```bash
curl -X POST "http://localhost:8000/chat" \
-H "Content-Type: application/json" \
-d '{"query":"Mera order 1001 kaha hai?"}'
```

Example response:

```json
{
  "answer": "Order 1001 (Wireless Headphones) is currently Out for Delivery. Payment method: UPI."
}
```

---

## 🧪 Testing

Run:

```bash
pytest -v
```

Current test coverage includes:

* Order status retrieval
* Invalid order handling
* Cancellation validation
* Refund validation
* Delivered-order refund

---

## 🐳 Docker

Build the image:

```bash
docker build -t shopease-ai-agent .
```

Run the container:

```bash
docker run -p 8000:8000 shopease-ai-agent
```

Then open:

```text
http://localhost:8000/docs
```

---

## 🤖 LLM Setup

This project uses **Ollama** for local LLM inference.

The configured model is:

```text
llama3.2:3b
```

Make sure Ollama is installed and the model is available before using LLM-powered endpoints.

---

## ⚠️ Current Limitations

This project is intentionally designed as a portfolio-scale production-style prototype.

Current limitations include:

* Order data is stored in JSON instead of a production database.
* Refund state is not persisted separately.
* The current tool agent uses deterministic routing rather than native LLM function calling.
* Embeddings/vector index are currently initialized during application usage rather than being managed as a persistent vector database service.
* Ollama is run separately from the Dockerized application.

These can be extended for a larger production deployment.

---

## 🔮 Future Improvements

* PostgreSQL integration
* Persistent vector database
* Redis caching
* Authentication and authorization
* Native LLM function calling
* Streaming responses
* Observability and tracing
* Production cloud deployment
* CI/CD pipeline
* Kubernetes deployment
* More comprehensive API and integration tests

---

## 🧰 Tech Stack

| Technology               | Purpose                  |
| ------------------------ | ------------------------ |
| Python                   | Core development         |
| FastAPI                  | REST API                 |
| Ollama                   | Local LLM inference      |
| Sentence Transformers    | Text embeddings          |
| FAISS                    | Vector similarity search |
| LangChain Text Splitters | Document chunking        |
| Pytest                   | Testing                  |
| Docker                   | Containerization         |
| JSON                     | Prototype order database |

---

## 🎯 Project Goal

The goal of this project is to demonstrate how a modern AI customer-support system can combine:

**RAG + Semantic Search + LLMs + Tools + Agentic Workflows + APIs + Testing + Docker**

into a single end-to-end application.

---

## 👨‍💻 Author

**Suraj Sharma**

AI/ML & Generative AI Engineer in progress.
