# Programmer Manual
### Dungeons & Developers

##### 1. Vision Statement: To simplify the process of playing Dungeons and Dragons 3.5 edition.

##### 2. Introduction
D&Dev is a web application that creates a helper-tool for D&D
players using Pathfinder 3.5 . This tool will allow users to
create accounts and manage characters. The database will house
character information, as well as allow users to bookmark
relevant game rules to their account. Alongside the web
application there is a discord bot that will be able to
reference data inside the database and perform simple functions like a dice roll.
##### 3. Component Overview
  - Web App
    - Database models
      - Characters
      - Users
    - User interface
  - Bot


##### 4. Tool Overview
  - Bot
    - Dice Roller: On a valid channel within a Discord server that includes the bot, the command "!roll" +"number of dice to be used"d
    "sides of the dice to be used" + "any positive or negative modifiers"
    - Example: !roll 2d20 = 2 dice rolled, with 20 sides
      - Returned value: Dice 1: 14 , Dice 2: 8 , Total: 22

##### 5. Project Repository
  - 1. Software: [https://github.com/huffola/Capstone.git](https://github.com/huffola/Capstone.git)
  - 2. Test Cases: [https://github.com/huffola/Capstone/blob/main/source/Assignments/RS-7.md](https://github.com/huffola/Capstone/blob/main/source/Assignments/RS-7.md)


###### 6. Installation for new install
  - 1. Clone the repository: [https://github.com/huffola/Capstone.git](https://github.com/huffola/Capstone.git) into desired installation location
  - 2. Navigate to src within the repo via terminal/command line
  - 3. Within the command line, run `pip install -r requirements.txt;`
  - 4. Within the command line, run `python app.py;`
  - 5. The terminal will provide a local URL, copy and paste this into your preferred internet browser
     - (Optional) Use a virtual environment within python to manage libraries/dependencies

##### 7. Further development statement
 If we had one more year to work on this project, we would provide more options and better formatting of data for the user to be able to create more of what they might want to make. We would also spend more time refining and improving upon the overall user experience through the website and the discord bot. We would also have converted our use of sqlite to a stronger database system such as mongoDB as conflicts were created when the database is queried by both the web application and the Discord bot at the same time.
