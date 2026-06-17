import os
import pandas as pd
import streamlit as st
import plotly.express as px
import folium
from streamlit_folium import st_folium
from utils import predict_event_plan


st.set_page_config(
    page_title="EventPulse",
    page_icon="🚦",
    layout="wide"
)


@st.cache_data
def load_data():
    path1 = "data/astram_event_data.csv"
    path2 = "data/astram_event_data.csv.csv"

    data_path = path1 if os.path.exists(path1) else path2

    df = pd.read_csv(data_path)

    df["start_datetime"] = pd.to_datetime(
        df["start_datetime"],
        format="mixed",
        errors="coerce"
    )

    df["hour"] = df["start_datetime"].dt.hour.fillna(0).astype(int)
    df["day_of_week"] = df["start_datetime"].dt.day_name().fillna("Monday")

    results = df.apply(
        lambda row: predict_event_plan(
            event_cause=str(row["event_cause"]),
            hour=int(row["hour"]),
            day_of_week=str(row["day_of_week"])
        ),
        axis=1
    )

    df["impact_score"] = results.apply(lambda x: x["impact_score"])
    df["impact_level"] = results.apply(lambda x: x["impact_level"])
    df["recommended_police"] = results.apply(lambda x: x["recommended_police"])
    df["recommended_barricades"] = results.apply(lambda x: x["recommended_barricades"])
    df["post_impact_score"] = results.apply(lambda x: x["post_impact_score"])

    return df


df = load_data()


st.title("🚦 EventPulse")
st.subheader("AI Powered Event Driven Traffic Forecasting")
st.write("Predict congestion and recommend manpower deployment")

st.sidebar.title("🚦 EventPulse")

st.sidebar.markdown("""
### Gridlock Hackathon 2.0

Theme:
Event-Driven Congestion

Built using:

• Streamlit

• FastAPI

• Plotly

• Folium

• Pandas


Prototype Version: 1.0
""")

st.sidebar.title("Event Configuration")

event = st.sidebar.selectbox(
    "Event Type",
    [
        "vehicle_breakdown",
        "accident",
        "construction",
        "water_logging",
        "public_event",
        "vip_movement",
        "protest",
        "procession",
        "tree_fall",
        "congestion",
        "road_conditions",
        "pot_holes",
    ]
)

hour = st.sidebar.slider("Hour", 0, 23, 18)

day = st.sidebar.selectbox(
    "Day",
    [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
)

predict = st.sidebar.button("Predict")


if predict:
    result = predict_event_plan(
        event_cause=event,
        hour=hour,
        day_of_week=day
    )

    st.success("Prediction Generated")

    col1, col2, col3 = st.columns(3)

    col1.metric("Impact Level", result["impact_level"])
    col2.metric("Police Needed", result["recommended_police"])
    col3.metric("Barricades", result["recommended_barricades"])

    st.divider()

    st.subheader("Traffic Impact After Intervention")

    col4, col5, col6 = st.columns(3)

    col4.metric("Impact Score", result["impact_score"])
    col5.metric("Post-Mitigation Score", result["post_impact_score"])
    col6.metric(
        "Mitigation Potential",
        f"{result['estimated_mitigation_potential']}%"
    )

    st.divider()

    st.subheader("Recommended Diversion Plan")

    if result["diversion_required"] == "Yes":
        st.warning("Diversion Required")
    else:
        st.info("No major diversion required")

    for route in result["alternate_routes"]:
        st.markdown(f"✅ {route}")
    report_text = f"""
    EventPulse Traffic Action Report

    Event Cause: {result['event_cause']}
    Day: {result['day']}
    Hour: {result['hour']}:00

    Risk Score: {result['risk_score']}
    Impact Score: {result['impact_score']}
    Impact Level: {result['impact_level']}

    Recommended Police Personnel:
    {result['recommended_police']}

    Recommended Barricades:
    {result['recommended_barricades']}

    Diversion Required:
    {result['diversion_required']}

    Alternate Routes:

    {chr(10).join(result['alternate_routes'])}

    Post-Mitigation Score:
    {result['post_impact_score']}

    Estimated Mitigation Potential:
    {result['estimated_mitigation_potential']}%

"""


    st.download_button(

    label="📥 Download Action Report",

    data=report_text,

    file_name="eventpulse_report.txt",

    mime="text/plain"

    )

st.divider()
st.header("📊 Analytics Dashboard")


colA, colB = st.columns(2)

with colA:
    st.subheader("Event Distribution")

    event_counts = df["event_cause"].value_counts().head(10).reset_index()
    event_counts.columns = ["event_cause", "count"]

    fig1 = px.bar(
        event_counts,
        x="event_cause",
        y="count",
        title="Top Event Causes"
    )

    st.plotly_chart(fig1, use_container_width=True)


with colB:
    st.subheader("Impact Levels")

    impact_counts = df["impact_level"].value_counts().reset_index()
    impact_counts.columns = ["impact_level", "count"]

    fig2 = px.pie(
        impact_counts,
        names="impact_level",
        values="count",
        title="Impact Level Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)


st.subheader("Average Police Requirement by Event")

avg_police = (
    df.groupby("event_cause")["recommended_police"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig3 = px.bar(
    avg_police,
    x="recommended_police",
    y="event_cause",
    orientation="h",
    title="Average Police Deployment Recommendation"
)

st.plotly_chart(fig3, use_container_width=True)
st.divider()
st.header("🗺️ Bengaluru Event Hotspot Map")

map_df = df.dropna(subset=["latitude", "longitude"]).copy()

map_df = map_df.sort_values(
    "impact_score",
    ascending=False
).head(200)

m = folium.Map(
    location=[12.9716, 77.5946],
    zoom_start=11
)

def get_color(level):
    if level == "Critical":
        return "darkred"
    elif level == "High":
        return "red"
    elif level == "Medium":
        return "orange"
    else:
        return "green"

for _, row in map_df.iterrows():

    popup_text = f"""
    Event: {row['event_cause']}<br>
    Impact Level: {row['impact_level']}<br>
    Impact Score: {round(row['impact_score'], 2)}<br>
    Police Needed: {row['recommended_police']}<br>
    Barricades: {row['recommended_barricades']}
    """

    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=6,
        popup=popup_text,
        color=get_color(row["impact_level"]),
        fill=True,
        fill_opacity=0.75
    ).add_to(m)

st_folium(
    m,
    width=1100,
    height=550
)
st.divider()
st.header("🚓 Resource Deployment Summary")

total_police = int(df['recommended_police'].sum())
total_barricades = int(df['recommended_barricades'].sum())

critical_events = len(df[df['impact_level'] == 'Critical'])
high_events = len(df[df['impact_level'] == 'High'])

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Police Required",
        total_police
    )

with c2:
    st.metric(
        "Barricades Required",
        total_barricades
    )

with c3:
    st.metric(
        "Critical Events",
        critical_events
    )

with c4:
    st.metric(
        "High Impact Events",
        high_events
    )
st.subheader("Peak Hour Impact Heatmap")

pivot = df.pivot_table(
    index="day_of_week",
    columns="hour",
    values="impact_score",
    aggfunc="mean"
).fillna(0)

fig4 = px.imshow(
    pivot,
    text_auto=".0f",
    aspect="auto",
    title="Average Impact Score by Day and Hour"
)

st.plotly_chart(fig4, use_container_width=True)

st.divider()
st.header("🔁 Post-Event Learning Insights")

learning_df = (
    df.groupby("event_cause")
    .agg(
        avg_impact_score=("impact_score", "mean"),
        avg_post_mitigation_score=("post_impact_score", "mean"),
        avg_police=("recommended_police", "mean"),
        avg_barricades=("recommended_barricades", "mean"),
        event_count=("event_cause", "count")
    )
    .reset_index()
)

learning_df["learning_gap"] = (
    learning_df["avg_impact_score"]
    - learning_df["avg_post_mitigation_score"]
)

learning_df = learning_df.sort_values(
    "learning_gap",
    ascending=False
)

st.write(
    "This module compares predicted impact with post-mitigation impact to identify which event types benefit most from proactive planning."
)

st.dataframe(
    learning_df.round(2),
    use_container_width=True
)

top_learning_event = learning_df.iloc[0]

st.info(
    f"Highest mitigation opportunity observed for **{top_learning_event['event_cause']}**, "
    f"with an average impact reduction gap of **{round(top_learning_event['learning_gap'], 2)}** points."
)

st.divider()
st.header("📊 Mitigation Effectiveness")

comparison = (
    df.groupby("event_cause")[
        ["impact_score", "post_impact_score"]
    ]
    .mean()
    .reset_index()
)

fig = px.bar(
    comparison,
    x="event_cause",
    y=["impact_score", "post_impact_score"],
    barmode="group",
    title="Impact Before vs After Mitigation"
)

st.plotly_chart(
    fig,
    use_container_width=True
)