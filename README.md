# Issue Tracker

### Description

The primary entity in the Issue Tracker is a ticket describing a user’s issue, and similar to Github’s issue tracker, it allows users to create tickets, comment on tickets, and show the status of the ticket (e.g. ‘to do,’ ‘doing,’ or ‘done’). As mentioned, issues come in two varieties – ‘bugs’ (which I’ll fix for free, eventually), and ‘features’ which are only developed if enough money is offered. Users will be able to upvote bugs (signifying ‘I have this too’), and upvote feature requests (signifying ‘I want to have this too’). While upvoting bugs is free, to upvote a feature request, users would need to pay some money to pay for time in working on it. In turn, at least 50% of time working will be spend on developing the highest-paid feature.
To offer transparency there is a page that contains some graphs showing how many bugs or features are tended to on a daily, weekly and monthly basis, as well as the highest-voted bugs and features.

## UX

#### Users stories

### Wireframes

## Database Schema

![Database Schema](https://istr-static.s3.eu-west-2.amazonaws.com/img/schema.png)

## Features

### Existing Features

### Features Left to Implement

- Blog app routes and templates naming are confusing (blog as entry) it needs reworking, but requires so many app and main project changes that it was left behind to be implemented post deployment.

##Known Issues
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
- [PEP8](http://pep8online.com/)
    - Used to check python syntax errors.
- [JSlint](https://www.jslint.com/)
    - Used to check JS snippet.
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

1. Log in
    1. Click on "Log In" to be redirected to form with "user" and "password" fields.
    2. Sign in with username and password of super user.
    3. Click "Log In" button to be redirected back to homepage.
    2. Check the user is logged in by seeing if "All Tickets", "New Ticket", "Blog", "Your Account" and "Logout" are visible in the navbar.

2. Log out:
    1. Make sure you are signed in. 
    2. Click on 'Log Out' navbar element.
    3. Verify that navbar has changed(no "Sign Out", "My Recipes" & "Add Recipes" link). Instead, only five initial links are visible.
    4. Click browser's back button. Verify, that you can't see "All Tickets", "New Ticket", "Blog", "Your Account" and "Logout" anymore.

3. Sign Up:
    1. Similar to logging in, use "Sign Up" link to register new user.
    2. Check the user is logged in by seeing if "All Tickets", "New Ticket", "Blog", "Your Account" and "Logout" are visible in the navbar.

4. Create ticket
    1. Click on "New Ticket" (when logged in).
    2. Add ticket title, text and decide the type.
    3. Click on "Add Ticket" to be redirected to index page.

5. Create comment
    1. Navigate to "All Tickets" and click on "View Details".
    2. Click on "Add comment" button.
    3. Type in the text and press "Send" button.
    4. Check if you are redirected to index page message is displayed.

6. Upvote ticket
    1. Navigate to "All Tickets" and click on one of the tickets with "Bug" tag.
    2. Click on "Upvote" button.
    3. Check if thank you screen is displayed.
    4. Check if you're being redirected to index page.

7. Pay for upvoting feature ticket
    1. Navigate to single ticket details with a "Feature" tag.
    2. Press on "Pay to upvote" button.
    3. Check if given ticket got extra upvote.
    4. Check if index page pie chart has changed, your nickname's chart part has changed.

8. Delete ticket
    1. If you created new ticket using "New Ticket" link navigate to your ticket.
    2. Press "Delete" button on ticket details page.
    3. Check if your ticket disappeared from "All Tickets" tab.

9. Create blog entry
    1. If you are admin user go to [admin address](http://issue-tracker-pch.herokuapp.com/admin).
    2. Go to blog tab.
    3. Add new blog entry with image.
    4. To check if it was added go back to the website and navigate to Blog link.

10. Comment blog entry
    1. Enter "All Blogs" and show details of single entry.
    2. Press "Add Comment" and enter text.
    3. Post it and check if it was added below blog entry.

11. Change user details
    1. From main page go to "Your Account".
    2. Change email, first name and second name.
    3. Post changes using button.

### User testing

Web application was also tested by group of users using similar scenarios as mentioned in manual testing. Feedback helped with further development.

## Deployment

The application is deployed to Heroku.

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

### Media

### Acknowledgements

- Big shout out to my mentor [Antonija Šimić](https://github.com/tonkec/) and Code Institute tutors