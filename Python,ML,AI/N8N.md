## Understanding N8N

N8N is used for Business Workflow Automation. It helps us to automate workflows using visual editor which is a no code tool.

**Terminology used in N8N for workflow Automation**

1.**Nodes** - Nodes represents the individual steps/tasks.</br>
2.**Edges** -Edges represents the connections between steps/tasks.</br>
3.**Data Movement** is done through Json in N8N.

**Setting up N8N through Docker**

**Link** - https://docs.n8n.io/hosting/installation/docker/#prerequisites

1. Install Docker Desktop.</br>
2. Create a volume for storing n8n data by running below command in cmd

   ```
   docker volume create n8n_data
   ```

3. Pull the image of N8N by running below command in cmd

   ```
    docker pull docker.n8n.io/n8nio/n8n
   ```

 4. Run the N8N container using below command

    ```
     docker run -it --rm --name n8n -p 5678:5678 -e GENERIC_TIMEZONE="Asia/Kolkata" -e TZ="Asia/Kolkata" -e   N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true -e N8N_RUNNERS_ENABLED=true -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
    ```

The above process enables you to run N8N on your local machine.

<img width="1513" height="923" alt="image" src="https://github.com/user-attachments/assets/21b59717-0a03-440e-8976-6540cb60450f" />



