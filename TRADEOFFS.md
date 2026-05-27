# TRADEOFFS.md

# Tradeoffs and Deliberately Excluded Features

This prototype intentionally prioritizes:
- workflow clarity
- normalization logic
- review lifecycle
- auditability

over enterprise-scale completeness.

---

# 1. Authentication and Role Management

Not implemented:
- login system
- RBAC
- analyst/admin separation

Why:
The assignment focused more heavily on ingestion and review workflows than authentication complexity.

In production:
- JWT/session authentication
- role-based permissions
would be required.

---

# 2. Advanced Data Validation and AI Detection

Not implemented:
- ML anomaly detection
- statistical outlier detection
- emissions factor validation

Why:
A simple suspicious rule was sufficient for demonstrating analyst review flow.

Production systems would likely require:
- anomaly scoring
- historical benchmarking
- configurable validation rules

---

# 3. PDF/OCR Utility Parsing

Not implemented:
- OCR extraction
- PDF parsing
- scanned bill ingestion

Why:
OCR pipelines introduce significant complexity and reliability concerns.

CSV utility exports were chosen as a more reliable prototype ingestion path.

---

# Additional Deferred Features

Other intentionally deferred capabilities:
- async ingestion queues
- retry pipelines
- detailed audit logs
- row-level change history
- emissions calculations
- tenant-specific normalization rules
- cloud object storage
- API authentication
- background processing