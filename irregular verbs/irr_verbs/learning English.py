from myassisstant import *

print(starting)
print(options)

with open("irr2.txt", "r") as myfile:
  all_verbs = myfile.read().splitlines()
  
score = 0
for n in range(10):
  verb = all_verbs[n].split(maxsplit=1)
  base_verb = verb[0]
  past_and_pp = verb[1]

  answer = ""
  while answer != past_and_pp:
    answer = input(f"What's the past and the past participle of {base_verb}?")

    if answer == past_and_pp:
      print("Correct")
      correct_answer(all_verbs[n])
      score += 1
      memorized(score)
      print("-"*50)

    elif answer == 'n':
      print(f"The answer is: {past_and_pp}")
      print("-"*50)
      break
    
    elif answer = 'q':
      print("Finish")
      exit()

    else:
      print("Wrong try again")
