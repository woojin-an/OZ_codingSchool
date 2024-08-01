from flask import Blueprint, jsonify, render_template, request, url_for
from .database import db
from .models import Participant, Answer
import pytz
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

main = Blueprint("main", __name__)


# 홈페이지 렌더링
@main.route("/", methods=["GET"])
def home():
    # 참여자 정보 입력 페이지를 렌더링합니다.
    return render_template("index.html")


# 참가자 정보를 post
@main.route("/participants", methods=["POST"])
def add_participant():
    data = request.get_json()
    new_participant = Participant(
        name=data["name"],
        age=data["age"],
        gender=data["gender"]
    )
    db.session.add(new_participant)
    db.session.commit()

    return jsonify(
        {"redirect": url_for("main.question"), "participant_id": new_participant.id}
    )


@main.route("/question", methods=["get"])
def question():
    return render_template("question.html")


@main.route("/submit", methods=["POST"])
def submit():
    participant_id = request.cookies.get("participant_id")
    if not participant_id:
        return jsonify({"error": "Participant ID not found"}), 400

    data = request.json
    answers = data.get("answers")

    if not answers:
        return jsonify({"error": "Answers not found"}), 400

    for answer in answers:
        question_id = answer.get("question_id")
        chosen_answer = answer.get("chosen_answer")

        new_answer = Answer(
            question_id=question_id,
            participant_id=participant_id,
            chosen_answer=chosen_answer
        )
        db.session.add(new_answer)

    db.session.commit()
    return jsonify({"redirect": url_for("main.home")})

@main.route("/results")
def show_results():
    # 모든 참가자의 답변을 가져옵니다.
    answers = Answer.query.all()
    participants = Participant.query.all()

    # 전체 참가자 그래프 데이터 준비
    graphJSON_participants = {
        'data': [{'type': 'bar', 'x': [p.name for p in participants], 'y': [p.id for p in participants]}],  # 예시 데이터
        'layout': {'title': 'All Participants'}
    }

    # 각 참가자별 그래프 데이터 준비
    graphsJSON_answers = {}
    for answer in answers:
        if answer.participant_id not in graphsJSON_answers:
            graphsJSON_answers[answer.participant_id] = {
                'data': [],
                'layout': {'title': f'Participant {answer.participant_id}'}
            }

        # 각 질문에 대한 데이터 추가
        graphsJSON_answers[answer.participant_id]['data'].append({
            'type': 'bar',
            'x': [f'Question {answer.question_id}'],
            'y': [answer.chosen_answer],
            'name': f'Question {answer.question_id}'
        })

    return render_template('results.html',
                           graphJSON_participants=graphJSON_participants,
                           graphsJSON_answers=graphsJSON_answers)

