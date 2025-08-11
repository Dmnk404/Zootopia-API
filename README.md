Animals Web Generator

This Python project generates an HTML webpage displaying information about animals.
It fetches animal data dynamically from an external API based on user input.

Features
User inputs an animal name (e.g., "Fox").

The program retrieves animal details from the API.

Generates an animals.html file with the animal information.

Setup
Install Python 3

Install dependencies:

pip install -r requirements.txt

Create a .env file in the project folder and add your API key:

API_KEY=your_api_key_here

Usage

python animals_web_generator.py

Notes
The .env file is included in .gitignore to keep your API key private.

Requires a valid API key from API Ninjas.