from app import app

@app.route("/person/add", methods=["POST"])
def create():
    return "Create a Person"