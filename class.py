from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")

def home():
    name = "Subhrajyoti Mahato"
    age = "15"
    return render_template("index.html",name=name,age=age)

@app.route("/father")

def father():
    name = "Tarani Mahato"
    age= "45"
    return render_template("father.html",name2=name,age2=age)

@app.route("/mother")

def mother():
    name="Kakali Mahato"
    age="39"
    return render_template("mother.html",name=name,age=age)

@app.route("/film")

def film():
    name="Pather Panchali (Song of the little road)"
    return render_template("film.html",name4=name)
app.run(debug=True)
