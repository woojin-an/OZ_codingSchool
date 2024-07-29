from db import db


class Reservation(db.Model):
    __tablename__ = 'reservations'

    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(100), nullable=False)
    reservation_time = db.Column(db.DateTime, nullable=False)
    number_of_people = db.Column(db.Integer, nullable=False)
    special_requests = db.Column(db.String(255))

    def to_dict(self):
        return {
            'reservation_id': self.reservation_id,
            'customer_name': self.customer_name,
            'customer_phone': self.customer_phone,
            'reservation_time': self.reservation_time,
            'number_of_people': self.number_of_people,
            'special_requests': self.special_requests
        }