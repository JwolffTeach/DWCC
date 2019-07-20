from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from app.forms import LoginForm, RegistrationForm, BuilderForm, BasicMoveForm
from app.models import Comment, User, Hero, Hero_Looks, Hero_Stats, LKUPLooks, LKUPRace, LKUPAlignment, LKUPHp, BasicMoves
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
    form.herorace.choices = [(item.id, item.race_name) for item in LKUPRace.query.all()]
    form.heroalignment.choices = [(item.id, item.alignment_name) for item in LKUPAlignment.query.all()]

    form.heroeyes.choices = [(item.id, item.look_details) for item in LKUPLooks.query.filter_by(look_type='Eyes').all()]
    form.herohair.choices = [(item.id, item.look_details) for item in LKUPLooks.query.filter_by(look_type='Hair').all()]
    form.heroclothing.choices = [(-1, "")] + [(item.id, item.look_details) for item in LKUPLooks.query.filter_by(look_type='Clothing').all()]
    form.herobody.choices = [(-1, "")] + [(item.id, item.look_details) for item in LKUPLooks.query.filter_by(look_type='Body').all()]
    form.heroskin.choices = [(-1, "")] + [(item.id, item.look_details) for item in LKUPLooks.query.filter_by(look_type='Skin').all()]
    form.herosymbol.choices = [(-1, "")] + [(item.id, item.look_details) for item in LKUPLooks.query.filter_by(look_type='Symbol').all()]

    if form.validate_on_submit():
        #hero_race = LKUPLooks.query.filter_by(id=request.form["herorace"]).first().race_name
        hero = Hero(
            owner_id=current_user.id, 
            hero_name=request.form["heroname"],
            hero_class=request.form["heroclass"],
            hero_race=LKUPRace.query.filter_by(id=request.form["herorace"]).first().race_name,
            hero_alignment=LKUPAlignment.query.filter_by(id=request.form["heroalignment"]).first().alignment_name
        )
        
        temp_clothing = None
        temp_body = None
        temp_skin = None
        temp_symbol = None
        if request.form["heroclothing"] is not "":
            temp_clothing=LKUPLooks.query.filter_by(id=request.form["heroclothing"]).first().look_details
        if request.form["herobody"] is not "":
            temp_body=LKUPLooks.query.filter_by(id=request.form["herobody"]).first().look_details
        if request.form["heroskin"] is not "":
            temp_skin=LKUPLooks.query.filter_by(id=request.form["heroskin"]).first().look_details
        if request.form["herosymbol"] is not "":
            temp_symbol=LKUPLooks.query.filter_by(id=request.form["herosymbol"]).first().look_details

        hero_looks = Hero_Looks(
            eyes=LKUPLooks.query.filter_by(id=request.form["heroeyes"]).first().look_details,
            hair=LKUPLooks.query.filter_by(id=request.form["herohair"]).first().look_details,
            clothing = temp_clothing,
            body = temp_body,
            skin = temp_skin,
            symbol = temp_symbol
        )

        hero_stats = Hero_Stats(
            strength=request.form["herostrength"],
            dexterity=request.form["herodexterity"],
            constitution=request.form["heroconstitution"],
            intelligence=request.form["herointelligence"],
            wisdom=request.form["herowisdom"],
            hp=request.form["herohp"]
        )
        
        db.session.add(hero)
        db.session.flush()
        hero_looks.hero_id = hero.id
        hero_stats.hero_id = hero.id
        db.session.add(hero_looks)
        db.session.add(hero_stats)
        db.session.commit()
        flash('Greetings ' + hero.hero_name + ', welcome to Dungeon World!')
        return redirect(url_for('index'))
    flash_errors(form)
    return render_template('builder.html', title='Build a Character', form=form)


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


@app.route('/race/<hero_class>')
def race(hero_class):
    lkup_race = LKUPRace.query.filter_by(class_name=hero_class).all()

    raceArray = []

    for raceVal in lkup_race:
        raceObj = {}
        raceObj['id'] = raceVal.id
        raceObj['class_name'] = hero_class
        raceObj['race_name'] = raceVal.race_name
        raceArray.append(raceObj)

    return jsonify({"race": raceArray})


@app.route('/alignment/<hero_class>')
def alignment(hero_class):
    lkup_alignment = LKUPAlignment.query.filter_by(class_name=hero_class).all()

    alignmentArray = []

    for alignmentVal in lkup_alignment:
        alignmentObj = {}
        alignmentObj['id'] = alignmentVal.id
        alignmentObj['class_name'] = hero_class
        alignmentObj['alignment_name'] = alignmentVal.alignment_name
        alignmentArray.append(alignmentObj)

    return jsonify({"alignment": alignmentArray})


@app.route('/hp/<hero_class>')
def hp(hero_class):
    lkup_hp = LKUPHp.query.filter_by(class_name=hero_class).all()

    hpArray = []

    for hpVal in lkup_hp:
        hpObj = {}
        hpObj['id'] = hpVal.id
        hpObj['class_name'] = hero_class
        hpObj['base_hp'] = hpVal.base_hp
        hpArray.append(hpObj)

    return jsonify({"hp": hpArray})


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


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


@app.route('/character/<hero_id>')
def character(hero_id):
    hero = Hero.query.filter_by(id=hero_id).first()
    return render_template('_character.html', title='Character Details', hero=hero)


@app.route('/addmove', methods=['GET', 'POST'])
def addmove():
    form = BasicMoveForm()
    if form.validate_on_submit():
        newMove = BasicMoves(
            move_name = request.form.get("movename", False),
            move_description = request.form.get("movedescription", False),
            move_details = request.form.get("movedetails", False)
        )

        db.session.add(newMove)
        db.session.commit()

        flash("You added the move " + newMove.move_name)
        return redirect(url_for('index'))
    return render_template('addmove.html', title='Add Move', form=form)

@app.route('/moves/basic')
def movesBasic():
    moves = BasicMoves.query.all()
    return render_template('moves/basic.html', title='Basic Moves', moves=moves)

@app.route('/move/<movename>')
def move(movename):
    move = BasicMoves.query.filter_by(move_name=movename).first()
    return render_template('_basic_move.html', title='Move', move=move)

@app.route('/topsecret')
def topsecret():
    return render_template('topsecret.html', title='Super Top Secret Stuff')

@app.route('/twentyfourtyeight')
def twentyfourtyeight():
    return render_template('2048/index.html', title='2048')