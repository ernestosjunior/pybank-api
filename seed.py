from app.models.person_model import Person
from app.utils.hash import generate_hash
from app import create_app
from app.extensions import db

app = create_app()

with app.app_context():
    password_hash = generate_hash("mudar123")
    person_created = Person(
        name="Pessoa Inicial",
        cpf="12345678907",
        birth_date="1997-08-02",
        email="pessoainicial@pybank.com",
        password=password_hash,
    )

    db.session.add(person_created)
    db.session.commit()
