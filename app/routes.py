from app import app
from app.controllers import person_controller

app.add_url_rule("/person","create_person", person_controller.create_person, methods=["POST"])