from api.utils import predict_event_plan

result = predict_event_plan(

event_cause="vip_movement",

hour=21,

day_of_week="Friday"

)

print(result)