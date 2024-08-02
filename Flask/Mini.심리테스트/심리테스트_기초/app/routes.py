from flask import Blueprint, jsonify, render_template, request, url_for
from .database import db
from .models import Participant, Answer
import pytz
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
from collections import Counter

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

    # 나이 별 참가자 수
    age_counts = Counter([p.age for p in participants])

    # 전체 참가자 그래프 데이터 준비
    graphJSON_participants = {
        'data': [{'type': 'bar', 'x': list(age_counts.keys()), 'y': list(age_counts.values())}],  # 예시 데이터
        'layout': {'title': 'All Participants'}
    }

    # 질문 별 응답자 수 집계
    answer_counts = {
        f'Question {i}': {'YES': 0, 'NO': 0} for i in range(1, 6)
    }
    for answer in answers:
        question_key = f'Question {answer.question_id}'
        if answer.chosen_answer.upper() in ['YES', 'NO']:
            answer_counts[question_key][answer.chosen_answer.upper()] += 1

    # 그래프 만들기
    graphsJSON_answers = {
        question: {
            'data': [
                {'type': 'bar', 'x': ['YES', 'NO'], 'y': [counts['YES'], counts['NO']], 'name': question}
            ],
            'layout': {'title': question}
        }
        for question, counts in answer_counts.items()
    }

    return render_template('results.html',
                           graphJSON_participants=graphJSON_participants,
                           graphsJSON_answers=graphsJSON_answers)

