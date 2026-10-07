name = input("What is your name?")
print("welcome", name) 
tasks = []
while True:

    task = input("please enter a task or exit")

    if task == "exit":
        break
    else:
        tasks.append(task)
        continue
