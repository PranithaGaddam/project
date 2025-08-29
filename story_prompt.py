import random

# Define options for each story component
genres = [
    "Mystery", "Fantasy", "Science Fiction", "Romance", "Horror", "Historical"
]

themes = [
    "Overcoming adversity", "Forbidden love", "Revenge", "Identity discovery",
    "Sacrifice", "Redemption", "Moral dilemma"
]

character_types = [
    "Reluctant hero", "Outcast", "Rebel", "Mentor", "Naive apprentice",
    "Unlikely villain", "Secretive stranger", "Loyal friend"
]

def generate_prompt():
    genre = input(f"Choose a genre {genres}: ")
    theme = input(f"Choose a theme {themes}: ")
    character = input(f"Choose a character type {character_types}: ")

    # If user leaves input blank, pick random
    genre = genre if genre in genres else random.choice(genres)
    theme = theme if theme in themes else random.choice(themes)
    character = character if character in character_types else random.choice(character_types)

    story_prompt = (
        f"Write a {genre.lower()} story with the theme of '{theme.lower()}', "
        f"featuring a {character.lower()} as the main character. "
        f"What challenges do they face and how does the theme shape their actions?"
    )
    print("\nGenerated Story Prompt:\n", story_prompt)

if _name_ == "_main_":
    generate_prompt()
