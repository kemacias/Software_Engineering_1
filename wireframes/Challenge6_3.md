### Kate Macias 
### Software Engineering 1
### Fall 2026

## Make a quick and dirty total day count estimate.

- 100 days for easy math

## Compute the days per task based on that estimate.

# Project management - 10 days 
  - planning -5 days
  - reporting - 5 days
# Requirements and Design - 15 days
  - requirements - 5 days
  - UX - 5 days
  - Architecture - 5 days
# Customer Web App - 35 days
  - 7 days for each of the 5 tasks
# Backend - 20 days
  - menu service 7 days
  - order service 7 days
  - auth 6 days 
# Staff Tools 7 Days
  - order queue 4 days
  - menue management 3 days
# Testing - 78 days
  - automated 4 days
  - usability and security - 4 days
# Deployment - 5 days
  - hosting and CI/CD 3 days
  - launch 2 days 


## Determine which of the tasks can be done in parallel.



## Draw a Gantt Chart in Mermaid showing the project timeline.
```mermaid
Answers to the "What To Do" questions:

1. **Total estimate:** About 100 working days of effort for the whole project, so each WBS percentage is also its day count (for example, Customer Web App at 35% is 35 days).

2. **Days per task:**
   - **Project Management (10):** planning 5, status reporting 5
   - **Requirements and Design (15):** requirements 5, UX 5, architecture 5
   - **Customer Web App (35):** 7 days each for its 5 tasks
   - **Back-End (20):** menu service 7, order service 7, auth 6
   - **Staff Tools (7):** order queue 4, menu management 3
   - **Testing (8):** automated 4, usability and security 4
   - **Deploy (5):** hosting and CI/CD 3, launch 2

3. **Parallel work:** Project management runs the whole time. UX and architecture can happen together once requirements are gathered. After design, the customer app, back-end and staff tools can all be built in parallel. Hosting setup can overlap with testing, but launch has to come last.

4. **Gantt chart (Mermaid):**

```mermaid
gantt
    title Online Pizza Ordering System
    dateFormat YYYY-MM-DD
    excludes weekends
    section Project Mgmt
    Planning and scheduling      :pm1, 2026-11-09, 5d
    Status reporting             :pm2, after pm1, 5d
    section Req and Design
    Requirements gathering       :r1, 2026-11-09, 5d
    UX design                    :r2, after r1, 5d
    Architecture and DB design   :r3, after r1, 5d
    section Customer Web App
    Menu browsing                :c1, after r2, 7d
    Pizza customization          :c2, after c1, 7d
    Shopping cart                :c3, after c2, 7d
    Checkout and payment         :c4, after c3, 7d
    Account and order tracking   :c5, after c4, 7d
    section Back-End
    Menu and pricing service     :b1, after r3, 7d
    Order service                :b2, after b1, 7d
    Authentication and security  :b3, after b2, 6d
    section Staff Tools
    Order queue dashboard        :s1, after b2, 4d
    Menu management              :s2, after s1, 3d
    section Testing
    Automated tests              :t1, after c5, 4d
    Usability and security tests :t2, after t1, 4d
    section Deployment
    Hosting and CI/CD setup      :d1, after c5, 3d
    Launch and support           :d2, after t2, 2d
```
