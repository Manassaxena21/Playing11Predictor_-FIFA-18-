import random
dict={"1": "Who is highest scorer in international football",
      "2": "Which footballer has won most number of balon d'or",
      "3": "Which team has won most world cups",
      "4": "Which team has won most number of champions league titles"}
Ques=list(dict.values())
print(random.choice(Ques))
answer=input()

for k,v in dict.items():
    if k=="1" and answer=="Ali Daei":
        print("Correct")
        break
    else:
        print("Incorrect")
        break
    if k=="2" and answer=="Lionel Messi":
        print("Correct")
        break
    else:
        print("Incorrect")
        break
    if k=="3" and answer=="Brazil":
        print("Correct")
        break
    else:
        print("Incorrect")
        break
    if k=="4" and answer=="Real Madrid":
        print("Correct")
        break
    else:
        print("Incorrect")
        break
