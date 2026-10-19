### Kate Macias
### Software Engineering 1
### Fall 2026


## Part 1
```mermaid
flowchart LR
    A[Web Server] -->|HTML| B(web front end)
    B <--> E[API] <-->F[(GIS Database)]
    B <--> D[User Applications]
```

## Part 2
```mermaid
flowchart LR
    A[User Applications] -->|API Calls| E[API]<-->|GIS info|F[(GIS Database)] 
    
    E<--> G[Web Front End]
```
