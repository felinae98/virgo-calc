from flask import Flask, render_template, request, abort, session
from flask_session import Session
from problem import Problem
from os import environ
import json
from fractions import Fraction

app = Flask(__name__)

app.config['SESSION_TYPE'] = "filesystem"
app.config['SESSION_FILE_DIR'] = "/tmp/flask-session"
app.config['SESSION_FILE_MODE'] = 384
app.config['SESSION_PERMANENT'] = True

app.secret_key = environ["SECRET_KEY"]
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        num = int(request.form['num'])
        enable_frac = request.form['enable_frac'] == "true"
        show_ans = request.form["show_ans"] == "true"
        enable_pow = request.form["enable_pow"] == "true"
        pow_symb = request.form["pow_symb"]
        assert pow_symb in ("^", "**")
    except:
        return abort(400)
    res = []
    for _ in range(num):
        problem = Problem(pow_symb, True, enable_frac, enable_pow)
        if show_ans:
            res.append("{}={}".format(str(problem), str(problem.root.number)))
        else:
            res.append("{}=?".format(str(problem)))
    return '\n'.join(res)

@app.route("/start", methods=["POST"])
def start():
    try:
        session['all_num'] = int(request.form['num'])
        session['enable_frac'] = request.form['enable_frac'] == "true"
        session['enable_pow'] = request.form['enable_pow'] == "true"
    except:
        abort(400)
    session['cur_num'] = 1
    session["correct_ans"] = 0
    problem = Problem("^", True, session['enable_frac'], session['enable_pow'])
    res = {"prob":str(problem), "cur_num": session['cur_num'], "all_num": session['all_num']}
    session['ans'] = str(problem.root.number)
    return json.dumps(res)

@app.route("/submit", methods=["POST"])
def submit():
    try:
        ans = Fraction(request.form['ans'])
    except:
        abort(400)
    if str(ans) == session["ans"]:
        session['correct_ans'] += 1
        res = {"correct": True}
        return json.dumps(res)
    else:
        res = {"correct": False, "ans": session['ans']}
        return json.dumps(res)

@app.route("/next", methods=["POST"])
def next():
    session['cur_num'] += 1
    problem = Problem("^", True, session['enable_frac'], session['enable_pow'])
    session['ans'] = str(problem.root.number)
    res = {
        "prob": str(problem),
        "cur_num": session['cur_num'],
        "all_num": session["all_num"]
    }
    return json.dumps(res)
