from flask.helpers import url_for
from werkzeug.utils import redirect
from flask import render_template, request, abort
from flask_login import login_required, current_user
from app.models import Comment, Blog, User
from app.main.forms import CommentForm, BlogForm
from . import main
from .. import db

# Views
@main.route("/")
def index():
    blogs = Blog.get_all_blogs()
    quote = {
        "quote": "Perl – The only language that looks the same before and after RSA encryption.",
        "author": "Keith Bostic",
    }
    return render_template("index.html", blogs=blogs, quote=quote)


@main.route("/blog", methods=["GET", "POST"])
@login_required
def add_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(
            title=form.title.data,
            category=form.category.data,
            content=form.content.data,
            user=current_user,
        )
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for("main.index"))

    title = "Add Blog"
    return render_template("new_blog.html", blog_form=form, title=title)
