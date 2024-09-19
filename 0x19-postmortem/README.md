Postmortem: When Our API Took a Nap 🛌💻

Issue Summary:

Duration: The outage lasted for 3 hours, from 11:00 AM to 2:00 PM UTC on September 15, 2024.
Impact:
The Genealogy and Health Platform’s API services were either unavailable access family tree visualizations, health records, and genetic risk assessments.
Users reported timeouts and slow response times when attempting to load data.
Root Cause: The root cause was a memory leak in the API service that overloaded the application servers, leading to unhandled out-of-memory (OOM) errors.

Timeline:
11:00 AM UTC: 🚨 Alert! Monitoring system alerts the team to a significant increase in response times for the API.
11:05 AM UTC: Engineer on call investigates API server logs and identifies slow queries.
11:20 AM UTC: Initial hypothesis is that the database is under heavy load due to large data queries.
11:40 AM UTC: Database and network load checks are normal; issue persists. Memory usage on API servers is noticed to be unusually high.
12:00 PM UTC: Incident escalated to backend engineering team.
12:15 PM UTC: Investigation continues into the codebase for possible memory leaks.
1:00 PM UTC: Memory leak identified in the genetic risk assessment module, causing memory overconsumption.
1:30 PM UTC: Temporary fix applied by restarting API services and adjusting memory limits.
2:00 PM UTC: Full resolution achieved by deploying a patch to fix the memory leak.

The root cause of the outage was traced to the genetic risk assessment feature, which uses Python to process health data for users
A specific function was improperly handling large datasets, failing to release memory after computation.
This resulted in memory consumption increasing over time, eventually triggering OOM errors and crashing the API service.
The issue was fixed by refactoring the memory management in the affected function.
This involved ensuring that large objects were explicitly deleted from memory after use.
Additionally, the deployment environment's memory limits were adjusted to prevent future crashes while more long-term fixes are implemented.

Corrective and Preventative Measures

Improve memory monitoring: Add detailed memory usage monitoring for all API services to alert when memory consumption exceeds predefined thresholds.
Code refactoring: Conduct a thorough review of the genetic risk assessment module and other memory-intensive areas of the application to identify
and fix potential memory leaks.
Incident management procedures: Enhance documentation on incident escalation and troubleshooting processes for better collaboration during outages.
Performance testing: Implement routine load testing on large datasets to simulate real-world usage and identify potential performance bottlenecks earlier.

Task List:

Patch the genetic risk assessment module to prevent memory leaks. 🛠️
Add memory usage alerts to the monitoring system 🕵️
Refactor code to improve memory efficiency across other API services 💪
Conduct bi-weekly load testing with real data sets to identify weaknesses.
Update incident response documentation for quicker resolution times in the future.

