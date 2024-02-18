from flask import Flask,render_template,request,flash,redirect,url_for
from dbs import app,User,db



@app.route("/")
def index():
    return "hello"


@app.route("/login")
def login():
    return render_template("/login&logout.html")


@app.route("/add-user", methods=["POST","GET"])
def add_user():
    if request.method=="POST":
        try:
            name=request.form.get("full_name")
            email=request.form.get("email")
            password=request.form.get("email")

            if not (name and email and password):
                raise ValueError("Ensure all fields are filled correctly")
            
            new_user=User(name=name,email=email,password=password)
            db.session.add(new_user)
            db.session.commit()
            
            flash("Account created succesfully! Login")
            return render_template("login&logout.html")
        
    
        except ValueError as e :
            return str(e)
          
    







if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)