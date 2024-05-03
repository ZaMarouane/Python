import random
import time

irregular_verbs = [
    {"base": "go", "past_simple": "went", "past_participle": "gone"},
    {"base": "eat", "past_simple": "ate", "past_participle": "eaten"},
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
    elapsed_time = end_time - start_time

    print(f"\nGame Over! Your final score is {score}/{len(irregular_verbs)}.")
    print(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    print("Welcome to the Enhanced Irregular Verb Quiz!")
    irregular_verb_quiz()
