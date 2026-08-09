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



