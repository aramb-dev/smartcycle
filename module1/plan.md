# Module 1 – Plan

## 1. Data Model

- **Distance readings (`distance_readings`)**
  - Unit: miles
  - One element = total distance ridden in one day.
  - Typical daily value: around 29.2 miles.
  - Expected range: from about 20 miles to about 80 miles.

- **Battery readings (`battery_readings`)**
  - Unit: percent (%)
  - One element = average battery used (or remaining – specify) for one day.
  - Expected range: **40%–60%** per day.
  - I will treat values below 10% or above 90% as suspicious or “bad data.”

- **Week structure**
  - Exactly **7 elements** in each list, one per day (Day 1–Day 7).
  - Day labels I will use in output: `D#` (e.g., Day 1–Day 7 or Mon–Sun).

## 2. Required Array Operations (Design)

I will demonstrate the following operations in my script.  
Below I describe **where** each operation occurs in the program and **why** I use it.

1. **Insert**
   - Operation point: After initializing the weekly distance data.
   - Purpose: To correct missing ride data for one day.
   - Applied to: `distance_readings`
   - Scenario: The distance for Day 4 was not recorded due to a logging issue, so the correct value is inserted at the appropriate position in the list.

2. **Update**
   - Operation point: After all distance data has been verified and inserted.
   - Purpose: To correct an incorrect battery percentage reading.
   - Applied to: `battery_readings`
   - Scenario: A battery reading was logged outside the expected 40–60% range, so the value is updated to the correct percentage for that day.

3. **Delete / Pop**
   - Operation point: After reviewing all battery readings.
   - Purpose: To remove a corrupted or incomplete battery entry.
   - Applied to: `battery_readings`
   - Scenario: The final day’s battery data was corrupted due to an unexpected device shutdown, so the last battery reading is removed from the list.

4. **Search**
   - Operation point: After all distance corrections have been completed.
   - Purpose: To determine whether any day exceeded a high-distance threshold.
   - Applied to: `distance_readings`
   - Scenario: The program checks if any daily distance is greater than 60 miles to identify unusually long rides.

5. **Slice**
   - Operation point: After validating the full week of distance data.
   - Purpose: To analyze riding patterns toward the end of the week.
   - Applied to: `distance_readings`
   - Slice range: Day 5 through Day 7.
   - Scenario: The program extracts the last three days of distance data to examine end-of-week riding behavior.

6. **Concatenate**
   - Operation point: After both arrays have been cleaned (insert/update/pop complete).
   - Purpose: To build a combined weekly dataset for reporting.
   - Arrays combined: `distance_readings` + `battery_readings`
   - Scenario: The program combines both arrays into one list so the week’s ride data can be output or processed as a single dataset.


## 3. Required Calculations

1. **Total Weekly Distance**
   - Calculated after distance corrections are complete.
   - Uses: all 7 daily distance values.
   - Output: a single total in miles.

2. **Average Battery Percentage**
   - Calculated after battery corrections are complete.
   - Uses: the cleaned battery list values.
   - Output: a single average percentage for the week.

## 4. ASCII Bar Graph Design

- Metric visualized: **Daily distance travelled**
- Scale: **1 `#` = 5 miles**
- Maximum expected bars:
  - 80 miles = 16 `#` characters
- Format per line:
  - `Day X: ####...`
- Purpose:
  - To provide a simple, readable visual comparison of daily riding distances across the week.
