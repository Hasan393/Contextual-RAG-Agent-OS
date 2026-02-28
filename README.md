# 🧠 Agent OS - Contextual RAG Operating System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)

**Agent OS** is an advanced operating system kernel for AI agents, implementing a biologically-inspired Retrieval-Augmented Generation (RAG) architecture. Rather than treating knowledge retrieval as a simple database lookup, this system models memory as a dynamic, self-optimizing cognitive hierarchy that mirrors human brain architecture.

## 📖 Table of Contents

- [The Concept](#-the-concept)
- [Architecture](#️-architecture)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Module Documentation](#-module-documentation)
- [Configuration](#-configuration)
- [Usage Examples](#-usage-examples)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 The Concept

Traditional AI agents rely on static vector databases that perform cosine similarity searches across pre-embedded documents. This system reimagines RAG as a living memory system inspired by human cognitive architecture:

### Key Innovations

1. **Short-Term Memory Buffer**
   - Captures immediate conversational context and recent interactions
   - Acts as a working memory for current problem-solving
   - Automatically triggers compression when capacity is exceeded

2. **Attention Controller**
   - Continuously monitors working memory load and relevance
   - Executes **Memory Consolidation**: transforms old conversational tokens into dense conceptual summaries
   - Routes consolidated memories to long-term storage while preserving semantic meaning
   - Dynamically adjusts attention weights based on task relevance

3. **Knowledge Graph**
   - Automatically extracts entities, relationships, and concepts from conversations
   - Builds a structured semantic graph of interconnected knowledge
   - Enables reasoning across multiple domains and concept relationships
   - Background thread continuously updates graph as new information arrives

4. **Retrieval Optimizer**
   - Dynamically learns which retrieval strategies work best for different query types
   - Adjusts ranking weights based on retrieval success/failure feedback
   - Balances between lexical search, semantic similarity, and graph-based retrieval
   - Continuously improves retrieval accuracy through experience

## ⚙️ Architecture

```
┌─────────────────────────────────────────────────────┐
│           Agent OS - Cognitive Architecture         │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌─────────────────────────────────────────────┐  │
│  │     Attention Controller (Monitor)          │  │
│  │  - Load balancing                           │  │
│  │  - Memory compression triggers              │  │
│  │  - Attention weight adjustment              │  │
│  └────────────────┬────────────────────────────┘  │
│                   │                                 │
│  ┌────────────────▼─────────────┐                  │
│  │  Short-Term Memory Buffer    │                  │
│  │  (Working Memory)            │                  │
│  │  - Conversation history      │                  │
│  │  - Current context (512 tk)  │                  │
│  └────────────────┬─────────────┘                  │
│                   │                                 │
│  ┌────────────────▼──────────────────────────────┐ │
│  │  Memory Hierarchy                            │ │
│  │  ┌─────────────────┐  ┌──────────────────┐  │ │
│  │  │ Knowledge Graph │  │ Long-Term        │  │ │
│  │  │ (Entity Links)  │  │ Storage (LTS)    │  │ │
│  │  └─────────────────┘  └──────────────────┘  │ │
│  └────────────────┬──────────────────────────────┘ │
│                   │                                 │
│  ┌────────────────▼──────────────────────────────┐ │
│  │  Retrieval Optimizer                         │ │
│  │  - Strategy selection                        │ │
│  │  - Weight learning                           │ │
│  │  - Multi-modal retrieval                     │ │
│  └──────────────────────────────────────────────┘ │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hasan393/Contextual-RAG-Agent-OS.git
   cd Contextual-RAG-Agent-OS/agent_os
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## 🎯 Quick Start

### Basic Usage

```python
from kernel.memory_hierarchy import MemoryHierarchy
from kernel.retrieval_optimizer import RetrievalOptimizer
from kernel.knowledge_graph import KnowledgeGraph
from kernel.attention_controller import AttentionController

# Initialize the Agent OS kernel
memory = MemoryHierarchy()
optimizer = RetrievalOptimizer()
graph = KnowledgeGraph()
attention = AttentionController()

# Process a user query
query = "What are the benefits of machine learning?"
retrieved_docs = optimizer.retrieve(query)
graph.extract_entities(query)
attention.update_context(query)
```

### Running the Application

```bash
python main.py
```

## 📁 Project Structure

```
agent_os/
├── .env                          # Environment configuration
├── requirements.txt              # Project dependencies
├── README.md                     # This file
├── main.py                       # Application entry point
│
└── kernel/                       # Core OS components
    ├── __init__.py              # Package initialization
    ├── memory_hierarchy.py       # Memory management system
    ├── retrieval_optimizer.py    # Smart retrieval engine
    ├── knowledge_graph.py        # Entity relationship graph
    └── attention_controller.py   # Attention & compression mechanism
```

## 📚 Module Documentation

### memory_hierarchy.py

Manages the hierarchical memory system with multiple storage tiers:

```python
class MemoryHierarchy:
    """Multi-tier memory management for AI agents."""
    
    def store_shortterm(data: dict) -> None:
        """Store data in working memory buffer."""
        
    def compress_memory() -> None:
        """Compress old data into conceptual summaries."""
        
    def store_longterm(data: dict) -> None:
        """Archive compressed data to long-term storage."""
```

**Key Features:**
- Automatic capacity management
- Lossless compression of conversational data
- Priority-based retention policies
- Fast access to recent context

### retrieval_optimizer.py

Intelligently retrieves relevant information based on learned strategies:

```python
class RetrievalOptimizer:
    """Optimizes information retrieval strategies."""
    
    def retrieve(query: str, top_k: int = 5) -> List[Document]:
        """Retrieve most relevant documents for query."""
        
    def update_weights(feedback: dict) -> None:
        """Learn from retrieval success/failure."""
```

**Key Features:**
- Multi-strategy retrieval (lexical, semantic, graph-based)
- Adaptive weight learning
- Feedback integration
- Query understanding and expansion

### knowledge_graph.py

Builds and maintains a semantic knowledge graph:

```python
class KnowledgeGraph:
    """Dynamic knowledge graph construction."""
    
    def extract_entities(text: str) -> None:
        """Extract entities and relationships from text."""
        
    def query_graph(entity: str) -> List[Relationship]:
        """Find connected concepts and relationships."""
```

**Key Features:**
- Automatic entity extraction
- Relationship mapping
- Graph traversal and inference
- Multi-hop reasoning support

### attention_controller.py

Manages working memory and triggers consolidation:

```python
class AttentionController:
    """Controls attention and memory consolidation."""
    
    def monitor_buffer() -> None:
        """Monitor working memory load."""
        
    def consolidate_memory() -> None:
        """Trigger memory compression and archival."""
        
    def update_attention_weights(context: dict) -> None:
        """Adjust attention based on task relevance."""
```

**Key Features:**
- Real-time memory load monitoring
- Automatic consolidation triggers
- Context-aware attention adjustment
- Priority memory preservation

## ⚙️ Configuration

### Environment Variables (.env)

```env
# Model Configuration
MODEL_NAME=google/gemini-pro
MAX_TOKENS=8192
TEMPERATURE=0.7

# Memory Settings
SHORT_TERM_CAPACITY=512
COMPRESSION_THRESHOLD=0.8
RETENTION_DAYS=30

# Retrieval Settings
RETRIEVAL_TOP_K=5
SIMILARITY_THRESHOLD=0.5

# Logging
LOG_LEVEL=INFO
DEBUG_MODE=False
```

### requirements.txt

Include necessary dependencies for:
- LLM integration (Google Gemini, OpenAI, etc.)
- Vector embeddings
- Graph databases
- NLP processing

## 💡 Usage Examples

### Example 1: Multi-Query Memory Management

```python
agent = AgentOS()

# First query establishes context
agent.process("Tell me about artificial intelligence")

# Second query retrieves from short-term buffer
relevant = agent.search("What did we discuss about AI?")

# Third query triggers memory consolidation
agent.process("Now let's discuss machine learning applications")
```

### Example 2: Knowledge Graph Extraction

```python
text = "Alice works at Google. She specializes in NLP. Google is located in Mountain View."

graph = KnowledgeGraph()
entities = graph.extract_entities(text)
# Output: {
#   "entities": ["Alice", "Google", "NLP", "Mountain View"],
#   "relationships": [
#     {"from": "Alice", "to": "Google", "type": "works_at"},
#     {"from": "Alice", "to": "NLP", "type": "specializes_in"}
#   ]
# }
```

### Example 3: Adaptive Retrieval

```python
optimizer = RetrievalOptimizer()

# Initial retrieval with default weights
docs = optimizer.retrieve("How to train neural networks?")

# Provide feedback on retrieval quality
optimizer.update_weights({
    "query": "How to train neural networks?",
    "successful_docs": [doc1, doc3],
    "failed_docs": [doc2]
})

# Subsequent retrievals use learned weights
docs = optimizer.retrieve("Best practices for deep learning?")
```

## 🔧 Development

### Running Tests

```bash
pytest tests/
```

### Code Style

This project follows PEP 8 conventions. Format code with:

```bash
black kernel/
pylint kernel/
```

### Building Documentation

```bash
sphinx-build -b html docs/ docs/_build/
```

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Areas
- Memory optimization algorithms
- Retrieval strategy improvements
- Graph reasoning enhancements
- Documentation and examples
- Performance benchmarking

## 🚀 Future Enhancements

- [ ] Multi-language support
- [ ] Distributed memory systems
- [ ] Advanced graph reasoning with GNNs
- [ ] Reinforcement learning for retrieval weights
- [ ] Real-time graph updates
- [ ] Semantic compression algorithms
- [ ] Integration with popular LLM APIs
- [ ] Web UI for memory visualization
- [ ] Performance benchmarking tools
- [ ] Caching and indexing optimizations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## 👨‍💻 Author

**Hasan Kumar** - [@Hasan393](https://github.com/Hasan393)

## 📞 Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/Hasan393/Contextual-RAG-Agent-OS/issues)
- Check [Discussions](https://github.com/Hasan393/Contextual-RAG-Agent-OS/discussions)
- Review the [Wiki](https://github.com/Hasan393/Contextual-RAG-Agent-OS/wiki)

## 🙏 Acknowledgments

This project draws inspiration from:
- Cognitive Science and memory consolidation research
- Advanced RAG architectures
- Knowledge graph construction techniques
- Attention mechanisms in neural networks

---

**Last Updated**: February 2026
**Version**: 1.0.0
