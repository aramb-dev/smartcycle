# Module 2 – Plan (Data Structures)

## 1. Dictionary: Component Inventory
**Structure:** dict  
**Purpose:** Store SmartCycle components so the program can quickly look up a part and update its quantity.

- **Key:** ____________________ (choose: component ID or part name)
- **Value:** __________________ (choose: quantity only OR a small record like {name, quantity})
- **Example operations I will demonstrate:**
  - Look up a component by key
  - Update quantity after a replacement
  - Add a new component entry

## 2. Set: Error Codes
**Structure:** set  
**Purpose:** Store unique error codes detected during rides (no duplicates).

- **Error code format:** ____________________ (e.g., "E101", "E203")
- **Example operations I will demonstrate:**
  - Add error codes from multiple ride logs
  - Show that duplicates are automatically removed
  - Check if a specific error code occurred

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
