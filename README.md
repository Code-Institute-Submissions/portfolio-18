# PATRYCJA.IO


# Introduction

**Patrycja.io is created by Patrycja Tyra as her Full - Stack Developer professional portfolio to be able to get freelance projects on side but as well to be visible to future employers**

<div align="center"><img src="static\img\testing0.png" >
</div>

***
# Table of Contents  

- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
- [UX](#ux)
    + [Goals](#goals)
      - [Visitor Goals](#visitor-goals)
      - [Business Goals](#business-goals)
  * [User Stories:](#user-stories-)
    + [Visitor Stories](#visitor-stories)
    + [Business Stories](#business-stories)
- [Design Choices](#design-choices)
    + [Fonts](#fonts)
    + [Colours](#colors)
    + [Wireframes](#wireframes)
- [Features:](#features-)
    + [Existing Features](#existing-features)
      - [NavBar](#nav-bar)
      - [Main Page](#main-page)
      - [Portfolio Page](#portfolio-page)
      - [Contact Page](#contact-page)
      - [Login Page](#login-page)
      - [User/Admin Page](#user-admin-page)
      - [View project](#view-project)
      - [Delete Project](#delete-project)
      - [Update Project](#update-project)
      - [Logout Page](#logout-page)
      - [Permission Denied Page](#permission-denied-page)
      - [404 Error Page](#404-error-page)
    + [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
    + [Tools](#tools)
    + [Libraries](#libraries)
    + [Languages](#languages)
- [Testing](#testing)
- [Deployment](#deployment)
  * [How to run this project locally](#how-to-run-this-project-locally)
    + [Instructions](#instructions)
  * [Heroku Deployment](#heroku-deployment)
- [Instructions how to log to admin panel](#instructions-how-to-log-to-admin-panel)
- [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
      - [Images](#images)
    + [Code](#code)
    + [Acknowledgements](#acknowledgements)
- [Disclaimer](#disclaimer)




<!-- markdownlint-disable MD033 -->




# UX

There are  two types of user to access website, unregistered visitor and registered admin:


## User Stories:

### Visitor Stories:

 1. As a visitor I want to see the latest projects of software developer Patrycja Tyra
 2. As a visitor I want to get known who she is and what is her story
 3. As a visitor I want to reach her GitHub to check the code
 4. As a visitor I want to see her work experience
 5. As a visitor I want to contact Patrycja Tyra if I would have any questions.
 6. As a visitor I am an owner of a business looking to hire someone for freelance
 7. As a visitor I want to send some business offer

### Admin user:

1. As an admin I want to log on to the website and be able to add new projects
2. As an admin I want to log on to the website and delete old not needed projects
3. As an admin I want to log on and edit previously created project.



# Design Choices

### Fonts 
- [Font Work Sans] (https://fonts.google.com/specimen/Work+Sans)- was for me the best choice of non serif font. As well it is very simple and not well know font. Because it seemed to be unique for me I decided to use those one.
- Font Awesome 5.0 - used to mark CRUD options( view, edit and delete), social icons, as well as programming languages icons. 

### Colours

<div align="center"><img src="static\img\colors.png" >
</div>

 - **White, Black and Grey** -Purpose of choosing mainly white and black colour scheme came with a reason to not interfere with projects photos.
 Most of the photos of project are colourful what would broke all concept of good user experience. I prefer to make my websites in monochromatic colours if not any specific theme/ reason dedicated to highlight purpose of the site.
Otherwise making website colourful would decrease value and UX and user would leave quickly as being confused and eyes tired.
 I used black to highlight important elements. Most of black elements change from gray to black when hover over.
 
 - **Other colours** - Programming languages - font awesome are made colorfull to show straigh away what languages are used by this full-stack developer.

### Wireframes
These wireframes were created using Balsamiq during the Scope Plane part of the design and planning process for this project.

<div align="center"><img src="wireframes\mainPage.png" ></div>
<div align="center"><img src="wireframes\portfolio.png" ></div>
<div align="center"><img src="wireframes\admin.png" ></div>
<div align="center"><img src="wireframes\contact.png" ></div>


# Features:

### Existing Features

#### NavBar 
Contains logotype and menu section. Logotype redirect to main/home page. In the menu section you can find buttons - home, portfolio, contact. Navbar stay the same always for not logged in user. Home button -redirect to home page. Portfolio leads to project views and contact redirect to contact form. 

-After **when user is logged in** in Navbar will appear **Log out** section, to log out from existing session, 


#### Main Page

The main page allows all users of the site to view just a couple words where user arrived and what this website is for The page is divided into 3 sections. The first section has explanation what this website is for. The second section contains photo of the owner. 3rd section explain who owner of the website is.

#### Footer
 In footer you can fin contact details (email) and as well my social icons.

#### Portfolio Page
 Portfolio Page is a main page when you can see collection of cards presenting projects added to data base.

#### Contact Page
 Classic contact form to fill out for future business offers.


#### Login Page

The login page allows a registered user to log into their user account using their unique username. If successful the user is directed to the main user page. NOTE! that there Register Page Do

#### User/Admin Page

To get to the Admin page, user needs to type in after website address **/admin**. Feature this is not redirected by any button on site by security purpose. As no one part of admin of this website should have access to this feature. And users visiting website shouldn't try to get to website backend. After typing "/admin" page will redirect to log in view. To log with credential only known to admin. **Note for Project Assessor** For credentials used to log in to admin page go to **instructions**.

In the Admin page by purpose I haven't use option to manage admin/user as admin/owner of the website should be just only one.

#### View project

The manage-runs page allows the user to view qc data for individual runs or groups of runs. Once an individual run has been selected, the user is able to access the delete-run or update-run pages.

#### Delete Project

The delete button allows the admin or to delete chosen project 

#### Edit/Update Project

The update button allows the admin to redirect to update form and edit/updated the currently selected project.


#### Logout Page
Accessed via the logout button and allows the user or admin-user to end their current session. Informs the user that they have successfully logged out and provides a link back to the main page.

#### Permission Denied Page
If the user tries to access a user account, other than the current user count, via the URL address then they will be redirected to the permission-denied page. The permission-denied page informs the current user that they don't have permission to go to that page and provides a link back to the main page.

#### 404 Error Page
If the user attempts to use a URL that does not exist then they will be redirected to the 404 page. The 404 page will inform the current user that the page they are trying to access doesn't exist and provides a link back to the main page.




### Features Left to Implement

- Skills tab - to show what frameworks/libraries are used with this projects.
- CV - downloader or , cv tab to make it useful for future recruiter browsing this portfolio.
- More animations and more fun stuff utilising front-end skills.
- Delete alert, preventing accidental deleting project


# Technologies Used
------
### Tools
- [Visual Studio Code](https://code.visualstudio.com/) is the IDE used for developing this project.
- PIP for installation of tools needed in this project.
- [Git to handle version control.](https://git-scm.com/)
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) is the database for this project.
- [GitHub](https://github.com/) to store and share all project code remotely.
- [Picresize](https://picresize.com/) to edit, crop and save images as well as ulitizing the colour picker to ensure colour consistency over the entire project.
- [GitHub Wiki TOC generator](https://ecotrust-canada.github.io/markdown-toc/)
- [Online Markdown Editor](https://dillinger.io/)
- [Favicon generator](https://favicon.io/favicon-generator/)
- [Sizzy](https://sizzy.co/) to check responsiveness on other devices
- [Am I Responsive](http://ami.responsivedesign.is/) to create the images in this readme file of each page displayed on different screen sizes.
- [Coolors](https://coolors.co/) colour schemes generator
- [Material Design Clours](https://www.materialui.co/colors)
- [The Padwan Project](https://github.com/Eventyret/Padawan)

### Libraries/Frameworks
- [Bootstrap](https://getbootstrap.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://fontawesome.com/) to provide icons for Family Hub.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.
- [PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) to make communication between Python and MongoDB possible.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) to construct and render pages.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) to simplify displaying data from the backend of this project smoothly and effectively in html.

### Languages

This project uses HTML, CSS, JavaScript and Python programming languages.


# Testing

Please see [Testing](TESTING.md) for all my testing

# Deployment

In order to deploy this project you must first set up an account at MongoDB Atlas. Click [here](https://www.youtube.com/watch?v=rPqRyYJmx2g) for instructions on how to set up able Mongo Atlas account.

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools:

-An IDE such as Visual Studio Code - Used in this projects

The following must be installed on your machine:

- PIP
- Python 3
- Git
- An account at MongoDB Atlas or MongoDB running locally on your machine.
     How to set up your Mongo Atlas account here.


### Instructions

***Instructions underneath are for Windows users please refer it to your OS**

1. Save a copy of the GitHub repository located at https://github.com/patrycja-io/portfolio by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.

`git clone https://github.com/patrycja-io/portfolio`

2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:

`python -m .venv venv`

NOTE: Your Python command may differ, such as python3 or py

Activate the .venv with the command:

`.venv\Scripts\activate`

Again this command may differ depending on your operating system, please check the Python Documentation on virtual environments for further instructions.

4. If needed, Upgrade pip locally with

`pip install --upgrade pip`

5. Install all required modules with the command

`pip -r requirements.txt`

6. In your local IDE create a file called `.venv`

7. Inside the `.venv` file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database `portfolio`, with 2 collections called `users` and `projects`. You will find example json structures for these collections in the schemas folder.

8. You can now run the application with the command

`python app.py`

You can visit the website at `http://127.0.0.1:5000`

## Heroku Deployment

  1. Create a `requirements.txt` file from the terminal using the command `pip3 freeze --local > requirements.txt`

  2. Create a `Procfile` from the terminal using the command `echo web: python app.py > Procfile.`

  3. `git add` and `git commit` the new requirements and ProcFile and then `git push` the project to GitHub.

  4. Create a new app on the [Heroku website](heroku.com) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

  5. From the Heroku dashboard of your new app, click on "Deploy" > "Deployment method" and select GitHub.

  6. In the App connected to GitHub section confirm the Heroku app is linked to the correct GitHub repository.

  7. In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

  8. Set the following config vars:
  
|Key     | Value | 
| -------|-------|
| DEV  | 1 | 
| HOSTNAME    | 0.0.0.0|  
| MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`      | 
| PORT   |5000   |  
| SECRET_KEY |	`<your_secret_key> `   |
 - To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/).
 
 9. In the Heroku dashboard, click "Deploy".

 10. In the Automatic Deploys section click Enable Automatic Deploys to ensure your Heroku app is automatically updated every time your GitHub repository is updated.

 11. Click on the "Open App" button at the top of the page. The Heroku website is now successfully deployed.

# Instructions how to log to admin panel 

**Note for Project Assessor**

To log in to admin panel type after page address **/admin**

| LOGIN | PASSWORD |
| ------ | ------ |
| admin@gmail.com | admin |





# Credits

 [Pretty Printed](https://www.youtube.com/watch?v=3ZS7LEH_XBg&t=78s)

### Content

- The text for content was created by myself

### Media

 [The Padwan Project](https://github.com/Eventyret/Padawan)

#### Images

- [404 page - Yoda image](https://c7.uihere.com/files/502/424/998/5bbbf8b5ba40f.jpg)
- Main page photo - picture of myself made by phone.
- Pictures of real life projects are made by snipping tool build in Windows OS.


### Acknowledgements


- The project is inspired by my experience made so far in software developmet.
- Manny thanks to my Code Institute Tutors team, especially Anna Greaves with her endless willing to help and patience with my lack of knowlegde.

- Special thanks to my Code Institute Mentor [Simen Daehlin](https://github.com/Eventyret) for his coding expertise, endless patience and generosity with his time. 

# Disclaimer
The content of this website is educational purposes only.