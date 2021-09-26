# Han Blogs

## Built By [Hannah Waruguru](https://github.com/HWaruguru/)

## Description
Han Blog is a blogging website where I create and share my opinions and other writers can also write, and delete degrading comments. Users are able to view the blogs and add their comments. There is also a random quote to inspire the users. 

## User Stories
These are the behaviours/features that the application implements for use by a user.

Users can:
* view the blog posts on the site
* comment on blog posts
* view the most recent posts
* receive an email alert when a new post is made by joining a subscription.
* see random quotes on the site

Writers can: 
* sign in to the blog.
* create a blog from the application.
* delete comments that I find insulting or degrading.
* update or delete blogs I have created.

## SetUp / Installation Requirements
### Prerequisites
* python
* flask
* postgres
* sqlalchemy
* bootstrap

### Cloning
* In your terminal:
        
        $ git clone https://github.com/HWaruguru/Han-Blog.git
        $ cd Han-Blog

## Running the Application
* To run the application:

        -> python -m venv virtual
        -> source ./virtual/bin/activate
        -> pip install -r requirements.txt
        -> Set environment variables
            export MAIL_USERNAME=""
            export MAIL_PASSWORD=""
            export ENV="development"
            export DATABASE_URL=""
            export SECRET_KEY=""
        -> After creating your local postgresql database run the migrations upgrade command below to apply migrations to your db
        -> python manage.py db upgrade
        -> python manage.py server
        
## Testing the Application
* To run the tests:

        $ python manage.py test
        
        
## Technologies Used
* Python3.9

## License
MIT &copy;2021 [Hannah Waruguru](https://github.com/HWaruguru/)

