package com.company;

import java.net.*;
import java.io.*;

public class Communication {
    private ServerSocket serverSocket;
    private Socket clientSocket;
    private PrintWriter out;
    private BufferedReader in;

    public void start(int port){
        try {
            serverSocket = new ServerSocket(port);
            clientSocket = serverSocket.accept();
            out = new PrintWriter(clientSocket.getOutputStream(),true);
            in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            String greeting = in.readLine();

            if("hello".equals(greeting)){
                out.println("hello client");
            }else {
                out.println("unrecognised greeting");
            }

        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("port error");
        }

    }

    public void stop(){
        try {
            in.close();
            out.close();
            clientSocket.close();
            serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("close without open");
        }

    }

}
