# Issue Tracker

## Description

Issue Tracker is a web application for handling user's issues and demands. It allows users to create tickets, comments on them and show its status. It can display two kinds of tickets: bugs and features. Features are upvoted by users willing to spend money on them, bugs are upvoted for free. To grab developers attention tickets are sorted by amount of upvotes. There are also three different statuses depending on stage of development: ‘to do,’ ‘doing,’ or ‘done’. There is also a subpage allowing users to check which one of them are most active and who is biggest contributor.

## UX

I wanted to build a user-friendly and user-oriented web application. My main inspiration was Reddit and its ascetic interface. This project was created with simplicity and responsiveness in mind. I tried to make functionalities obvious and easy to use. I also wanted to make upvoting easy, so it's represented in clear, visually appealing way. My goal was to make browsing, adding, updating and deleting user's tickets straight-forward and enjoyable, especially in mobile mode. Thanks to its design practices and clear concept I believe this web application can fulfill it's purpose.

#### Users stories

User stories that helped me developing this project: 

- As a user, I want to add new tickets, so I share them with other users and developers.
- As a user, I want to delete my old tickets.
- As a user, I want to vote on tickets, so other users/developers know how important is given ticket.
- As a user, I want to know other people's opinion about any given ticket.
- As a user, I want to sort tickets using particular method (recent, most commented, type etc.).
- As a user, I want to easily access tickets of particular type.
- As a user, I want to read some additional info about the project.
- As a user, I want to be able to see how much top users contributed.
- As a user, I want to view updates from developers in their blog.
- As a user, I want to comment developer's blog entries.
- As a user, I want to change my account details.
- As a developer, I want to keep in touch with users via blog.
- As an administrator, I want to have control over content of the website.

### Wireframes

Examples of wireframes I've used for this project:

- [Index page](https://istr-static.s3.eu-west-2.amazonaws.com/img/wireframe_1.png)
- [All tickets](https://istr-static.s3.eu-west-2.amazonaws.com/img/wireframe_2.png)
- [Detailed ticket](https://istr-static.s3.eu-west-2.amazonaws.com/img/wireframe_3.png)
- [Mobile screen](https://istr-static.s3.eu-west-2.amazonaws.com/img/wireframe_4.png)

## Database Schema

![Database Schema](https://istr-static.s3.eu-west-2.amazonaws.com/img/schema.png)

## Features

 - Sign in/Register form - allows users to use existing account or create new account, adding to database. Followed by flash message and redirect.
 - Edit user details form - Some user's details can be updated after registration.
 - Add ticket form - user can create a new ticket, inserting it to database.
 - Delete feature  - users that are logged in can delete ticket from database(only available for ticket's author or administrator in admin panel).
 - Filter by different criteria - this will allow the user to be shown all tickets of a specific type(bug or feature).
 - Sort by different criteria - user can sort existing tickets by date, number of upvotes and amount of comments.
 - Sign Out - user will be logged out from current session, returning to initial page.
 - Edit - Administrator can also edit, delete and create existing tickets and/or comments, add or edit blog entries/comments, change user details.
 
### Existing Features

- Browsing feature - allows users browse tickets, by type or all at once.
- Ticket feature - allows users to create, delete their ticket, register and sign in.
- Voting feature - allows users to upvote existing tickets.
- Payment feature - allows users to pay for "feature" ticket to help prioritize development.
- Summary feature - allows user to check who contributed to most tickets and who comments the most.

### Features Left to Implement

- Blog app routes and templates naming are confusing (blog as entry) it needs reworking, but requires so many app and main project changes that it was left behind to be implemented post deployment.

## Known Issues
Password form field at account details still being displayed even after explicitly ordered not to in custom form class. Temporary work-around it is to add hidden status to that field block in css rules file.

## Technologies Used

- HTML and CSS
    - project uses **HTML** and **CSS** to build webpages.
- [Bootstrap 4](https://getbootstrap.com/)
    - The project uses some **Bootstrap** elements for more responsive layout.
- [Python](https://www.python.org/)
    - Back-end was written in **Python** .
    - **vnev** library was used in development of the project.
- [JavaScript](https://www.javascript.com/)
    - This project uses **JavaScript** for interactive functionality of the application.
- [Django](https://www.djangoproject.com/)
    - The project was built **django** micro-framework due to its simplicity.
    - **flask.session** was used to store all variables values. 
- [D3.js](https://d3js.org/)
    - Used for creating charts.
- [checkout.js](https://docs.checkout.com/docs/checkoutjs)
    - Used for creating checkout.
- [unit-test](https://docs.python.org/3/library/unittest.html)
    - Used for automated testing.
- [Balsamiq](https://balsamiq.com/)
    - Before development started, **Balsamiq** was used for wireframes.
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/)
    - Adjusting elements of project's frontend.
- [PostgreSQL](https://www.postgresql.org/)
    - Postgres database hosted by AWS used by Heroku.
- [Flake8](http://flake8.pycqa.org/)
    - Used for Python linting.
- [Faker](https://faker.readthedocs.io/en/master/)
    - Python project, generates fake users, emails and text.
- [PEP8](http://pep8online.com/)
    - Used to check python syntax errors.
- [JSlint](https://www.jslint.com/)
    - Used to check JS snippet.
- [Black](https://black.readthedocs.io/en/stable/)
    - Used as a Python code formatter.
- [CSSlint](http://csslint.net/)
    - Check for CSS errors.
- [Font Awesome](https://fontawesome.com/)
    - Icons for the application.

## Testing

### Automated tests

There are eleven automated tests that use Django test module:
1. test_homepage - checks if index page is being created.
2. test_blog_page - checks if main blog page is being created.
3. test_login_page - checks if user login page is being created.
4. test_signup_page - checks for sign up page being created.
5. test_ticket_fields - checks if instance of ticket model is being created.
6. test_all_tickets -  checks for "all tickets" page.
7. test_single_ticket - checks if ticket page with id "1" is created.
8. test_user_fields - checks for user instance creation.
9. test_login_POST - checks if user login data is being posted.
10. test_blog_fields - checks if blog entry is being created.
11. test_blog_page - checks for single blog entry with id "1".


In order to run automated tests in Django you need to:

1. Replace Database entry in issue_tracker/settings.py to:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}
```
2. Change settings.py DEBUG entry:
```
DEBUG=False
```
3. Run commands:
```
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```
4. Run the test itself by typing:
```
python manage.py test
```

### Manual testing

This web application has been manually tested with different scenarios that the user may experience:

1. Log in
2. Log out
3. Sign Up
4. Create ticket
5. Create comment
6. Upvote ticket
7. Pay for upvoting feature ticket
8. Delete ticket
9. Create blog entry
10. Comment blog entry
11. Change user details

#### Manual testing breakdown

1. Log in
    - Click on "Log In" to be redirected to form with "user" and "password" fields.
    - Sign in with username and password of super user.
    - Click "Log In" button to be redirected back to homepage.
    - Check the user is logged in by seeing if "All Tickets", "New Ticket", "Blog", "Your Account" and "Logout" are visible in the navbar.

2. Log out:
    - Make sure you are signed in. 
    - Click on 'Log Out' navbar element.
    - Verify that navbar has changed(no "Sign Out", "My Recipes" & "Add Recipes" link). Instead, only five initial links are visible.
    - Click browser's back button. Verify, that you can't see "All Tickets", "New Ticket", "Blog", "Your Account" and "Logout" anymore.

3. Sign Up:
    - Similar to logging in, use "Sign Up" link to register new user.
    - Check the user is logged in by seeing if "All Tickets", "New Ticket", "Blog", "Your Account" and "Logout" are visible in the navbar.

4. Create ticket
    - Click on "New Ticket" (when logged in).
    - Add ticket title, text and decide the type.
    - Click on "Add Ticket" to be redirected to index page.

5. Create comment
    - Navigate to "All Tickets" and click on "View Details".
    - Click on "Add comment" button.
    - Type in the text and press "Send" button.
    - Check if you are redirected to index page message is displayed.

6. Upvote ticket
    - Navigate to "All Tickets" and click on one of the tickets with "Bug" tag.
    - Click on "Upvote" button.
    - Check if thank you screen is displayed.
    - Check if you're being redirected to index page.

7. Pay for upvoting feature ticket
    - Navigate to single ticket details with a "Feature" tag.
    - Press on "Pay to upvote" button.
    - Check if given ticket got extra upvote.
    - Check if index page pie chart has changed, your nickname's chart part has changed.

8. Delete ticket
    - If you created new ticket using "New Ticket" link navigate to your ticket.
    - Press "Delete" button on ticket details page.
    - Check if your ticket disappeared from "All Tickets" tab.

9. Create blog entry
    - If you are admin user go to [admin address](http://issue-tracker-pch.herokuapp.com/admin).
    - Go to blog tab.
    - Add new blog entry with image.
    - To check if it was added go back to the website and navigate to Blog link.

10. Comment blog entry
    - Enter "All Blogs" and show details of single entry.
    - Press "Add Comment" and enter text.
    - Post it and check if it was added below blog entry.

11. Change user details
    - From main page go to "Your Account".
    - Change email, first name and second name.
    - Post changes using button.

### User testing

Web application was also tested by group of users using similar scenarios as mentioned in manual testing. Feedback helped with further development.

## Deployment

The application is deployed on [Heroku](https://issue-tracker-pch.herokuapp.com/).

In order to deploy, following changes has been made:

1. Changed settings.py DEBUG entry:
```
DEBUG=False
```
2. Added requirements.txt and Procfile, as required by heroku.
3. Set Heroku Config Vars:
4. IP to 0.0.0.0
5. PORT to 5000
6. Added environmental variables for AWS S3 account.
7. Added environmental variables for app secret key.
8. Heroku's PostgreSQL configuration variables.
9. For payments set Stripes environmental variables.
10. Run:
```
python manage.py collecstatic
```
11. Configured dynos with this line:
```
web gunicorn issue_tracker.wsgi:application
```
12. Imported django_heroku module and added this line at the bottom of settings.py:
```
django_heroku.settings(locals())
```

To run it locally:

- Install python 3
- Install django framework
- Install packages requierd by project using pip3:
    boto3
    certifi
    chardet
    dj-database-url
    django-crispy-forms
    django-heroku
    django-storages
    gunicorn
    idna
    Pillow
    psycopg2
    psycopg2-binary
    pytz
    requests
    stripe
    urllib3
- Start the web server with commands:
```
python manage.py runserver
```
- Type http://127.0.0.1:8000 address or http://localhost:8000 in your browser window

## Credits

### Content

- Images where taken from [Shutterstock.com](https://www.shutterstock.com/)
- Font was taken from [FontSquirrel.com](https://www.fontsquirrel.com/)
- Icons taken from [Font Awsome](https://fontawesome.com/) 

### Media

- The background photo used in this site were obtained from [Shutterstock.com](https://www.shutterstock.com/)

### Acknowledgements

- Big shout out to my mentor [Antonija Šimić](https://github.com/tonkec/) and Code Institute tutors