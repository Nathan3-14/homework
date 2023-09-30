import random

def ask():
    if len(questions) == 0:
        print("No more questions to ask!\n  Type 'quit' to exit")
        return None
    index = list(questions.keys())[random.randint(0, len(questions)-1)]
    print(questions[index])
    questions.pop(index)
    return index

print("CHATBOT\n  Type 'quit' to exit\n")

questions = { 
    0: "How are you doing today?",
    1: "What's your favorite food?",
    2: "Yes?"
}
foods = [
    "pizza",
    "pasta",
    "fish and chips"
]

while True:
    question = ask()
    user_in = input(">> ")
    if user_in == "quit":
        break

    if question == 0:
        print(f"I'm feeling {user_in.lower()} too")
    elif question == 1:
        bot_food = foods[random.randint(0, len(foods)-1)]
        if user_in.lower() == bot_food.lower():
            print(f"I like {user_in.lower()} too!")
        else:
            print(f"{user_in.capitalize()} is a pretty good food, but I like {bot_food}")
    elif question == 2:
        print(f"Yes")

    print("")