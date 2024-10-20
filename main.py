from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/about/')
def index():
    return render_template("about.html")

@app.route('/home/')
def index2():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()