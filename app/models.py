from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'Role {self.name}'


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.Text)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    blogs = db.relationship('Blog',backref='user',lazy="dynamic")


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),index = True)
    category = db.Column(db.String(255), index = True)
    content = db.Column(db.Text)
    hearts = db.Column(db.Integer, default=0)
    date_published = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref='blog',lazy="dynamic")

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @property
    def preview(self):
        return self.content[:300] + '...'


    @classmethod
    def get_blogs(cls, user_id):
       blogs = Blog.query.filter_by(user_id=user_id).all()
       return blogs
    
    @classmethod
    def get_all_blogs(cls):
        blogs = Blog.query.order_by(Blog.date_published.desc()).all()
        return blogs

    @classmethod
    def get_blog(cls, blog_id):
        blog = Blog.query.filter_by(id=blog_id).one()
        return blog

    def __repr__(self):
        return f'Blog {self.title}'


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_comments(cls, blog_id):
       comments = Comment.query.filter_by(blog_id=blog_id).all()
       return comments

    def __repr__(self):
        return f'Comment {self.id}'



