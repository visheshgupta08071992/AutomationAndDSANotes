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

# How to Configure Cursor to Use MCP Playwright

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

---

# How to Configure MSSQL MCP

## 📑 Reference Documents

* [Unlocking AI-powered database interactions](https://medium.com/@Daradev/unlocking-ai-powered-database-interactions-a-complete-guide-to-mssql-mcp-server-integration-134998978d4b)
* [Introducing MSSQL MCP Server (Microsoft Blog)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/)

---

### ⚙️ Steps to Follow

1. **Clone repository**

   ```bash
   git clone https://github.com/Azure-Samples/SQL-AI-samples.git
   ```

2. **Navigate to the Node.js project directory**

   ```bash
   cd SQL-AI-samples/MssqlMcp/Node
   ```

3. **Install dependencies and build the project**

   ```bash
   npm install
   ```

4. **Configure SQL Authentication**

   * Open the file:
     `SQL-AI-samples\MssqlMcp\Node\src\index.ts`
   * Search for the function `createSqlConfig`.
   * Replace the existing implementation with the following enhanced version (supports **dual authentication modes**):

   ```js
   // Function to create SQL config with fresh access token, returns token and expiry
   export async function createSqlConfig(): Promise<{ config: sql.config, token: string, expiresOn: Date }> {
     const trustServerCertificate = process.env.TRUST_SERVER_CERTIFICATE?.toLowerCase() === 'true';
     const encrypt = process.env.ENCRYPT?.toLowerCase() !== 'false'; // Default to true unless explicitly set to false
     const connectionTimeout = process.env.CONNECTION_TIMEOUT ? parseInt(process.env.CONNECTION_TIMEOUT, 10) : 30;

     // Check if USERNAME and PASSWORD are provided for SQL Server authentication
     const username = process.env.USERNAME;
     const password = process.env.PASSWORD;

     if (username && password) {
       // Use SQL Server authentication
       return {
         config: {
           server: process.env.SERVER_NAME!,
           database: process.env.DATABASE_NAME!,
           user: username,
           password: password,
           options: {
             encrypt,
             trustServerCertificate
           },
           connectionTimeout: connectionTimeout * 1000, // convert seconds to milliseconds
         },
         token: 'sql-auth', // placeholder token for SQL auth
         expiresOn: new Date(Date.now() + 24 * 60 * 60 * 1000) // 24 hours from now
       };
     } else {
       // Use Azure AD authentication
       const credential = new InteractiveBrowserCredential({
         redirectUri: 'http://localhost'
         // disableAutomaticAuthentication : true
       });
       const accessToken = await credential.getToken('https://database.windows.net/.default');

       return {
         config: {
           server: process.env.SERVER_NAME!,
           database: process.env.DATABASE_NAME!,
           options: {
             encrypt,
             trustServerCertificate
           },
           authentication: {
             type: 'azure-active-directory-access-token',
             options: {
               token: accessToken?.token!,
             },
           },
           connectionTimeout: connectionTimeout * 1000, // convert seconds to milliseconds
         },
         token: accessToken?.token!,
         expiresOn: accessToken?.expiresOnTimestamp ? new Date(accessToken.expiresOnTimestamp) : new Date(Date.now() + 30 * 60 * 1000)
       };
     }
   }
   ```

5. **Rebuild the project**
   After implementing the code changes, rebuild to regenerate `dist/index.js`:

   ```bash
   npm run build
   ```

6. **Add MCP Config File (inside Cursor)**
   Add the following configuration to allow MCP to connect to the database:

   ```json
   "mssql": {
     "command": "node",
     "args": [
       "C:\\Users\\guptvis\\OneDrive\\OneDrive - MSCI Office 365\\Desktop\\VisheshProjects\\AI-MCPProjects\\SQL-AI-samples\\MssqlMcp\\Node\\dist\\index.js"
     ],
     "env": {
       "SERVER_NAME": "{serverName}",
       "DATABASE_NAME": "{databaseName}",
       "USERNAME": "{userName}",
       "PASSWORD": "{password}",
       "ENCRYPT": "false",
       "TRUST_SERVER_CERTIFICATE": "true",
       "READONLY": "true"
     }
   }
   ```

---


## How to Configure FileSystem MCP Server

**GitHub Repository**: [FileSystem MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)

**Purpose of FileSystem MCP Server**

The FileSystem MCP server can be used for:

* Read/write files
* Create/list/delete directories
* Move files/directories
* Search files
* Get file metadata
* Dynamic directory access control via **Roots**

**File System MCP JSON Configuration**

Here, `args` contains the path where the file will be present or where the file needs to be written.

```json
"filesystem": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "C:\\Users\\guptvis\\OneDrive\\OneDrive - MSCI Office 365\\Desktop\\VisheshProjects\\AI-MCPProjects"
  ]
}
```

## How to Configure Excel MCP Server


**GitHub Repository**: [Excel MCP Server](https://github.com/negokaz/excel-mcp-server)

**Purpose of Excel MCP Server**

The Excel MCP server can be used for:

* Read/Write text values
* Read/Write formulas
* Create new sheets
* Capture screen image from a sheet
* Live editing

**Excel MCP server Json Configuration**

```json

 "excel": {
            "command": "cmd",
            "args": ["/c", "npx", "--yes", "@negokaz/excel-mcp-server"],
            "env": {
                "EXCEL_MCP_PAGING_CELLS_LIMIT": "4000"
            }
        }


```

---

# Understanding Microsoft Autogen Framework

**Autogen** is an open-source multi-agent orchestration framework that helps you build applications where multiple AI agents collaborate with each other (and optionally humans) to solve tasks.  

It provides abstractions to:

- **Create agents with roles**
- **Enable structured conversations between agents**
- **Integrate external tools and APIs**
- **Manage multi-step workflows**

# Setting up Autogen

**Documentation Link** - https://microsoft.github.io/autogen/stable//user-guide/agentchat-user-guide/installation.html

Autogen suggests  using a virtual environment for the installation. This will ensure that the dependencies for AgentChat are isolated from the rest of your system.

<img width="1503" height="606" alt="image" src="https://github.com/user-attachments/assets/5db7d649-f18a-4a02-aedb-6e2f03c5a9fe" />


Once Project is setup within the IDE, You need to install all the packages required for setting up AutoGen Framework

Install Below packages:

**pip install -U "autogen-agentchat"**  - For installing autogen Agent-Chat

**pip install "autogen-ext[openai]"** - To use OpenAI models

**pip install "autogen-ext[azure]"** - To use Azure OpenAI models

**pip install -U "autogen-ext[mcp]"** - To use MCP within Agent


You can check the installed packages by going to **settings -> project -> Python Interpreter**

<img width="1217" height="897" alt="image" src="https://github.com/user-attachments/assets/152fdf27-4a71-4a63-8b5d-f895b2128390" />













