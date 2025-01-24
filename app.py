from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret_key_for_session'

@app.route('/')
def home():
    return redirect(url_for('stage1'))

@app.route('/stage1', methods=['GET', 'POST'])
def stage1():
    if request.method == 'POST':
        session['full_name'] = request.form['full_name']
        session['dob'] = request.form['dob']
        session['nationality'] = request.form['nationality']
        session['contact'] = request.form['contact']
        return redirect(url_for('stage2'))
    return render_template('stage1.html')

@app.route('/stage2', methods=['GET', 'POST'])
def stage2():
    if request.method == 'POST':
        session['departure_date'] = request.form['departure_date']
        session['return_date'] = request.form['return_date']
        session['accommodation'] = request.form['accommodation']
        session['special_requests'] = request.form.get('special_requests', '')
        return redirect(url_for('stage3'))
    return render_template('stage2.html')

@app.route('/stage3', methods=['GET', 'POST'])
def stage3():
    if request.method == 'POST':
        session['health_declaration'] = request.form['health_declaration']
        session['emergency_contact'] = request.form['emergency_contact']
        session['medical_conditions'] = request.form.get('medical_conditions', '')
        return redirect(url_for('success'))
    return render_template('stage3.html')

@app.route('/success')
def success():
    return render_template('success.html', data=session)

if __name__ == '__main__':
    app.run(debug=True)
