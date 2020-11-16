# Smart Pharmaceutical Warehousing
---

### Group Members :
>[K.R. De Silva](https://github.com/RashmikaDeSilva) **E/16/068  (e16069@eng.pdn.ac.lk)**

>[J.M.Praveen Dhananjaya](https://github.com/praveendhananjaya) **E/16/081  (e16081@eng.pdn.ac.lk)**

>[F.S Marzook](https://github.com/ShamraMarzook) **E/16/232  (e16232@eng.pdn.ac.lk)**

### Supervisors
Dr. Isuru Nawinne

Dr. Ziyan Maraikar

### Table Of Content
1. [Problem Overview](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing#Problem-Overview)
2. [Our solution](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing#Our-Solution)
3. [Solution Architecture](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing#Solution-Architecture)
4. [Hardware & Software Designs](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing#hardware--software-designs)
5. [Testing](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing#Testing)
6. [Detailed budget](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing#Bill-of-Material)
7. [Related Links](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing#Related-Links)

### Problem Overview
Conventional pharmaceutical warehouses mostly use manpower to manage and handle goods inside their warehouse complexes. Some warahouses use small indoor vehicles. But all these conventional methods has some inevitable downsides. Most common suhc disadvantages are redundant activities, higher labor cost, suboptimal handling of goods and internal and external thefts. These downsides cause losses in both time and profitability and lead to inefficent warehouse management. 

### Our Solution
In this project, we are trying to address this issue by developing a fully automated warehouse management which will minimize the drawbacks while improving efficiency and profitability. We are implementing a warehouse managament system which consists two types of robots; robots arms - to handle loading/unloading of goods, automated guided vehicles(AGVs) to transport goods inside warehouse. Also an online shopping portal to make the purchases from the warehouse.

Once a customer places an order, the order will be received, processed and will be delivered to the delivery station without any human involvement. The customer will then be informed to pickup his/her order from the warehouse.

   ![alt text](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/docs/Overall.png?raw=true)

 

### How It Works 
   ![alt text](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/docs/line.png?raw=true)
   
Our solution consists three components :-
  1. [Fully automated warehouse](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/Hardware)
  
  2. Controller interface to control and override(if necessary) the autonomous operations
  
  3. Warehouse database with an online shopping portal, as an interface to retailers to make their purchases

The warehouse has two base stations, the delivery post and receiving post, to deliver goods to the customers and receive any stocks to the warehouse respectively. In these base stations, two fixed robot arms are placed to do the loading and unloading process for goods.  Inside the warehouse, movable robot arms are placed among shelves to load and unload the goods to AGVs.

Once a client places an order, the database is updated and the computer fetches the relevant information about the goods and triggers up the local warehouse controller. The warehouse controller then generates instructions and are passed to the robot arm and the delivery robot to perform the task. Here, the local controller sends status messages like Insert, Takeout, Store etc. while they are processing the goods. Once the fetching of goods is done, they are delivered to the client.

When more than one orders are received, a queueing algorithm will process them and will assign the automated guided robots (AGVs) nearby those relevant shelves in such a way that no collision will occur as well as no AGV will have an overloaded queue. This queueing algorithm will assure that all AGVs and robot arms are used efficiently. A separate algorithm will choose the shortest path for AGVs to reach their destination, minimizing the travel time. 

   ![alt text](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/docs/Solution_overview.jpg)

### Hardware & Software Designs
The current progress and the implementations of the project can be viewed from the following links:
1. [Hardware](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/tree/main/Hardware)
2. [Software](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/tree/main/Software)
3. [Network](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/tree/main/Network)

### Bill of Material
   ![alt text](https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/docs/BoM.jpg)
 
### Related Links
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [Faculty of Engineering](http://eng.pdn.ac.lk/)
- [University of Peradeniya](https://www.pdn.ac.lk/)
