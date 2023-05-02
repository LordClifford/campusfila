import urllib.request, urllib.parse
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for,request,jsonify,get_flashed_messages
from flask_migrate import Migrate
import json
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_login import login_required,login_user,logout_user,current_user,UserMixin, LoginManager
from flask_marshmallow import Marshmallow
from flask import(
Flask,g,redirect,render_template,request,session,url_for,flash,jsonify
)
from flask_cors import CORS
#from flask_uploads import UploadSet,IMAGES, configure_uploads



app=Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:password@eligibility.central.edu.gh:5432/alumni'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://post:password@eligibility.central.edu.gh:5432/alumni'
app.config['SECRET_KEY'] =" thisismysecretkey"
app.config['UPLOADED_PHOTOS_DEST'] ='uploads'

# photos=UploadSet('photos', IMAGES)
# configure_uploads(app, photos)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)



login_manager = LoginManager(app)
login_manager.login_view = "ulogin"
login_manager.login_message_category = "info"
migrate = Migrate(app, db)
from forms import *

@login_manager.user_loader
def load_user(user_id):
    return Person.query.get(int(user_id))




def sendtelegram(params):
    url = "https://api.telegram.org/bot5738222395:AAEM5NwDAN1Zc052xI_i9-YlrVnvmSkN9p4/sendMessage?chat_id=-633441737&text=" + urllib.parse.quote(params)
    content = urllib.request.urlopen(url).read()
    print(content)
    return content

''''
#login for admin
class User:
    username = StringField('username', validators=[DataRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=80)])
    submit = SubmitField('Login')
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='admin', password='central'))
users.append(User(id=2, username='likem', password='likem'))
users.append(User(id=3, username='john', password='some'))



@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
'''

#DATABASE MODEL
#person table
class Person(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200), nullable=True)
    yearCompleted= db.Column(db.String(200), nullable=True)
    nationality= db.Column(db.String(200), nullable=True)
    contact= db.Column(db.Integer(), nullable=True)
    email= db.Column(db.String(200), nullable=True)
    faculty= db.Column(db.String(200), nullable=True)
    hallofresidence= db.Column(db.String(200), nullable=True)
    password= db.Column(db.String(20))
    school= db.Column(db.String(20))
    email= db.Column(db.String(20), nullable=True)
    phone= db.Column(db.String(10), nullable=True )
    indexnumber=db.Column(db.String())
    password=db.Column(db.String)
    gender= db.Column(db.String()    )
    department= db.Column(db.String()    )
    program= db.Column(db.String()   )
    telephone= db.Column(db.String()   )
    admitted= db.Column(db.Integer()  )
    address= db.Column(db.String()   )
    work= db.Column(db.String()  )
    guardian= db.Column(db.String()  )
    kin= db.Column(db.String()   )
    relationship= db.Column(db.String()  )
    marital= db.Column(db.String()   )
    health= db.Column(db.String()    )
    form=db.Column(db.String())
    extra= db.Column(db.String()     )
    image_file = db.Column(db.String(20))
    def __repr__(self):
        return f"Person('{self.id}', {self.name}', {self.yearCompleted})"

class alumni(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(20) )
    name= db.Column(db.String(200) )
    password= db.Column(db.String(200) )
    email= db.Column(db.String(20) )
    indexnumber= db.Column(db.String(10)  )
    telephone= db.Column(db.String(10)  )
    def __repr__(self):
        return f"alumni('{self.id}', {self.name}', {self.email})"

    
    
class User(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    fullname= db.Column(db.String()  )
    indexnumber= db.Column(db.Integer())
    gender= db.Column(db.String()    )
    laspag=db.column(db.String())
    faceofcu=db.column(db.String)
    school= db.Column(db.String()    )
    department= db.Column(db.String()    )
    program= db.Column(db.String()   )
    completed= db.Column(db.Integer()     )
    admitted= db.Column(db.Integer()  )
    email= db.Column(db.String()     )
    telephone= db.Column(db.String()     )
    hall= db.Column(db.String()  )
    nationality= db.Column(db.String()   )
    address= db.Column(db.String()   )
    work= db.Column(db.String()  )
    guardian= db.Column(db.String()  )
    kin= db.Column(db.String()   )
    relationship= db.Column(db.String()  )
    marital= db.Column(db.String()   )
    health= db.Column(db.String()    )
    extra= db.Column(db.String()     )
    image_file = db.Column(db.String(20))
    def __repr__(self):
        return f"User('{self.id}', {self.fullname}, {self.gender}, {self.health}'"
    
class Department(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String())
    school= db.Column(db.String()) 
    def __repr__(self):
        return f"Department('{self.id}', {self.name}'"
    
class School(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    def __repr__(self):
        return f"School('{self.id}', {self.name}'"
    
    
    
class Postme(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    extra=db.Column(db.String)
    address=db.Column(db.String)
    telephone=db.Column(db.String)
    def __repr__(self):
        return f"School('{self.id}', {self.extra}'"
    
        
class Year(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    def __repr__(self):
        return f"year('{self.id}', {self.name}'"
    
class Program(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String) 
    school =db.Column(db.String) 
    department =db.Column(db.String) 
    def __repr__(self):
        return f"Program('{self.id}', {self.name}'"
    
    
@app.route('/dashboard')
@login_required
def dashboard():
    if current_user == None:
        flash("Welcome to the CentralAlumina " + current_user.email, "Success")
        flash(f"There was a problem")
    return render_template('dashboard.html', title='dashboard')

    eay
@app.route('/getstudent')
def getstudent():
    return render_template('getstudent.html')

@app.route('/chat')
@login_required
def chat():
    return render_template('chat.html')

@app.route('/votes')
def votes():
    return render_template('votes.html')



@app.route('/addpost', methods=['GET', 'POST'])
@login_required
def addpost():
    form=Post()
    if form.validate_on_submit():
  
            post=Postme(  
                   telephone=form.telephone.data,  
                  
                   address=form.address.data,  
                   
                  extra=form.extra.data,    
               
                  )
       
            db.session.add(post)
            db.session.commit()
            flash("You Just Wrote a Post", "success")
            return redirect('/userbase')
    print(form.errors)
    return render_template("addpost.html", form=form)



@app.route('/addalumni', methods=['GET', 'POST'])
@login_required
def addalumni():
    form=Adduser()
    if form.validate_on_submit():
  
            new=User(fullname=form.fullname.data,
                 
                  
                   work=form.work.data,  
                   guardian=form.guardian.data,  
                    
               image_file=form.image_file.data
                  )
       
            db.session.add(new)
            db.session.commit()
            flash("You Just Posted", "success")
            return redirect('/userbase')
    print(form.errors)
    return render_template("addAlumni.html", form=form)





@app.route('/chats', methods=[ 'POST'])
def chats():  
    return render_template("search.html")



#search for user
@app.route('/usersearch', methods=[ 'POST'])
def usersearch():
    form= UserSearch()
    if request.method == 'POST': 
        posts =User.query
        if form.validate_on_submit():
            postsearched=form.searched.data
            posts =posts.filter(User.fullname.like('%'+ postsearched + '%') )
            posts =posts.order_by(User.indexnumber).all() 
            flash("You searched for "+ postsearched, "success")  
            print(posts)   
    return render_template("usersearch.html", form=form, searched =postsearched, posts=posts, header="Year Group", smalltitle="Central Alumni Platform", name="", numberofentries="16 entries")


# @app.route('/userbase')
# @login_required
# def userbase():
#     print("Fetching all")
#     users=User.query.order_by(User.id.desc()).all()
#     print(users)
#     print(current_user)
#     return render_template("userbase.html", users=users, current_user=current_user, header="Information Technology", smalltitle="2021", name="- CCSITA", numberofentries="16 entries")
 



@app.route('/list/<int:userid>', methods=['GET', 'POST'])
@login_required
def list(userid):
    form=Post()
    if form.validate_on_submit():
  
            post=Postme(  
                    
                   
                  extra=form.extra.data,    
               
                  )
       
            db.session.add(post)
            db.session.commit()
    print("Fetching one")
    profile=User.query.get_or_404(userid)
    print(current_user)
    user=Postme.query.order_by(Postme.id.desc()).all()
    print(user)
    return render_template("profileid.html",current_user=current_user, user=user, profile=profile, title="list",form=form)
 


@app.route('/list', methods=['GET', 'POST'])
@login_required
def lists():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("list.html", users=users, current_user=current_user, title="list")



@app.route('/<int:year>/newschools', methods=['GET', 'POST'])
def newschools(year ):
    form=Addschool()
    schools=School.query.all()
    if request.method== 'POST':
        schools=School(name=form.data)
        db.session.add(schools)
        db.session.commit()
    return render_template('newschools.html', form=form, title="newschools",schools=schools,year=year)



@app.route('/userlogout')
@login_required
def userlogout():
    if current_user:
        logout_user()
        # print(current_user.email)
    else:
        print("Well that didnt work")
    flash('You have been logged out.','danger')
    return redirect(url_for("ulogin"))






@app.route('/form', methods=['POST', 'GET'])
def form():
    form=RegistrationForm()
    if form.validate_on_submit():
       
        new=Person(name=form.name.data, yearCompleted=form.yearCompleted.data,
                   nationality=form.nationality.data, 
                   contact=form.contact.data, email=form.email.data,faculty=form.faculty.data,
                   hallofresidence=form.hallofresidence.data, password=form.password.data)
        db.session.add(new)
        db.session.commit()
        return redirect('information')
       
    flash("Added a New Alumni", "success")
    print(form.errors)
    return render_template("form.html", form=form)

@app.route('/information')
@login_required
def information():
    persons=Person.query.order_by(Person.id.desc()).all()
    print(persons)
    return render_template("information.html", persons=persons)
 



#CRUD(update and delete routes)
@app.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id):
    form=Adduser()
    user=User.query.get_or_404(id)
    if request.method== 'GET':
        form.fullname.data = user.fullname
        form.indexnumber.data = user.indexnumber
        form.gender.data = user.gender
        form.school.data = user.school
        form.department.data = user.department
        form.completed.data = user.completed
        form.admitted.data = user.admitted
        form.email.data = user.email   
        form.telephone.data = user.telephone  
        form.hall.data = user.hall  
        form.nationality.data = user.nationality   
        form.address.data = user.address  
        form.work.data = user.work 
        form.guardian.data = user.guardian   
        form.marital.data = user.marital   
        form.extra.data = user.extra  
        form.image_file.data = user.image_file 
    if request.method== 'POST':
        new=User(fullname=form.fullname.data,
                 indexnumber=form.indexnumber.data,
                   gender=form.gender.data, 
                    school=form.school.data,
                    department=form.department.data,
                   completed=form.completed.data,
                   admitted=form.admitted.data,
                   email=form.email.data,  
                   telephone=form.telephone.data,  
                   hall=form.hall.data,  
                   nationality=form.nationality.data,  
                   address=form.address.data,  
                   work=form.work.data,   
                   guardian=form.guardian.data,  
                  marital=form.marital.data,
                  extra=form.extra.data,    
               image_file=form.image_file.data
                  )
        try:    
            db.session.add(new)
            db.session.commit()
            return redirect(url_for('list')) 
        except:
            return render_template("dashboard.html")
    return render_template("addAlumni.html", form=form)
    
    
#CRUD(update and delete routes)
@app.route("/updateuser/<int:id>", methods=['POST', 'GET'])
def updateuser(id):
    form=RegistrationForm()
    user=Person.query.get_or_404(id)
    if request.method== 'GET':
        form.name.data = user.name
        form.indexnumber.data = user.indexnumber
        form.gender.data = user.gender
        form.school.data = user.school
        form.department.data = user.department
        form.yearCompleted.data = user.yearCompleted
        form.admitted.data = user.admitted
        form.email.data = user.email   
        form.telephone.data = user.telephone  
        form.hallofresidence.data = user.hallofresidence  
        form.nationality.data = user.nationality   
        form.address.data = user.address  
        form.work.data = user.work 
        form.guardian.data = user.guardian   
        form.marital.data = user.marital   
        form.extra.data = user.extra  
        form.image_file.data = user.image_file 
    if request.method== 'POST':
        new=Person(name=form.name.data,
                 indexnumber=form.indexnumber.data,
                   gender=form.gender.data, 
                    school=form.school.data,
                    department=form.department.data,
                   yearCompleted=form.yearCompleted.data,
                   admitted=form.admitted.data,
                   email=form.email.data,  
                   telephone=form.telephone.data,  
                   hallofresidence=form.hallofresidence.data,  
                   nationality=form.nationality.data,  
                   address=form.address.data,  
                   work=form.work.data,  
                   guardian=form.guardian.data,  
                  marital=form.marital.data,
                  extra=form.extra.data,    
               image_file=form.image_file.data
                  )
        try:    
            db.session.add(new)
            db.session.commit()
            return redirect(url_for('information')) 
        except:
            return "errror"
    return render_template("userprofile.html", form=form)
    
    
#delete route
@app.route("/delete/<int:id>")
def delete(id):
    delete=User.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect(url_for('list')) 
    except: 
        return "errrrrorrr"
   
   
@app.route('/usersignup', methods=['POST','GET'])
def usersignup():
    form = Registration()
    print(form.faculty.data)
    print(form.email.data)
    print(form.name.data)
    print(form.password.data)
   
    
    if request.method == "POST": 
        if form.validate_on_submit():
            print('Success')
            user =Person(password=form.password.data, email=form.email.data, faculty=form.faculty.data, name=form.name.data)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            print(current_user)
           
            return redirect(url_for('ulogin'))
        else:
            print(form.errors)
           
    return render_template('usersignup.html', form=form)
   

@app.route('/ulogin', methods=['POST','GET'])
def ulogin():
    form = LoginForm()
    print ('try')
    print(form.email.data)
    print(form.password.data)
    
    if form.validate_on_submit():
        print("form Validated successfully")
        user = Person.query.filter_by(email = form.email.data).first()
        #     # flash (f'Wrong Password', 'success')
        #     # sendtelegram('Entered Wrong Emai')
        # if user != None:
        #     print("user:" + user.email + "found")
        #     print(user.password)
        #     if user and form.password.data == user.password:
        #         print(user.email + "validored successfully")
        login_user(user)
        
        flash ('Welcome to CampusFila' +' ' + user.name ,'success')
        return redirect(url_for('userbase'))
                # next = request.args.get('next')
        #     else:
        #         flash (f'Wrong Password', 'success')
        #         sendtelegram(user.email +' '+ 'Entered Wrong Password')
        # else:
        #     sendtelegram("BEANS")
        #     flash (f'Wrong Password', 'danger')
            
            
    return render_template('userlogin.html', form=form)



@app.route('/userdisplay/<int:userid>', methods=['GET', 'POST'])
@login_required
def userdisplay(userid):
  
    profile=User.query.get_or_404(userid)
    print(current_user)
    return render_template("userdisplay.html",current_user=current_user, profile=profile, title="list")
 

@app.route('/post')
@login_required
def post():
    return render_template("post.html")
 
 


@app.route('/')
def userlanding():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    return render_template("userlanding.html",  users=users, current_user=current_user,form=form)
 

@app.route('/userbase',methods=['GET', 'POST'])
@login_required
def userbase():
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    user=Postme.query.order_by(Postme.id.desc()).all()
    print(user)
    print(current_user)
    return render_template("userbase.html", users=users,user=user,current_user=current_user,form=form)
 

  


@app.route('/userinformation/<int:userid>', methods=['GET', 'POST'])
@login_required
def userinformation(userid):
    profile=User.query.get_or_404(userid)
    print(current_user)
    return render_template("userinformation.html",current_user=current_user, profile=profile, title="list")
 
   
#ending user



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=8000, debug=True)
    
    
