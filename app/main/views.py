from flask import render_template, redirect, url_for, abort, request
from flask_login import login_required, current_user
from . import main
from .. import db, photos
from .form import PitchForm, CommentForm, UpdateProfile
from ..models import Pitch, Comment, User, Upvote, Downvote


@main.route('/')
def index():
    pitches = Pitch.query.all()
    art = Pitch.query.filter_by(category='art').all()
    poetry = Pitch.query.filter_by(category='poetry').all()
    music = Pitch.query.filter_by(category='music').all()
    return render_template('index.html', art=art, poetry = poetry, music = music, pitches = pitches)


@main.route('/posts')
@login_required
def posts():
    posts = Post.query.all()
    likes = Upvote.query.all()
    user = current_user
    return render_template('pitch_display.html', posts=posts, likes=likes, user=user)


@main.route('/create_new', methods = ['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user._get_current_object().id
        new_pitch_obj = Post(post=post, title=title, category=category, user_id=user_id)
        new_pitch_obj.save()
        return redirect(url_for('main.index'))

    return render_template('pitch.html', form=form)


@main.route('/comment/<int:pitch_id>', methods=['POST', 'GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(
            comment=comment,
            pitch_id=pitch_id,
            user_id=user_id
        )
        new_comment.save()
        new_comments = [new_comment]
        print(new_comments)
        return redirect(url_for('.comment', pitch_id=pitch_id))
    return render_template('comment.html', form=form, pitch=pitch, all_comments=all_comments)


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    posts = Pitch.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)
    return render_template('profile/profile.html', user=user, posts=posts)


@main.route('/user/<name>/updateprofile', methods=['POST', 'GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username=name).first()
    if user is None:
        error = 'The user does not exist'
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile', name=name))
    return render_template('profile/update_profile.html', form=form)


@main.route('/like/<int:id>', methods=['POST', 'GET'])
@login_required
def upvote(id):
    get_pitches = Post.query.get(id)
    new_post = Upvote(post=post, upvote=1)
    new_post.save()
    return redirect(url_for('main.posts'))


@main.route('/dislike/<int:id>', methods=['GET', 'POST'])
@login_required
def downvote(id):
    post = Post.query.get(id)
    np = Downvote(post=post, downvote=1)
    np.save()
    return redirect(url_for('main.posts'))
