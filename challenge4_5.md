### Kate Macias
### Software Engineering 
### Fall 2026

```mermaid
flowchart TD
    A[Chess] --> B(log_In)
    B --> C{SERVER}
    C <-->|checks with|D[View_games/Lobby]
    C <-->E[Match_Creation]
    C <-->F[Statistics/Matchmaking]
    C <-->G[Account_Management]
    B <-->G
    H[Chat Interface]<--> D
```
