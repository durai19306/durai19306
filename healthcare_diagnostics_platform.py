
# healthcare_diagnostics_platform.py
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Dummy knowledge base (can be replaced by ML model)
symptom_diagnosis_map = {
    "fever": ("Common Cold or Flu", "Stay hydrated, rest, and take paracetamol if needed."),
    "headache": ("Migraine or Stress", "Rest in a quiet room, take pain relievers, manage stress."),
    "cough": ("Bronchitis or Common Cold", "Warm fluids, cough syrup, consult doctor if persistent."),
    "chest pain": ("Consult Immediately", "This could be serious. Seek immediate medical help."),
}

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Diagnosis API route
@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.get_json()
    symptoms = data.get('symptoms', [])
    diagnosis_result = []

    for symptom in symptoms:
        diag = symptom_diagnosis_map.get(symptom.lower(), ("Unknown", "Please consult a healthcare provider."))
        diagnosis_result.append({
            "symptom": symptom,
            "diagnosis": diag[0],
            "treatment": diag[1]
        })

    return jsonify({"results": diagnosis_result})

# Run server
if __name__ == '__main__':
    app.run(debug=True)
