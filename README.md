# Ultimate RAG Bootcamp

Nederlandstalige aantekeningen en voorbeelden voor het leren werken met
Retrieval-Augmented Generation (RAG). De repository bevat eerst theorie over
RAG en aanwijzingen voor het opzetten van een lokale AI-omgeving met Anaconda,
Ollama, Qwen en Nomic Embed Text.

## Inhoud

| Bestand | Beschrijving |
| --- | --- |
| [1. installatie anaconda.md](./1.%20installatie%20anaconda.md) | Anaconda/Conda installeren en beheren |
| [2. Installatie Ollama en Qwen.md](./2.%20Installatie%20Ollama%20en%20Qwen.md) | Ollama, Qwen 2.5 3B en Nomic Embed Text lokaal installeren |
| [theorie.md](./theorie.md) | Uitleg over RAG, embeddings, chunks, retrieval en generation |
| [ollama_test.py](./ollama_test.py) | Python-voorbeeld dat een bericht via de Ollama API naar Qwen stuurt |
| [LICENSE](./LICENSE) | GNU General Public License v3.0 |

## Aan de slag

### Benodigdheden

- Linux
- Anaconda of Miniconda
- Python 3.11
- Ollama
- Het Ollama-model `qwen2.5:3b`
- Voor RAG-experimenten: `nomic-embed-text`

De gedetailleerde instructies staan in de twee installatiehandleidingen.

### Python-omgeving instellen

Maak een aparte Conda-omgeving voor het bootcamp:

```bash
conda create --name rag-bootcamp python=3.11
conda activate rag-bootcamp
```

Installeer daarna de Python-bibliotheek voor Ollama:

```bash
python -m pip install ollama
```

Zie [1. installatie anaconda.md](./1.%20installatie%20anaconda.md) voor meer
Conda-opdrachten en voorbeelden.

### Ollama en de modellen klaarzetten

Installeer Ollama op Linux en controleer de installatie:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama --version
ollama serve
```

De Ollama-service kan al automatisch draaien na de installatie. Gebruik daarom
alleen `ollama serve` als je de service handmatig moet starten.

Download of start Qwen:

```bash
ollama run qwen2.5:3b
```

Het commando `ollama run` downloadt het model indien nodig en opent een
interactieve sessie. Typ `/bye` om af te sluiten.

Installeer voor toekomstige RAG-oefeningen ook het embeddingmodel:

```bash
ollama pull nomic-embed-text
ollama list
```

De volledige installatie en een overzicht van de lokale architectuur staan in
[2. Installatie Ollama en Qwen.md](./2.%20Installatie%20Ollama%20en%20Qwen.md).

### Ollama-test uitvoeren

Voer vanuit de hoofdmap van deze repository het testscript uit:

```bash
python ollama_test.py
```

Het script stuurt een korte begroeting naar `qwen2.5:3b` en toont het antwoord
in de terminal. Zorg dat de Ollama-service actief is en installeer het model
vooraf met `ollama pull qwen2.5:3b`.

## RAG in het kort

RAG staat voor *Retrieval-Augmented Generation*. Een RAG-toepassing haalt
relevante informatie uit eigen documenten of een kennisbron op en geeft die
informatie mee aan een taalmodel bij het beantwoorden van een vraag. Zo kan
een antwoord gebaseerd zijn op de opgegeven bron naast de kennis die het model
tijdens de training heeft opgedaan.

De kernfasen zijn documentinvoer en verwerking, queryverwerking en generatie.
De [theorie](./theorie.md) legt uit hoe documenten worden opgesplitst in
chunks, hoe embeddings en vectorzoeking werken en hoe opgehaalde context wordt
opgenomen in de prompt.

## Huidige inhoud

Deze repository is een leeromgeving. Op dit moment bevat de repository:

- Nederlandstalige RAG-theorie;
- installatie-instructies voor Anaconda en Conda;
- installatie-instructies voor Ollama, Qwen en Nomic Embed Text;
- één eenvoudig Python-script dat met een lokaal Qwen-model communiceert.

Er is nog geen complete RAG-pipeline of applicatie met een vector database
opgenomen.

## Licentie

Dit project bevat een [GNU General Public License v3.0](./LICENSE).
