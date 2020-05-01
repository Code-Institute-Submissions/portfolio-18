# Portfolio - Patrycja Tyra


# Introduction

Patrycja.io is created by Patrycja Tyra as her Full - Stack Developer professional portfolio to be able to get freelance projects on side but as well to be visible to future employers

***
##### Table of Contents  
- [UX](#ux)
  * [Goals](#goals)
- [Features](#features)
  * [Existing features:](#existing-features-)
    + [Main Page](#main-page)
    + [Login Page](#login-page)
    + [Signup Page](#signup-page)
    + [User Page](#user-page)
    + [Add Run Page](#add-run-page)
    + [Manage Runs Page](#manage-runs-page)
    + [Admin or User Page](#admin-or-user-page)
    + [Admin Page](#admin-page)
    + [Delete Run Page](#delete-run-page)
    + [Update Run Page](#update-run-page)
    + [Manage Users Page](#manage-users-page)
    + [Delete User Page](#delete-user-page)
    + [Update User Page](#update-user-page)
    + [Logout Page](#logout-page)
    + [Permission Denied Page](#permission-denied-page)





<!-- markdownlint-disable MD033 -->
<div align="center">
<img src="/wireframes/main.PNG" >
</div>

One or two paragraphs providing an overview of your project.

Essentially, this part is your sales pitch.

## UX

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

### Existing features:

#### Main Page
The main page allows all users of the site to view the qc data for all sequencing runs. The page is divided into two sections. The first section has four modal links that display qc data as line charts. The second section contains two modal links that display qc data as pie charts. From the main page the user is able to access the login or signup page.

#### Login Page
The login page allows a registered user to log into their user account using their unique username. If successful the user is directed to the main user page.
#### User/Admin Page
The user page (accessed by logging in with username) allows the user to view all of the qc data for their own sequencing runs. The page has the main layout features as the main page. From the user page the user is able to access the add-run page and the manage-runs page.

#### Add Run Page
The add-run page allows the user to add new qc run data to the database.

#### Manage Runs Page
The manage-runs page allows the user to view qc data for individual runs or groups of runs. Once an individual run has been selected, the user is able to access the delete-run or update-run pages.

#### Admin or User Page
The admin-or-user page allows users with admin privileges to choose to login as a standard user or as an admin user.

#### Delete Run Page
The delete-run page allows the user or admin-user to delete the currently selected run.

#### Update Run Page
The update-run page allows the user or admin-user to update the currently selected run.

#### Delete User Page
The delete-user page allows the admin-user to delete the currently selected user account.

#### Update User Page
The update-user page allows the admin-user to update the currently selected user account.

#### Logout Page
Accessed via the logout button and allows the user or admin-user to end their current session. Informs the user that they have successfully logged out and provides a link back to the main page.

#### Permission Denied Page
If the user tries to access a user account, other than the current user count, via the url address then they will be redirected to the permission-denied page. The permission-denied page informs the current user that they don't have permission to go to that page and provides a link back to the main page.

#### 404 Error Page
If the user attempts to use a url that does not exist then they will be redirected to the 404 page. The 404 page will inform the current user that the page they are trying to access doesn't exist and provides a link back to the main page.

### Existing Features

- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement

- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
- [The Padwan Project](https://github.com/Eventyret/Padawan)
https://favicon.io/favicon-generator/

## Testing

Please see [Testing](TESTING.md) for all my testing

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits

### Content

- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media

- The photos used in this site were obtained from ...

### Acknowledgements


- I received inspiration for this project from X
- [Simen Daehlin](https://github.com/Eventyret) - [The Padwan Project](https://github.com/Eventyret/Padawan)
https://fonts.google.com/specimen/Montserrat?selection.family=Montserrat
https://code.visualstudio.com/docs/python/environments
https://flask-pymongo.readthedocs.io/en/latest/
