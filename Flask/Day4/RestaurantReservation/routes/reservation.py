from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint
from flask.views import MethodView
from models import Reservation
from db import db

reserve_blp = Blueprint('Reservations',
                        'reservations',
                        description='Operations on reservations',
                        url_prefix='/')

reserve_edit_blp = Blueprint('ReservationsEdit',
                             'reservations_edit',
                             description='Operations on reservations',
                             url_prefix='/rsv_edit')


#API List
#/rsv
# 모든 예약 조회 (GET)
@reserve_blp.route('/')
class ReservationsList(MethodView):
    def get(self):
        reservations = Reservation.query.all()
        return jsonify([{"customer_name": reservation.customer_name,
                         "customer_phone": reservation.customer_phone,
                         "reservation_time": reservation.reservation_time,
                         "number_of_people": reservation.number_of_people,
                         "special_requests": reservation.special_requests}
                        for reservation in reservations])

    def post(self):
        data = request.json
        new_reservation = Reservation(
            customer_name=data['customer_name'],
            customer_phone=data['customer_phone'],
            reservation_time=data['reservation_time'],
            number_of_people=data['number_of_people'],
            special_requests=data['special_requests']
        )
        db.session.add(new_reservation)
        db.session.commit()

        return jsonify({"msg": "new reservation created successfully"}), 201


# API List
# 특정 예약 수정
@reserve_edit_blp.route('/<int:reservation_id>')
class ReservationsEdit(MethodView):
    def put(self, reservation_id):
        data = request.json
        reservation = Reservation.query.get_or_404(reservation_id)

        reservation.reservation_time = data['reservation_time']
        reservation.number_of_people = data['number_of_people']
        reservation.special_requests = data.get['special_requests']

        db.session.commit()
        return jsonify({"msg": "reservation edited successfully"}), 201

    def delete(self, reservation_id):
        reservation = Reservation.query.get_or_404(reservation_id)
        db.session.delete(reservation)
        db.session.commit()

        return jsonify({"msg": "reservation deleted successfully"}), 204
