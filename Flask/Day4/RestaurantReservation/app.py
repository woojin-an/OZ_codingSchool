from flask import Flask, request, redirect, url_for, render_template
from flask_smorest import Api
from db import db
from models import Reservation
from routes.reservation import reserve_blp, reserve_edit_blp
from flask_migrate import Migrate
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:oz-password@localhost/restaurantreservation'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(reserve_blp)
api.register_blueprint(reserve_edit_blp)

migrate = Migrate(app, db)


@app.route('/manage_reservation', methods=['GET', 'POST'])
def manage_reservation():
    if request.method == 'POST':
        data = request.form  # HTML 폼에서 전송된 데이터 가져오기
        new_reservation = Reservation(
            customer_name=data['customer_name'],
            customer_phone=data['customer_phone'],
            reservation_time=data['reservation_time'],
            number_of_people=data['number_of_people'],
            special_requests=data.get('special_requests')  # 빈 문자열일 수 있으므로 get() 사용
        )
        db.session.add(new_reservation)
        db.session.commit()
        return redirect(url_for('manage_reservation'))  # 데이터 저장 후 페이지 새로고침

    reservations = Reservation.query.all()  # 예약 목록 조회
    return render_template('index.html', reservations=reservations)


@app.route('/edit_reservation', methods=['PUT'])
def edit_reservation():
    reservation = Reservation.query.all()

    if request.method == 'PUT':
        data = request.form
        reservation.customer_name = data['customer_name']
        reservation.customer_phone = data['customer_phone']
        reservation.reservation_time = data['reservation_time']
        reservation.number_of_people = data['number_of_people']
        reservation.special_requests = data.get('special_requests')

        db.session.commit()
        return redirect(url_for('manage_reservation'))

    return render_template('edit.html', reservation=reservation)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)