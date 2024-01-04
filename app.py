from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home.html")
def home():
    return render_template('home.html')

# @app.route("/about.html")
# def about():
#     return render_template('about.html')

@app.route("/projects.html")
def projects():
    return render_template('projects.html')

@app.route("/projects_details_gcashcalc.html")
def projects_details_gcashcalc():
    return render_template('projects_details_gcashcalc.html')

@app.route("/projects_details_gcashcalc_web.html")
def projects_details_gcashcalc_web():
    return render_template('projects_details_gcashcalc_web.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/thanks.html")
def thanks():
    return render_template('thanks.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
