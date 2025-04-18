from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# This function simulates the parking logic
def execute_parking_logic(car_number, action):
    if action == 'park':
        return f"Car {car_number} parked successfully!"
    elif action == 'remove':
        return f"Car {car_number} removed from parking!"
    else:
        return "Invalid action"

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
        stack = get_stack()
        if car_number in stack:
            session['message'] = f"Car {car_number} is already parked!"
        else:
            stack.append(car_number)
            session['stack'] = stack
            session['message'] = execute_parking_logic(car_number, 'park')
    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove():
    stack = get_stack()
    if stack:
        removed_car = stack.pop()
        session['stack'] = stack
        session['message'] = execute_parking_logic(removed_car, 'remove')
    else:
        session['message'] = 'No cars to remove'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
