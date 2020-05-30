from flask import Blueprint
from flask_api.extensions import db
from flask_api.models import Users, Banks

debugging = Blueprint('debugging', __name__)


@debugging.route('/debug_users', methods=['GET'])
def debug_users():

    gavin = Users(first_name="Gavin",
                  last_name="Slusher",
                  email="slusherg@gmail.com",
                  account_balance=10000.00)

    slusher_bank = Banks(account_number=123456789,
                         bank_name="Slusher Bank",
                         email="slusherg@gmail.com")

    db.session.add(gavin)
    db.session.add(slusher_bank)
    db.session.commit()

    tj = Users(first_name="TJ",
               last_name="Prange",
               email="pranget@gmail.com",
               account_balance=100000.00)

    tj_bank = Banks(account_number=987654321,
                    bank_name="Smells Cargo",
                    email="tjprange@gmail.com")

    db.session.add(tj)
    db.session.add(tj_bank)
    db.session.commit()

    return "successful debugging"
