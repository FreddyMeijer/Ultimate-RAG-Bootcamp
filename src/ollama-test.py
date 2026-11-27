"""
Module: Ollama Chat-interactie

Beschrijving:
    Deze module demonstreert hoe je verbinding maakt met een lokaal
    draaiend Ollama-taalmodel met behulp van de Ollama Python-bibliotheek.
"""

import ollama


def main():
    """
    Verstuur een bericht naar een lokaal Ollama-taalmodel en toon het antwoord.

    Deze functie voert de volgende stappen uit:
        1. Maakt verbinding met de Ollama-service.
        2. Verstuurt een gebruikersbericht naar het opgegeven taalmodel.
        3. Ontvangt het gegenereerde antwoord.
        4. Toont het antwoord in de console.

    Returns
    -------
    None
        Deze functie retourneert geen waarde.
        Het antwoord van het taalmodel wordt rechtstreeks in de console getoond.
    """

    # Verstuur een chatverzoek naar het opgegeven Ollama-taalmodel.
    response = ollama.chat(
        model='qwen2.5:3b',
        stream=False,
        messages=[
            {
                # Geef aan dat het bericht afkomstig is van de gebruiker.
                'role': 'user',

                # Definieer de invoerprompt voor het taalmodel.
                'content': 'Hallo Qwen! Kun je mij helpen met mijn RAG Bootcamp?'
            }
        ]
    )

    # Haal het gegenereerde antwoord op en toon dit in de console.
    print(response['message']['content'])


# Voer de hoofdfunctie alleen uit wanneer dit bestand rechtstreeks wordt gestart.
if __name__ == "__main__":
    main()
    