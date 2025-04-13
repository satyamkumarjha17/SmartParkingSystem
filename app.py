from flask import Flask, render_template, request, jsonify, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Configure server-side session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

def get_stack():
    if 'stack' not in session:
        session['stack'] = []
    return session['stack']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/park', methods=['POST'])
def park():
    car_number = request.form['car_number']
    stack = get_stack()
    stack.append(car_number)
    session['stack'] = stack
    return jsonify({'success': True, 'stack': stack})

@app.route('/remove', methods=['POST'])
def remove():
    stack = get_stack()
    if stack:
        removed_car = stack.pop()
        session['stack'] = stack
        return jsonify({'success': True, 'removed_car': removed_car, 'stack': stack})
    else:
        return jsonify({'success': False, 'message': 'No cars to remove'})

@app.route('/get_stack', methods=['GET'])
def get_stack_route():
    stack = get_stack()
    return jsonify({'stack': stack})

if __name__ == '__main__':
    app.run(debug=True)
