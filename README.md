#  EventPulse
### AI Powered Event-Driven Traffic Forecasting and Resource Optimization System



# 📌 Problem Statement

Urban events such as political rallies, VIP movements, protests, construction activities, and public gatherings frequently cause localized traffic disruptions.

Current traffic management systems rely heavily on manual planning and experience-driven decisions.

EventPulse aims to provide an AI-assisted decision support system capable of:

✔ Forecasting traffic impact

✔ Recommending optimal police deployment

✔ Suggesting barricade allocation

✔ Generating diversion plans

✔ Simulating mitigation effectiveness

✔ Learning from historical events


---

# 🌐 Live Deployment

### Frontend Dashboard

https://eventpulse-gridlock-nfsuqwmfsc8nshpqvnu5mk.streamlit.app/


### Backend API

https://eventpulse-gridlock.onrender.com/


### Swagger Documentation

https://eventpulse-gridlock.onrender.com/docs


---

# 📊 Dataset Overview

Dataset Source

ASTraM Bengaluru Event Dataset


Dataset Statistics


• Total Events : 8173

• Event Categories : 16

• Geographic Coverage : Bengaluru

• Temporal Coverage : Multiple years


Major Event Categories


Vehicle Breakdown

Construction

Accident

VIP Movement

Public Event

Water Logging

Procession

Tree Fall

Protest

Road Conditions

Congestion

Pot Holes



---

# 🔍 Exploratory Data Analysis

Insights extracted from historical event records


### Peak Hour Analysis

Identified time periods with maximum event frequency


### Road Closure Probabilities


VIP Movement → 80%

Public Event → 46%

Construction → 26%

Procession → 26%



### Day Wise Analysis


Pot holes peak on Saturdays

Accidents peak on Tuesdays

Construction remains consistent across weekdays



---

# 🧠 Risk Scoring Engine

Traffic risk is estimated using a rule-based scoring mechanism.


Factors considered


Event Severity

Peak Hour Indicator

Road Closure Requirement

Historical Frequency

Day Impact


Risk Categories


Low

Medium

High

Critical


---

# 🚓 Resource Allocation Engine


EventPulse recommends resources dynamically.


Outputs


Recommended Police Personnel

Recommended Barricades

Traffic Diversion Requirement



Examples


VIP Movement

34 officers

16 barricades


Public Event

22 officers

12 barricades


Tree Fall

20 officers

10 barricades


Vehicle Breakdown

5 officers

2 barricades



---

# 🛣 Diversion Planning


Alternative routes are suggested for high impact events.


Examples


Outer Ring Road


Hebbal Flyover


Airport Service Road


NICE Road


ORR Service Road



---

# 📉 Mitigation Simulator


Measures expected congestion reduction after interventions.


Metrics


Impact Score


Post Mitigation Score


Mitigation Potential


Examples


VIP Movement

50% reduction


Tree Fall

55% reduction


Public Event

43% reduction



---

# 📚 Learning Insights


A post-event learning module identifies event categories that benefit most from proactive planning.


Metrics


Average Impact Score


Average Police Requirement


Average Barricades


Learning Gap



Observation


VIP Movement exhibits the highest mitigation opportunity.



---

# 🗺 Interactive Dashboard


Dashboard Features


✔ Event Prediction


✔ Resource Recommendations


✔ Diversion Plans


✔ Peak Hour Heatmaps


✔ Event Hotspot Maps


✔ Learning Insights


✔ Mitigation Effectiveness Analysis


✔ Downloadable Action Reports



---

# ⚙ Technology Stack


Frontend


Streamlit


Plotly


Folium



Backend


FastAPI


Uvicorn



Data Processing


Pandas


NumPy


Scikit-Learn



Deployment


Render


Streamlit Community Cloud



---

# 🏗 System Architecture


Dataset

↓

EDA

↓

Feature Engineering

↓

Risk Engine

↓

Impact Estimation

↓

Resource Allocation

↓

Diversion Planning

↓

Mitigation Simulator

↓

Learning Module

↓

FastAPI Backend

↓

Streamlit Dashboard



---



#  Local Setup:


Clone Repository


```bash
git clone https://github.com/nitinth001/eventpulse-gridlock.git
```


Install Dependencies


```bash
pip install -r requirements.txt
```


Run Frontend


```bash
streamlit run api/app.py
```


Run Backend


```bash
uvicorn api.main:app --reload
```


---

# 🔮 Future Improvements


Real-time CCTV Integration


Weather Forecast Integration


Google Maps API


Adaptive Signal Timing


Reinforcement Learning Based Diversion Optimization


Emergency Vehicle Routing



---

# 👨‍💻 Author

## Nitin Thakur

Mathematics and Computing

Gridlock Hackathon 2.0 Submission


---

### Overall Project Status

✅ End-to-End Prototype Built

✅ Frontend Deployed

✅ Backend Deployed

✅ Interactive Dashboard

✅ Resource Recommendation Engine

✅ Event Learning Module

✅ Submission Ready
