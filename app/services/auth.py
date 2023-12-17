from flask_jwt_extended import get_jwt_identity
from app.models import Person, Account
from app.exc import NotFoundException, NotAllowedException


def check_person(current_person):
    current_user_id = get_jwt_identity()
    person = Person.query.filter_by(id=current_user_id).first()

    if not person:
        raise NotFoundException("User not found.")

    is_current_person = person.id == current_person.get("person_id")

    if not is_current_person:
        raise NotAllowedException(
            "It is not possible to create an account for another user."
        )

    return person
