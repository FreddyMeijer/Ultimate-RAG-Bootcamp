# Ultimate RAG Bootcamp

Nederlandstalige aantekeningen en voorbeelden voor het leren werken met Retrieval-Augmented Generation (RAG) op basis van de Udemy-cursus *Ultimate RAG Bootcamp*. De repository bevat theorie over RAG en handleidingen voor het opzetten van een lokale AI-omgeving met Anaconda, Ollama, Qwen en Nomic Embed Text.

## Inhoud

| Bestand | Beschrijving |
| --- | --- |
| [theorie.md](theorie.md) | Uitleg over RAG, chunks, embeddings, vectorzoeking, queryverwerking en generatie |
| [1. installatie anaconda.md](1.%20installatie%20anaconda.md) | Anaconda/Conda installeren en beheren op Linux |
| [2. Installatie Ollama en Qwen.md](2.%20Installatie%20Ollama%20en%20Qwen.md) | Ollama, `qwen2.5:3b` en `nomic-embed-text` lokaal installeren |
| [ollama_test.py](ollama_test.py) | Python-script dat via de Ollama-bibliotheek een bericht naar `qwen2.5:3b` stuurt |
| [LICENSE](LICENSE) | GNU General Public License v3.0 |

## Aan de slag

### Benodigdheden

* Linux
* Anaconda of Miniconda
* Python 3.11
* Ollama
* Het taalmodel `qwen2.5:3b`
* Het embeddingmodel `nomic-embed-text` (voor RAG-experimenten)

Uitgebreide instructies vind je in [1. installatie anaconda.md](1.%20installatie%20anaconda.md) en [2. Installatie Ollama en Qwen.md](2.%20Installatie%20Ollama%20en%20Qwen.md).

### 1. Python-omgeving instellen

Maak een aparte Conda-omgeving voor het bootcamp:

```bash
conda create --name rag-bootcamp python=3.11
conda activate rag-bootcamp