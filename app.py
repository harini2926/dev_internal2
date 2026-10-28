from flask import Flask, render_template, request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("register.html")
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name= request.form("name")
        email= request.form("email")
        course= request.form("course")
        if name and email and course: 
            return render_template("success.html", name=name, email=email, course=course)
        return render_template("register.html", error="field need to fill")
    return render_template("register.html")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    
