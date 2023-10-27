
import random

# Functie om een vraag te stellen
def stel_vraag(vraag, opties):
    print(vraag)
    for i, optie in enumerate(opties, start=1):
        print(f"{i}. {optie}")
    antwoord = int(input("Kies het juiste antwoord (1-4): "))
    return antwoord

# Functie om het antwoord te controleren
def controleer_antwoord(antwoord, correct_antwoord):
    if antwoord == correct_antwoord:
        print(willekeurig_goed_bericht())
        return True
    else:
        print(willekeurig_fout_bericht())
        return False

# Functie voor een willekeurig goed bericht
def willekeurig_goed_bericht():
    goed_berichten = ["Goed gedaan!", "Fantastisch!", "Super slim!", "Correct!"]
    return random.choice(goed_berichten)

# Functie voor een willekeurig fout bericht
def willekeurig_fout_bericht():
    fout_berichten = ["Helaas, dat is niet correct.", "Niet juist.", "Probeer het nog eens.", "Fout antwoord."]
    return random.choice(fout_berichten)

# Een lijst met vragen en antwoorden
vragen = [
    {
        "vraag": "Wat is de hoofdstad van Frankrijk?",
        "opties": ["Berlijn", "Madrid", "Parijs", "Rome"],
        "correct_antwoord": 3,
    },
     {
        "vraag": "Welke rivier stroomt door Egypte?",
        "opties": ["Nijl", "Amazone", "Mississippi", "Rijn"],
        "correct_antwoord": 1,
    },
    {
        "vraag": "In welk land ligt de Kilimanjaro, de hoogste berg van Afrika?",
        "opties": ["Kenia", "Zuid-Afrika", "Tanzania", "Egypte"],
        "correct_antwoord": 3,
    },
    {
        "vraag": "Wat is de hoofdstad van Japan?",
        "opties": ["Beijing", "Tokio", "Seoul", "Bangkok"],
        "correct_antwoord": 2,
    },
    {
        "vraag": "Welk land staat bekend om zijn fjorden en vikinggeschiedenis?",
        "opties": ["Zweden", "Noorwegen", "IJsland", "Denemarken"],
        "correct_antwoord": 1,
    },
    {
        "vraag": "Wat is de grootste woestijn ter wereld?",
        "opties": ["Gobiwoestijn", "Saharawoestijn", "Atacamawoestijn", "Kalahariwoestijn"],
        "correct_antwoord": 1,
    },
    {
        "vraag": "In welk continent ligt de Amazone-regenwoud?",
        "opties": ["Afrika", "Zuid-Amerika", "Azië", "Oceanië"],
        "correct_antwoord": 1,
    },
    {
        "vraag": "Wat is de langste rivier ter wereld?",
        "opties": ["Mississippi", "Nijl", "Amazonerivier", "Rijn"],
        "correct_antwoord": 1,
    },
    {
        "vraag": "In welk land ligt de stad Wenen?",
        "opties": ["Italië", "Duitsland", "Oostenrijk", "Tsjechië"],
        "correct_antwoord": 2,
    },
    {
        "vraag": "Welk land heeft de meeste eilanden ter wereld?",
        "opties": ["Filipijnen", "Indonesië", "Griekenland", "Japan"],
        "correct_antwoord": 1,
    },
    {
        "vraag": "Wat is de grootste stad ter wereld (in bevolking)?",
        "opties": ["Shanghai", "Mumbai", "Peking", "New York"],
        "correct_antwoord": 1,
    },
    {
        "vraag": "Wat is het kleinste continent ter wereld?",
        "opties": ["Azië", "Afrika", "Europa", "Australië"],
        "correct_antwoord": 3,
    },
    {
        "vraag": "Welk land ligt ten zuiden van de Verenigde Staten?",
        "opties": ["Mexico", "Canada", "Brazilië", "Argentinië"],
        "correct_antwoord": 0,
    },
    {
        "vraag": "In welk land vind je de Kilimanjaro-berg?",
        "opties": ["Tanzania", "Kenia", "Ethiopië", "Nigeria"],
        "correct_antwoord": 0,
    },
]

# Willekeurige volgorde van vragen
random.shuffle(vragen)

score = 0

print("Welkom bij de Aardrijkskunde Quiz!")
print("Beantwoord de volgende vragen:")
for i, vraag in enumerate(vragen, start=1):
    antwoord = stel_vraag(vraag["vraag"], vraag["opties"])
    if controleer_antwoord(antwoord, vraag["correct_antwoord"]):
        score += 1

print(f"Je hebt {score} van de {len(vragen)} vragen correct beantwoord.")
if score == len(vragen):
    print("Goed gedaan!")
    for _ in range(3):
        print("." * 10)
else:
    print("Blijf leren en je zult het nog beter doen!")
