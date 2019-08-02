# Issue Tracker

### Description

The primary entity in the Issue Tracker is a ticket describing a user’s issue, and similar to Github’s issue tracker, it allows users to create tickets, comment on tickets, and show the status of the ticket (e.g. ‘to do,’ ‘doing,’ or ‘done’). As mentioned, issues come in two varieties – ‘bugs’ (which I’ll fix for free, eventually), and ‘features’ which are only developed if enough money is offered. Users will be able to upvote bugs (signifying ‘I have this too’), and upvote feature requests (signifying ‘I want to have this too’). While upvoting bugs is free, to upvote a feature request, users would need to pay some money to pay for time in working on it. In turn, at least 50% of time working will be spend on developing the highest-paid feature.
To offer transparency there is a page that contains some graphs showing how many bugs or features are tended to on a daily, weekly and monthly basis, as well as the highest-voted bugs and features.



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

In order to run automated tests in Django you need to:

1. Replace Database entry in issue_tracker/settings.py to:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}
2. Run commands:
```
python manage.py runserver
python manage.py makemigrations
python manage.py collectstatic
```
3. Run the test itself by typing:
```
python manage.py test
```

### Manual testing:

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
    1. Click on 'Log In' to be redirected to form with "user" and "password" fields.
    2. Sign in with username "user" and password "user".
    3. Click on 'Submit' to be redirected to homepage.
    4. Check the user is logged in by seeing if 'Add Recipe' and 'My Recipes' are visible in the navbar.

2. Log out:
    1. Make sure you are signed in. 
    2. Click on 'Sign Out' button.
    3. Verify that navbar has changed(no "Sign Out", "My Recipes" & "Add Recipes" link). Instead, only five initial links are visible.
    4. Click browser's back button. Verify, that you can't see  "My Recipes" and "Add Recipes" anymore.

3. Sign Up:
    1. Similar to signing in, use "Sign Up" link to register new user.
    2. Check the user is logged in by seeing if "All Tickets", "New Ticket", "Blog", "Your Account" and "Logout" are visible in the navbar.

4. Create ticket
5. Create comment
6. Upvote ticket
7. Pay for upvoting feature ticket
8. Delete ticket
9. Create blog entry
10. Comment blog entry
11. Change user details



### Acknowledgements

- Big shout out to my mentor [Antonija Šimić](https://github.com/tonkec/) and Code Institute tutors