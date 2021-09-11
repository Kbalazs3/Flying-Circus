# Flying Circus

## Story

You work for an English school named Flying Circus. Your boss came up with the
wonderful idea of having an online English test for the customers of the company
to help them practice their vocabulary knowledge. It is important to keep the
application secure (protected by password) but we don't want to store anything
about our customers just provide them the opportunity to practice and give feedback.

## What are you going to learn?

You'll learn about:

- web routing and redirects,
- authentication,
- sessions,
- hashed passwords.

## Tasks

1. Create a webform through which the user can log into the applicaton.
    - Opening the application's `/login` page in a web browser shows a web form with an email and a password input and a submit button
    - Entering a correct email-password pair that is built in the program and pressing the submit button redirects the user to the index (`/`) page
    - Entering invalid email-password pair and pressing the submit button shows an error message `Wrong password!`
    - Passwords are stored in a hashed form with salt using some modern, key streching algorithms such as bcrypt, PBKDF2 or scrypt

2. Create an index page where there is some welcome text, it can be seen whether the user logged in, the user can log out and there is a link to the `/test` page.
    - Opening the application's index (`/`) page in a web browser shows a web page with some welcome text
    - If the user is not logged in, opening the application's index (`/`) page in a web browser shows a web page with a link to the `/login` page
    - If the user is logged in, opening the application's index (`/`) page in a web browser shows a web page showing the email address of the logged in user, a link to the `/logout` route and a link to the `/test` page
    - If the user is logged in and the application's index (`/`) page is refreshed then the user stays logged in

3. Create a route through which the user can log out from the application.
    - Opening the application's `/logout` route in a web browser logs the user out and redirects the user to the index (`/`) page

4. Create a test page which shows one question and the corresponding answers at a time. The user can answer all the questions. After answering them, the user is redirected to the results.
    - If the user is logged in, opening the application's `/test` page in a web browser shows a web page showing one question, the corresponding answers as radio buttons and a submit button
    - If the user is not logged in, opening the application's `/test` page in a web browser redirects the user to the index (`/`) page
    - Clicking the submit button loads the next question or if there are no more questions, redirects the user to the `/result` page
    - Refreshing the `/test` page keeps the actual answer shown (the browser doesn't ask about resending POST data)

5. Create a result page where it is shown how many questions has the user answered right.
    - If the user is logged in, opening the application's `/result` page in a web browser shows a web page showing how many questions has the user answered right
    - If the user is not logged in, opening the application's `/result` page in a web browser redirects the user to the index (`/`) page

## General requirements

- The application is built with the Flask framework

## Hints


- Use the functions `redirect()` and `url_for()` insensively (but meaningfully),
  e.g. in the following cases:
  - If you want to prevent a page from showing if the user is not logged in
    you can redirect the user to the index page.
  - If you want to prevent the user from resubmitting a form by refreshing the page
    you can create a separate route for processing the POST request and redirect
    after processing back to the page showing the form.
- Use Jinja2's `if` statement when you want to show data on a condition (e.g.
  some data when the user is logged in, and some other when the user isn't logged in).
- Use Jinja2's `for` statement when you want to show multiple data elements in the same format.
- Don't forget to clear all session variable upon logging out the user.
  

## Background materials

- <i class="far fa-exclamation"></i> [Sessions](project/curriculum/materials/pages/web/authentication-sessions.md)
- <i class="far fa-book-open"></i> [Cookies](project/curriculum/materials/pages/web/authentication-cookies.md)
- <i class="far fa-exclamation"></i> [Salted password hashing](project/curriculum/materials/pages/web-security/salted-password-hashing.md)
- <i class="far fa-exclamation"></i> [Flask documentation](http://flask.palletsprojects.com/) (especially the quickstart#the-request-object and quickstart#sessions part)
- <i class="far fa-book-open"></i> [Jinja2 documentation](https://jinja.palletsprojects.com/en/2.10.x/templates/)
- <i class="far fa-book-open"></i> [HTTP is stateless](project/curriculum/materials/pages/web/authentication-http-stateless.md)
