import requests

def load_data_from_api(search_term):
    """Fetches animal data from the API by search term"""
    url = f"https://api.api-ninjas.com/v1/animals?name={search_term}"
    headers = {
        "X-Api-Key": "DEIN_API_KEY_HIER"  # <-- Deinen API-Key hier einfügen
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def serialize_animal(animal_obj):
    """ Serializes an animal object """
    output = ""
    output += '<li class="cards__item">'
    output += '<div class="card__title">'
    output += f"{animal_obj['name']} </div>"
    output += '<div class="card__text">'
    output += "<ul>"
    if animal_obj.get("characteristics", {}).get("diet"):
        output += f"<li><strong>Diet</strong>: {animal_obj['characteristics']['diet']}</li>"
    if animal_obj.get("locations"):
        output += f"<li><strong>Location</strong>: {animal_obj['locations'][0]}</li>"
    if animal_obj.get("characteristics", {}).get("type"):
        output += f"<li><strong>Type</strong>: {animal_obj['characteristics']['type']}</li>"
    if animal_obj.get("characteristics", {}).get("color"):
        output += f"<li><strong>Color</strong>: {animal_obj['characteristics']['color']}</li>"
    if animal_obj.get("characteristics", {}).get("lifespan"):
        output += f"<li><strong>Lifespan</strong>: {animal_obj['characteristics']['lifespan']}</li>"
    output += "</ul></div></li>"
    return output

def main():
    """Main function"""
    # 🐾 1. Tiernamen vom Benutzer abfragen
    search_term = input("Enter a name of an animal: ").strip()

    # 🐾 2. Daten aus API laden
    animals_data = load_data_from_api(search_term)

    if not animals_data:
        print(f"No results found for '{search_term}'.")
        return

    # 🐾 3. HTML-Template laden
    with open("animals_template.html", encoding="utf-8") as f:
        html_file = f.read()

    # 🐾 4. Daten in HTML umwandeln
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    # 🐾 5. HTML-Datei erzeugen
    new_html = html_file.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(new_html)

    # 🐾 6. Erfolgsmeldung
    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()