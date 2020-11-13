This folder contains the algorithms designed for Scheduling orders/AGVs, Routing and Collision avoidance. 

#Scheduling Algorithm

Aim of scheduling orders/AGVs is to dispatch a set of AGVs to complete a batch of pickup/drop-off jobs to achieve certain goals under given constraints.
Minimize total travel time and AGV idle time while maximizing the system throughput were the main concern.
Completion of all pickup/drop-off jobs under given priority or deadline was also taken into consideration.

Every order is breakdown into set of pickup/drop-off jobs. Processing time of a pickup/drop-off job is given by;
                
Tp = Tld + Ttr + Tc    ; where      Tld  - loading/unloading time
                                    Ttr   - travel time, 
                                    Tc -  path conflict resolution time    
                
Total processing time of the order is the summation of  Tp over the number of pickup/drop-off jobs.

Every order is assigned with a waiting time (Tw) which counts the time a particular order has been waiting once it’s been placed.

For each and every order, the  value Tw/𝚺Tp is calculated and the tuple ((Tw/𝚺Tp), i) is put into an array sorted with the first element of the tuple.

Order corresponding to the ArgMax of the array is then popped out from the array and sent to be processed.

Taking ArgMax of the array (order corresponding to the max(Tw/𝚺Tp) ensures that orders with short processing time or orders that has been waiting longer period gets priority.



