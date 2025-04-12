from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Stack to manage parking
parking_stack = []

@app.route("/")
def index():
    return render_template("index.html", parking_stack=list(reversed(parking_stack)))

@app.route("/park", methods=["POST"])
def park():
    car_number = request.form["car_number"]
    parking_stack.append(car_number)
    return render_template("index.html", parking_stack=list(reversed(parking_stack)), message=f"Car {car_number} parked successfully!")

@app.route("/remove", methods=["POST"])
def remove():
    if parking_stack:
        removed_car = parking_stack.pop()
        return render_template("index.html", parking_stack=list(reversed(parking_stack)), message=f"Car {removed_car} removed.")
    else:
        return render_template("index.html", parking_stack=[], message="No cars in the parking stack.")

# 🔥 Required for Render deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
