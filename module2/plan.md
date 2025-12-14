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
**Structure:** List  
**Purpose:** Store a chronological record of user activity within the SmartCycle application.

- **Each log entry contains:**
  - User identifier
  - Action performed (e.g., "viewed weekly report", "synced device")
  - Timestamp of the action

**Operations I will demonstrate:**
- Append a new activity log entry
- Display recent user actions in order
- Scan the log to find when a specific action occurred

## 4. Justification Summary

- **Dictionary:**  
  The component inventory uses a dictionary because each component can be uniquely identified by its component ID. This allows for fast lookups, easy updates to quantities, and scalable management as more components are added.

- **Set:**  
  Error codes are stored in a set because only unique error codes are meaningful for diagnostics. Using a set automatically removes duplicates and allows quick checks to determine whether a specific error occurred.

- **List:**  
  User activity logs are stored in a list because order matters. Lists preserve the sequence of events and allow duplicate actions, which is necessary when tracking repeated user behavior over time.
