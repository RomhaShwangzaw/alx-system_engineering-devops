<img src=./image.png width=50%>

# Issue Summary
Last week, on February 26 at 14:11 East African Time (EAT), it was reported that the BestMovies platform was returning 500 Error on all requests made on the platform routes, until it was fixed a few hours later, at 20:47 EAT. All the services were down. 90% of the users were affected. The root cause was the failure of our master server web-01.

## Timeline
The error was realized on Sunday 26th February 14:11 hours (East Africa Time) when our Site Reliability Engineer, Mr Surafel, saw the master server lagging in speed. Our engineers on call disconnected the master server web-01 for further system analysis and channelled all requests to client server web-02. They thought it was a CPU problem, but that wasn't the issue. Another engineer, the System Admin, was called up to investigate the issue. Together, they solved the problem by testing the server for memory and security issues. The problem was resolved by 20:47 hours (East Africa Time) of the same day.

## Root cause and resolution
The BestMovies platform is served by 2 ubuntu cloud servers. The master server web-01 was connected to serve all requests, and it stopped functioning due to memory outage as a result of so many requests because during a previous test, the client server web-02 was disconnected temporarily for testing and was not connected to the load balancer afterwards. 


The issue was fixed when the master server was temporarily disconnected for memory clean-up, then connected back to the loadbalancer and round-robin algorithm was configured so that both the master and slave servers can handle equal amount of requests.

## Corrective and Preventative Measures
- Choose the best loadbalancing algorithm for your programs
- Always keep an eye on your servers to ensure they are running properly
- Have extra back-up servers to prevent your program from completely going offline during an issue
- Implement monitoring services to monitor the health of your servers
