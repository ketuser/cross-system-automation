import csv
import json

# Load requests from CSV (System A)
with open('system_a.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    system_a_requests = list(reader)

print("✅ Loaded requests from System A:")
print(system_a_requests)

# Load existing requests from JSON (System B)
with open('system_b.json', 'r') as jsonfile:
    system_b_requests = json.load(jsonfile)

print("✅ Loaded requests from System B:")
print(system_b_requests)

# Extract request_ids from System B
existing_ids = {req['request_id'] for req in system_b_requests}
print("🔍 Existing IDs in System B:", existing_ids)

# Find and add new requests
new_requests = []
for req in system_a_requests:
    if req['request_id'] not in existing_ids:
        print("🆕 New request found:", req)
        new_requests.append(req)

system_b_requests.extend(new_requests)

# Save back to JSON
with open('system_b.json', 'w') as jsonfile:
    json.dump(system_b_requests, jsonfile, indent=4)

print(f"✅ Added {len(new_requests)} new request(s) to System B.")
