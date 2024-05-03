import random

# Irregular verbs and their correct past forms
irregular_verbs = {
    "eat": ["ate", "eaten"],
    "go": ["went", "gone"],
    "sing": ["sang", "sung"],
    "take": ["took", "taken"],
    "speak": ["spoke", "spoken"],
    "write": ["wrote", "written"],
    "swim": ["swam", "swum"],
    "break": ["broke", "broken"]
    # Add more verbs as needed
}

def irregular_verb_game():
    while True:
        # Randomly select a verb from the dictionary
        base_verb, correct_past_forms = random.choice(list(irregular_verbs.items()))

        # Ask the user for the past tense
        user_past_tense = input(f"What is the past tense of the verb '{base_verb}'? ")

        # Ask the user for the past participle
        user_past_participle = input(f"What is the past participle of the verb '{base_verb}'? ")

        # Check if the user wants to end the game
        if user_past_tense.lower() == 'q' or user_past_participle.lower() == 'q':
            print("Thanks for playing! Goodbye.")
            break

        # Check if the user's answers are correct
        if user_past_tense.lower() == correct_past_forms[0] and user_past_participle.lower() == correct_past_forms[1]:
            print("Correct! Well done.")
        else:
            print(f"Oops! The correct answers are: {correct_past_forms[0]} (past) and {correct_past_forms[1]} (past participle).")

# Play the game
irregular_verb_game()
