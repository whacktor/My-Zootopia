import os
import data_fetcher

OUTPUT_DIR = "output"
OUTPUT_FILE = "animals.html"


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


def generate_animals_list_html(data):
    return "".join(serialize_animal(a) for a in data)


def build_full_page(content_html, title="Animals"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>{title}</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 24px; }}
    ul {{ list-style: none; padding: 0; }}
    .cards__item {{ border: 1px solid #ddd; border-radius: 8px; padding: 12px; margin-bottom: 12px; }}
    .card__title {{ font-size: 18px; font-weight: 700; margin-bottom: 6px; }}
    .card__text {{ margin: 0; }}
  </style>
</head>
<body>
  {content_html}
</body>
</html>
"""


def write_html_file(file_path, html):
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    animal_name = input("Please enter an animal: ").strip()

    if not animal_name:
        html = build_full_page('<h2>Please enter an animal name.</h2>')
        out_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
        write_html_file(out_path, html)
        print(f"Website was successfully generated to the file {out_path}.")
        return

    data = data_fetcher.fetch_data(animal_name)

    # Milestone 3: keine Ergebnisse
    if not data:
        content = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
        html = build_full_page(content)
    else:
        animals_list = generate_animals_list_html(data)
        html = build_full_page(f"<ul>\n{animals_list}</ul>")

    out_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    write_html_file(out_path, html)
    print(f"Website was successfully generated to the file {out_path}.")


if __name__ == "__main__":
    main()