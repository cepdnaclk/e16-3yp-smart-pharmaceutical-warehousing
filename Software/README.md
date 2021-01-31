# Smart Pharmaceutical Warehousing software
---

The current progress and the implementations of the project can be viewed from the following links:

1.simulation

2.mqtt


1.simulation

    line following
![alt text]( https://github.com/cepdnaclk/e16-3yp-smart-pharmaceutical-warehousing/blob/main/Web%20application/aws/doc/line_following.gif)

    algorithm 

---

2.mqtt

    There is two type mqtt

        1.website to local server
        2.local server to robot

        

    * Website to local server
        Every message send through public mosquitto mqtt broker and messages are at fernet encryption 
        1.database syncing ( local data base is the main)
            not implemented 
        2.purchase / order detail ( web site to local ) 
            website as publisher send the message ( implemented )

    * local server to robot
        Every message send through local mqtt broker and messages are at fernet encryption and wifi protection
        1.Junction handling ( mqtt base traffic light ) ( under developing )
        2.agv destination ( simulator level working )
        3.Battery level ( operator interface side work )
        3.arm work order ( under developng )
    