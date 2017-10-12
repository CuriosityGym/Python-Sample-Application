import json
json_data='{"status":"processing","product_id":"83941b0d-4be1-4979-a9c0-f0af5ee2b89b","destination":{"latitude":19.0822507,"longitude":72.8811862},"driver":null,"pickup":{"latitude":18.936404,"region":{"latitude":19.054377,"country_name":"India","country_code":"IN","name":"Mumbai","longitude":72.847026},"eta":14,"longitude":72.832546},"request_id":"c273a584-4b72-4f22-a62c-b530da17f8ae","location":null,"vehicle":null,"shared":false}'
data = json.loads(json_data)
print(data["status"])
