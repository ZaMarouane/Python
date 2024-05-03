import random
import time

irregular_verbs = [
    {"base": "fly", "past_simple": "flew", "past_participle": "flown"},
    {"base": "forbid", "past_simple": "forbad", "past_participle": "forbidden"},
    {"base": "freeze", "past_simple": "froze", "past_participle": "frozen"},
    {"base": "saw", "past_simple": "sawed", "past_participle": "sawn"},
    {"base": "shear", "past_simple": "sheared", "past_participle": "shorn"},
    {"base": "slay", "past_simple": "slew", "past_participle": "slain"},
    {"base": "stink", "past_simple": "stank", "past_participle": "stunk"},
    {"base": "stride", "past_simple": "strode", "past_participle": "stridden"},
    {"base": "swell", "past_simple": "swelled", "past_participle": "swollen"},
    {"base": "sneak", "past_simple": "snuck", "past_participle": "snuck"},
    {"base": "dive", "past_simple": "dove", "past_participle": "dived"},
    {"base": "tread", "past_simple": "trod", "past_participle": "trodden"},
    {"base": "relay", "past_simple": "relaid", "past_participle": "relaid"},
    

    # Add more verbs as needed
]

def irregular_verb_quiz():
    random.shuffle(irregular_verbs)
    score = 0
    start_time = time.time()

    for verb in irregular_verbs:
        print(f"\nBase form: {verb['base']}")
        user_past_simple = input("Past Simple: ").strip().lower()
        user_past_participle = input("Past Participle: ").strip().lower()

        if user_past_simple == verb["past_simple"].lower() and user_past_participle == verb["past_participle"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct forms are: {verb['past_simple']} (Past Simple) and {verb['past_participle']} (Past Participle)")

    end_time = time.time()
    elapsed_time = (end_time - start_time) / 60

    print(f"\nGame Over! Your final score is {score}/{len(irregular_verbs)}.")
    print(f"Time taken: {elapsed_time:.2f} minutes")

if __name__ == "__main__":
    print("Welcome to the Enhanced Irregular Verb Quiz!")
    irregular_verb_quiz()
