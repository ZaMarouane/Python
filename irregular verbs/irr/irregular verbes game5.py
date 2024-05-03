# Irregular verbs and their correct past forms
irregular_verbs = {
    "beat": ["beat", "beaten"],
    "begin": ["began", "begun"],
    "bend": ["bent", "bent"],
    "blow": ["blew", "blown"],
    "break": ["broke", "broken"],
    "bring": ["brought", "brought"],
    "buy": ["bought", "bought"],
    "bite": ["bit", "bitten"],
    "breed": ["bred", "bred"],
    "burn": ["burnt", "burnt"],
    "build": ["built", "built"],
    "catch": ["caught", "caught"],
    "cling": ["clung", "clung"],
    "creep": ["crept", "crept"],
    "clothe": ["clad", "clad"],
    "dwell": ["dwelt", "dwelt"],
    "deal": ["dealt", "dealt"],
    "dig": ["dug", "dug"],
    "dream": ["dreamt", "dreamt"],
    "choose": ["chose", "chosen"],
    "come": ["came", "come"],
    "dive": ["dove", "dived"],
    "do": ["did", "done"],
    "draw": ["drew", "drawn"],
    "drink": ["drank", "drunk"],
    "drive": ["drove", "driven"],
    "eat": ["ate", "eaten"],
    "wake": ["woke", "woken"],
    "wear": ["wore", "worn"],
    "weave": ["wove", "woven"],
    "write": ["wrote", "written"],
    "read": ["read", "read"],
    "rebid": ["rebid", "rebid"],
    "rebind": ["rebound", "rebound"],
    "relay": ["relaid", "relaid"],
    "ride": ["rode", "ridden"],
    "ring": ["rang", "rung"],
    "rise": ["rose", "risen"],
    "run": ["ran", "run"],
    "partake": ["partook", "partaken"],
    "prove": ["proved", "proven"],
    "fall": ["fell", "fallen"],
    "fly": ["flew", "flown"],
    "forbid": ["forbade", "forbidden"],
    "forsake": ["forsook", "forsaken"],
    "freeze": ["froze", "frozen"],
    "get": ["got", "gotten"],
    "give": ["gave", "given"],
    "go": ["went", "gone"],
    "grow": ["grew", "grown"],
    "hew": ["hewed", "hewn"],
    "hide": ["hid", "hidden"],
    "saw": ["sawed", "sawn"],
    "sew": ["sewed", "sewn"],
    "shake": ["shook", "shaken"],
    "shave": ["shaved", "shaven"],
    "shear": ["sheared", "shorn"],
    "shine": ["shone", "shone"],
    "shit": ["shit", "shit"],
    "show": ["showed", "shown"],
    "shrink": ["shrank", "shrunk"],
    "slay": ["slew", "slain"],
    "sow": ["sowed", "sown"],
    "speak": ["spoke", "spoken"],
    "spit": ["spat", "spat"],
    "spring": ["sprang", "sprung"],
    "steal": ["stole", "stolen"],
    "stink": ["stank", "stunk"],
    "strew": ["strewed", "strewn"],
    "stride": ["strode", "stridden"],
    "strike_delete": ["struck", "stricken"],
    "strike_hit": ["struck", "struck"],
    "strive": ["strove", "striven"],
    "swear": ["swore", "sworn"],
    "sweat": ["sweat", "sweat"],
    "swell": ["swelled", "swollen"],
    "swim": ["swam", "swum"],
    "see": ["saw", "seen"],
    "sing": ["sang", "sung"],
    "take": ["took", "taken"],
    "tear": ["tore", "torn"],
    "throw": ["threw", "thrown"],
    "tread": ["trod", "trodden"],
    "light": ["lit", "lit"],
    "teach": ["taught", "taught"],
    "tell": ["told", "told"],
    "sit": ["sat", "sat"],
    "think": ["thought", "thought"],
    "thrust": ["thrust", "thrust"],
    "say": ["said", "said"],
    "seek": ["sought", "sought"],
    "sell": ["sold", "sold"],
    "send": ["sent", "sent"],
    "shoot": ["shot", "shot"],
    "sit": ["sat", "sat"],
    "sink": ["sank", "sunk"],
    "sleep": ["slept", "slept"],
    "slide": ["slid", "slid"],
    "sling": ["slung", "slung"],
    "slink": ["slunk", "slunk"],
    "smell": ["smelt", "smelt"],
    "sneak": ["snuck", "snuck"],
    "speed": ["sped", "sped"],
    "spell": ["spelt", "spelt"],
    "spend": ["spent", "spent"],
    "spill": ["spilt", "spilt"],
    "spin": ["spun", "spun"],
    "feed": ["fed", "fed"],
    "feel": ["felt", "felt"],
    "fight": ["fought", "fought"],
    "find": ["found", "found"],
    "flee": ["fled", "fled"],
    "fling": ["flung", "flung"],
    "grind": ["ground", "ground"],
    "hang": ["hung", "hung"],
    "have": ["had", "had"],
    "hear": ["heard", "heard"],
    "hold": ["held", "held"],
    "keep": ["kept", "kept"],
    "kneel": ["knelt", "knelt"],
    "spoil": ["spoilt", "spoilt"],
    "stand": ["stood", "stood"],
    "stick": ["stuck", "stuck"],
    "sting": ["stung", "stung"],
    "string": ["strung", "strung"],
    "sweep": ["swept", "swept"],
    "swing": ["swung", "swung"],
    "pay": ["paid", "paid"],
    "weep": ["wept", "wept"],
    "whet": ["whetted", "whetted"],
    "win": ["won", "won"],
    "wind": ["wound", "wound"],
    "wring": ["wrung", "wrung"],
    "lay": ["laid", "laid"],
    "lead": ["led", "led"],
    "lean": ["leant", "leant"],
    "leap": ["leapt", "leapt"],
    "learn": ["learnt", "learnt"],
    "leave": ["left", "left"],
    "lend": ["lent", "lent"],
    "lie as in 'to recline' ": ["lay", "lain"],
    "lie (not tell the thrut)": ["lied", "lied"],
    "light": ["lit", "lit"],
    "lose": ["lost", "lost"],
    "know": ["knew", "known"],
    "make": ["made", "made"],
    "mean": ["meant", "meant"],
    "meet": ["met", "met"],
    "mow": ["mowed", "mown"],
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
