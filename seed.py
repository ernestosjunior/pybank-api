from app.models.person_model import Person
from app.utils.hash import generate_hash
from app import create_app
from app.extensions import db
from sqlalchemy import or_

app = create_app()

with app.app_context():
    email = "pessoainicial@pybank.com"
    cpf = "12345678907"

    person = Person.query.filter(or_(Person.email == email, Person.cpf == cpf)).first()

    if not person:
        password_hash = generate_hash("mudar123")
        person_created = Person(
            name="Pessoa Inicial",
            cpf=cpf,
            birth_date="1997-08-02",
            email=email,
            password=password_hash,
        )

        db.session.add(person_created)
        db.session.commit()
        print("Seed applied.")
    else:
        print("There is no seed to apply.")
