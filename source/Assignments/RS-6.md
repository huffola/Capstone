# Test Plan Document
### Dungeons & Developers

#### 1.0 - Introduction

D&Dev is a web application that creates a helper-tool for D&D
players using Pathfinder 3.5 . This tool will allow users to
create accounts and manage characters. The database will house
character information, as well as allow users to bookmark
relevant game rules to their account. Alongside the web
application there is a discord bot that will be able to
reference data inside the database and perform simple functions like a dice roll.

#### 2.0 - Objectives & Tasks

##### 2.1 - Objectives
- User Creation
 - Hashed Password
 - Change Password
- User Deletion
 - DB Removal
- Profile
 - Profile Image
  - Change Image
- Discord Bot
 - Dice Roll
 - Delete Message
 - !lookup
- Database Integration
- Compendium
 - Add to account
 - Remove from account
- Character creation
 - Data types
 - Throwing errors
 - Character deletion

##### 2.2 - Tasks
- Testing
- Problem Report
- Post-Testing
- De-bugging
- Deployment Testing
- Problem Report
- De-bugging
- Deployment
- Testing strategy

#### 3.0 - Testing
- 3.1 - Unit Testing
	 - Manual unit testing

- 3.2- System Testing
	 - Test Scripts with PyTest

- 3.3 - Stress Testing
	 - Manual Stress Testing

- 3.4 User Acceptance Testing
	 - Manual UAT

#### 4.0 - Hardware Requirements
  4.1 - 2 GB memory

  4.2 - 16 GB Storage

#### 5.0 - Environment Requirements
  - 5.1 - OS:
    - Windows 7 +
    - Mac OS 10.10 +
  - 5.2 - Access to Modern internet browser
    - Edge
    - Firefox
    - Chrome
    - Safari
  - 5.3 - Discord

#### 6.0 - Test Schedule
- 6.1 - Initial Testing
  - Manual testing of button functionality
  - Manual testing of table entry
- 6.2 - Testing 2
  - Manual testing of URL exstension
  - Manual testing of valid user input
- 6.3 - Testing 3
  - Manual testing account creation
  - Manual testing correct Password
  - Manual testing incorrect Password
- 6.4 - Testing 4
  - Manual testing character creation
    - Character-specific data type conflict testing
  - Manual verification hashed passwords
- 6.5 - Testing 5
  - Automated user validation
  - Automated password validation

#### 7.0 - Features To Be Tested
- 7.1 - Live Links
- 7.2 - 404 error
- 7.3 - Account Creation
- 7.4 - Password Change
- 7.5 - Username Change
- 7.6 - Correct password
- 7.7 - Incorrect password
- 7.8 - Hashed password validation

#### 8.0 - Features Not To Be Tested
- 8.1 - All functioning features tested

#### 9.0 - Roles & Responsibilities
- 9.1 - Project Manager : Aaron Huff
  - Present devleopment cycle updates to faculty sponsor
  - Set sprint goals and deadlines
  - Format and complete RS assignments
    - with team assistance
  - Manual testing
  - Code review
- 9.2 - Web Developer : Isaac Brimner
  - Web application development
    - Python
      - Flask
  - Database management
    - SQLite
    - SQLAlchemy
  - Automated Testing
- 9.3 - Bot Developer : Justin King
  - Discord bot implementation
    - Bot functions
  - Debugging
  - Manual Testing

#### 10.0 - Schedules
- 10.1 Sprint 1
  - Storyboarding
  - Conceputalize design space
  - Locate tools
- 10.2 Sprint 2
  - Implement rough outline
  - Test tools for implementation
    - assign new tools as needed
  - Outline key functionalities
- 10.3 Sprint 3
  - Web app framework designed
    - flask front-end development
  - Discord bot started
- 10.4 Sprint 4
  - Test web app Links
  - Begin user/password DB setup
  - Test discord functions
- 10.5 Sprint 5
  - Complete user interface and hashed PW
  - Test user interface manually
- 10.6 Sprint 6
  - Database linking and Testing
  - Account linking, testing multiple characters to one user
- 10.7 Sprint 7
  - Final manual Testing
  - Automated user Testing
- 10.8 Sprint 8
  - Deployment and beta Testing
  - Final bug fixes
  - Presentation practice
- 10.9 Sprint 9
  - GM Deployment
  - Presentation

#### 11.0 - Dependencies
- alembic==0.9.9
- blinker==1.4
- chardet==3.0.4
- click==6.7
- Flask==1.0.2
- Flask-Dance==0.14.0
- Flask-DebugToolbar==0.10.1
- Flask-Login==0.4.1
- Flask-Migrate==2.1.1
- Flask-OAuth==0.12
- Flask-OAuthlib==0.9.4
- Flask-SQLAlchemy==2.3.2
- Flask-WTF==0.14.2
- httplib2==0.11.3
- idna==2.6
- itsdangerous==0.24
- Jinja2==2.10
- lazy==1.3
- Mako==1.0.7
- MarkupSafe==1.1.1
- oauth2==1.9.0.post1
- oauthlib==2.0.7
- python-dateutil==2.7.2
- python-editor==1.0.3
- requests==2.18.4
- requests-oauthlib==0.8.0
- six==1.11.0
- SQLAlchemy==1.2.6
- SQLAlchemy-Utils==0.33.2
- urllib3==1.22
- URLObject==2.4.3
- Werkzeug==0.14.1
- wincertstore==0.2
- WTForms==2.1
#### 12.0 - Risks/Assumptions
- 12.1: Risks
  - Larger user base could cause crashes
  - "Trolls" seeking bugs
  - Copyright concerns
- 12.2: Assumptions
  - Majority of material is opensource or found easily with no copyright concerns
  - Most users will use for intended purpose
  - limited rollout, only localhost for the time being as a test
#### 13.0 - Tools
- 13.1 - Atom (Text Editor)
- 13.2 - Terminal/Powershell (Program Execution)
- 13.3 - DBBrowserSQLite (SQL Database Management System)
- 13.4 - Vultr (Bot Hosting)
- 13.5 - VS Code (Compiling)
- 13.6 - Discord (Testing)
