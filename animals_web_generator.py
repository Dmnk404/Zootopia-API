import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

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

def list_skin_types(animals):
    skin_types = []
    for animal in animals:
        if animal.get("characteristics", {}).get("skin_type"):
            skin_types.append(animal["characteristics"]["skin_type"].lower())
    return set(skin_types)


def main():
    """Main function"""

    animals_data = load_data('animals_data.json')
    with open("animals_template.html", encoding="utf-8") as f:
        html_file = f.read()
    print("Choose a skin type.")
    print("Available skin types:")
    skins = (list_skin_types(animals_data))
    for skin in skins:
        print(f"{skin} ", end="")
    while True:
        user_choice = input("").lower()
        if user_choice in skins:
            user_animals = [
                animal for animal in animals_data
                if animal["characteristics"].get("skin_type").lower() == user_choice]
            break
        else:
            print("Invalid choice")
            continue
    try:
        output = ""
        for animal in user_animals:
            output += serialize_animal(animal)

        new_html = html_file.replace("__REPLACE_ANIMALS_INFO__", output)

        with open("animals.html", "w", encoding="utf-8") as output_file:
            output_file.write(new_html)


    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()