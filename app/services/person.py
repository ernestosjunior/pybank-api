from app.models import Person
from app import db
from app.utils.hash import generate_hash


def create_person_profile(person_data):
    password_hash = generate_hash(person_data.get("password"))
    person_created = Person(
        name=person_data.get("name"),
        cpf=person_data.get("cpf"),
        birth_date=person_data.get("birth_date"),
        email=person_data.get("email"),
        password=password_hash,
    )
    db.session.add(person_created)
    db.session.commit()
    return person_created
