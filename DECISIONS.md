# DECISIONS.md

# Overview

This document explains key implementation decisions and ambiguities resolved during development.

---

# SAP Ingestion Choice

Chosen format:
- CSV flat-file export

Why:
SAP exports are commonly shared as flat-file exports for operational reporting workflows.

A CSV ingestion flow was significantly simpler to prototype within the assignment timeline compared to:
- IDocs
- BAPIs
- OData integrations

Handled:
- fuel consumption data
- inconsistent units

Ignored:
- multilingual column mappings
- plant hierarchy lookups
- deeply nested SAP structures

---

# Utility Data Choice

Chosen format:
- CSV export from utility portal

Why:
Facilities teams commonly export electricity usage from utility dashboards into spreadsheets.

This was more realistic and easier to validate than:
- PDF OCR extraction
- direct utility APIs

Handled:
- billing period
- electricity quantity
- units

Ignored:
- tariff complexity
- demand charges
- multi-meter reconciliation

---

# Corporate Travel Choice

Chosen ingestion:
- simplified CSV upload

Why:
Travel platforms like Concur or Navan often provide exportable expense/activity reports.

Handled:
- travel category
- quantity
- travel activity

Ignored:
- airport code distance calculations
- hotel-night estimation
- travel policy enforcement

---

# Review Workflow Decision

Chosen workflow:
- pending
- approved
- locked

Why:
This mirrors real operational analyst review flows while remaining simple enough for a prototype.

---

# Suspicious Data Rules

Current suspicious logic:
- negative quantities

Why:
Negative operational activity data is commonly invalid.

More advanced anomaly detection was intentionally deferred.

---

# Multi-Tenancy

The system supports tenant separation through tenant_id references.

Why:
Breathe ESG serves multiple enterprise clients simultaneously.

---

# Frontend Choice

React was selected because:
- component-based architecture
- fast dashboard prototyping
- easy API integration

---

# Backend Choice

Django REST Framework was selected because:
- rapid API development
- strong ORM
- admin tooling
- serialization support

---

# Deployment Choice

Render was selected because:
- simple deployment workflow
- GitHub integration
- fast prototype deployment
- suitable free-tier hosting

---

# What I Would Ask The PM

Questions:
- expected ingestion scale?
- should rejected rows remain editable?
- should normalization rules be configurable per tenant?
- are uploads batch-based or streaming?
- how long must audit records remain immutable?