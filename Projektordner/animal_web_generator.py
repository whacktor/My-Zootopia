import json

def load_data(file_path):
    """Lädt die JSON-Datei mit Tierdaten."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

# JSON laden
data = load_data("animals_data.json")

# HTML-String erzeugen
output = ''  # leerer String

for animal_data in data:
    name = animal_data.get('name', 'Unknown')
    characteristics = animal_data.get('characteristics', {})
    diet = characteristics.get('diet')
    animal_type = characteristics.get('type')
    locations = animal_data.get('locations', [])
    location = locations[0] if locations else None

    # HTML für ein Tier
    card_html = f'<li class="cards__item">\n'
    card_html += f'  <div class="card__title">{name}</div>\n'
    card_html += f'  <p class="card__text">\n'
    if diet:
        card_html += f'      <strong>Diet:</strong> {diet}<br/>\n'
    if location:
        card_html += f'      <strong>Location:</strong> {location}<br/>\n'
    if animal_type:
        card_html += f'      <strong>Type:</strong> {animal_type}<br/>\n'
    card_html += '  </p>\n</li>\n\n'

    output += card_html

# HTML-String ausgeben
print(output)