# Module 2 – Plan (Data Structures)

## 1. Dictionary: Component Inventory
**Structure:** Dictionary (dict)  
**Purpose:** Store SmartCycle components so the system can quickly look up parts and update quantities.

- **Key:** Component ID (e.g., "BAT001", "SEN102")
- **Value:** A small record containing:
  - Component name
  - Quantity available

**Operations I will demonstrate:**
- Look up a component using its ID
- Update the quantity after a component replacement
- Add a new component to the inventory

## 2. Set: Error Codes
**Structure:** Set  
**Purpose:** Store unique error codes detected during SmartCycle rides.

- **Error code format:** Numeric-style strings (e.g., "E101", "E202", "E305")

**Operations I will demonstrate:**
- Add multiple error codes from ride logs
- Automatically remove duplicate error codes
- Check whether a specific error code occurred during the week

## 3. List: User Activity Logs
**Structure:** list  
**Purpose:** Store a chronological record of user actions in the app.

- **Each log entry contains:** ____________________ (e.g., user, action, timestamp)
- **Example operations I will demonstrate:**
  - Append a new log entry
  - Display the most recent actions
  - Filter or scan for a particular action

## 4. Justification Summary
Explain why each structure is the best fit:

- **Dictionary:** fast lookup + easy updates by key
- **Set:** uniqueness + fast membership tests
- **List:** preserves order + supports duplicates + natural for logs
