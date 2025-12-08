import json


def load_data(file_path):
    """Lädt die JSON-Datei mit Tierdaten."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def serialize_animal(animal_obj):

    name = animal_obj.get("name", "Unknown")
    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type")
    locations = animal_obj.get("locations", [])
    location = locations[0] if locations else None

    html = '<li class="cards__item">\n'
    html += f'  <div class="card__title">{name}</div>\n'
    html += '  <p class="card__text">\n'
    if diet:
        html += f'      <strong>Diet:</strong> {diet}<br/>\n'
    if location:
        html += f'      <strong>Location:</strong> {location}<br/>\n'
    if animal_type:
        html += f'      <strong>Type:</strong> {animal_type}<br/>\n'
    html += '  </p>\n</li>\n\n'

    return html


def generate_html(data):
    output = ""
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output


def main():
    data = load_data("animals_data.json")
    html_output = generate_html(data)
    print(html_output)


if __name__ == "__main__":
    main()