import requests
import json
import cdsw

model_endpoint = 'MODEL_ENDPOINT'
access_key = "MODEL_ACCESS_KEY"

monthly_charges = 70.00
tenure = 30

if len(sys.argv) > 1:
  monthly_charges = float(sys.argv[1])
  tenure = float(sys.argv[2])

model_input = {"StreamingTV":"No","MonthlyCharges":monthly_charges,"PhoneService":"No","PaperlessBilling":"No","Partner":"No","OnlineBackup":"No","gender":"Female","Contract":"Month-to-month","TotalCharges":1500,"StreamingMovies":"No","DeviceProtection":"No","PaymentMethod":"Bank transfer (automatic)","tenure":tenure,"Dependents":"No","OnlineSecurity":"No","MultipleLines":"No","InternetService":"DSL","SeniorCitizen":"No","TechSupport":"No"}
data = {"accessKey":access_key, "request":model_input}
headers = {'Content-Type': 'application/json'}

r = requests.post(model_endpoint, data=json.dumps(data), headers=headers)
churn_probability = (json.loads(r.json()["response"])["probability"])


cdsw.track_metric("monthly_charges",round(monthly_charges,2))
cdsw.track_metric("tenure",round(tenure,2))
cdsw.track_metric("churn_probability",round(churn_probability,5))