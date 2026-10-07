import os
from dotenv import load_dotenv
from tasks import  show_task, add_task
name = input ("Whats your name?")
print("welcome", name)

load_dotenv()
admin_password = os.getenv("QUIZ_ADMIN_PASSWORD")
open_admin = input("do you want to open admin mode? yes/no: ")
if open_admin.lower() == "yes":
    entered_password = input("enter admin password: ")

    if entered_password == admin_password:
        print("admin, hi")
    else:
        print("wrong password")

tasks = []
while True:

    task = input("enter a task or enter exit: ")
    if task == "exit":
        break
    else:
        add_task(task)
        continue

with  open("tasks.txt", "a") as file:
    file.write(f"{name} - {tasks}\n")

show_task()