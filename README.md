# Ultimate RAG Bootcamp

Nederlandstalige aantekeningen en kleine experimenten bij de Udemy-cursus
**Ultimate RAG Bootcamp**. Deze repository bevat uitleg over Retrieval-Augmented
Generation (RAG), instructies voor een lokale AI-omgeving en een Python-script
dat een lokaal Ollama-model test. Het is een leeromgeving; er staat nog geen
complete RAG-applicatie in.

## Inhoud

| Bestand | Beschrijving |
| --- | --- |
| [rag.md](./rag.md) | Korte introductie tot RAG |
| [Installatie.md](./Installatie.md) | Linux-installatie van Ollama en de modellen Qwen 2.5 3B en Nomic Embed Text |
| [Virtuele omgeving.md](./Virtuele%20omgeving.md) | Conda-omgevingen maken, activeren en beheren |
| [ollama-test.py](./ollama-test.py) | Voorbeeldscript dat een chatbericht naar Ollama stuurt |
| [LICENSE](./LICENSE) | GNU General Public License v3.0 |

## Aan de slag

### Benodigdheden

- Python 3.11 en Conda, of een andere Python-omgeving.
- [Ollama](https://ollama.com/) geïnstalleerd en actief.
- Het model `qwen2.5:3b`.

De installatiehandleiding beschrijft de installatie van Ollama op Linux. De
Conda-instructies zijn bedoeld om de Python-afhankelijkheden in een aparte
omgeving te houden.

### Python-omgeving instellen

Maak en activeer een Conda-omgeving en installeer de Ollama Python-bibliotheek:

```bash
conda create --name rag-bootcamp python=3.11
conda activate rag-bootcamp
python -m pip install ollama
```

### Ollama-model klaarzetten

Installeer Ollama volgens de [installatiehandleiding](./Installatie.md) en
download het taalmodel:

```bash
ollama pull qwen2.5:3b
```

### Voorbeeld uitvoeren

Voer vanuit de hoofdmap van deze repository het testscript uit:

```bash
python ollama-test.py
```

Het script stuurt een korte begroeting naar `qwen2.5:3b` en toont het antwoord
in de terminal. Zorg dat de Ollama-service actief is.

## RAG in het kort

RAG staat voor *Retrieval-Augmented Generation*. Een RAG-toepassing haalt
relevante informatie uit eigen documenten of een kennisbron op en geeft die
informatie mee aan een taalmodel bij het beantwoorden van een vraag. Zo kan
het antwoord worden gebaseerd op die bron, naast de kennis die het model
tijdens de training heeft opgedaan. Lees de [RAG-notities](./rag.md) voor de
introductie en de [installatiehandleiding](./Installatie.md) voor het
beschreven model- en architectuuroverzicht.

## Licentie

Dit project bevat een [GNU General Public License v3.0](./LICENSE).
