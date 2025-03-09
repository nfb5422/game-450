# Retrieval-Augmented Generation (RAG) System

## Overview
This lab demonstrates a Retrieval-Augmented Generation (RAG) system using ChromaDB for vector storage, text chunking, and Ollama for both embeddings and LLM inference. RAG enhances LLM responses by retrieving relevant information from a knowledge base before generating answers, leading to more accurate, contextual, and up-to-date responses.

## What is RAG?
Retrieval-Augmented Generation combines two key components:
1. **Retrieval**: Finding relevant documents or information from a corpus based on a query
2. **Generation**: Using an LLM to generate responses based on both the query and the retrieved information

RAG addresses several limitations of traditional LLMs:
- **Knowledge cutoffs**: Provides access to information beyond the LLM's training data
- **Hallucination reduction**: Grounds responses in retrieved facts
- **Source attribution**: Enables citations to source documents
- **Domain specificity**: Tailors responses to specialized knowledge bases

## System Components

### ChromaDB
[ChromaDB](https://www.trychroma.com/) is an open-source embedding database designed for AI applications. It provides:
- Efficient storage and retrieval of vector embeddings
- Support for metadata and filtering
- Easy integration with Python applications
- Persistent storage options (PersistentClient)

### Ollama
[Ollama](https://ollama.ai/) allows running various large language models locally, offering:
- Easy model management
- Lower latency compared to API-based services
- Privacy advantages by keeping data local
- Support for various open models (Llama, Mistral, etc.)
- **Embedding capabilities**: Generate embeddings for vector search using models like `nomic-embed-text`

## Getting Started
### Demo Script
The `lab08.py` script shows RAG in action:
- Document loading and chunking using LangChain's text preprocessing utilities
- Vector embedding using Ollama
- Vector storage with ChromaDB
- Query processing
- Retrieval of relevant context
- LLM response generation with the retrieved context

### Using LangChain for Text Chunking
This demo supports using LangChains's built-in text preprocessing utilities for document chunking:

1. The script leverages `langchain.text_splitter.RecursiveCharacterTextSplitter`
2. It uses word tokenization (`word_tokens`) and entity processing for more intelligent chunking
3. Benefits of LangChain chunking:
   - Integrated solution with the same library used for vector storage
   - Customizable tokenization and text processing options
   - Direct integration with ChromaDB's document processing pipeline

### Using Ollama for Embeddings
This demo supports using Ollama for both text embeddings and response generation:

1. The script includes a custom `OllamaEmbeddingFunction` class that interfaces with Ollama's embedding API
2. By default, it uses the `nomic-embed-text` model, which is optimized for text embeddings
3. Performance considerations:
   - Ollama embeddings may be slower but run completely locally
   - If speed is a concern, you can use sentence-transformers instead

## Lab File Structure
```
lab08/
├── RAG_README.md          # This documentation
├── lab08.py               # Main demonstration script
└── data/                  # Sample documents for the knowledge base
```

## Lab Instructions
1. pull the lab08 directory from the repo
2. complete the two functions in `lab08.py`:
   - `__call__()` in `OllamaEmbeddingFunction`
      - This function should use the Ollama embeddings API to generate embeddings for a list of texts
      - Refer to the [Ollama API](https://github.com/ollama/ollama-python) for more information
   - `retrieve_context()`
      - This function should use the ChromaDB collection to retrieve the top 3 most relevant context chunks for a given query
      - Refer to the [ChromaDB Retrieval API](https://docs.trychroma.com/docs/querying-collections/query-and-get) for more information
3. run the script to see the RAG in action

__Note__: *On Windows, refer https://github.com/chroma-core/chroma/issues/2513 for a bug in chromadb. Installing ChromaDB==0.5 and numpy==1.26.0 should fix the issue*. 

## References and Further Reading
- [LangChain RAG Documentation](https://python.langchain.com/docs/use_cases/question_answering/)
- [ChromaDB Documentation](https://docs.trychroma.com/docs)
- [Ollama GitHub Repository](https://github.com/ollama/ollama)
- [Ollama API](https://github.com/ollama/ollama-python)
- [RAG Paper: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"](https://arxiv.org/abs/2005.11401) 
- [Evaluating Text Chunking Strategies](https://research.trychroma.com/evaluating-chunking)