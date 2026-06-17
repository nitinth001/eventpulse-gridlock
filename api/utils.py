# utils.py

severity_map = {
    'vip_movement': 5,
    'protest': 5,
    'public_event': 4,
    'procession': 4,
    'construction': 3,
    'accident': 4,
    'tree_fall': 4,
    'water_logging': 3,
    'vehicle_breakdown': 2,
    'congestion': 3,
    'road_conditions': 2,
    'pot_holes': 1,
    'others': 2,
    'debris': 2,
    'Debris': 2,
    'Fog / Low Visibility': 1,
}

closure_prob = {
    'debris': 100,
    'vip_movement': 80,
    'public_event': 46,
    'protest': 40,
    'tree_fall': 39,
    'construction': 26,
    'procession': 26,
    'road_conditions': 12,
    'water_logging': 8,
    'vehicle_breakdown': 4,
    'accident': 3,
    'pot_holes': 2,
    'others': 8,
    'congestion': 4,
    'Debris': 8,
    'Fog / Low Visibility': 0,
}

road_suggestions = {
    'vip_movement': [
        'Outer Ring Road',
        'Hebbal Flyover',
        'Airport Service Road'
    ],
    'public_event': [
        'MG Road',
        'Cubbon Road',
        'Residency Road'
    ],
    'protest': [
        'Outer Ring Road',
        'Bellary Road',
        'Hebbal Service Road'
    ],
    'construction': [
        'ORR Service Road',
        'NICE Road'
    ],
    'tree_fall': [
        'Nearest Parallel Street'
    ],
    'accident': [
        'Flyover Alternate Route'
    ],
    'water_logging': [
        'Elevated Corridor'
    ],
    'procession': [
        'Parallel Arterial Road',
        'Service Road Diversion'
    ],
    'congestion': [
        'Nearest Parallel Corridor'
    ],
}


def suggest_route(event_cause):
    return road_suggestions.get(event_cause, ['No diversion needed'])


def predict_event_plan(event_cause, hour, day_of_week):
    event_cause = event_cause.strip()

    severity = severity_map.get(event_cause, 1)
    closure = closure_prob.get(event_cause, 0)

    peak = 1 if hour in [5, 6, 19, 20, 21, 22] else 0
    risky_day = 1 if day_of_week in ['Thursday', 'Friday', 'Tuesday', 'Saturday'] else 0

    risk_score = (
        severity * 10
        + closure * 0.5
        + peak * 15
        + risky_day * 10
    )

    risk_score = min(100, max(0, risk_score))

    police = int(round(severity * 2 + closure * 0.3))
    police = max(police, 2)

    barricades = int(round(closure / 5))

    diversion_required = 1 if risk_score >= 60 else 0

    impact_score = (
        risk_score * 0.5
        + police * 1.5
        + barricades * 2
    )

    impact_score = min(100, impact_score)

    if impact_score < 20:
        impact_level = "Low"
    elif impact_score < 40:
        impact_level = "Medium"
    elif impact_score < 60:
        impact_level = "High"
    else:
        impact_level = "Critical"

    routes = suggest_route(event_cause)

    reduction_score = (
        police * 0.6
        + barricades * 1.2
        + (12 if diversion_required == 1 else 0)
    )

    reduction_score = min(reduction_score, 50)

    post_impact_score = max(0, impact_score - reduction_score)

    mitigation_percent = (
        round((reduction_score / impact_score) * 100, 2)
        if impact_score > 0 else 0
    )

    return {
        "event_cause": event_cause,
        "hour": hour,
        "day": day_of_week,
        "risk_score": round(risk_score, 2),
        "impact_score": round(impact_score, 2),
        "impact_level": impact_level,
        "recommended_police": police,
        "recommended_barricades": barricades,
        "diversion_required": "Yes" if diversion_required else "No",
        "alternate_routes": routes,
        "post_impact_score": round(post_impact_score, 2),
        "estimated_mitigation_potential": mitigation_percent
    }