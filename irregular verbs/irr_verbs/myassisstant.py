starting = "==========================\nWelcome to irregular verbs game\n=========================="
options = ">>>>Write 'n' for unknowing the answer, and 'q' to quit the game<<<<\n"

def memorized(number):
  if number == 1:
    print(f"Correct, you have memorized {number} verb")
  else:
    print(f"Correct, you have memorized {number} verbs")

def correct_answer(current_line):
  with open("SavedWords.txt", "a") as mysavedwords:
    mysavedwords.write(current_line + "\n")

  total = ""
  with open("irr2.txt", "r") as file:
    all_irr_verbs =  file.read().splitlines()

  for line in all_irr_verbs:
      if line != current_line:
        total += line + "\n"
  with open("irr2.txt", "w") as mywordsfile:
    mywordsfile.write(total)

