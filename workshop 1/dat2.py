# Importeer de nodige bibliotheken voor schermafbeeldingen en bestandsbeheer.
import pyautogui  # Voor het maken van schermafbeeldingen
from PIL import Image  # Voor beeldbewerking
import os  # Om bestanden te beheren

# Stap 1: Maak een schermafbeelding.
my_screenshot = pyautogui.screenshot()

# Stap 2: Sla de schermafbeelding op een specifieke locatie op.
screenshot_path = r'screenshot.png'
my_screenshot.save(screenshot_path)

# Stap 3: Converteer de schermafbeelding naar een PDF-bestand.
image_1 = Image.open(screenshot_path)
im_1 = image_1.convert('RGB')

# Stap 4: Sla de PDF op een andere locatie op.
pdf_path = r'screenshot.pdf'
im_1.save(pdf_path)

# Stap 5: Verwijder de tijdelijke schermafbeelding, omdat we nu de PDF hebben.
os.remove(screenshot_path)

# Klaar! We hebben een schermafbeelding gemaakt, omgezet in een PDF en de tijdelijke schermafbeelding verwijderd.
