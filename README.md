# AFK - Gamer - MS4

This is the final Milestone Project, The Full Stack Framework with Django Module.
A live version of the project can be viewed here: [link](http://afk-gamer.herkouapp.com).

# Project Purpose

The aim of this project was to create a fully functional E-commerce website, where customer can view product, 
check the details and choose to purchase them and go through a simplified and painless process to ship the products.
The idea of simplicity was imbuled in every function of the project: the layout has a completely simple and sleek design,
the login and register page has large icons and field so that anyone can access them and see them. This project was created with
the intention to work for a Twitch / Youtube Gamer, that wanted to sell merchandise, but also plug and promote his channels. This
is why the Homepage is designed to link to their pages to promote subscription and get customers in the gaming spirit.

## UX
The user has been put at the forefront where design has been thought out. A big, clear nav is displayed at the from for easy access
and navigation of the website. At the top right two icons can be seen, for Profile management and viewing the bag. There is also a search
bar on the left for quick access and not having to scroll through the website looking for one. Furthermore when
a user clicks on the bag they can find out whats in it through a handy sidebar, which is not only and aesthetically pleasing sidebar,
but also guides them to the checkout. It also displays an alert if the peroson is below the free delivery can so they can make an
informed decision to spend more, without having to go all the way to checkout to find out.

## User Stories:

1. As a user I would like to have a great experience of the website regardless of the device being used.

2. As a user I would like a quick search function to find what I need.

3. As a user if I want more info on a product I would like very current and trendy merchandise that has an emblem.

4. As a user I would like my order history recorded and be able to log in and out of the website freely

5. As a user I would like to see trending, discounted and seasonal offers on the page.

## Admin Stories

1. As an Admin I would like easy access to get into the website, and be able to edit and delete product on the fly.

## Mockups
Balsamaq has been nused for the design implementation process. This has helped to correlate ideas into a rough idea of what the Intended
client would like. This can be viewed here: [link](https://github.com/Morad17/ms4/static/mockups/AfkGamer.bmpr)

## Design
In terms of the design larger and more catchy icons and fonts were used to promote the gaming and social ideas, which is what the indended 
cliend would be. The google fonts used were 'Catamaran' and 'Montserrat' as they have a simplistic and slightly thicker format. Also a 
special font was used for the logo and certain subheadings called verminvibes, to promote the gaming genre of the site. The official 
hex colors of Twitch (#6441a5) and Youtube (#c4302b) were used to remind users of the platform. Simplicity was the key in this project,
with simple lines used for styling and separating information, which has worked well.

## Features
Key features of this project are:

1. Clear Homescreen that can always be returned to, followed by navigation linked that stay at the forefront

2. Login into and out of the account, which saves your order history. You can also edit your default information. Furthermore 
Registered Admin can view and edit new products and also delete them.

3. One of the Models that were used was for the Hot items as they were key for the Project: Seasonal products are intended to be changeed every season and
are Limited Time Only offer to attract customers. Special Items are Special Offers that the Store has, which go up every time theres a
sale, to entice customers to buy, and Hightest rated products are displayed to Show customers the most poppular items. A rating system
was one thing that was thought off, but didnt have time to finish.

4. Models were created for Seasonal Products, so to promote Porducts in the seasonal promotion times, e.g. black friday and christmas in the Winter. There
are also certain discount depending on the seasons. If a product has a True on
discounted it appear in the 'Hot' Page.


# Libraries and Frameworks used

1. Bootstrap was predominantly used for its mobile first aspect and simple design
2. Django was used also to implement the E-commerce apps.
3. Stripe is used for the card payment 
4. Heroku is the platform that contains the site
5. AWS S3 Bucket used for Cloud Storage
6. PostGresQL database used that links with Heroku

# Testing

1. Regular Testing was implemented throughout the project to aleviate bugs and issues coming up. One way was through the Chrome
Dev Tool, for css and checking of console.

Several Issues have appeared throughout examples are:

    "Top navigation Bar overlapping the information in the page" 
The fix was to sort the padding out on all html pages through a class in the base.css

    "For the Hot Items nothing appears at the bottom"
This was fixed in the views.py of products by sorting out the filer in the arguements

    "Local errors appearing when trying to checkout"
Stripe was troubleshooted to determine the issue, which was one of the keys had expired

# DEPLOYMENT
Running Code Locally
Follow this [link](https://github.com/Morad17/ms4)to my Repository on Github and open it.

1. Click Clone or Download.

2. In the Clone with HTTPs section, click the copy icon.

3. In your local IDE open Git Bash.

4. Change the current working directory to where you want the cloned directory to be made.

5. Type git clone, and then paste the URL you copied earlier.

6. Press enter and your local clone will be ready.

7. Create and start a new environment:
python -m .venv venv
source env/bin/activate

8. Install the project dependencies:
pip install -r requirements.txt

9. Create a new file, called env.py and add your environment variables:

10. import os
os.environ.setdefault("STRIPE_PUBLISHABLE", "secret key here") os.environ.setdefault("STRIPE_SECRET", "secret key here") os.environ.setdefault("DATABASE_URL", "secret key here") os.environ.setdefault("SECRET_KEY", "secret key here") os.environ.setdefault("AWS_ACCESS_KEY_ID", "secret key here") os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "secret key here")

11. Go to settings.py file and add your environment variables.

12. Add env.py to .gitignore file

13. Go to terminal and run the following: python3 manage.py makemigrations, then python3 manage.py migrate to migrate all existing migrations to postgres database.

14. Create a superuser: python3 manage.py createsuperuser

15. Run it with the following command:
python manage.py runserver

16. Open localhost:8000 on your browser

17. Add /admin to the end of the url address and login with your superuser account and create new products.

# Credits

There are many websites that I drew Aesthetica and Practical Inspiration from, such as:
1. lttstore.com
2. https://tsmbreak.co.uk/
3. sidementclothing.com

The Font I used was from Google Fonts, and font verminvibes,is by Chequered Ink, The images from Twitch and Youtube
are copyright of theirs respectively. CodeInstituce was of course a bit Inclusion in my project, with the framework and 
implementation.

# Acknowledgements

I want To thank Brian Macharia my Mentor for the help and inspiration that has helped me finish this project.
