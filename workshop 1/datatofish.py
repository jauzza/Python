# Importeer de module matplotlib.pyplot en geef deze de alias 'plt' voor gebruiksgemak.
import matplotlib.pyplot as plt

# Definieer de gegevens die we willen weergeven in de taartgrafiek.
my_data = [300, 500, 700]

# Definieer labels voor de verschillende delen van de taartgrafiek.
my_labels = 'Taken in afwachting', 'Taken in uitvoering', 'Voltooide taken'

# Definieer de kleuren voor de verschillende delen van de taartgrafiek.
my_colors = ['lightblue', 'lightsteelblue', 'silver']

# Specificeer hoeveel elk deel van de taartgrafiek moet uitsteken (0 betekent geen uitsteking).
my_explode = (0, 0.1, 0)

# Maak een taartgrafiek met de opgegeven gegevens en instellingen.
plt.pie(my_data, labels=my_labels, autopct='%1.1f%%', startangle=15, shadow=True, colors=my_colors, explode=my_explode)

# Voeg een titel toe aan de taartgrafiek voor duidelijkheid.
plt.title('Verdeling van mijn taken')

# Zorg ervoor dat de taartgrafiek er cirkelvormig uitziet.
plt.axis('equal')

# Toon de taartgrafiek.
plt.show()


