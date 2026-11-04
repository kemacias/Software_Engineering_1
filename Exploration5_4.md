### Kate Macias
### Software Engineering 1
### Fall 2026

## For the ATM example, come up with - 
## Three more things that should be in the failure modes

| ID | Failure | Response | Impact | Notification |
|----|---------|----------|--------|--------------|
| Stuck_Card | A jammed card in the ATM | Returns ERROR if card stuck | | Local branch notification |
| External_Change | A tampered-with ATM (skimmers, etc.) | Suspicious activity detected | ATM disabled | Branch notification |
| No_Funds | No more cash to dispense | Returns ERROR when cash is empty | ATM disabled | Branch notified |

## Three things that should be in the regular interface section, and not included as a failure mode

- Wrong Pin
- Insufficient Funds
- Undispensible Ammount (not in $20's)
