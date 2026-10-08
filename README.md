# Personal Task Manager
A simple personal task manager built with python
![Python](https://img.shields.io/badge/-python-C9A0A0?logo=python&logoColor=white)

## Table of Contents
- [Personal Task Manager](#personal-task-manager)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Project Structure](#project-structure)
  - [File Description](#file-description)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Environment Setup](#environment-setup)
  - [Usage](#usage)
  - [Explore Output](#explore-output)
  - [Screenshots](#screenshots)
    - [Start Program](#start-program)
    - [Tasks](#tasks)
    - [The end of the program](#the-end-of-the-program)
  - [Demo](#demo)
  - [Roadmap](#roadmap)
  - [Author](#author)

## Features
- Task Manager System 
  - Asks users name
  - Add multiple tasks
  - Displays all tasks
- Result storage
  - saves tasks in `tasks.txt` 

- Asks for the admin password 
    - Checks if the password is correct
    - Keeps the private information outside the main python file
    - loads the password from `.env`

## Project Structure
```
personal_task_manager/
│   .env.example
│   .gitignore
│   main.py
│   requirement.txt
│   tasks.py
│   tasks.txt
│
├───gif
│       Animation.gif
│
├───pictures
│       img1.png
│       img2.png
│       img3.png

```

## File Description

| File | Description | 
| --- | --- | 
| ` main.py ` | main file used to run quiz game |
| `  task.py ` | stores questions and answers |
| `requirements.txt` | lists the python packages needed for the project. |
| `.env.example ` | shows the environment variables needed by the project |
| `.gitignore ` | tells git which files and folders should not be tracked |
| `.README.md ` | contains the project documentation |
| `pictures/ ` | stores project screenshots |   
| `pictures/img1.png ` | screenshot of the  start program |
| `pictures/img2.png ` | screenshot of the task section |
| `pictures/img3.png ` | screenshot of the final result |
| `gif/ ` | stores demo GIF files |
| `gif/Animation.gif ` | shows the project demo |

## Requirements
before running the project, make sure you have:
- `python 3`
- `python-dotenv`

## Installation
1. Open a terminal in the project folder.
2. check that python is installed :
```bash
python--version
```
3. Install the python packages:
```bash
pip install -r requirements.txt

```

## Environment Setup
1. create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```
2. Open the new `.env` file
3. Replace the example value  with your own password
```text
TASK_MANAGER_ADMIN_PASSWORD =your_password_here
```
4. save the file.
> do not commit your `.env` file becuase it may contain private information


## Usage
1.  Open a terminal in the project folder
2. Run the task manager
```bash
python main.py
```
3. Choose `yes` or `no` for admin mode
4. If you choose `yes` enter a password from your `.env` file
5. Enter your name
6. Enter a task
7. See all your saved tasks
8. Enter another task or exit
8. Your result is saved in `tasks.txt`

## Explore Output
```text
do you want to open admin mode? yes/no: no

Whats your name?aramis

welcome aramis

enter a task or enter exit: do my homework

your task  ['do my homework'] added

enter a task or enter exit: exit

do my homework
```

## Screenshots
### Start Program
![start program](pictures\img1.png)

### Tasks
![tasks](pictures\img2.png)

### The end of the program
![end](pictures\img3.png)


## Demo
![demo](gif\Animation.gif)

## Roadmap
- [x] add multiple tasks
- [x] show all tasks
- [x] admin mode
- [x] save tasks to a file
- [ ] remove completed tasks
- [ ] add due dates
- [ ] categorize tasks
- [ ] search tasks
- [ ] filter tasks
- [ ] add reminders


## Author
create by [Aramis]