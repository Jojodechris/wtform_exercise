from flask import Flask, render_template, redirect, flash,session

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"

app.config['WTF_CSRF_ENABLED'] = False


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///Pet_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
with app.app_context():
    db.create_all()
# db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)




@app.route('/')
def list_Pet():
    pets= Pet.query.all()
    # request.form.get("")
    return render_template('pet_list.html',pets=pets)


@app.route('/add')
def add_Pet():
    return render_template('addPet.html')

@app.route("/add/new",methods =['GET','POST'])
def add_new_pet():
    form = AddPetForm()
    pets= Pet.query.all()
    if form.validate_on_submit():
    
        name = form.name.data
        photo_url = form.photo_url.data
        age = form.ages.data
        notes = form.notes.data
        species= form.species.data
        available = form.available.data
        
        pet = Pet(name=name, photo_url=photo_url, age=age, notes=notes, available=available, species=species)
        db.session.add(pet)
        db.session.commit()

        # flash(f"Added {name} at {price}")
        return render_template('pet_list.html',pets=pets)
    else:
        return render_template("addPet.html",form=form)
        # (url_for('list_pets'))


        




    


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5002)








    





