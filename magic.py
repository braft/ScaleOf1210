from flask import render_template, request
from app.forms import InputForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/scale', methods=['GET', 'POST'])
def scale():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        inquiry = form.inquiry.data
        x = 0
        p = 0
        for i in inquiry:
            x += ord(i.lower()) - 96
        y = abs(x) % 10
        if y == 0:
            p = 10
        else:
            p = y
        answer = p
    else:
        answer = None
    return render_template("scale.html", form = form, answer = answer)
