from flask import Flask, render_template
import os

# Initialize Flask app and explicitly specify the template folder
app = Flask(__name__, template_folder='templates')

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')  # Render the index.html template

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
