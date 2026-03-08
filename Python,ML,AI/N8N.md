## Understanding N8N

N8N is used for Business Workflow Automation. It helps us to automate workflows using visual editor which is a no code tool.

**Terminology used in N8N for workflow Automation**

1.**Nodes** - Nodes represents the individual steps/tasks.</br>
2.**Edges** -Edges represents the connections between steps/tasks.</br>
3.**Data Movement** is done through Json in N8N.

**Setting up N8N through Docker**

**Link** - https://docs.n8n.io/hosting/installation/docker/#prerequisites

1. Install Docker Desktop.</br>
2. Create a volume for storing n8n data by running below command in cmd. It is important to create volume so that n8n data like workflows is stored on your hardisk as well.If you dont create volumne whenever you close docker container all your n8n workflows would be lost.

   ```
   docker volume create n8n_data
   ```

4. Pull the image of N8N by running below command in cmd

   ```
    docker pull docker.n8n.io/n8nio/n8n
   ```

 5. Run the N8N container using below command

    ```
     docker run -it --rm --name n8n -p 5678:5678 -e GENERIC_TIMEZONE="Asia/Kolkata" -e TZ="Asia/Kolkata" -e   N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true -e N8N_RUNNERS_ENABLED=true -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
    ```

The above process enables you to run N8N on your local machine.

<img width="1513" height="923" alt="image" src="https://github.com/user-attachments/assets/21b59717-0a03-440e-8976-6540cb60450f" />

6. You can get paid features of N8N by navigating to settings -> usage and plans and enter your emailID. On your emailId you would get your activation key which you can use to get your paid plan.

<img width="1362" height="989" alt="image" src="https://github.com/user-attachments/assets/f276d574-aecf-46fb-92de-33f3850c186c" />




**Piece Of Advise while using N8N**

1. Whenever you try to create a workflow in N8N, Ensure to create a workflow on a piece of paper rather then directly creating on N8N
2. N8N does not have autosave, so always keep on saving your work whenver you finish some small steps.


**Different Types of Nodes in N8N**

1.**Trigger Nodes** - Trigger Nodes are used to Trigger a workflow. Below image shows some of the Trigger Nodes

<img width="1670" height="822" alt="image" src="https://github.com/user-attachments/assets/8e00352f-97c8-430d-9c1f-555dda173b51" />



Using pin command,we can pin the output of a node so that we can use it as an  input for following node without executing the node.If we dont pin the output then we might need to execute node again and again.

<img width="1868" height="893" alt="image" src="https://github.com/user-attachments/assets/51373951-6b6b-4415-b650-c043f5130eb7" />




