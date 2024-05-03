# Irregular verbs and their correct past forms
irregular_verbs = {
    "rebid": ["rebid", "rebid"],
    "rebind": ["rebound", "rebound"],
    "fly": ["flew", "flown"],
    "forbid": ["forbade", "forbidden"],
    "forsake": ["forsook", "forsaken"],
    "freeze": ["froze", "frozen"],
    "frostbite": ["frostbit", "frostbitten"],
    "hew": ["hewed", "hewn"],
    "hide": ["hid", "hidden"],
    "saw": ["sawed", "sawn"],
    "shear": ["sheared", "shorn"],
    "slay": ["slew", "slain"],
    "spit": ["spat", "spat"],
    "stride": ["strode", "stridden"],
    "strike_delete": ["struck", "stricken"],
    "strike_hit": ["struck", "struck"],
    "swell": ["swelled", "swollen"],
    "seek": ["sought", "sought"],
    "hear": ["heard", "heard"],
    "whet": ["whetted", "whetted"],
    "deal": ["dealt", "dealt"],
    "lead": ["led", "led"],
    "lie as in 'to recline' ": ["lay", "lain"],
    "lie (not tell the thrut)": ["lied", "lied"],
    "dive": ["dove", "dived"],
    # Add more verbs as needed
}

def irregular_verb_game():
    for base_verb, correct_past_forms in irregular_verbs.items():
        # Ask the user for the past tense
        user_past_tense = input(f"What is the past tense of the verb '{base_verb}'? ")

        # Ask the user for the past participle
        user_past_participle = input(f"What is the past participle of the verb '{base_verb}'? ")

        # Check if the user wants to end the game
        if user_past_tense.lower() == 'q' or user_past_participle.lower() == 'q':
            print("Thanks for playing! Goodbye.")
            break

        # Check if the user's answers are correct
        if user_past_tense.lower() == correct_past_forms[0].lower() and user_past_participle.lower() == correct_past_forms[1].lower():
            print("Correct! Well done.")
        else:
            print(f"Oops! The correct answers are: {correct_past_forms[0]} (past) and {correct_past_forms[1]} (past participle).")

# Play the game
irregular_verb_game()
