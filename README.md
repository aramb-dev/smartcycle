# SmartCycle Data Console – Project Roadmap

> Capstone project for “SmartCycle Data Console (SDC)” – a mini-software prototype to monitor data, troubleshoot devices, collaborate with a team, and address IP & privacy. 

---

## Overall Repo Structure (Suggested)

* `/README.md` – main overview + this roadmap
* `/module1/` – arrays & weekly data processing
* `/module2/` – data structures & justification
* `/module3/` – troubleshooting report & flowchart
* `/module4/` – collaboration evidence & notes
* `/module5/` – IP & innovation strategy
* `/module6/` – data privacy & ethics blueprint

You can adjust folder names, but keep it clear which files belong to which module.

---

## Module 1 – Data Acquisition & Array Processing (Python)

**Goal:** Handle weekly SmartCycle data with arrays, basic operations, stats, and a simple ASCII “graph.” 

### What you need to design

* A simple data model for:

  * Battery output readings for 7 days
  * Distance travelled per day for 7 days
* A plan for how the user will see:

  * Total weekly distance
  * Average battery output
  * An ASCII “bar graph” per day

### Implementation plan (no code)

* Decide how you’ll **store**:

  * 7 battery readings in an array
  * 7 distance values in another array
* Plan concrete examples of the following operations:

  * Insert a missing reading
  * Update an incorrect value
  * Remove (pop) the last entry
  * Search for a given value
  * Slice the first 3 days
  * Concatenate both arrays into a single weekly dataset
* Decide **where in your script** each operation will happen (e.g., “data setup”, “data cleaning”, “analysis”, “output”).
* Design the **output format**:

  * How you’ll print total weekly distance
  * How you’ll print average battery output
  * How each ASCII bar will look:

    * e.g. `Day 1: ######` (define what one `#` means: a fixed number of km or a scaled ratio)

### Files / artifacts to create

* `module1/PLAN.md` – short description of:

  * What arrays you’ll use
  * List of operations you’ll demonstrate
  * Example of how one ASCII line will look
* `module1/smartcycle_module1.py` – your actual code (you will write later)
* `module1/OUTPUT_SAMPLE.md` – copy/paste a sample run once you’ve tested it

---

## Module 2 – Choosing the Right Data Structure

**Goal:** Choose appropriate data structures (dictionary, set, list) for different SmartCycle information and explain why. 

### What you need to model

* Component inventory: part name, quantity, ID
* Error codes detected during rides
* Authorized users & app activity

### Implementation plan (no code)

* Plan a **dictionary** for components:

  * Decide the key (e.g., component ID)
  * Decide the value structure (e.g., name + quantity + notes)
* Plan a **set** for error codes:

  * Decide how error codes look (strings? numbers? “E101”?)
  * Show how uniqueness matters (e.g., many logs, but only unique codes kept)
* Plan a **list** for user activity logs:

  * Decide what one log entry contains (user, action, timestamp, etc.)

### Explanation / justification plan

* For each structure (dict, set, list) write:

  * What real-world SmartCycle problem it solves
  * Which properties make it the “best fit”:

    * Dictionary: fast lookup by ID, easy to update
    * Set: uniqueness of codes, fast membership tests
    * List: ordered history of actions, allows duplicates
* Plan at least one **example scenario** for each:

  * E.g., “We use the dictionary when we need to quickly find part details from an ID.”

### Files / artifacts to create

* `module2/PLAN.md` – table or bullets for:

  * Data type → What it stores → Why it’s used
* `module2/demo_structures.py` – your small Python demo
* `module2/EXPLANATION.md` – final written justification in paragraph form

---

## Module 3 – Systematic Troubleshooting Report

**Goal:** Use a six-step troubleshooting model to explain how you’d fix a sync issue between SmartCycle and phone, and represent the logic with a flowchart. 

### Scenario

> SmartCycle stops syncing its data to the user’s phone.

### Report structure (outline)

Create a document with these sections:

1. **Identify the problem**

   * Describe observable symptoms (e.g., app not updating distance, error messages, etc.)
   * Mention tools/logs you’d check first.

2. **Form hypotheses**

   * List possible causes, grouped by type:

     * Connectivity (Bluetooth/Wi-Fi/data)
     * Hardware (sensors, battery)
     * Software/app (version, permissions, storage, bugs)
     * Cloud/backend issues

3. **Propose solutions**

   * For each hypothesis, write 1–2 possible fixes:

     * e.g., “If Bluetooth is off → Turn on and re-pair.”

4. **Test solutions**

   * Explain how you’ll test each fix step-by-step.
   * Note what result means “pass” vs “fail”.

5. **Verify & monitor**

   * Decide how long you’ll monitor after a “fix” (extra rides, logs, user feedback).

6. **Document the process**

   * Plan what you’ll record:

     * Problem summary
     * Steps tried and results
     * Final resolution
     * Recommendations for future incidents

### Flowchart plan

* Decide your **start point**: e.g., “User reports sync failure.”
* Add decision nodes such as:

  * “Is Bluetooth on?”
  * “Is app updated?”
  * “Can other apps access the internet?”
* Add action steps:

  * “Restart SmartCycle device,” “Clear app cache,” etc.
* End nodes:

  * “Issue resolved”
  * “Escalate to support / hardware repair”

You can sketch first on paper or with a diagram tool, then redraw neatly for submission.

### Files / artifacts to create

* `module3/TROUBLESHOOTING_REPORT.md` – full 6-step writeup
* `module3/FLOWCHART.(png|pdf|drawio)` – exported diagram
* `module3/NOTES.md` – quick brainstorm / rough notes if needed

---

## Module 4 – Collaboration Plan (Google Tools)

**Goal:** Show that you can collaborate using Google Docs, Drive, Meet, and Groups with a structured workflow. 

### Workflow design

Plan out and then execute these steps:

1. **Google Doc (Project Plan)**

   * Create a document with:

     * Project overview
     * Module responsibilities per teammate
     * Deadlines and checkpoints

2. **Google Drive sharing**

   * Put all capstone files in a shared folder.
   * Set permissions (e.g., “Editor” for teammates, “Viewer” for teacher if required).
   * Record what permissions you chose and why.

3. **Comments & tagging**

   * Agree on a commenting style (e.g., `@Name – please review Module 2 section`).
   * Plan to use suggestions mode for edits.
   * Capture at least one example where a teammate responds to your comment.

4. **Google Meet**

   * Schedule a short planning or review meeting.
   * Prepare a minimal agenda (3–4 bullet points).
   * Take quick meeting notes.

5. **Google Group**

   * Create a group for project communications (if allowed).
   * Decide what types of messages go there (updates, meeting reminders, file links).

### Evidence collection

* Plan which screenshots you will take:

  * Google Doc with comments + tags visible
  * Drive folder with sharing settings
  * Google Meet event from Calendar
  * Google Group overview page

### Files / artifacts to create

* `module4/COLLAB_PLAN.md` – describes the workflow and roles
* `module4/screenshots/…` – images of each tool in use
* `module4/MEETING_NOTES.md` – summary of at least one Meet session

---

## Module 5 – Intellectual Property & Innovation Strategy

**Goal:** Decide which parts of SmartCycle need patent, copyright, and trademark protection, and write a 1-page IP plan. 

### IP mapping plan

Make a table or list mapping system components → IP type:

* **Patent candidates**

  * Any novel algorithms or hardware designs (e.g., unique energy-saving algorithm, custom sensor fusion method).
* **Copyright**

  * UI screens and layout
  * Documentation, manuals, and help content
  * Source code (by default, if original)
* **Trademark**

  * Product name “SmartCycle Data Console” (if used commercially)
  * Logo and distinctive branding

### 1-page IP plan structure

Organize your page roughly as:

1. **Introduction**

   * Short statement: why IP protection matters for SmartCycle.

2. **IP by component**

   * For each major component, state:

     * Which IP type applies
     * Why that type is appropriate

3. **Steps to secure IP**

   * Examples:

     * Patent: prior art search, file a provisional, then a full application
     * Copyright: keep dated copies, mention copyright notices
     * Trademark: search for name conflicts, register mark, use consistently

4. **Risks if not protected**

   * Copycat products
   * Loss of brand identity
   * Difficulty enforcing rights
   * Loss of competitive advantage

5. **Connection to Parker’s PEC kit**

   * Briefly relate how his protection strategy inspires yours (e.g., identify innovation, then pick correct protection route).

### Files / artifacts to create

* `module5/IP_PLAN.md` – the final 1-page (or close) protection plan
* `module5/MAPPING_TABLE.md` – optional, a more detailed component → IP mapping

---

## Module 6 – Data Privacy & Ethics Blueprint

**Goal:** Analyze SmartCycle’s data collection, privacy risks, and ethical issues, and write a protection and impact plan, using Cambridge Analytica as a warning example. 

### Data inventory plan

List all data SmartCycle could collect, such as:

* Location and route history
* Speed, distance, ride duration
* Battery usage patterns
* Device identifiers
* User account details (name, email)

Group them into categories (identifying info, behavioural data, technical data, etc.).

### Privacy risk analysis

For each category, explain:

* What could go wrong:

  * Unwanted tracking
  * Data leaks / hacking
  * Commercial misuse (e.g., targeted ads)
* Who might be harmed:

  * Individual riders
  * Communities (e.g., patterns revealing where people live/work)

Connect at least one risk to lessons from Cambridge Analytica (e.g., misuse of personal data for purposes users never agreed to).

### Data protection plan structure

Write a blueprint with these sections:

1. **Permissions**

   * What permissions the app will request (location, notifications, etc.)
   * How you’ll explain why each is needed (plain-language examples).

2. **Data minimization (what NOT to collect)**

   * Identify data you deliberately won’t collect (e.g., exact address history if not needed).
   * Justify: “We avoid collecting X to reduce harm if data is breached.”

3. **Storage & security**

   * Where data is stored (device only / cloud).
   * How long you keep it (retention).
   * Basic protections (encryption, access controls, anonymization).

4. **User control & opt-out**

   * How users can:

     * Turn off certain data collection
     * Delete their data
     * Export their data (if relevant)

5. **Impact evaluation**

   * **Positive impacts:** fitness tracking, safety, performance optimization.
   * **Negative impacts:** surveillance, discrimination risks, misuse by third parties.
   * **Legal concerns:** data protection laws, consent, purpose limitation.

### Files / artifacts to create

* `module6/PRIVACY_BLUEPRINT.md` – full writeup with sections above
* `module6/DATA_INVENTORY_TABLE.md` – optional, list of data + risks + controls

---

## Final Deliverables Checklist

* [ ] **Module 1** – Python script, array operations, ASCII visual, sample output
* [ ] **Module 2** – Data structures demo + written justification
* [ ] **Module 3** – Troubleshooting report + flowchart diagram
* [ ] **Module 4** – Collaboration workflow + screenshots + meeting notes
* [ ] **Module 5** – IP protection plan
* [ ] **Module 6** – Privacy & ethics blueprint
