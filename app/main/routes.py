from flask import render_template, flash, redirect, url_for, request, current_app
from app import db
from app.main import bp
from app.models import User
from .forms import AddingUserForm


@bp.route('/')
def index():
    return redirect(url_for('main.add_user'))


@bp.route('/add_user', methods=('GET', 'POST'))
def add_user():
    form = AddingUserForm()
    if form.validate_on_submit():
        ln, fn, mn = form.name_parts
        pet = form.pet.data if form.pet.data != 'other' else form.other_pet.data
        user = User(first_name=fn, last_name=ln, middle_name=mn,
                    pet=pet, gender=form.gender.data, birthday=form.birthday.data)
        db.session.add(user)
        db.session.commit()

        flash(f'User {user.full_name} successfully added')
        return redirect(url_for('main.add_user'))

    return render_template('main/add_user.html', form=form)


@bp.route('/users_table')
def users_table():
    page = request.args.get('page', 1, type=int)
    users = User.query.paginate(
        page, current_app.config['USERS_PER_PAGE'], True)
    next_url = url_for('main.users_table', page=users.next_num) if users.has_next else None
    prev_url = url_for('main.users_table', page=users.prev_num) if users.has_prev else None
    return render_template('main/users_table.html', users=users.items, next_url=next_url, prev_url=prev_url)
