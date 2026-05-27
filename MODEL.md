# MODEL.md

## Overview

The application is designed as a simplified ESG data ingestion and analyst review workflow system.

The core goal of the system is to ingest emissions-related operational data from multiple enterprise sources, normalize it into a consistent structure, flag suspicious records, and support analyst review and audit locking.

The prototype focuses on:
- Multi-source ingestion
- Unit normalization
- Review workflow
- Audit traceability
- Multi-tenant support

---

# Core Models

## Tenant

Represents a client company onboarded into the ESG platform.

Fields:
- id
- name
- created_at

Why:
Breathe ESG operates in a multi-tenant environment where multiple enterprise customers use the same platform.

---

## SourceRecord

Represents raw uploaded data before normalization.

Fields:
- tenant_id
- source_type
- raw_payload
- uploaded_at

Why:
Source-of-truth tracking is important for auditability. Raw records are preserved before normalization.

---

## NormalizedRecord

Represents normalized ESG activity data.

Fields:
- tenant_id
- category
- scope
- activity_type
- quantity
- normalized_unit
- original_quantity
- original_unit
- source_record_id
- suspicious_flag
- review_status
- locked_for_audit
- created_at

Why:
This acts as the central operational ESG dataset after ingestion.

---

# Scope Categorization

The prototype supports:
- Scope 1
- Scope 2
- Scope 3

Current implementation mainly focuses on:
- Fuel consumption
- Electricity usage
- Corporate travel activities

---

# Unit Normalization

The system normalizes inconsistent units into standard units.

Examples:
- gallon → liter
- kWh retained as standard electricity unit

Why:
Different enterprise systems export data in inconsistent units.

Normalization ensures:
- comparability
- reporting consistency
- downstream emissions calculations

---

# Suspicious Record Detection

Records are flagged suspicious if:
- quantity < 0

Why:
Negative fuel or utility consumption is usually invalid operational data.

The suspicious_flag enables analyst review before audit approval.

---

# Review Workflow

Lifecycle:
1. Data uploaded
2. Data normalized
3. Analyst reviews records
4. Record approved/rejected
5. Record locked for audit

Once locked:
- records cannot be modified

Why:
Audit workflows require immutable approved records.

---

# Auditability

The system tracks:
- source record linkage
- original units
- normalized values
- review status
- lock status

This supports:
- traceability
- reproducibility
- audit readiness

---

# Database Choice

SQLite was used for rapid prototyping simplicity.

For production:
- PostgreSQL would be preferred
- partitioning and indexing would be required for scale

---

# Future Improvements

Potential improvements:
- emissions factor engine
- asynchronous ingestion pipeline
- OCR utility bill parsing
- role-based access control
- detailed audit logs
- versioned normalization rules