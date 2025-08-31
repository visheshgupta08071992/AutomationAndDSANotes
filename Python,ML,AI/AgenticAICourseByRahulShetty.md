# AI Agents with AutoGen

**Course Link** : https://www.udemy.com/course/agentic-ai-for-automation-multi-agent-autogen


**What is LLM** - A Large Lanuguage Model is an AI system trained on large set of data capable of understanding and generating human like language for diverse tasks.

**What is AI Agents and how it is different from LLM**

Imagine you need to apply for a passport.

One way is to **search on Google** or **ask an LLM** about the process. You’ll get the steps, documents required, and where to apply. But after gathering this knowledge, **you still need to do all the work yourself**—filling forms, submitting documents, and following up.

Now, consider using a **passport agent**. The agent already knows the entire process. Instead of you doing everything, the agent **handles the application on your behalf**—submitting forms, coordinating with the office, and delivering the passport to you. Your effort is minimal, and the task gets done.

This is similar to how **AI Agents** work. Instead of just providing information, AI Agents can **act on your behalf** using their knowledge and tools.

* A **Personal Assistant Agent** might compare prices and book a flight for you.
* A **Code Agent** could debug and fix issues in your repository.
* A **Data Analyst Agent** might automatically generate your monthly sales report.

In short: **LLMs give you the knowledge, but AI Agents use that knowledge to get the job done.**


<img width="1048" height="419" alt="image" src="https://github.com/user-attachments/assets/2b047f40-35dc-4f53-93ca-9f56d347372a" />


## Understanding MCP

MCP is Model Context Protocol which is a Standardized way for AI agents to connect to and use external tools and services. IDEs like Cursor,VsCode,Claude Desktop are all MCP Clients through which we can connect to MCP Servers and then to respective tool.

 **How does MCP Client and Server works:**
 
 
   1.There are different MCP Clients like Claude Code, Cursor , VS Code.</br>
 
 2. These MCP clients are configured to various MCP servers like Playwright,MYSQL , Excel by configuring respective MCP server json.</br>
 
 3. Once these MCP server json are configured within the MCP client , These MCP servers are started with help of config file.</br>
 
 4. Once the MCP server is starterd ,LLM uses MCP protocol to communicate with various tools</br>


![image](https://github.com/user-attachments/assets/c2e79f69-e4e8-479c-a2cb-73eda75b0f56)


![image](https://github.com/user-attachments/assets/2aa84a5e-d9c2-4bbd-85a6-619f794e83e7)

![image](https://github.com/user-attachments/assets/a75961a7-85f2-4c0e-81f8-286744ba6e3b)

![image](https://github.com/user-attachments/assets/d171884b-ff10-4a4f-ae97-59bd2eb2da64)


**There are different types of MCP servers available for connecting to different tools like Playwright MCP,MySQL MCP , RestAPI MCP ,Excel MCP,FileSystem MCP**


<img width="1442" height="863" alt="image" src="https://github.com/user-attachments/assets/9b201c4b-95fd-40e9-93a3-7aa2e6e38dbb" />

---

## How to Configure Cursor to Use MCP Playwright

**1. Get the Playwright MCP Config**
- Search for **Playwright MCP** on Google and open the [official GitHub repository](https://github.com/microsoft/playwright-mcp).
- Copy the configuration file required to set up the Playwright MCP server.

![Playwright MCP Config](https://github.com/user-attachments/assets/70917d58-8fb6-40a5-ba38-9cecf10ee87f)


**2. Explore MCP Tools**
- Each MCP server exposes a set of **tools**.  
- Tools are essentially functions that the MCP server can perform.  
- Below is a snapshot of the tools exposed by the Playwright MCP server:

![Playwright MCP Tools](https://github.com/user-attachments/assets/1b73bcc1-3a17-4bab-939f-ad05eb5ac987)


**Add MCP Server in Cursor**
1. Go to **Settings → MCP & Integrations → New MCP Server**.
2. Paste the configuration JSON you copied earlier.
3. Once added, you can view the different tools exposed by the Playwright MCP server.

Example screenshots:

![MCP Server Added](https://github.com/user-attachments/assets/f924536e-0702-4fe5-b01f-6d08380fbbfa)

![Playwright MCP Tools in Cursor](https://github.com/user-attachments/assets/c3281ab0-0c3e-407c-9e64-a6dc4477b398)



   


   
 






