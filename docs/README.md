# Smart Pharmaceutical Warehousing
smart pharmaceutical warehousing management system 

### Group Members
        * K.R. De Silva             E/16/068    e16069@eng.pdn.ac.lk
        * J.M.Praveen Dhananjaya    E/16/081    e16081@eng.pdn.ac.lk
        * F.S Marzook               E/16/232    e16232@eng.pdn.ac.lk
        
### OVERVIWE
Conventional pharmaceutical warehouses mostly use man power to manage and handle goods inside their warehouse complexes. But this manual method has some inevitable downsides which cause losses in both time and profitability. In this project, we are trying to address this issue by developing a fully automated warehouse management which will minimize the drawbacks while improving efficiency and profitability.


### Our Solution
   ![alt text](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/website/Overall.png?raw=true)

    Our solution consists three components :-
        1. Fully automated robot operated warehouse
        2. Control interface to control and override (if necessary) the operations of robots
        3. Warehouse database with a website and a mobile applications, as an interface to retailers to make their purchases


### How It Work 
   ![alt text](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/website/line.png?raw=true)

The warehouse has two base stations, namely the delivery post and receiving post, to deliver goods to the customers and receive any stocks to the warehouse respectively. In these base stations, two fixed robot arms are placed to do the loading and unloading process for goods.  In side the warehouse, movable robot arms are placed among shelves to load and unload the good to AGVs.  
Once a client places an order, the database is updated and the computer fetches the relevant information about the goods and triggers up the local warehouse controller. The warehouse controller then generates instructions and are passed to the robot arm and the delivery robot to perform the task. Here, the local controller sends status messages like Insert, Takeout, Store etc... while they are processing the goods. Once the fetching of goods is done, they are delivered to the client.
When more than one orders are received, a queueing algorithm will process them and will assign the automated guided robots (AGVs) nearby those relevant shelves in such a way that no collision will occur as well as no AGV will have an overloaded queue. This queueing algorithm will assure that all AGVs and robot arms are used efficiently. A separate algorithm will choose the shortest path for AGVs to reach their destination, minimizing the travel time. 

        

### 