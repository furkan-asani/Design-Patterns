# Example for the Observer Pattern
We are creating a Dashboard for a technical support center.
This dashboard displays certain KPIs:
* Open tickets
* New tickets in the last hour
* Closed tickets in the last hour <br /> <br />
The dashboard is the observer <br />
The KPI source is the subject
# Improvements/SOLID principles
Separated the concerns of subject and observer #SingleResponsibilityPrinciple <br />
Provided easier extensibility of observers 
# When to use?
The observer pattern is especially useful when modelling a one to many relationship where the many need to be notified about pending changes <br />
A famous example where the observer pattern is used is MVC and in general in GUIs 
