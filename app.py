from flask import Flask, render_template, request, jsonify, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Configure server-side session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

def get_stack():
    # Initialize a new stack if not already in session for the current user
    if 'stack' not in session:
        session['stack'] = []
    return session['stack']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/park', methods=['POST'])
def park():
    # Get car number from the form data
    car_number = request.form.get('car_number')  
    
    if not car_number:
        # If no car number is provided, return an error response
        return jsonify({'success': False, 'message': 'Car number is required'})
    
    # Get the stack for the current user session
    stack = get_stack()
    stack.append(car_number)  # Add car number to stack
    session['stack'] = stack  # Update session with new stack
    
    return jsonify({'success': True, 'message': f'Car {car_number} parked successfully', 'stack': stack})

@app.route('/remove', methods=['POST'])
def remove():
    # Get the stack for the current user session
    stack = get_stack()
    
    if stack:
        # If there are cars in the stack, remove the last car
        removed_car = stack.pop()
        session['stack'] = stack  # Update session with new stack
        return jsonify({'success': True, 'removed_car': removed_car, 'message': f'Car {removed_car} removed', 'stack': stack})
    else:
        return jsonify({'success': False, 'message': 'No cars to remove'})

@app.route('/get_stack', methods=['GET'])
def get_stack_route():
    # Get the stack for the current user session
    stack = get_stack()  
    return jsonify({'stack': stack})

if __name__ == '__main__':
    app.run(debug=True)
