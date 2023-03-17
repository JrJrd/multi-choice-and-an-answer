import json

with open("q.json", "r") as file:
    content = file.read()
    data = json.loads(content)

score = 0
for question in data:
    print(question["question"])
    for i, alternatice in enumerate(question["alt"]):
        print(i +1, '-', alternatice)
    user_choice = int(input("enter num: "))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct"]:
        score = score +1

for question in data:
    message = f" Your answer: {question['user_choice']}," \
             f"correct answer:{question['correct']}"
    print(message)


print(score, '/', len(data))