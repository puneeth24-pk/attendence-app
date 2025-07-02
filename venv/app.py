from flask import Flask, render_template, request
import csv
import os
from datetime import datetime

app = Flask(__name__)

# CSV file path
CSV_FILE = 'attendance.csv'

# Ensure the CSV file exists and has a header
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Timestamp'])  # Header row

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mark', methods=['POST'])
def mark():
    name = request.form['name']
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write attendance to CSV file
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, time])

    return render_template('index.html', success=True, name=name)

if __name__ == '__main__':
    app.run(debug=True)
