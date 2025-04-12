from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Stack to keep track of parked cars
parking_stack = []

@app.route('/')
def index():
    return render_template('index.html', parking_stack=list(reversed(parking_stack)))

@app.route('/park', methods=['POST'])
def park():
    car_number = request.form['car_number']
    if car_number:
        parking_stack.append(car_number)
    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove():
    if parking_stack:
        parking_stack.pop()
    return redirect(url_for('index'))

#  REQUIRED for Render deployment
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
