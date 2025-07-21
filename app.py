from flask import Flask, request, send_file
from flask_cors import CORS
from geopy.geocoders import Nominatim
import swisseph as swe
from reportlab.pdfgen import canvas
import io
import datetime

app = Flask(__name__)
CORS(app)

swe.set_ephe_path("./ephemeris")

def get_lat_lon(place):
    geolocator = Nominatim(user_agent="astro-app")
    location = geolocator.geocode(place)
    return location.latitude, location.longitude

def get_positions(jd):
    sun = swe.calc_ut(jd, swe.SUN)[0]
    moon = swe.calc_ut(jd, swe.MOON)[0]
    return sun[0], moon[0]

def generate_prediction_pdf(name, dob, tob, pob):
    lat, lon = get_lat_lon(pob)
    dt_obj = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    jd = swe.julday(dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour + dt_obj.minute / 60.0)

    sun_deg, moon_deg = get_positions(jd)

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer)
    c.drawString(100, 800, f"Future Prediction Report for {name}")
    c.drawString(100, 780, f"DOB: {dob}, TOB: {tob}, POB: {pob}")
    c.drawString(100, 760, f"Sun Position: {sun_deg:.2f}°")
    c.drawString(100, 740, f"Moon Position: {moon_deg:.2f}°")
    c.drawString(100, 700, f"Prediction: You will face positive transformation in career and relationships.")
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    pdf = generate_prediction_pdf(
        data['name'], data['dob'], data['tob'], data['pob']
    )
    return send_file(pdf, download_name="future_prediction.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
