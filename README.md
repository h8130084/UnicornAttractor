# Mile Stone project 4 - Full Stack-  Unicorn Attractor

[![Build Status](https://travis-ci.org/h8130084/UnicornAttractor.svg?branch=master)](https://travis-ci.org/h8130084/UnicornAttractor)


The website was designed to allow users to add bugs they have found and features they would like.
The site also allows users to write comments about the bugs and features and upvote a bug to say they have had the same bug.
In a similar way users that have registered are able to add features they would like to be added to the app which they are then able to pledge to.
In turn allows users to see how much money has been pledged to this feature and in essence shows how in demand this feature is, similarly to the way the upvotes work for the bugs.
The website shows a list of bugs/features with a description and also the current progress.
The site also allows users to edit the bug/feature details to help allow users to edit any inaccurate information about the bug/feature.

The overall aim is to have an easy to navigate website that was designed desktop first to enable users to add bugs and features so the site owner is able to prioritize work on the application.

# UX

The UX has been designed for desktop first to make it easy for all users to navigate and access the content they want.

I have provided a number of user stories below: 

* As a user who has found a bug  I want to be able to add it to the site

* As a user who has found a feature  I want to be able to add it to the site

* As a user who wants to know more about a bug or feature I want to be able to see a title and description before loading the page

* As a user who has the same bug as someone else I want to be able to upvote the bug to inform the site owner that it is an issue

* As a user who wants the same feature as someone else I want to be able to pledge an amount to inform the site owner that it is something I would like in the app

* As a user who is not sure of other features I would like, I want to be able to look through a list of bugs and features for inspiration

* As a user who likes to share my opinion I want to be able to add my own comment of the bug/feature

* As a user who likes to share my opinion I want to be able to see the name and timestamp of the comments in the comment section

* As a desktop user I want to be able to navigate the website easily so I and find the information I want with ease

* As a mobile user I want to be able to navigate the website easily so I and find the information I want with ease

* As a user who created the bug/ feature I want to be able to edit the bug or feature

* As a new user I want to be able to register for the site

* As a user I want to be able to log in

* As a user I want to be able to log out

* As a user who wants to pledge money to a new feature I want to be able to add/edit a pledge and checkout

* As a user who has pledged or upvoted, I want to be able to see the current work status of the bug or feature chosen

* I have also included some mock-ups/wireframes for the initial planning phase of the website

# Features

The navigation bar allows users to navigate back to the Home page quickly without needing to use the back button. 
The navigation bar is responsive and collapses to enable a better experience across multiple devices
The navigation bar also has the logo in the top corner to allow users to always navigate home
This feature is clear and users should be able to navigate around the site with ease. 

The site has forms to allow users to Create and Edit bugs or features

When a user clicks edit on a bug or feature they current information is pre populated into the fields

The site has a comments feature that allows users to write a comment about the bug or feature and then displays it on the relevant bug deatails page.
There is also a button for upvotes so users can quickly glance at how many people have had the same bug.
The is a similar button on for features, the logged in user is able to pledge money towards a feature they would like and in turn helping the site owner determine which features are most popular

The footer provides a brief description around the purpose of the website and gives links for social media pages.

The profile page has limited information currently and I had debated taking it out. it serves no real purpose however
as a user, I feel a profile page is something you would want to be able to have access to and not putting it in would cause frustration for a user.
I therefore kept the profile page in and used it as an example of a bug for the site. Given more time it would be useful to display more information, 
perhaps saving payment methods or displaying the bugs or features that particular user had created. 


# Technologies used

* used HTML5 and CSS3 Python and JQuery/ Javascript

* used SQLite, PostgresSQL, Django, Jinja Templating and Stripe payments API

* used Git and Herkou

* Bootstrap
used Bootstrap for aspects of the grid and some of the styling including navbar

* Google fonts - https://fonts.google.com 
used google fonts to apply fonts to the text within the website

# Testing

I completed much of my testing as I built the website up.

I firstly made some wireframes/mock ups to come up with the how I wanted the website to look structurally and to help think about 
the data I would need from users.

I initially started with the base.html page that had the bare bones of a layout to include a header a footer and a main content section 
that had some colour just to differentiate and ensure my styling was correct.

I then made the accounts app which allowed me to have some general structure to the website and register users.

Following this, I made the tickets app. This was the main purpose of the site, it allowed me to have a page that displayed all current known/ requested bugs/features
and then display more details  around each one. I tested the general workings of the account and made notes of anything I thought could be better or 
I felt needed tweaking. 

As I have worked throug the project my ideas of how I wanted the users to be able to interact have changed as I intially had
had not thought to different the features availabl to a registered user and a non registered user. This required me to implement some extra code on my views
and also if statements to hide buttons and links across the site.

I added the cart and checkout apps, I had some trouble implementing the checkout app however after further reading I was able to get this working correctly.

My previous project helped my top level thought process in some ways as I already had faced issues with implementing comments into my previous project, 
and whilst I didn't encounter the same issues, it did help me quickly progress through the implementation of the comments section.

The CSS across the whole site has been changed mostly towards the end of the development process. The CSS was useful for trial and
error of assessing how the website looked across multiple devices. After feedback on my previous project, I have decided to limit the colour scheme on the website rather than a host of colours. 
I did change the edit button to a warning button to give users a clear indicator this is what the button was for.

I did start some automated testing and tested the urls on site. However I encountered an error with Travis, and for some reason it appears git has
updated my version of Django which in turn I think has thrown Travis out of sync, so my build that was passing is now failing. 
I have not continued with any further testing as I have time constraint and I have been unable to fix the issue with Travis. 

One issue I have had since an early point is the restting a password feature which I am unable to fix. I have made the relevant changes to account settings
and even created a new email address to help test and trial, however I have had no success. This is a known bug I have been unable to fix. 
The other issue I have had is in the cart app. If I want to amend the amount and I delete out the pre populated amount and click amend it causes an error,
whilst this doesn't break the website it is not a good experience for the user. 


# Deployment

The deployment was completed through Github with regular commits and heroku.

I used heroku to create an app. I had to change my app.py file in order to deploy to heroku. I changed the debug mode to False.
I had to update the requirements file in order to help deploy to heroku as I had to install whitenoise and gunicorn. 
Created a Procfile to tell heroku I am running a python webapp. I had to link my herkou with my github. Once linked up I had to 
ensure my PORT and IP and Config Vars all had the relevant information in. Finally, I restarted the dynos. 



# Credits and media

* I used w3school website and stack overflow for assistance with moving footer to the bottom of the page
* I used front awesome bootstrap website for code on the social media links
* I used Bootstrap for the aspects of the grid and the styling of the page including the nav bar
* I used google fonts to style the font on the page


# Acknowledgement

The inspiration for this project came from the authentication and ecommerce mini projects.











