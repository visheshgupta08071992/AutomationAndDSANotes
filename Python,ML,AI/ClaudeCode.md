# Claude Code

**Command to start Claude** - claude

**Command to open bash mode in Claude terminal** - Shift + 1

**Command to return from bash mode into Claude mode** - Backspace

**Command to switch between different modes of Claude(Auto/Plan)** : Shift + Tab

**Command to exit Claude CLI session** - /exit

**Understanding session**

A session is one conversation with Claude Code - everything from when you run claude to when you type /exit. Sessions are saved automatically to !!/.claude/projects/ and can be resumed at any time even after closing the terminal.

Best practices one should follow while working in a session -</br>

1.Name your session immediately - Use /rename command to rename a session. Whenever you start some work name your session using /rename command.</br>
2.One session = one task </br>
3.use /btw for  quick question: Used for quick question agar kuch develop krte waqt kuch out of context question aagya toh /btw use krna and wo question context ka part nhi banega and context pollute nhi.</br>
4.Export a session before a big refactor : Session export we can do with command /export fileName.md. The same can be used for reference to other context.</br>


A common power-user pattern is to use Opus for the planning phase — where you're thinking through architecture, writing specs, making decisions — then switch to Sonnet for the implementation phase where the thinking is done and you just need reliable code generation.

**/model** - Command is used to switch between models.

**/usage**- Used to check the usage.

**/voice**- To enable voice command

**/**- Use / command to find all the commands available

---

Here’s a cleaner, reference-friendly version in Markdown:

# Claude Session Workflow

This document summarizes the basic Claude CLI workflow for creating, managing, resuming, and exporting sessions.

## 1. Start a New Claude Session

Start Claude using:

```bash
claude
```

Once the session starts, rename it to something meaningful using:

```text
/rename <session-name>
```

**Example:**

```text
/rename playwright-automation
```

Using descriptive session names makes it easier to identify and resume sessions later.

---

## 2. Resume an Existing Session from the CLI

If you want to start Claude by resuming an existing session instead of creating a new one, use:

```bash
claude -r
```

Claude will display the available sessions. Select the appropriate session from the list to continue working from where you left off.

---

## 3. Switch to Another Session

If you are already inside a Claude session and want to resume a different session, use:

```text
/resume
```

Select the appropriate session from the displayed list.

This allows you to switch sessions without first exiting Claude.

---

## 4. Ask an Unrelated Question Without Affecting the Session

Sometimes you may want to ask Claude a question that is unrelated to the current session's work.

Use:

```text
/btw <your-query>
```

**Example:**

```text
/btw What is the difference between TCP and UDP?
```

The `/btw` command is useful for side questions because the conversation is kept separate from the main session context.

---

## 5. Exit a Session

To exit the current Claude session, use:

```text
/exit
```

Your session can be resumed later when needed.

---

## 6. Export a Session

To export the current session to a Markdown file, use:

```text
/export <filename>.md
```

**Example:**

```text
/export playwright-session.md
```

This creates a Markdown file containing the exported session.

The exported file can also be referenced from another Claude session when you want to provide context from previous work.

---

## Quick Reference

| Requirement                               | Command                  |
| ----------------------------------------- | ------------------------ |
| Start a new Claude session                | `claude`                 |
| Rename the current session                | `/rename <session-name>` |
| Start Claude and resume a session         | `claude -r`              |
| Resume another session from within Claude | `/resume`                |
| Ask a side/unrelated question             | `/btw <query>`           |
| Export the current session                | `/export <filename>.md`  |
| Exit the current session                  | `/exit`                  |

## Typical Workflow

```text
claude
   │
   ├──> /rename my-project
   │
   ├──> Work with Claude...
   │
   ├──> /btw <unrelated-question>     # Ask a side question
   │
   ├──> /export my-project.md         # Export if required
   │
   └──> /exit

Later...

claude -r
   │
   └──> Select "my-project"           # Continue previous work

OR, from an active session...

/resume
   │
   └──> Select another session        # Switch/resume another session
```

I’ve kept this focused on the commands in your original flow while making it suitable as a quick-reference document.



## What are Slash Commands?

**Slash commands** are shortcuts that you type inside a Claude Code session. They begin with a forward slash (`/`) and execute a predefined action or workflow immediately, eliminating the need to write a complete prompt.

> **Syntax**
>
> ```text
> /<command>
> ```

### Benefits

- Slash commands always start with `/`.
- They act as shortcuts for predefined actions or workflows.
- They save time by replacing long prompts with simple commands.
- Claude Code provides built-in commands out of the box.
- You can create custom commands to fit your own development workflow.

---


## Summary

| Feature | Built-in Commands | Custom Commands |
|---------|-------------------|-----------------|
| Available by default | ✅ Yes | ❌ No |
| Created by | Claude Code | User |
| Installation required | No | Yes (you create them) |
| Purpose | Common workflows | Personalized workflows |



☑ Use /branch to explore risky changes without touching main flow
☑ Use /rewind to undo bad turns without restarting everything
☑ Use /memory to persist project rules across sessions
☑ Use /compact to shrink context without losing useful progress
☑ Use /resume to continue past sessions instead of re-explaining work
☑ Use /migrate for batch refactors across matching files safely
☑ Use /handoff to write clean status notes for future-you
 
 
claude -r - : Claude will show which sessions took place and then we can select specific sessions
 
 
/resume : Agar ek session se dusre session mai jana hai toh /resume command use krna.
 
/rename : Given command help to rename a session, We should always rename a session based on the task which we are performing.
 
/btw : Used for quick question agar kuch develop krte waqt kuch out of context question aagya toh /btw use krna and wo question context ka part nhi banega and context pollute nhi.
hoga. Phir answer milne ke baad space daba do toh phir wo aapke context window ka part nhi hoga
 
 
/export fileName.md : Ye kya karega na aapke session ka export lega and md file banadega so that it can be used as a context


---

## Context Window

A context window is the amount of information that a model can see and remember at one time while generating a response. Think of it as the models working memory


Use /context command to see kitna context window consume hogya

<img width="1334" height="454" alt="image" src="https://github.com/user-attachments/assets/489e02d6-698f-4f17-aa6e-f9613ba6c848" />


Jub bhi 75% context use hogya, Better to switch context or use /compact command to shrink context



**Best Practices to while using context**
<img width="1273" height="572" alt="image" src="https://github.com/user-attachments/assets/8924666b-4283-40e6-9c6d-b57bd032fdc6" />



---

## CLAUDE.md
This video lecture provides a comprehensive guide to **CLAUDE.md**, which is considered the most important file in **Claude Code**. It serves as the project's "memory," allowing the AI to understand the context, rules, and structure of a codebase without needing repeated explanations in every session.

### 1. The Problem: LLM Memory Constraints
LLMs, by nature, do not have long-term memory of past conversations. For developers using Claude Code, this presents two main issues:
*   **Cumbersomeness:** You must repeatedly explain project details (database setup, libraries, coding conventions) every time you start a new session.
*   **Inconsistency:** Forgetting to mention a specific detail can lead to inconsistent code generation, which becomes a significant problem in large projects.

### 2. The Solution: CLAUDE.md
**CLAUDE.md** is a special project-level instruction file used to guide how Claude behaves while working on a specific codebase. 
*   It acts as a **persistent system prompt**.
*   Claude Code automatically pulls and reads this markdown file at the start of every session.
*   It eliminates the need to manually repeat project structures, build commands, and testing procedures.

### 3. Creating CLAUDE.md
There are two ways to create this file:
*   **Manual:** Create a markdown file named `CLAUDE.md` (all caps) in the project root and manually type the details.
*   **Automatic (`/init` command):** Running `/init` triggers an internal agent that scans the codebase (starting with high-signal files like `package.json` or `README.md`) to analyze the tech stack, folder layout, and naming conventions. 
    *   **Advantage of `/init`:** It is faster, identifies patterns you might miss, and is helpful when working on an unfamiliar codebase.
    *   **Note:** The generated file is often only about 30% complete; the remaining 70% (specific workflows, constraints, and conventions) must be added by the programmer.

### 4. Ideal Content of a CLAUDE.md File
A well-structured `CLAUDE.md` should include:
*   **Project Overview:** A concise (one-line) description so Claude understands the application's purpose.
*   **Architecture:** Explanation of where different logic lives (e.g., routes, schemas, services).
*   **Coding Style:** Specific conventions, such as using Python type hints or keeping functions focused.
*   **Preferred Libraries/Tools:** Explicitly stating which frameworks to use (e.g., Fast API for APIs, Pydantic for validation).
*   **Commands:** Exact commands for installation, running the dev server, and testing.
*   **Critical Roles & Constraints:** Warnings about what to avoid, such as not modifying a specific database file unless necessary.
*   **Development Roadmap:** A status-tracked list of features to help streamline the workflow across multiple sessions.

### 5. The `.claude` Folder: The "Toolbox"
The `.claude` folder acts as a configuration directory for skills, custom commands, and sub-agents.
*   **Project Level:** Located in the project root, committed to Git, and shared with the team.
*   **Global/User Level:** Located in the machine's home directory. It is personal to the developer, applies to all projects on that machine, and is not shared via Git.
*   **Contents:** Includes `settings.json`, custom `/commands`, `skills` (markdown files for specific tasks like deployment), and `agents` (for specific sub-agents like a code reviewer).

### 6. Types of CLAUDE Files
*   **`CLAUDE.md` (Root or `.claude` folder):** The primary instruction file.
*   **`CLAUDE.local.md`:** Stores personal project-level preferences that are automatically ignored by Git so they don't affect the rest of the team.
*   **User-level `CLAUDE.md`:** Located in the global home directory for personal coding styles applied across all projects.
*   **Sub-directory `CLAUDE.md`:** Useful for massive repositories; a specific folder (like `/backend`) can have its own instruction file that Claude reads only when working in that directory.

### 7. Best Practices and Maintenance
*   **Line Limit:** Keep the file under **200–300 lines**. LLM performance and instruction-following quality degrade as the context gets too large.
*   **Splitting Files:** If instructions exceed 200 lines, split them into topic-specific files (e.g., `testing.md`, `security.md`) inside a **`/rules` folder** within the `.claude` directory. These are "lazy loaded" only when needed.
*   **Living Document:** Treat it as an organic document. Refresh it after every feature, removing redundant info and adding new patterns.
*   **Codifying Errors:** If Claude makes the same mistake repeatedly, "codify" the correction by adding it to `CLAUDE.md`.
*   **Spairing Use of "IMPORTANT":** Use the word "Important" only for critical instructions; if everything is labeled important, nothing is.

### 8. Auto Memory (`memory.md`)
Claude Code features **Auto Memory**, where it silently observes and records patterns, insights, and learnings into a `memory.md` file.
*   **Example:** If Claude notices you always track expenses in INR instead of USD, it saves this insight to memory.
*   **Storage:** These files are stored in the global `.claude/projects/` directory under a specific project's folder.
*   **Relationship:** For Claude, `CLAUDE.md` (written by the programmer) and `memory.md` (written by the AI) both serve as persistent memory loaded at the start of sessions.
*   **Manual Updates:** You can prompt Claude to "update your memory files" with specific instructions at the end of a session.

<img width="1086" height="540" alt="image" src="https://github.com/user-attachments/assets/16445b53-c304-419a-a29c-3ce68318c7cd" />

<img width="1018" height="524" alt="image" src="https://github.com/user-attachments/assets/f9203712-bc4b-448f-8dc5-cb5797bec3c9" />

<img width="1139" height="537" alt="image" src="https://github.com/user-attachments/assets/f96c66e5-9f60-455f-953e-b90b65cbb45b" />



**Understaning .Claude folder**







