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



