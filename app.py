from flask import Flask, render_template, redirect, request, session, url_for, escape, request


import data
import bcrypt


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def welcome_page():
    if not session:
        return render_template("log_or_main.html", logged_in=False)
    elif session:
        aut_username = session['email'].split('@')
        return render_template("log_or_main.html", logged_in=True, username=aut_username[0].capitalize())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = session['email'] = request.form['email']
        user_password = request.form['password']
        if user_email in data.users:
            veryfi = verify_password(user_password, data.users[user_email])
            if veryfi:
                return redirect(url_for('welcome_page'))
            elif not veryfi:
                return render_template("log_in.html", tried=True)
        elif user_email not in data.users:
            return render_template("log_in.html", tried=True)
    elif request.method == 'GET':
        return render_template("log_in.html", tried=False)


@app.route("/test/<id>/<result>", methods=['POST', 'GET'])
def render_test(id, result):
    if session:
        questions, a = put_data_to_list_from_dict()
        if request.method == 'GET':
            return render_template("test.html", max=len(questions), question=questions[int(id)], answers=a[int(id)], id=int(id), result=result)
        elif request.method == 'POST':
            user_answer = request.form['answer']
            if str(user_answer) == 'True':
                result = int(result) + 1
            return render_template("test.html", max=len(questions), question=questions[int(id)], answers=a[int(id)],                         id=int(id), result=result)
    elif not session:
        return redirect('/')


@app.route('/logout')
def logout():
    session.pop('email')
    return redirect("/")


@app.route("/result/<result>")
def result(result):
    percent = (int(result) / 5) * 100
    if session:
        return render_template("result.html", result=result, percent=percent)
    else:
        return redirect("/")


def put_data_to_list_from_dict():
    questions_list = [question for question, answer in data.questions.items()]
    answers = [answer for question, answer in data.questions.items()]
    #for question, answer in data.questions.items():
        #questions_list.append(question)
        #answers.append(answer)
    return questions_list, answers


def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


if __name__ == '__main__':
    app.run(
        port=8000,
        debug=True,
    )

