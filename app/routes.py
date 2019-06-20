from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, BuilderForm
from app.models import Comment, User, Hero
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/', methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "GET":
        return render_template("main_page.html", heroes=current_user.heroes.all(), title='Dungeon World Character Creator')

    hero = Hero(owner_id=current_user.id, hero_name=request.form["hero_name"], hero_class=request.form["hero_class"])
    db.session.add(hero)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/newmain', methods=["GET", "POST"])
def newmain():
    return render_template("new_main.html", comments=Comment.query.all())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/builder', methods=['GET', 'POST'])
@login_required
def builder():
    form = BuilderForm()
    if form.validate_on_submit():
        hero = Hero(
            owner_id=current_user.id, 
            hero_name=request.form["heroname"],
            hero_class=request.form["heroclass"],
            hero_race=request.form["herorace"],
            hero_alignment=request.form["heroalignment"]
            #,hero_eyes=request.form["heroeyes"],
            #hero_hair=request.form["herohair"],
            #hero_clothing=request.form["heroclothing"],
            #hero_body=request.form["herobody"],
            #hero_skin=request.form["heroskin"],
            #hero_symbol=request.form["herosymbol"]
        )        
"""         heroLooks = Hero_Looks(
            hero_id = hero.id,
            hero_eyes=request.form["heroeyes"],
            hero_hair=request.form["herohair"],
            hero_clothing=request.form["heroclothing"],
            hero_body=request.form["herobody"],
            hero_skin=request.form["heroskin"],
            hero_symbol=request.form["herosymbol"]
        ) """
        db.session.add(hero)
        db.session.commit()
        flash('Greetings ' + hero.hero_name + ', welcome to Dungeon World!')
        return redirect(url_for('index'))
    return render_template('builder.html', title='Build a Character', form=form)


@app.route('/slidingforms', methods=['GET', 'POST'])
@login_required
def slidingforms():
    form = BuilderForm()
    if form.validate_on_submit():
        hero = Hero(
            owner_id=current_user.id, 
            hero_name=request.form["heroname"], 
            hero_class=request.form["heroclass"], 
            hero_race=request.form["herorace"], 
            hero_alignment=request.form["heroalignment"],
            hero_eyes=request.form["heroeyes"],
            hero_hair=request.form["herohair"],
            hero_clothing=request.form["heroclothing"],
            hero_body=request.form["herobody"],
            hero_skin=request.form["heroskin"],
            hero_symbol=request.form["herosymbol"]
        )
        db.session.add(hero)
        db.session.commit()
        flash('Greetings ' + hero.hero_name + ', welcome to Dungeon World!')
        return redirect(url_for('index'))
    return render_template('slidingforms.html', title='Build a Character', form=form)