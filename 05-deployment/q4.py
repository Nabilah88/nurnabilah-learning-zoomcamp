import json
import urllib.request

lead = {
    "lead_source": "organic_search",
    "industry": "technology",
    "employment_status": "employed",
    "location": "europe",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0,
    "interaction_count": 7,
    "lead_score": 0.74,
}

request = urllib.request.Request(
    "http://localhost:9696/predict",
    data=json.dumps(lead).encode("utf-8"),
    headers={"Content-Type": "application/json"},
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read())

print(result)
print(round(result["conversion_probability"], 3))