from app.email import mail_message
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask import render_template, request, abort
from flask_login import login_required, current_user
from app.models import Comment, Blog, User, Subscribe
from app.main.forms import CommentForm, BlogForm, SubscribeForm, UpdateProfile
from ..requests import get_quote
from . import main
from .. import db, photos

# Views
@main.route("/", methods=["GET", "POST"])
def index():
    form = SubscribeForm()
    blogs = Blog.get_all_blogs()
    quote = get_quote()
    if form.validate_on_submit():
        subscribe = Subscribe(email=form.email.data)
        db.session.add(subscribe)
        db.session.commit()

        form.email.data = ""
        return redirect(url_for("main.index"))
    form.email.data = ""
    return render_template("index.html", blogs=blogs, quote=quote, subscribe_form=form)


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
        subscribers = Subscribe.query.all()
        to = [sub.email for sub in subscribers]
        mail_message("New Blog Alert","email/welcome_user", to, url=request.url_root, blog=blog)
        return redirect(url_for("main.index"))
    title = "Add Blog"
    return render_template("new_blog.html", blog_form=form, title=title)

@main.route("/blog/<int:id>", methods=["GET", "POST"])
def blog(id):
    blog = Blog.get_blog(id)
    form = CommentForm()
    if request.method == "GET":
        comments = blog.comments
        return render_template("blog.html", blog=blog, comments=comments, user=current_user, comment_form=form)
    else:
        if form.validate_on_submit():
            comment = Comment(
                comment=form.comment.data, blog=blog, user_id=current_user.id
            )
            db.session.add(comment)
            db.session.commit()
            # refetch comments
            comments = blog.comments
            # clear form since we are rendering same view
            form.comment.data = ""
            return render_template("blog.html", comments=comments, user=current_user, comment_form=form, blog=blog)
    return render_template("blog.html", blog=blog)

@main.route('/blog/<int:blog_id>/delete/comment/<int:id>')
@login_required
def delete_comment(blog_id, id):
    comment = Comment.query.filter_by(id=id, blog_id=blog_id).first()
    db.session.delete(comment)
    db.session.commit()
 
    return redirect(url_for("main.blog", id=blog_id))

@main.route('/delete/blog/<int:id>')
@login_required
def delete_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    db.session.delete(blog)
    db.session.commit()
 
    return redirect(url_for("main.index"))


@main.route("/blog/<int:id>/update", methods=["GET", "POST"])
@login_required
def update_blog(id):
    blog = Blog.get_blog(id)
    form = BlogForm()
    form.title.data = blog.title
    form.category.data = blog.category
    form.content.data = blog.content
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

    return render_template("new_blog.html", blog_form=form)

@main.route("/blog/<int:id>/like", methods=["GET", "POST"])
def like(id):
    blog = Blog.get_blog(id)
    blog.hearts = blog.hearts + 1
    db.session.commit()
    return redirect(url_for("main.blog", id=id))

@main.route("/user/<uname>")
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route("/user/<uname>/update", methods=["GET", "POST"])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("main.profile", uname=user.username))

    return render_template("profile/update.html", form=form)


@main.route("/user/<uname>/update/pic", methods=["POST"])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if "photo" in request.files:
        filename = photos.save(request.files["photo"])
        path = f"photos/{filename}"
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for("main.profile", uname=uname))

@main.route("/filter/<category>")
def filter_blogs(category):
    blogs = Blog.query.filter_by(category=category).all()
    form = SubscribeForm()
    quote = get_quote()
    return render_template("index.html", blogs=blogs, quote=quote, subscribe_form=form)
