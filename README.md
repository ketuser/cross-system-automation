
# Description

This project simulates a real-world automation task:  
Checking request records from one system (CSV) against another system (JSON)  
and updating the second system with missing entries.

The goal is to reduce manual work and ensure data consistency across platforms.

## Cross-System Request Sync Automation 

This Python script automates the syncing of request data between two systems.


### How it works

- Reads requests from a CSV file (System A).
- Checks if each request already exists in a JSON file (System B).
- Adds missing requests to System B automatically.

### Files

- `system_a.csv`: Source data (CSV).
- `system_b.json`: Target system data (JSON).
- `main.py`: Python script to compare and sync.

### How to run

```bash
python3 main.py


---

### 💡 Example

If `system_a.csv` contains:

REQ001,Create new user John
REQ002,Update email for Mary
REQ003,Delete account for Bob

And `system_b.json` only has REQ001,  
the script will detect and add REQ002 and REQ003.

---

Created by Anatoly Lunev