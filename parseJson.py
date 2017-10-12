import json
json_data='{"fare":{"breakdown":[{"type":"base_fare","name":"Base Fare","value":363.27}],"value":363.27,"fare_id":"ca47d4c93be77439113fb8ba1932351cfd322d6fbee40a58ce8c0c81af91465e","expires_at":1507791613,"display":"\u20b9363.27","currency_code":"INR"},"trip":{"distance_unit":"mile","duration_estimate":2520,"distance_estimate":15.17},"pickup_estimate":3}'
data = json.loads(json_data)
print(data["fare"]["fare_id"])
