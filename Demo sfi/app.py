from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Serves index.html

@app.route('/motor_control')
def motor_control():
    return render_template('motor_control.html')  # Serves motor_control.html

@app.route('/sensor-data')
def sensor_data():
    data = {
        "temperature": 25.0,
        "humidity": 60,
        "soil_moisture": 35
    }
    return jsonify(data)

@app.route('/toggle-pump')
def toggle_pump():
    return "Pump toggled"

if __name__ == '__main__':
    app.run(debug=True)
