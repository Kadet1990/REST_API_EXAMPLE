from flask import render_template

from configuration import connex_app as connex


connex_app = connex

# Configuration server file - swagger.yml
connex_app.add_api("swagger.yml")


# Create route
@connex_app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    #debug mode
    connex_app.run(debug=True)