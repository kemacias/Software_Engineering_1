### Kate Macias
### Software Engineering 1
### Fall 2026

# Ko-Tistics Technical Design Document

# Overview

Ko-Tistics syncs reading data from a Kobo e-reader to Google Drive with one tap, so it can feed a personal reading-statistics and progress dashboard.

# Actors

- Storygraph user 
- 

# Goals/Non-Goals

## Goals
- easy syncing of reading data from Kobo e-reader to Google Drive with one tap
- capture side loaded reading data
- feed a personal reading-statistics and progress dashboard
- normalized data model
- export CSV for easy storygraph updates

## Non_Goals

- Native storygraph support
- Realtime syncing
- spoofing kobo data syncing with kobo cloud
- Two way syncing. Kobo files remain unchanged after sync
- KO reader support

# Constraints

- personal information must not be stored or shared with any third parties
- does not interfere with Kobo UI/Firmware
- intermitent wifi connectivity (eReaders are used primarily offline)

# Assumptions

- Nickel Menue has already been installed
- Working on compatable kobo device
- Kobo database schema stays consistent through firmware updates
- All reading data is being captured by KoboReader.sqlite file
- Wifi will be available for syncing
- Side loaded books may have the wrong metadata 

# Non-Functional Requirements

 - Failed syncs do not leave corrupted data
 - all syncs incluse -wal file that is merged 
 - Every sync is timestamped and logged success or failure
 - Easy to set up again if firmware update removes modifications
 -  

# Component Diagram and Description

```mermaid
flowchart LR
    A[KOBO] -->|tap sync| B(Google Drive)
    C[Ko-Tistics] -->|fetch| B
    C -->D[merge files]
    D -->E[normalize data]
    G -->F[Streamlit Dashboard]
    E -->G[(local normalized database)]
    G -->|Drive Cleanup| B
```

| Component | Description |
|-----------|-------------|
| KOBO | E-reader running a NickelMenu custom one tap sync |
| Google Drive | Holds timestamped database snapshots until Ko-Tistics fetches them. 
| Ko-Tistics | Python application on the laptop that coordinates fetching, merging, normalizing, and cleanup. |
| merge files | Combines each snapshot's `.sqlite` and `-wal` files into one standalone database so no recent progress is lost. |
| normalize data | Filters to sideloaded books and converts Kobo's raw columns into usable, normalized data structure. |
| local normalized database | SQLite database storing the normalized data for the dashboard. |
| Streamlit Dashboard | Local web dashboard that displays reading statistics and progress over time. |
| Drive Cleanup | Deletes ingested snapshots from Google Drive after the local database update succeeds. |
