## Moose Leather Online Store

Moose Leather was a store I owned back in the 90's in San Diego, California that specialized in custom-made leather goods.
We also carried off-the-rack merchandise as well as consignment of people's leather items in which we received a commission 
when the item sold.

For my final project I decided to create an online version of that store, including the ability for users to post their own 
items for sale on consignment. 

**NEED MORE DECRIPTION HERE**



###UX
User Stories
* Users want to be able to purchase specialty leather goods online
* Users want to be able to sell their own used specialty leather goods
* Users want to be able to search for items
* Users want to be able to see photos of any potential item for purchase

Future User Stories
* Users want to be able to search for items by category, price, etc.
* Users want to learn about the how each type of leather item is used or worn
* Admins need to approve consignment items
* Admins to be able to generate reports

Basic mock-ups of the site can be downloaded from my GitHub site at https://github.com/swendt57/moose_leather_project/tree/master/support/mock-ups

### Features

* A Home page that gives background on Moose Leather and the concept behind the website.
* A built-in Django Admin function for entering items for sale, and editing uploaded consigned items, and manipulating users.
* The project is broken into the following sections:
  * An Accounts app that handles user registration, logging in and out, and a reset-password function. It also handles storing User Shipping Info.
  * A General app that serves up the Home page and the Disqus-based Comments / Discussion page.
  * A Products app that is responsible for showing the items for sale, both retail and consigned. The main models are Item and Category
  * An Order app which provides Order and Line Item models which are used for storing sales info
  * A Cart app, which maintains the user's selected items for purchase that can be displayed from any page of the application.
  * A Checkout app that handles processing payments using Stripe.com, and upon success, inserts the sales info into the appropriate tables. 
  * A Disqus based Comments and Discussion page where users can add and comment on each other's posts.
* Other features include:
  * A JavaScript based photo handler that adjusts the image's dimensions as the Bootstrap panels expand and contract depending on screen size for maximum visual impact.
  * A JavaScript based card sizer that adjusts the size and position of the cart's total / price panel to be aesthetically pleasing to the eye.
  * A collapsible search input field that does not detract from the look and feel of the web app.
  * The ability for a user to store the shipping information that allows us to pre-populate their order checkout form.
  * WORKING!! Add a details page for each item that provides the user with background information on how the item is used and the history behind it.
  
#### ER Diagram
![](support/Moose_leather_ER.png)
The full size diagram is available in GitHub a`t https://github.com/swendt57/moose_leather_project/blob/master/support/Moose_Leather_ER.pdf

#### Future Features

* Add a consignment approval process that will allow an admin to approve or disapprove a consignment posting.
* Add an Inventory app that maintains current stock levels and that the Products app can use to verify availability.
* Add in support for sales tax.
* Extend the Search app to allow searching by category, size, etc.
* Write an Image Adjuster app that will automatically trim down larger photos on their way into the system.
* Allow for multiple images for an item, instead of just one. 
* Provide single-sign-on for both the website and Disqus. Currently posting to Disqus requires a separate log in.

### Technologies Used 

* Python
  * https://www.python.org/
  * The main language used for the project
* Django
  * https://www.djangoproject.com/
  * The Python framework used for the project
* JavaScript
  * https://www.javascript.com/
  * The main scripting language that I used for navigation, photo adjustment, etc
* jQuery
  * https://jquery.com/
  * JavaScript library that simplifies DOM manipulation
* PyCharm
  * https://www.jetbrains.com/pycharm/
  * Python integrated development environment
  * My preferred Python IDE
* Bootstrap 4
  * https://getbootstrap.com/docs/4.0/getting-started/introduction/
  * Responsive, mobile-first, framework
* Google Fonts
  * https://fonts.google.com/
  * Free, open-source, on-demand, fonts
* Font Awesome
  * https://fontawesome.com
  * Icons and such
* GitHub
  * https://github.com/swendt57
  * Code repository
* Heroku
  * https://www.heroku.com/home
  * Cloud host of the website
* SQLite Database
  * https://www.sqlite.org/
  * Embedded database used by Django for development
* PostgresSQL Database
  * https://www.postgresql.org/
  * Production database hosted on Heroku
* Amazon Web Services S3 Bucket
  * https://aws.amazon.com/
  * For storing static and media files
* Stripe
  * https://stripe.com
  * Payment processor for the site (credit cards)
* Stack Overflow
  * https://stackoverflow.com/
  * Community of developers that has potential solutions to almost any problem
* X
  * X
* X
  * X
* WHAT AM I FORGETTING??
  * X
* X
  * X
* X

### Testing

TBD

### Travis Continuous Integration
[![Build Status](https://travis-ci.org/swendt57/moose_leather_project.svg?branch=master)](https://travis-ci.org/swendt57/moose_leather_project)

### Deployment

TBD

### Acknowledgements
* Wood texture background courtesy of https://www.deviantart.com/ftourini
* Text shadowing - https://html-css-js.com/css/generator/text-shadow/
* Fixtures and testing - https://django-testing-docs.readthedocs.io/en/latest/fixtures.html
* Calling super() on setUpClass in tests - https://stackoverflow.com/questions/29653129/
* Resetting migrations - https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html
* Buttons that act like a link - https://www.w3docs.com/snippets/html/how-to-create-an-html-button-that-acts-like-a-link.html
* Expandable search box - Elwin Tamminga - https://codepen.io/elwint/pen/vGMRaB
* Encrypting secret key for use with Travis - https://pypi.org/project/travis-encrypt/
