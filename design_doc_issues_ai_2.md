Here is a comprehensive report on the logical, structural, and technical issues identified in the **Ko-Tistics Technical Design Document**:

---

### 1. Structural & Formatting Inconsistencies

* **Incomplete Sections & Bullet Points:**
* Under **Actors**, the second bullet point is left completely blank (`- `).
* Under **Non-Functional Requirements**, there is a trailing empty bullet point.


* **Naming and Casing Discrepancies:**
* The section header is spelled `Non_Goals` (with an underscore), whereas standard technical documents use `Non-Goals`.
* "Storygraph" has inconsistent capitalization across the document (e.g., "Storygraph user" under Actors vs. "storygraph updates" under Goals).


* **Typos:** Several spelling errors exist throughout the text, including `intermitent` (should be *intermittent*), `compatable` (should be *compatible*), and `incluse` (should be *include*).

---

### 2. Architectural & Component Discrepancies

* **Component Diagram vs. Description Table Mismatch:**
* In the Mermaid flowchart, node `G` (`(local normalized database)`) points to `|Drive Cleanup| B` (`Google Drive`). In reality, cleanup is an orchestration task executed by the Python application (`Ko-Tistics`), not by the database itself.
* Node `G` also points directly to `F` (`Streamlit Dashboard`), but the flow arrow origins and labels are slightly disorganized compared to the descriptive table.


* **Omitted Pipeline Function in Interface Summary:**
* The **Component Description**, **Non-Functional Requirements**, and **Data Fetching** logic emphasize merging `.sqlite` and `-wal` (Write-Ahead Log) files. However, the **Interface Functions** section completely omits a `merge_data()` or `merge_snapshots()` function, listing only `push_data()`, `data_fetch()`, `parse_data()`, `normalize_data()`, `store_data()`, and `query_data()`.



---

### 3. Data Model & ER Diagram Flaws

* **Primary Key Constraint in `word_lookup`:**
* The `word_lookup` table defines `text word PK`. Setting `word` as the primary key means a specific word (e.g., "ephemeral") can only exist **once** across the entire database. If a user looks up the same word in a different book or at a later date, the database will throw a primary key violation. The primary key should be a composite key `(word, book_id, looked_up_at)` or an auto-incrementing surrogate ID.


* **Redundant Invariants Section:**
* In the **Invariants** section, the statement *“Only complete data is displayed on the dashboard.”* is duplicated verbatim as both a header and a standalone rule.



---

### 4. Failure Modes Deficiencies

* **Boilerplate and Inaccurate Responses:**
* Every single failure mode in the **Failure Modes** table (`Incomplete_Data`, `parse_error`, `no_new_data`, `NM_down`) shares the exact same Response (`Save warning file`), Impact (`Data loss`), and Notification (`Data loss notification`).
* This is structurally lazy and logically incorrect. For example:
* `no_new_data` does **not** result in data loss; it is a normal operational state where no new snapshots are found.
* `NM_down` (NickelMenu removed by a firmware update) results in sync failure, not direct data loss of existing local logs, and requires manual re-installation of NickelMenu rather than simply saving a warning file.





---

### 5. Logic & Scope Clarifications

* **Handling of Side-Loaded Metadata:**
* Under **Assumptions**, the doc notes: *"Side loaded books may have the wrong metadata."* However, there is no corresponding error-handling strategy, normalization rule, or user interface component in the pipeline or data model to handle manual overrides, ISBN cleaning, or metadata merging for side-loaded EPUBs/PDFs.
