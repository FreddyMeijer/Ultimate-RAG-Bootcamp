# Anaconda installeren

![Linux](https://img.shields.io/badge/Ubuntu-26.04.1-orange)
![Conda](https://img.shields.io/badge/Conda-25.11-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)

## Waarom Anaconda?
Met Anaconda (Conda) kun je verschillende Python-omgevingen aanmaken en beheren.

Een omgeving bevat een eigen:
- Python-versie.
- Geïnstalleerde Python-packages.
- Afhankelijkheden (dependencies).

Dit is vooral handig wanneer je met verschillende projecten werkt. Zo voorkom je dat packages van het ene project conflicteren met packages van een ander project.

**Voorbeeld:** Voor het Ultimate RAG Bootcamp gebruik je een aparte omgeving met Python, LangChain, LangGraph en andere AI-libraries.

## Anaconda downloaden
Open de terminal in `sudo` modus en typ:

```bash
cd ~/Downloads
curl -O https://repo.anaconda.com/archive/Anaconda3-2026.07-1-Linux-x86_64.sh
bash Anaconda3-2026.07-1-Linux-x86_64.sh
```
Volg de aanwijzingen en beantwoord de vragen.

Als de installatie voltooid is kan je controleren of de installatie voltooid is met `conda info`:

```bash
(rag-bootcamp) freddy-meijer@freddy-meijer-Legion-5-17ITH6H:~$ conda info

     active environment : rag-bootcamp
    active env location : /home/freddy-meijer/anaconda3/envs/rag-bootcamp
            shell level : 2
       user config file : /home/freddy-meijer/.condarc
 populated config files : /home/freddy-meijer/anaconda3/.condarc
                          /home/freddy-meijer/anaconda3/condarc.d/anaconda-auth.yml
          conda version : 25.11.1
    conda-build version : 25.11.1
         python version : 3.13.9.final.0
                 solver : libmamba (default)
       virtual packages : __archspec=1=icelake
                          __conda=25.11.1=0
                          __cuda=13.0=0
                          __glibc=2.43=0
                          __linux=7.0.0=0
                          __unix=0=0
       base environment : /home/freddy-meijer/anaconda3  (writable)
      conda av data dir : /home/freddy-meijer/anaconda3/etc/conda
  conda av metadata url : None
           channel URLs : https://repo.anaconda.com/pkgs/main/linux-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/linux-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /home/freddy-meijer/anaconda3/pkgs
                          /home/freddy-meijer/.conda/pkgs
       envs directories : /home/freddy-meijer/anaconda3/envs
                          /home/freddy-meijer/.conda/envs
               platform : linux-64
             user-agent : conda/25.11.1 requests/2.32.5 CPython/3.13.9 Linux/7.0.0-43-generic ubuntu/26.04.1 glibc/2.43 solver/libmamba conda-libmamba-solver/25.11.0 libmambapy/2.3.2 aau/0.7.5 c/. s/. e/.
                UID:GID : 1000:1000
             netrc file : None
           offline mode : False

(rag-bootcamp) freddy-meijer@freddy-meijer-Legion-5-17ITH6H:~$ 

```

## Een nieuwe omgeving aanmaken

Open de Anaconda Prompt of een terminal waarin Conda beschikbaar is.

Gebruik het volgende commando:

```bash
conda create --name rag-bootcamp python=3.11
```

Uitleg:

| Onderdeel | Betekenis |
|---|---|
| `conda create` | Maakt een nieuwe omgeving aan |
| `--name` | Geeft de omgeving een naam |
| `rag-bootcamp` | Naam van de omgeving |
| `python=3.11` | Installeert Python-versie 3.11 |

Bevestig de installatie met `y` wanneer Conda daarom vraagt.

## Een omgeving activeren

Voordat je met een omgeving gaat werken, moet je deze activeren.

```bash
conda activate rag-bootcamp
```

Je ziet nu de naam van de actieve omgeving voor de prompt staan:

```bash
(rag-bootcamp) C:\Users\Gebruiker>
```

Vanaf dit moment worden Python en de packages uit deze omgeving gebruikt.

## Packages installeren

Wanneer de omgeving actief is, kun je Python-packages installeren.

Bijvoorbeeld voor het Ultimate RAG Bootcamp:

```bash
pip install langchain langgraph langsmith
```

Voor Jupyter Notebook:

```bash
pip install jupyter notebook
```

**Let op:** Installeer packages bij voorkeur binnen de actieve Conda-omgeving. Zo houd je de afhankelijkheden per project gescheiden.

---

## Controleren welke omgevingen bestaan

Met het volgende commando krijg je een overzicht van alle Conda-omgevingen:

```bash
conda env list
```

Voorbeeld:

```text
# conda environments:
#
# * -> active
# + -> frozen
base                     /home/freddy-meijer/anaconda3
data_analyse             /home/freddy-meijer/anaconda3/envs/data_analyse
rag-bootcamp         *   /home/freddy-meijer/anaconda3/envs/rag-bootcamp
```

Het sterretje (`*`) geeft aan welke omgeving momenteel actief is.

---

## Wisselen tussen omgevingen

Wil je een andere omgeving gebruiken? Deactiveer dan eerst de huidige omgeving.

```bash
conda deactivate
```

Activeer vervolgens de gewenste omgeving:

```bash
conda activate data_analyse
```

Je kunt op deze manier eenvoudig tussen verschillende projecten wisselen.

---

## Een omgeving verwijderen

Wanneer je een omgeving niet meer nodig hebt, kun je deze verwijderen.

```bash
conda env remove --name rag-bootcamp
```

Hiermee worden de omgeving en de daarin geïnstalleerde packages verwijderd.

**Let op:** Dit verwijdert niet je projectbestanden of Python-scripts.

---

## Overzicht van belangrijke Conda-commando's

| Commando | Functie |
|---|---|
| `conda create -n naam python=3.11` | Nieuwe omgeving aanmaken |
| `conda activate naam` | Omgeving activeren |
| `conda deactivate` | Omgeving deactiveren |
| `conda env list` | Alle omgevingen tonen |
| `conda info` | Conda-configuratie bekijken |
| `conda list` | Packages in actieve omgeving tonen |
| `conda install package` | Package installeren via Conda |
| `conda env remove -n naam` | Omgeving verwijderen |

---

## Een omgeving exporteren

Wil je een Conda-omgeving reproduceerbaar maken of delen via GitHub? Dan kun je de configuratie exporteren.

Activeer eerst de gewenste omgeving:

```bash
conda activate rag-bootcamp
```

Exporteer vervolgens de configuratie:

```bash
conda env export --from-history > environment.yml
```

Hiermee maak je een bestand met de belangrijkste expliciet geïnstalleerde Conda-afhankelijkheden.

Een andere computer kan deze omgeving vervolgens aanmaken met:

```bash
conda env create -f environment.yml
```

Dit is handig wanneer je jouw RAG-project op een andere computer wilt voortzetten.

---

## Samenvatting

De belangrijkste commando's om te onthouden:

```bash
# Nieuwe omgeving maken
conda create -n rag-bootcamp python=3.11

# Omgeving activeren
conda activate rag-bootcamp

# Packages installeren
pip install langchain langgraph langsmith

# Omgevingen bekijken
conda env list

# Omgeving verlaten
conda deactivate

# Omgeving exporteren
conda env export --from-history > environment.yml
```

**Belangrijk principe:** Maak voor ieder groter Python-project een eigen Conda-omgeving. Daarmee voorkom je versieconflicten en houd je jouw ontwikkelomgeving overzichtelijk.