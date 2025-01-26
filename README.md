# Karte-Memuar: Flashcard Learning Application

## Overview
Karte-Memuar is a language learning application built using Python and Tkinter. It helps users learn French words with flashcards, providing the English translation after a timed delay. Users can mark words they know to focus on unfamiliar ones, fostering efficient learning.

## Problem Details
Learning a new language often involves memorizing vocabulary. Flashcards are a proven method for this, but physical cards can be inconvenient. Karte-Memuar provides a digital solution, allowing users to interactively learn French vocabulary with automatic progress tracking.

## Example
1. The app displays a flashcard with a French word.
2. After 3 seconds, the card flips to show the English translation.
3. The user can mark the word as "Known" by clicking the Green checkmark, or Red X if the user did not know the word. 
4. Known words are removed from the learning pool, and the progress is saved automatically.
5. After the user clicks on either button, the game shows the next card.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/karte-memuar.git
   cd karte-memuar
   ```
2. Install dependencies:
- Ensure Python 3.8+ is installed.
- Install required libraries:
  ```bash
  pip install pandas
  ```
## Usage
1. Run the program:
   ```bash
   python karte_memuar.py
   ```
2. The application window will open. Use the buttons to mark words as known or move to the next word.
3. Progress is saved in ```words_to_learn.csv```.

## Input File
- ```french_words.csv```: A CSV file containing two columns: ```French``` and ```English```. Example: 
   ```csv
   French,English
   chat,cat
   chien,dog
   pomme,apple
   ```

## Error Handling
- If ```words_to_learn.csv``` is missing or empty, the program regenerates it from ```french_words.csv```.
- If any required assets (images or data files) are missing, the program will raise an error.

## Explanation of the Code
1. Data Loading:
   - The program loads the words from ```words_to_learn.csv``` or regenerates it from ```french_words.csv```.
2. Card Management:
   - Words are displayed randomly.
   - Users can mark words as known, removing them from future practice.
3. UI Design:
   - Built with Tkinter, the interface includes a canvas for flashcards and buttons for interaction.
4. State Management:
   - Tracks progress by saving unlearned words to ```words_to_learn.csv```.

## Features
- Digital flashcard system.
- Automated tracking of known and unknown words.
- Randomized word selection for varied practice.
- Intuitive user interface with button controls.

## Future Enhancements
- Add support for multiple languages.
- Include a scoring system for motivation.
- Allow users to upload custom word lists.

## Acknowledgments
- Data sourced from publicly available French-English word lists.
- Inspiration from traditional flashcard learning methods.

## License
This project is licensed under the [GNU General Public Use v3 License](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Affiliation
This code is part of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" by Dr. Angela Yu and AppBrewery.