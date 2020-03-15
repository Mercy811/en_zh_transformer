from flask import Flask
from flask import render_template


app = Flask(__name__) # create a instance of the Flask object

# add a function that returns content
# use Flask's app.route decorator to map the URL route / to that function:
@app.route("/")
@app.route("/hello/<name>")
def hello_there(name):
    return render_template(
        "base.html", name=name #render_template assumes that the first argument is relative to the templates folder
    )


