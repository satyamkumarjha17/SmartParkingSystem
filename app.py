from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
import subprocess

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

def execute_parking_logic(car_number, action):
    try:
        result = subprocess.run(['./parking.exe', car_number, action], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

def get_stack():
    if 'stack' not in session:
        session['stack'] = []
    return session['stack']

@app.route('/')
def index():
    stack = get_stack()
    message = session.pop('message', '')
    return render_template('index.html', stack=stack, message=message)

@app.route('/park', methods=['POST'])
def park():
    car_number = request.form.get('car_number')
    if not car_number:
        session['message'] = 'Car number is required'
    else:
        result = execute_parking_logic(car_number, 'park')
        session['message'] = result
        stack = get_stack()
        stack.append(car_number)
        session['stack'] = stack
    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove():
    stack = get_stack()
    if stack:
        removed_car = stack.pop()
        result = execute_parking_logic(removed_car, 'remove')
        session['message'] = result
        session['stack'] = stack
    else:
        session['message'] = 'No cars to remove'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
