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
   - Operation point: _________________________________
   - Purpose: _________________________________________
   - Applied to: distance_readings / battery_readings  
   - Example scenario: (e.g., missing Day 3 distance reading)

2. **Update**
   - Operation point: _________________________________
   - Purpose: _________________________________________
   - Applied to: distance_readings / battery_readings  
   - Example scenario: (e.g., incorrect battery % logged)

3. **Delete / Pop**
   - Operation point: _________________________________
   - Purpose: _________________________________________
   - Applied to: distance_readings / battery_readings  
   - Example scenario: (e.g., discard a corrupted final entry)

4. **Search**
   - Operation point: _________________________________
   - Purpose: _________________________________________
   - Applied to: distance_readings / battery_readings  
   - Example scenario: (e.g., check if any day hit 80 miles)

5. **Slice**
   - Operation point: _________________________________
   - Purpose: _________________________________________
   - Applied to: distance_readings / battery_readings  
   - Slice range: (e.g., first 3 days, or weekend)

6. **Concatenate**
   - Operation point: _________________________________
   - Purpose: _________________________________________
   - Arrays combined: _________________________________
   - Example scenario: (e.g., combine battery and distance into one report array)
