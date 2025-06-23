# Project Setup Guide

This project utilizes [n8n](https://n8n.io), a powerful workflow automation tool. It creates an AI agent capable of scrapping data from a [sample faq website](https://www.motivi.com/fr_FR/faq) open to web-scrapping and accessing a Postgres database through an MCP server.  
You can now search the database using natural language thanks to PostgreSQL’s powerful full text search. This makes it easier for the AI agent to find relevant products based on keywords in names, descriptions, ingredients, or skin tone compatibility.
## Prerequisites

Before getting started, ensure you have the following installed on your system:

- **[Docker](https://docs.docker.com/get-docker/)**
- **[Git](https://git-scm.com/)**

## Getting Started

### Step 1: Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone "https://github.com/mohamedali05/AI-Agent-using-a-database-and-a-web-scrapping-tool"
```


```bash
cd AI-Agent-using-a-database-and-a-web-scrapping-tool
```


### Step 2: Launch the n8n Container

In a terminal, run the official n8n Docker container:



```bash
docker volume create n8n_data
```

```bash
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```

This command will:
- Start n8n on port 5678
- Create a persistent data volume for your workflows
- Run the container interactively

### step 3 : copy the workflow : 

Once n8n is running:
- Create a new workflow via the n8n interface.

- Open the workflow.json file in this repository.

- Copy its content and paste it into the workflow editor.

### Step 4: Start the MCP Server

In a **second terminal**, navigate to your project directory and start the MCP server using Docker Compose:

```bash
docker-compose up --build
```

This will run the MCP server that exposes the tools to access to the sample database so that the AI agent can read through it 




### Step 5: Configure OpenAI Credentials

To integrate with OpenAI services:

1. Access your n8n instance at `http://localhost:5678`
2. Follow the [official n8n OpenAI credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/openai/)
3. Add your OpenAI API key to establish the connection

### Step 6: Configure Supabase Credentials

Set up your Supabase database connection using the following credentials:

- **Host**: `https://cpvqgnhjzfzdtyiozrjq.supabase.co`
- **Service Role Key**: 
  ```
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNwdnFnbmhqemZ6ZHR5aW96cmpxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0ODkzNjkwOCwiZXhwIjoyMDY0NTEyOTA4fQ.nuQNiT43OWzvdsvHRfxOORds1v-t8XmXsV1F5Pszgec
  ```

### Optional : Configure your ports 
If the default ports are already in use on your machine, you can easily update them:

- **Edit the .env file** located in the project root:

- Change the port numbers defined there.

- If you have modified the MCP server's port, be sure to update it in the "MCP Client Tool" node within the n8n workflow (see the image below for reference).

<p align="center">
  <img src="images/MCP_node_n8n.png" alt="n8n workflow demo" width="200"/>
</p>

### step 7 : Interact with the AI Agent ! 


You can test the AI agent either directly within the n8n workflow or through a simple web interface:

- **First**, make sure to **activate the workflow** (using the toggle switch at the top right of the n8n editor).

-  Then, open the `index.html` file located in the `front-end/` folder with your browser to interact with the agent via the web demo.