# 🚦 EventPulse

### AI-Powered Event-Driven Traffic Forecasting & Resource Optimization

**Version:** v1.2 (Gridlock Hackathon 2.0 Final Submission)

---

# 📌 Problem Statement

Urban events such as political rallies, VIP movements, protests, construction activities, public gatherings, accidents, and waterlogging frequently cause localized traffic disruptions.

Current traffic management systems rely heavily on manual planning and experience-driven decisions, making it difficult to estimate event impact, optimize resource deployment, and learn from previous incidents.

EventPulse is an AI-assisted traffic intelligence platform designed to:

✔ Forecast traffic impact

✔ Recommend optimal police deployment

✔ Suggest barricade allocation

✔ Generate diversion plans

✔ Simulate mitigation effectiveness

✔ Learn from historical events

✔ Provide operational awareness through live incident monitoring

---

# 🌐 Live Deployment

## Frontend Dashboard

https://eventpulse-gridlock-nfsuqwmfsc8nshpqvnu5mk.streamlit.app/

---

## Backend API

https://eventpulse-gridlock.onrender.com/

---

## Swagger Documentation

https://eventpulse-gridlock.onrender.com/docs/

---

# 📊 Dataset Overview

### Dataset Source

ASTraM Bengaluru Event Dataset

### Dataset Statistics

• Total Events : **8173**

• Event Categories : **16**

• Geographic Coverage : **Bengaluru**

• Temporal Coverage : **Multiple Years**

---

### Major Event Categories

* Vehicle Breakdown
* Construction
* Accident
* VIP Movement
* Public Event
* Water Logging
* Procession
* Tree Fall
* Protest
* Road Conditions
* Congestion
* Pot Holes

---

# 🔍 Exploratory Data Analysis

EventPulse performs extensive historical event analysis to identify traffic patterns and congestion trends.

### Peak Hour Analysis

Identifies time periods with maximum event frequency.

---

### Road Closure Probabilities

VIP Movement → **80%**

Public Event → **46%**

Construction → **26%**

Procession → **26%**

---

### Day-wise Analysis

• Pot holes peak on Saturdays

• Accidents peak on Tuesdays

• Construction remains consistent across weekdays

---

# 🧠 Risk Scoring Engine

Traffic risk is estimated using a rule-based scoring mechanism.

### Factors Considered

* Event Severity
* Peak Hour Indicator
* Road Closure Requirement
* Historical Frequency
* Day Impact

---

### Risk Categories

• Low

• Medium

• High

• Critical

---

# 🚓 Resource Allocation Engine

EventPulse dynamically recommends resources based on estimated event impact.

### Outputs

✔ Recommended Police Personnel

✔ Recommended Barricades

✔ Traffic Diversion Requirement

---

### Examples

VIP Movement

34 officers

16 barricades

---

Public Event

22 officers

12 barricades

---

Tree Fall

20 officers

10 barricades

---

Vehicle Breakdown

5 officers

2 barricades

---

# 🛣 Diversion Planning

Alternative routes are suggested for high impact events.

### Examples

* Outer Ring Road
* Hebbal Flyover
* Airport Service Road
* NICE Road
* ORR Service Road

---

# 📉 Mitigation Simulator

Measures expected congestion reduction after interventions.

### Metrics

Impact Score

Post Mitigation Score

Mitigation Potential

---

### Examples

VIP Movement

50% reduction

---

Tree Fall

55% reduction

---

Public Event

43% reduction

---

# 📚 Post-Event Learning Insights

A learning module identifies event categories that benefit most from proactive interventions.

### Metrics

✔ Average Impact Score

✔ Average Police Requirement

✔ Average Barricades

✔ Learning Gap

---

### Observation

VIP Movement exhibits the highest mitigation opportunity.

---

# 🗺 Interactive Dashboard

### Dashboard Features

✔ Event Prediction

✔ Police & Barricade Recommendations

✔ Diversion Route Planning

✔ Peak Hour Heatmaps

✔ Bengaluru Event Hotspot Mapping

✔ Event Timeline Across the Day

✔ Post-Event Learning Insights

✔ Mitigation Effectiveness Simulator

✔ Simulated Live Incident Feed

✔ Downloadable Action Reports

✔ Interactive Analytics Dashboard

---

# 📈 Prototype Highlights

✔ 8173 Traffic Events Processed

✔ 16 Event Categories

✔ 34 Maximum Police Personnel Recommended

✔ 16 Maximum Barricades Suggested

✔ 50% Congestion Reduction Simulated

✔ Fully Deployed Cloud Prototype

✔ Interactive Operational Dashboard

---

# ⚙ Technology Stack

## Frontend

* Streamlit
* Plotly
* Folium

---

## Backend

* FastAPI
* Uvicorn

---

## Data Processing

* Pandas
* NumPy

---

## Testing

* Pytest

---

## Deployment

* Render
* Streamlit Community Cloud

---

# 🏗 System Architecture

Dataset (ASTraM)

↓

Exploratory Data Analysis

↓

Feature Engineering

↓

Risk Scoring Engine

↓

Impact Estimation

↓

Resource Allocation Engine

↓

Diversion Planning

↓

Mitigation Simulator

↓

Post Event Learning Module

↓

FastAPI Backend

↓

Streamlit Interactive Dashboard

↓

Cloud Deployment

---

# ⚙ Local Setup

### Clone Repository

```bash
git clone https://github.com/nitinth001/eventpulse-gridlock.git
cd eventpulse-gridlock
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start FastAPI Backend

```bash
uvicorn api.main:app --reload
```

Backend URL

```text
http://localhost:8000
```

Swagger Docs

```text
http://localhost:8000/docs
```

---

### Start Streamlit Frontend

```bash
streamlit run api/app.py
```

Frontend URL

```text
http://localhost:8501
```

---

# 🔮 Future Improvements

* Real-time CCTV Integration

* Weather Forecast Integration

* Google Maps API Integration

* Adaptive Signal Timing

* Reinforcement Learning Based Diversion Optimization

* Emergency Vehicle Routing

---

# 👨‍💻 Author

### Nitin Thakur

NIT HAMIRPUR

BRANCH : Mathematics and Computing

Gridlock Hackathon 2.0 Submission

---

# ✅ Project Status

✔ End-to-End Prototype Built

✔ Streamlit Dashboard Deployed

✔ FastAPI Backend Deployed

✔ Risk Scoring Engine

✔ Resource Allocation Engine

✔ Diversion Planning Module

✔ Mitigation Simulator

✔ Learning Insights Module

✔ Simulated Incident Feed

✔ Downloadable Reports

✔ Interactive Visual Analytics

✔ Submission Ready
