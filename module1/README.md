# Module 1 – Weekly Data Arrays & Basic Analytics

SmartCycle Data Console – **Module 1** focuses on processing one week of SmartCycle ride data using basic Python arrays (lists). You will design how the data is stored, manipulated, and displayed, including a simple text-based “graph.”

> **Important:** This module is about *designing and demonstrating* array operations and basic analysis. Keep the scenario realistic but simple.


## 1. Learning Objectives

By the end of this module, you should be able to:

* Represent weekly SmartCycle data using Python lists (arrays).
* Perform basic list operations:

  * Insert, update, delete (pop), search, slice, and concatenate.
* Compute:

  * Total weekly distance travelled.
  * Average battery output for the week.
* Display results in a clear textual format, including a simple ASCII bar graph.



## 2. Scenario Overview

SmartCycle logs ride data for each day of a 7-day week. For this prototype, you will work with:

* **Battery output** per day (7 values)
* **Distance travelled** per day (7 values)

You will design:

* How the data is stored in arrays.
* How to fix or adjust data (e.g., incorrect or missing readings).
* How to present a **summary report** for the week.



## 3. Data Model (Design, Not Code)

You must decide:

1. **What each element represents**

   * `battery_readings`: one numeric value per day (e.g., average battery percentage used or average voltage).
   * `distance_readings`: one numeric value per day (e.g., kilometers or miles ridden).

2. **Assumptions**

   * Units (km vs miles, % vs Wh, etc.).
   * Reasonable ranges (e.g., 0–100 for battery %, 0–50 km per day).

Document your choices in `PLAN.md`:

* What arrays you will use.
* What each element means.
* Example sample values for at least 2 days.



## 4. Required Array Operations

You need to **demonstrate** the following operations at least once somewhere in your script:

1. **Insert**

   * Add a missing reading at a specific position (e.g., forgot to log Day 3 distance).

2. **Update**

   * Correct an incorrect value (e.g., change a wrong battery reading).

3. **Delete / Pop**

   * Remove the last entry, or a specific entry, to simulate discarding bad data.

4. **Search**

   * Check if a given battery or distance value exists in the week’s data (or find its position).

5. **Slice**

   * Extract a portion of the week (e.g., first 3 days, weekend only).

6. **Concatenate**

   * Join two lists (e.g., combine battery and distance readings, or combine two weeks of distance data).

In `PLAN.md`, list **exactly where** in the script each operation will appear (e.g., “After initial setup, I will update Day 2 battery reading,” “Before final stats, I’ll slice the weekdays,” etc.).



## 5. Required Calculations

Your script must calculate and display:

1. **Total Weekly Distance**

   * Sum of all 7 daily distance values.

2. **Average Battery Output**

   * Mean of all 7 daily battery readings.

Document in `PLAN.md`:

* Which variables will hold these results (names only, no code).
* Where in the program flow you will perform these calculations (before or after adjustments?).



## 6. ASCII Bar Graph Design

You must design a simple text-based graph to visualize at least one of the arrays (distance or battery).

Examples (concept, not code):

* `Day 1: ######`
* `Day 2: ##########`
* `Day 3: ###`

Decide and document:

* What **one bar unit** (`#` or `*`) represents:

  * e.g., `1 # = 5 km` or `1 # = 10% battery`.
* How you will label each line:

  * `Day 1`, `Mon`, or something else.
* Whether you will graph:

  * Distance, battery, or both (start with one to keep it simple).

Write this clearly in `PLAN.md` under “ASCII Graph Design.”



## 7. Suggested File Structure

Inside `/module1`:

* `README.md` – this file (module overview).
* `PLAN.md` – your detailed design and planning:

  * Data model
  * Array operations locations
  * Calculation plan
  * ASCII graph design
* `smartcycle_module1.py` – your actual Python implementation (code – written by you).
* `OUTPUT_SAMPLE.md` – example of the program’s output copied from a real run.



## 8. Implementation Steps (High-Level)

When you are ready to code later, follow these phases:

1. **Phase 1 – Data Setup**

   * Create and initialize the weekly arrays.
   * Print the raw data for verification.

2. **Phase 2 – Corrections & Operations**

   * Perform insert, update, delete, search, slice, and concatenate operations as planned.
   * Print the data after each key change (or at least after all changes).

3. **Phase 3 – Analysis**

   * Compute total distance and average battery output.
   * Print a short text summary of the results.

4. **Phase 4 – ASCII Graph**

   * Print the bar graph for the chosen metric (distance or battery).
   * Ensure the scaling is clear and consistent.

5. **Phase 5 – Final Output Capture**

   * Run the full program.
   * Copy the terminal output into `OUTPUT_SAMPLE.md`.



## 9. Testing & Validation Checklist

Before considering Module 1 “done,” verify:

* [ ] Arrays include 7 values to represent each day’s data.
* [ ] Insert, update, and delete are clearly demonstrated.
* [ ] Search, slice, and concatenate are clearly demonstrated.
* [ ] Total weekly distance is shown and makes sense with the chosen values.
* [ ] Average battery output is shown and makes sense.
* [ ] ASCII bar graph is readable, labeled, and scaled.
* [ ] `PLAN.md` matches what actually happens in `smartcycle_module1.py`.
* [ ] `OUTPUT_SAMPLE.md` includes one complete run of the program.



## 10. Reflection (for yourself or your report)

Answer these questions briefly in `PLAN.md` or a separate section:

1. Which array operation felt most natural or useful for this problem?
2. Which part of the design did you change after seeing the output the first time?
3. How could this small prototype grow into a real SmartCycle analytics dashboard?

