from app import app

@app.route("/transaction/add", methods=["POST"])
def create():
    return "Create a Transaction"