# Module 1 – Plan

## 1. Data Model

- **Distance readings (`distance_readings`)**
  - Unit: miles
  - One element = total distance ridden in one day.
  - Typical daily value: around 29.2 miles.
  - Expected range: from about ____ miles to about ____ miles.

- **Battery readings (`battery_readings`)**
  - Unit: percent (%)
  - One element = average battery used (or remaining – specify) for one day.
  - Expected range: **40%–60%** per day.
  - I will treat values below 10% or above 90% as suspicious or “bad data.”

- **Week structure**
  - Exactly **7 elements** in each list, one per day (Day 1–Day 7).
  - Day labels I will use in output: `D#` (e.g., Day 1–Day 7 or Mon–Sun).
