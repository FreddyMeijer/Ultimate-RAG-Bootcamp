# Ultimate RAG Bootcamp

Nederlandstalige aantekeningen en voorbeelden voor het leren werken met Retrieval-Augmented Generation (RAG) op basis van de Udemy-cursus *Ultimate RAG Bootcamp*. De repository bevat theorie over RAG en handleidingen voor het opzetten van een lokale AI-omgeving met Anaconda, Ollama, Qwen en Nomic Embed Text.

## Inhoud

| Bestand | Beschrijving |
| --- | --- |
| [requirements.txt](requirements.txt) | Python-afhankelijkheden voor de RAG-experimenten |
| [notes/1-installatie-anaconda.md](notes/1-installatie-anaconda.md) | Anaconda/Conda installeren en beheren op Linux |
| [notes/2-installatie-ollama-en-qwen.md](notes/2-installatie-ollama-en-qwen.md) | Ollama, `qwen2.5:3b` en `nomic-embed-text` lokaal installeren |
| [notes/3-rag-theorie.md](notes/3-rag-theorie.md) | Uitleg over RAG, prompt engineering en fine-tuning |
| [src/ollama-test.py](src/ollama-test.py) | Python-script dat via de Ollama-bibliotheek een bericht naar `qwen2.5:3b` stuurt |
| [LICENSE](LICENSE) | GNU General Public License v3.0 |

## Projectstructuur

```text
├── data/
├── LICENSE
├── .gitignore
├── README.md
├── requirements.txt
├── notes/
│   ├── 1-installatie-anaconda.md
│   ├── 2-installatie-ollama-en-qwen.md
│   └── 3-rag-theorie.md
└── src/
    └── ollama-test.py
```

## Aan de slag

### Benodigdheden

* Linux
* Anaconda of Miniconda
* Python 3.11
* Ollama
* Het taalmodel `qwen2.5:3b`
* Het embeddingmodel `nomic-embed-text` (voor RAG-experimenten)

Uitgebreide instructies vind je in [notes/1-installatie-anaconda.md](notes/1-installatie-anaconda.md) en [notes/2-installatie-ollama-en-qwen.md](notes/2-installatie-ollama-en-qwen.md).

### 1. Python-omgeving instellen

Maak een aparte Conda-omgeving en installeer de Python-afhankelijkheden vanuit de hoofdmap van de repository:

```bash
conda create --name rag-bootcamp python=3.11
conda activate rag-bootcamp
pip install -r requirements.txt
pip install ollama
```

Met `pip install -r requirements.txt` installeer je alle pakketten die in `requirements.txt` staan. De Ollama-Python-bibliotheek installeer je apart, omdat die niet in dat bestand is opgenomen.

### 2. Ollama en modellen instellen

Installeer Ollama met de [handleiding voor de lokale AI-omgeving](notes/2-installatie-ollama-en-qwen.md) en zorg dat de Ollama-service actief is. Download daarna de modellen:

```bash
ollama pull qwen2.5:3b
ollama pull nomic-embed-text
```

`qwen2.5:3b` is nodig voor het voorbeeldscript. `nomic-embed-text` is bedoeld voor RAG-experimenten.

### 3. Voorbeeldscript uitvoeren

Voer vanuit de hoofdmap van de repository het script uit:

```bash
python src/ollama-test.py
```

Het script stuurt een bericht naar `qwen2.5:3b` en toont het antwoord in de terminal.
