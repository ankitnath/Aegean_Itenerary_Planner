# Aegean Itinerary Planner

A Python-based command-line utility to plan a transportation itinerary across island hops in the Aegean region, ensuring maximum customer satisfaction based on individual travel preferences.

## Developed By

**Ankit Nath**

---

## Project Description

This tool calculates an optimal itinerary of travel modes (either `airborne` or `by-sea`) for a fixed number of hops based on preferences from multiple customers. Each customer specifies a list of preferred travel modes for specific hops, with a maximum of one `airborne` preference. The script ensures:

- All customers are satisfied with at least one preferred hop.
- Airborne hops are assigned where necessary.
- Airborne hops are prioritized where they help the most unsatisfied customers.

Invalid inputs or infeasible solutions return `"INVALID INPUT"` or `"NO ITINERARY"` respectively.

---

## File Structure

- `itinerary_planner.py` – The main Python script.
- `input.txt` – Sample input file.
- `run.sh` – Bash script to execute the program.
---

## Input Format

The script expects input from standard input (e.g., via `input.txt`)

---
## Run the File

- `chmod +x run.sh` – make sure the run.sh is executable
- `./run.sh`
