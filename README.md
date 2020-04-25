# An.Ghera

# What does it do and what does it fulfill?

This project uses skills to build a Flask website that uses a Mango backend. It is for people to view films and create, update and delete
their own films. Users can also search for films that contain for the searched word in its tags, title or ingredients. The project can be 
viewed at: 

#Functionality of project

The website is fully responsive and uses Mongo DB to hold users collection and a films collection. The user is able to register and login 
to view films. Logged in users are able to create, update (edit) and delete their own films. Any user (logged in) can search for films 
using the search box. A user can also log out. The films page shows all films in order of the amount of views each film has. The films are
paginated (by the database). The jQuery method has not been adopted as it would not be fast enough and would affect the user experience. 
Each film on the films page can be clicked onto and that will load the single films page which shows the entire entry. If the user created/
added the film on this page, he/she will not be able to edit and delete the film from the page. The add film allows the logged in user to 
create a film and enter it in a database.

#Technologies used
Python, HTML 5, CSS/Bootstrap 4, JS/JQuery, MongoDB, Flask

#Deployment
The website was coded in Gitpod, a local GIt directory was used for version control and then uploaded to Github. A MongoDB database was used
and setv up inside Heroku. The details of the database connection are found inside of the requirements.txt which uses the os class environ 
method to point Heroku to its own config available(MONGODB_URI) in order to keep the production database connection string secret. A 
Procfile is also used to help Heroku know what commands are run by the application's dynos and how to run various pieces of the app 
including the starting point app.py. Heroku's deployment from  Github repository function was used to deploy. 

#Testing
My tests check the page loading, as well as the business logic of the views. They are in the tests.py. The index page and films page is 
tested that they load correctly. The registration page and logic are tested. I test for mismatched passwords, duplicate user names, as well \
as succesful registration. The login page is tested throughout my tests as a number of my test operations require a logged in user. The 
Create film page is tested by checking that a film is entered, the page redirects and the new film is present on the index page. The film
to films page is tested by searching for any films on the films page, getting its ID number and going to that films details page and 
checking that the contents are there. The update films page is tested by going to a loggedx in user edit films page and changing some data 
and committing it. This then redirects the user to the index page and that is tested that the information has changed on that film. The 
Delete Film page is tested by going to its Film details page and deleting it, then checking the redirect has happened and that the film does
not appear on the index page. It is impossible to test at 100% coverage. All of my testing is done in  tests. py. I concentrated on logic 
and functionality with the project and I kept my design usable and simple to navigate with readable font. As the site is built with 
responsive design it works for mobiles and I have checked it on iphones 6 to x, samsung galaxy, ipads (mini to pro). Google pixel 2 and
3. I also tested it on various browsers.

