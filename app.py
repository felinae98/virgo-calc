from flask import Flask, render_template, request, abort
from problem import Problem
app = Flask(__name__)

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
