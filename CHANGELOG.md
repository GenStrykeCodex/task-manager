# Task Manager CLI (SQLite edition)

**Project Status** : `STABLE RELEASE`

---

## v2.0.0 Changelog – Major Refactor & Feature Upgrade

### Date : 09-02-2026

### Added
- SQLite-backed persistent storage
- Modular project architecture
- Task model with status, priority, and timestamps
- CRUD service layer
- Task filtering by status
- Task filtering by priority
- Input validation utilities
- Database integrity constraints
- Developer-safe database reset utility
- Clean CLI menu system

### Changed
- Migrated from single-file / file-based logic to SQLite
- Improved error handling and user feedback
- Enforced separation of concerns
- Standardized task data flow using models and services

#### Fixed
- Prevented invalid status/priority values
- Handled Windows SQLite file-lock edge cases
- Eliminated runtime crashes from bad input

---

## v1.0.0 Changelog – Legacy Version

### Date: 15-12-2025

### Added
- Basic CLI task management
- File-based storage
- Single-file architecture

---