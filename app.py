from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Stack to store parked cars
parking_stack = []

@app.route('/')
def index():
    # LIFO: Show latest entry at the top
    return render_template('index.html', parking_stack=list(reversed(parking_stack)))

@app.route('/park', methods=['POST'])
def park_car():
    car_number = request.form['car_number'].strip()
    if car_number:
        parking_stack.append(car_number)
    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove_car():
    if parking_stack:
        parking_stack.pop()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
