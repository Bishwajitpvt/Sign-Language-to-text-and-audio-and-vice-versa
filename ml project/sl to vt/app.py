from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/sign-to-text')
def run_script():
    # Execute the Python script
    output = subprocess.check_output(['python', './final_pred.py'])
    return output
