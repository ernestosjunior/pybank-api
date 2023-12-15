from flask import jsonify, request
from app.interfaces.person import PersonInput
from app.utils.hash import generate_hash
from app.models.person_model import Person
from app import db


def create_person():
    schema = PersonInput()
    body = request.get_json()
    try:
        person = schema.load(body)
        password_hash = generate_hash(person.get("password"))
        person_created = Person(
            name=person.get("name"),
            cpf=person.get("cpf"),
            birth_date=person.get("birth_date"),
            email=person.get("email"),
            password=password_hash,
        )
        db.session.add(person_created)
        db.session.commit()
        response_data = schema.dump(person_created)
        del response_data["password"]
        return response_data, 201 
    except Exception as e:
        return jsonify({"error": str(e)}), 400
