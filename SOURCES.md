# SOURCES.md

# Real-World Source Research

This document summarizes research performed for the three ingestion source categories.

---

# 1. SAP Fuel and Procurement Data

Research:
- SAP exports are commonly shared as:
  - flat-file CSV exports
  - IDocs
  - OData services
  - BAPIs

Prototype choice:
- CSV flat-file ingestion

Why:
CSV exports are realistic for sustainability reporting teams and easier to prototype quickly.

Observed characteristics:
- inconsistent units
- operational abbreviations
- non-standard column names
- mixed date formats

Sample data includes:
- fuel type
- quantity
- unit
- scope categorization

Real-world risks:
- multilingual exports
- plant code mapping complexity
- inconsistent master data

---

# 2. Utility Electricity Data

Research:
Facilities teams commonly retrieve electricity usage through:
- utility dashboards
- billing portals
- downloadable spreadsheets
- PDF invoices

Prototype choice:
- CSV utility export

Why:
Portal CSV exports are operationally realistic and easier to normalize than PDFs.

Sample data includes:
- billing period
- electricity quantity
- kWh units

Real-world risks:
- multiple meters
- tariff structure complexity
- missing billing periods
- delayed utility reporting

---

# 3. Corporate Travel Data

Research:
Platforms like:
- SAP Concur
- Navan
- TravelPerk

commonly expose:
- expense exports
- travel activity reports
- APIs

Prototype choice:
- simplified CSV ingestion

Sample data includes:
- travel category
- travel quantity
- scope categorization

Real-world risks:
- missing airport distance data
- duplicate bookings
- partial trip reporting
- inconsistent travel categories

---

# Overall Prototype Assumptions

The prototype intentionally focuses on:
- realistic ingestion workflows
- normalized operational structure
- analyst review lifecycle

instead of:
- enterprise-scale integrations
- emissions calculations
- production-grade infrastructure