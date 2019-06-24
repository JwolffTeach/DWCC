from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from app.forms import LoginForm, RegistrationForm, BuilderForm, LooksForm
from app.models import Comment, User, Hero, Hero_Looks, LKUPLooks
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/', methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "GET":
        user_heroes = current_user.heroes.all()
        user_heroes_looks = Hero_Looks.query.all()
        return render_template("main_page.html", heroes=user_heroes, hero_looks=user_heroes_looks, title='Dungeon World Character Creator')

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
    looks_form = LooksForm()

    looks_form.eyes.choices = [("", "")] + [(item.id, item.look_details) for item in LKUPLooks.query.filter_by(class_name='Bard', look_type='Eyes').all()]
    looks_form.hair.choices = [("", "")] + [(item.id, item.look_details) for item in LKUPLooks.query.filter_by(class_name='Bard', look_type='Hair').all()]
    looks_form.clothing.choices = [("", "")] + [(item.id, item.look_details) for item in LKUPLooks.query.filter_by(class_name='Bard', look_type='Clothing').all()]
    looks_form.body.choices = [("", "")] + [(item.id, item.look_details) for item in LKUPLooks.query.filter_by(class_name='Bard', look_type='Body').all()]
    looks_form.skin.choices = [("", "")] + [(item.id, item.look_details) for item in LKUPLooks.query.filter_by(class_name='Bard', look_type='Skin').all()]
    looks_form.symbol.choices = [("", "")] + [(item.id, item.look_details) for item in LKUPLooks.query.filter_by(class_name='Bard', look_type='Symbol').all()]

    if form.validate_on_submit():
        hero = Hero(
            owner_id=current_user.id, 
            hero_name=request.form["heroname"],
            hero_class=request.form["heroclass"],
            hero_race=request.form["herorace"],
            hero_alignment=request.form["heroalignment"]
        )

        hero_looks = Hero_Looks(
            eyes=request.form["heroeyes"],
            hair=request.form["herohair"],
            clothing=request.form["heroclothing"],
            body=request.form["herobody"],
            skin=request.form["heroskin"],
            symbol=request.form["herosymbol"]
        )
        
        db.session.add(hero)
        db.session.flush()
        hero_looks.hero_id = hero.id
        db.session.add(hero_looks)
        db.session.commit()
        flash('Greetings ' + hero.hero_name + ', welcome to Dungeon World!')
        return redirect(url_for('index'))
    return render_template('builder.html', title='Build a Character', form=form, looks_form=looks_form)


@app.route('/looks/<hero_class>/<look_property>')
def looks(hero_class, look_property):
    lkup_looks = LKUPLooks.query.filter_by(class_name=hero_class, look_type=look_property).all()

    lookArray = []

    for look in lkup_looks:
        lookObj = {}
        lookObj['id'] = look.id
        lookObj['look_details'] = look.look_details
        lookArray.append(lookObj)

    return jsonify({look_property: lookArray})


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