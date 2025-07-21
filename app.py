from flask import Flask, request, send_file, make_response
from fpdf import FPDF
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route("/")
def home():
    return "Future Prediction API is live!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    name = data.get("name")
    dob = data.get("dob")
    time = data.get("time")
    place = data.get("place")

    # Dummy prediction logic
    prediction = f"Dear {name}, based on your birth date ({dob}), time ({time}), and place ({place}), you have a bright future ahead!"

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, prediction)

    pdf_stream = io.BytesIO()
    pdf.output(pdf_stream)
    pdf_stream.seek(0)

    response = make_response(send_file(pdf_stream, download_name="future_prediction.pdf", as_attachment=True))
    response.headers["Content-Type"] = "application/pdf"
    return response

if __name__ == "__main__":
    app.run(debug=True)

