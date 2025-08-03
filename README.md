# Multi-LLM Debate CLI

> A Python framework for orchestrating AI debates — multiple language models engage in structured dialogue, with their insights compressed into a rolling summary to surface emergent consensus and divergent perspectives.

---

## 🚀 Project Description

The Multi-LLM Debate CLI is a command-line tool that brings together diverse AI models to debate any topic through structured, multi-round discussions. By orchestrating heterogeneous models from different providers (OpenAI, Anthropic, Google, Ollama, and more) and compressing their dialogue through recursive summarization, we unlock new possibilities in AI interaction and knowledge synthesis.

### Core Capabilities

- **Harvest Composite Insights**: By combining perspectives from models trained on different datasets with different objectives, we surface insights that single-model prompts rarely reveal. Each model brings its unique training biases and strengths, creating a richer analytical landscape.

- **Quantify Convergence and Divergence**: Track how AI models align or diverge on complex topics in real-time. Our alignment matrix and convergence metrics provide quantitative measures of consensus, revealing which aspects of a problem space have clear agreement versus persistent disagreement.

- **Create Portable Knowledge Artifacts**: Every debate produces a self-contained knowledge artifact that includes the final synthesis, chronological summary evolution, agent positions, and comprehensive metadata. These artifacts are designed for easy versioning, sharing, and integration into research workflows.

- **Provide an Open, Vendor-Neutral Platform**: Unlike closed platforms, our framework treats all models equally. Whether you're using cutting-edge commercial APIs or local open-source models, the debate framework provides the same powerful orchestration capabilities.

### How It Works

The system operates on a simple but powerful principle: intelligent compression. As models debate, their responses are continuously summarized by a dedicated summarizer agent, maintaining the essential arguments while preventing context overflow. This allows for extended debates that would be impossible with traditional context windows.

---

## 🧠 What Makes This Different?

### Provider Agnostic Architecture
Our abstract backend system means you can seamlessly integrate models from any provider. Mix GPT-4 with Claude, add Gemini for a third perspective, or run entirely local debates with Ollama. The framework handles the complexity of different APIs, rate limits, and response formats transparently.

### Rolling Summarization Technology
Unlike simple chat interfaces, our recursive compression algorithm maintains coherent context over unlimited rounds. The summarizer identifies new arguments, tracks stance changes, and preserves the essential thread of conversation while aggressively pruning redundancy.

### Asynchronous by Design
Built on asyncio from the ground up, the framework makes concurrent API calls to all participating models. This isn't just about speed — it ensures that models respond independently without being influenced by response order.

### Configuration-First Philosophy
Every aspect of the debate is configurable through TOML files. From model parameters to summarization frequency, from output formats to tool capabilities — researchers have complete control without touching code.

### Observable Debate Dynamics
We don't just show you the final answer. Track token usage, response latencies, argument novelty scores, stance evolution, and inter-model alignment throughout the debate. These metrics reveal the underlying dynamics of AI disagreement and consensus formation.

### Research-Grade Output
Outputs aren't just text files — they're structured documents ready for analysis. With built-in support for versioning, metadata, statistical summaries, and multiple export formats, every debate contributes to a growing corpus of AI interaction data.

---

## 🏗️ Core Design Principles

### 1. Modularity Through Abstraction
Every component implements a clean interface. LLM backends, output writers, summarization strategies, and analysis tools are all pluggable. This isn't over-engineering — it's essential for a research tool that needs to adapt to a rapidly evolving AI landscape.

### 2. Stateless Agent Design
Agents are stateless between rounds, seeing only the rolling summary plus their system prompt. This design choice enables several critical features:
- Unlimited debate length without context overflow
- Consistent computational requirements regardless of debate duration
- Clean separation between agent reasoning and debate history
- Ability to add or remove agents mid-debate

### 3. Deterministic Orchestration
While model outputs may vary, the debate framework itself is deterministic. Given the same configuration and random seed, debates can be reproduced exactly. This is crucial for scientific reproducibility and debugging.

### 4. Fail-Safe Error Handling
API failures, rate limits, and network issues are inevitable. The framework implements exponential backoff, automatic retries, and graceful degradation. If one model fails repeatedly, the debate continues with remaining participants rather than crashing entirely.

### 5. Comprehensive Instrumentation
Every API call, every summarization, every decision point is instrumented. This isn't just for debugging — it's about understanding the emergent properties of multi-model interaction. When does consensus emerge? How do models influence each other through the summary? These questions require detailed operational data.

---

## Configuration Examples

### Global Agent Configuration

```toml
# OpenAI Configuration
[gpt4]
provider = "openai"
model = "gpt-4"
api_key = "${OPENAI_API_KEY}"  # Environment variable reference
temperature = 0.7
max_tokens = 500
top_p = 0.95
frequency_penalty = 0.0
presence_penalty = 0.0
retry_max = 3
retry_delay = 1.0

# Anthropic Configuration
[claude3]
provider = "anthropic"
model = "claude-3-opus-20240229"
api_key = "${ANTHROPIC_API_KEY}"
temperature = 0.8
max_tokens = 1000

# Google Configuration
[gemini-pro]
provider = "google"
model = "gemini-pro"
api_key = "${GOOGLE_API_KEY}"
temperature = 0.6
top_k = 40
top_p = 0.95

# Local Ollama Configuration
[llama2-local]
provider = "ollama"
model = "llama2:13b"
base_url = "http://localhost:11434"
temperature = 0.7
```

### Global Debate Configuration

```toml
[experiment]
name = "consciousness_ethics_debate"
description = "Exploring the ethical implications of potential AI consciousness"
agents = ["gpt4", "claude3", "gemini-pro"]
rounds = 20
seed = 42  # For reproducibility

[debate]
summary_every = 2  # Summarize every 2 rounds
summary_model = "gpt-3.5-turbo"  # Use cheaper model for summaries
summary_max_tokens = 1500
convergence_threshold = 0.85  # Stop if alignment exceeds threshold
max_stagnation = 5  # Stop if no new arguments for 5 rounds

[prompts]
# Override default prompts
agent_system = """
You are participating in a structured debate about {topic}.
Focus on logical arguments and empirical evidence.
Be concise but thorough in your responses.
"""

summarizer_system = """
Summarize the debate progress, highlighting:
1. New arguments introduced
2. Points of agreement/disagreement
3. Stance changes
Keep summary under {max_tokens} tokens.
"""

[output]
format = "markdown"  # Options: markdown, json, html
include_metadata = true
include_stats = true
include_alignment_matrix = true
include_summary_evolution = true
save_intermediate = true  # Save after each round

[tools]
# Enable agent tools (Milestone 8+)
web_search = true
calculator = true
citation_fetcher = false

[logging]
level = "INFO"  # DEBUG, INFO, WARNING, ERROR
file = "debate.log"
format = "json"  # Structured logging
```

---

## 📍 Development Roadmap

### High-Level Milestone Preview

- [ ] **Single LLM Interface** - Basic CLI with one model responding
- [ ] **Multi-Model Conversations** - Enable back-and-forth between multiple models
- [ ] **Recursive Summarization Engine** - Add intelligent compression for context management
- [ ] **Configuration & Output System** - TOML-based configuration and structured outputs
- [ ] **Async Execution & Performance** - Concurrent operations and optimization
- [ ] **Advanced Analytics** - Debate dynamics analysis and metrics
- [ ] **Local Model Support** - Ollama integration for offline debates
- [ ] **Tool Integration Layer** - Web search, calculations, and citations
- [ ] **Interactive TUI** - Real-time monitoring with Rich/Textual
- [ ] **Research Platform Features** - Advanced modes for academic research
- [ ] **Multi-Modal Debates** - Support for image and code discussions
- [ ] **Distributed Debates** - Network multiple instances for large-scale debates

### Detailed Milestone Descriptions

#### ✅ Milestone 1: Single LLM Interface
> **Goal**: Establish core infrastructure with a single model responding via CLI

**Technical Objectives:**
- Create clean project structure following Python best practices
- Implement comprehensive error handling and logging
- Build extensible foundation for future features
- Establish testing patterns and CI/CD pipeline

**Key Features:**
- [x] Project initialization with poetry/setuptools
- [x] Implement basic CLI using Typer with rich help text
- [x] Build abstract `LLMBackend` interface with async support
- [x] Create OpenAI backend with full API coverage
- [x] Add comprehensive error handling with retry logic
- [x] Implement environment-based configuration
- [x] Create logging infrastructure with structured output
- [x] Add basic unit and integration tests
- [x] Set up GitHub Actions for CI/CD

**Deliverable**: `debate "Hello AI" --agent gpt4` returns a single formatted response

---

#### 📍 Milestone 2: Multi-Model Conversations
> **Goal**: Enable two or more LLMs to have a conversation

**Technical Objectives:**
- Design message passing architecture
- Implement conversation state management
- Build provider-agnostic communication layer
- Create foundations for debate dynamics

**Key Features:**
- [ ] Extend CLI to accept multiple `--agents` parameter
- [ ] Design `Message` data structure with metadata
- [ ] Implement `ConversationState` manager
- [ ] Build turn-based orchestration with configurable order
- [ ] Add Anthropic backend with Claude support
- [ ] Add Google backend with Gemini support
- [ ] Create message formatting for each provider
- [ ] Implement conversation history tracking
- [ ] Add round limiting and termination conditions
- [ ] Build colored console output with agent identification
- [ ] Create conversation export functionality
- [ ] Add conversation resumption from checkpoint

**Deliverable**: `debate "Topic" --agents gpt4,claude3 --rounds 5` shows formatted back-and-forth dialogue

---

#### 📍 Milestone 3: Recursive Summarization Engine
> **Goal**: Add intelligent compression to maintain context

**Technical Objectives:**
- Implement sophisticated summarization algorithm
- Build token budget management system
- Create summary quality metrics
- Enable long-running debates

**Key Features:**
- [ ] Create dedicated `Summarizer` agent class
- [ ] Design summary state representation (S₀ → S₁ → ... → Sₙ)
- [ ] Implement structured summarization prompts
- [ ] Build token counting and budget allocation
- [ ] Add summary-every-N-rounds configuration
- [ ] Create delta detection for new arguments
- [ ] Implement stance change tracking
- [ ] Add summary quality validation
- [ ] Build summary persistence between rounds
- [ ] Create summary evolution visualization
- [ ] Implement adaptive compression ratios
- [ ] Add fallback for summary failures

**Deliverable**: Debates maintain coherent context via compression, enabling 50+ round discussions

---

#### 📍 Milestone 4: Configuration & Output System
> **Goal**: Full configurability and multiple output formats

**Technical Objectives:**
- Design comprehensive configuration schema
- Build flexible output system
- Implement experiment management
- Create reproducible workflows

**Key Features:**
- [ ] Design TOML schema with JSON Schema validation
- [ ] Create configuration dataclasses with Pydantic
- [ ] Implement hierarchical configuration loading
- [ ] Build `~/.debate/agents.toml` global config
- [ ] Add `.debate.toml` project-specific overrides
- [ ] Create environment variable interpolation
- [ ] Implement configuration validation with helpful errors
- [ ] Build Markdown output writer with template system
- [ ] Add JSON/JSONL export with metadata
- [ ] Create HTML output with styling
- [ ] Implement token usage and cost tracking
- [ ] Add experiment tracking with MLflow integration
- [ ] Build configuration generator CLI command

**Deliverable**: `debate --config experiment.toml` with full experimental control

---

#### 📍 Milestone 5: Async Execution & Performance
> **Goal**: Maximize throughput with concurrent operations

**Technical Objectives:**
- Refactor to pure async architecture
- Implement intelligent batching
- Add caching layers
- Optimize token usage

**Key Features:**
- [ ] Refactor all backends to async/await
- [ ] Implement concurrent agent calls with asyncio
- [ ] Add connection pooling with aiohttp
- [ ] Build request queuing with priority support
- [ ] Create token counting optimization
- [ ] Implement response caching layer
- [ ] Add incremental summary updates
- [ ] Build performance profiling tools
- [ ] Create benchmark suite
- [ ] Implement adaptive rate limiting
- [ ] Add batch API support where available
- [ ] Create performance regression tests

**Deliverable**: 3-5x faster debates through parallel execution and optimization

---

#### 📍 Milestone 6: Advanced Analytics
> **Goal**: Extract insights from debate dynamics

**Technical Objectives:**
- Build comprehensive metrics system
- Create visualization tools
- Implement statistical analysis
- Enable research workflows

**Key Features:**
- [ ] Build agent alignment matrix with similarity scores
- [ ] Implement convergence metrics (consensus tracking)
- [ ] Add stance evolution tracking over rounds
- [ ] Create argument novelty detection
- [ ] Build argument dependency graphs
- [ ] Add semantic similarity analysis
- [ ] Implement topic modeling on debates
- [ ] Create interactive visualizations with Plotly
- [ ] Build statistical significance tests
- [ ] Add debate quality metrics
- [ ] Create comparative analysis tools
- [ ] Generate LaTeX-ready figures
- [ ] Build research paper export templates

**Deliverable**: Comprehensive analytics dashboard and research-ready outputs

---

#### 📍 Milestone 7: Local Model Support
> **Goal**: Enable fully offline debates

**Technical Objectives:**
- Integrate with local model runners
- Optimize for local constraints
- Build hybrid workflows
- Create model management tools

**Key Features:**
- [ ] Implement Ollama backend with full API support
- [ ] Add LlamaCPP integration
- [ ] Create model capability detection
- [ ] Build automatic model downloading
- [ ] Implement memory usage optimization
- [ ] Add CPU/GPU detection and allocation
- [ ] Create fallback strategies for failures
- [ ] Build hybrid local/cloud debates
- [ ] Implement prompt optimization for smaller models
- [ ] Add quantization support (GGUF, GPTQ)
- [ ] Create model recommendation system
- [ ] Build performance benchmarks for local models
- [ ] Add model conversion tools

**Deliverable**: `debate "Topic" --agents ollama:llama2,ollama:mistral --local` runs fully offline

---

#### 📍 Milestone 8: Tool Integration Layer
> **Goal**: Enhance debates with external capabilities

**Technical Objectives:**
- Design plugin architecture
- Implement tool safety
- Build result integration
- Create tool marketplace

**Key Features:**
- [ ] Design tool plugin interface with capabilities
- [ ] Implement web search tool with multiple providers
- [ ] Add Python REPL with sandboxing
- [ ] Create citation fetcher with DOI support
- [ ] Build fact-checking integration
- [ ] Add calculator with symbolic math
- [ ] Implement Wikipedia search tool
- [ ] Create arXiv paper search
- [ ] Build tool result formatting
- [ ] Add tool usage in summaries
- [ ] Implement tool cost tracking
- [ ] Create custom tool SDK
- [ ] Build tool testing framework

**Deliverable**: Agents enhance arguments with real-time search, calculations, and citations

---

#### 📍 Milestone 9: Interactive TUI
> **Goal**: Real-time debate monitoring and control

**Technical Objectives:**
- Build responsive terminal interface
- Implement real-time updates
- Add intervention capabilities
- Create replay system

**Key Features:**
- [ ] Build Rich/Textual-based dashboard
- [ ] Add streaming response display
- [ ] Create live statistics panel
- [ ] Implement token usage meters
- [ ] Add alignment matrix visualization
- [ ] Build pause/resume functionality
- [ ] Create intervention system for prompts
- [ ] Add agent muting/unmuting
- [ ] Implement debate branching
- [ ] Build export from TUI
- [ ] Create replay functionality
- [ ] Add keyboard shortcuts
- [ ] Implement theming support

**Deliverable**: `debate --live` launches fully interactive terminal interface

---

#### 📍 Milestone 10: Research Platform Features
> **Goal**: Advanced capabilities for academic use

**Technical Objectives:**
- Implement advanced debate modes
- Build hypothesis testing
- Create collaboration features
- Enable meta-research

**Key Features:**
- [ ] Add self-critique phase after main debate
- [ ] Implement debate branching for exploration
- [ ] Create hypothesis testing mode
- [ ] Build A/B testing for prompts
- [ ] Add cross-debate analysis
- [ ] Implement debate genealogy tracking
- [ ] Create DOI minting for debates
- [ ] Build collaboration features
- [ ] Add peer review workflow
- [ ] Create debate corpora analysis
- [ ] Implement meta-debate capabilities
- [ ] Build research paper integration
- [ ] Add Jupyter notebook export

**Deliverable**: Complete research platform with advanced experimental capabilities

---

#### 📍 Milestone 11: Multi-Modal Debates
> **Goal**: Support debates about images, code, and mixed content

**Technical Objectives:**
- Extend message format for media
- Add vision model support
- Implement code understanding
- Build media management

**Key Features:**
- [ ] Extend message format for attachments
- [ ] Add image upload and management
- [ ] Implement vision model support (GPT-4V, Claude Vision)
- [ ] Add code syntax highlighting
- [ ] Build code execution sandboxing
- [ ] Create diagram generation tools
- [ ] Implement OCR for documents
- [ ] Add audio transcription support
- [ ] Build media storage system
- [ ] Create multi-modal summaries
- [ ] Add visualization exports
- [ ] Implement media citations

**Deliverable**: Debates can reference and discuss images, code, and documents

---

#### 📍 Milestone 12: Distributed Debates
> **Goal**: Scale debates across multiple machines

**Technical Objectives:**
- Build distributed architecture
- Implement coordination protocol
- Add fault tolerance
- Create management tools

**Key Features:**
- [ ] Design distributed debate protocol
- [ ] Implement coordinator node system
- [ ] Add worker node management
- [ ] Build debate sharding strategies
- [ ] Create node discovery system
- [ ] Implement failure recovery
- [ ] Add load balancing
- [ ] Build monitoring dashboard
- [ ] Create deployment tools
- [ ] Add Kubernetes operators
- [ ] Implement cross-region support
- [ ] Build security layer

**Deliverable**: Orchestrate massive debates across distributed infrastructure

---

## 🤝 Contributing

I welcome contributions from the community! The Multi-LLM Debate CLI is an open-source project that benefits from diverse perspectives and expertise.

### Areas for Contribution

**Core Features:**
- Additional LLM provider backends (Cohere, AI21, Hugging Face)
- New output format writers (LaTeX, EPUB, Jupyter)
- Advanced summarization strategies
- Novel analysis metrics

**Research Tools:**
- Statistical analysis methods
- Visualization improvements
- Benchmark tasks
- Evaluation frameworks

**Infrastructure:**
- Performance optimizations
- Testing improvements
- Documentation enhancements
- CI/CD pipelines

**Community:**
- Example configurations
- Tutorial creation
- Bug reports
- Feature requests
