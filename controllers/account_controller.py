from app import app

@app.route("/account/add", methods=["POST"])
def create():
    return "Create an Account"