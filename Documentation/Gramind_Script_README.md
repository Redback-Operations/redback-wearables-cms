
# Garmin Connect Data Extraction Script

This Python script interacts with the Garmin Connect API to fetch and process data from a Garmin account. It requires the `garminconnect` library for API interactions. The script performs the following tasks:

1. **Login to Garmin Connect:**
   - Prompts the user for their email address and password.
   - Logs in to the Garmin Connect account using the provided credentials.

2. **Fetch Activity Data:**
   - Retrieves the last recorded activity's details.
   - Fetches the maximum metrics for the previous day.
   - Extracts and computes specific metrics such as VO2 Max, distance, training effect, and activity duration.

3. **Save and Display Data:**
   - Saves the Garmin Connect session data to a specified directory.
   - Prints personal records and the number of records retrieved.

## Dependencies

- `garminconnect`: A Python library for interacting with the Garmin Connect API.
- `getpass`: Used for securely inputting credentials.
- `os`: Provides a way of using operating system-dependent functionality.
- `datetime`: Used for manipulating dates and times.

## Script Details

### 1. Import Libraries
```python
import garminconnect
from getpass import getpass
import os
from datetime import date, timedelta
```

### 2. User Authentication
```python
email = getpass("Enter email address: ")
password = getpass("Enter Password: ")
```
- Prompts the user to input their Garmin Connect email and password securely.

### 3. Initialize Garmin Connect Object
```python
garmin = garminconnect.Garmin(email, password)
garmin.login()
```
- Creates an instance of the `Garmin` class and logs in with the provided credentials.

### 4. Save Session Data
```python
GARTH_HOME = os.getenv("GARTH_HOME", "~/.garth")
garmin.garth.dump(GARTH_HOME)
```
- Saves the Garmin Connect session data to a specified directory, defaulting to `~/.garth`.

### 5. Fetch and Process Activity Data
```python
today = date.today() - timedelta(days=1)
today = today.isoformat()

lastrun = garmin.get_last_activity()['splitSummaries'][0]
stats = garmin.get_max_metrics(today)

vo2max = stats[0]['generic']['vo2MaxPreciseValue']
miles = round(lastrun['distance']/1609.34, 2)
effect = garmin.get_last_activity()['trainingEffectLabel']
duration = round(garmin.get_last_activity()['duration'], 2)
```
- Sets the date for the previous day.
- Retrieves details of the last recorded activity and maximum metrics for the previous day.
- Calculates VO2 Max, converts distance from meters to miles, fetches the training effect, and calculates the activity duration.

### 6. Print Personal Records
```python
records = garmin.get_personal_record()
print(records)
print(len(records))
```
- Retrieves and prints personal records from the Garmin Connect account.
- Prints the number of personal records retrieved.

## Notes

- Ensure you have the `garminconnect` library installed and properly configured.
- Replace `GARTH_HOME` with the desired path to save session data if different from the default.
- Handle any exceptions or errors that may occur during API interactions, such as authentication failures or network issues.

