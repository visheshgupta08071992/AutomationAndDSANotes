## Understanding GithubActions

**GitHub Actions** is a powerful automation tool provided by GitHub that allows you to define custom workflows to automate various tasks in your software development process. These workflows are defined in `.yml` files, called GitHub Action workflow files, and are stored in a `.github/workflows` directory in your repository. GitHub Actions can be used for building, testing, deploying, and more.

**Terminologies:**

1. **Workflow**: A workflow is a defined set of automated steps that run on specific events in your repository (e.g., push, pull request, release, etc.). It's defined in a YAML file and can include multiple jobs.

2. **Job**: A job is a set of steps that run sequentially on the same runner (a virtual machine or container). A workflow can contain one or more jobs, each with its own set of steps.

3. **Step**: A step is an individual task within a job. Steps can be shell commands, actions, or other scripts.

4. **Action**: An action is a reusable unit of code that you can use in your workflows. It can be created by GitHub, the community, or you. Actions can simplify complex tasks and enhance your workflows.

**Example:**

Here's a simple example of a GitHub Action workflow to build and test a Node.js project:

```yaml
name: Node.js CI

on: [push]  # Trigger the workflow when a push event occurs

jobs:
  build:
    runs-on: ubuntu-latest  # Use the latest version of the Ubuntu runner

    steps:
    - name: Check out code
      uses: actions/checkout@v2  # This action checks out the repository

    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'  # Install Node.js 14.x

    - name: Install dependencies
      run: npm install

    - name: Run tests
      run: npm test
```

In this example:
1. The workflow is triggered on every push event.
2. The workflow has a single job named "build" that runs on an Ubuntu runner.
3. The steps within the job:
   - Check out the code using the `actions/checkout` action.
   - Set up Node.js using the `actions/setup-node` action.
   - Install project dependencies.
   - Run tests using the `npm test` command.

**Sample GitHub Action Template File:**

```yaml
name: My Custom Action

on: [push]  # Trigger the workflow on push event

jobs:
  my-job:
    runs-on: ubuntu-latest

    steps:
    - name: Check out code
      uses: actions/checkout@v2

    - name: Run custom script
      run: |
        echo "Hello, GitHub Actions!"
```

This example defines a simple GitHub Action named "My Custom Action" that echoes a message when a push event occurs. This action can be used as a building block within your larger workflows.


## Triggers

In GitHub Actions, triggers are events that initiate the execution of a workflow. When a trigger event occurs in your GitHub repository, such as a push, pull request, or a scheduled time, the associated workflow is automatically started. There are several types of triggers available in GitHub Actions:

1. **Push Trigger**: This trigger runs the workflow when there is a push event to the repository. This includes pushes to any branch or tag.

   Example:
   ```yaml
   on:
     push:
       branches:
         - main
   ```

2. **Pull Request Trigger**: This trigger runs the workflow when a pull request is created or updated, including pushes to the branches associated with the pull request.

   Example:
   ```yaml
   on:
     pull_request:
       branches:
         - main
   ```

3. **Schedule Trigger**: This trigger allows you to schedule workflows to run at specific times or intervals, even if there are no code changes. It's useful for regular maintenance tasks.

   Example:
   ```yaml
   on:
     schedule:
       - cron: '0 0 * * *' # Run every day at midnight
   ```

4. **Repository Dispatch Trigger**: This trigger lets you trigger workflows using a custom event from outside the repository. It's useful when you want to trigger a workflow from an external event.

   Example:
   ```yaml
   on:
     repository_dispatch:
       types: [custom-event]
   ```

5. **Workflow Dispatch Trigger**: This trigger allows you to manually trigger a workflow run using the GitHub API. It's useful for running workflows on-demand.

   Example:
   ```yaml
   on:
     workflow_dispatch:
   ```

6. **Webhook Trigger**: This trigger runs the workflow when a specific webhook event occurs, which can be useful for integrating with other services or systems.

   Example:
   ```yaml
   on:
     push:
       branches:
         - main
     issue_comment:
       types: [created]
   ```

7. **External Triggers**: Some actions or events in GitHub, such as a new release being published, can indirectly trigger workflows. These are based on specific events within GitHub itself.

These trigger types can be combined, customized, and configured to create workflows that fit your specific use case. You can define triggers in the `on` section of your workflow YAML file to specify when the workflow should run.


## Contexts

In GitHub Actions, **contexts** are predefined environment variables that provide information about the GitHub and workflow runtime environment. These variables are available for use within your workflow configuration file (YAML) and can be accessed as placeholders for specific information.

Contexts are particularly useful when you need to access information about the repository, the workflow run, the current event, or the runner environment. They enable you to make dynamic decisions or customize the behavior of your workflows based on the context in which they run.

Here are a few common contexts and their descriptions:

1. **`github`**: Provides access to various GitHub-related properties and information.

2. **`runner`**: Provides information about the runner (the machine or container running the workflow).

3. **`job`**: Provides information about the current job within the workflow.

4. **`steps`**: Provides information about the current step within a job.

5. **`matrix`**: Provides information about the matrix configuration (used when defining matrix builds).

**Example**:

Let's say you want to create a workflow that automatically comments on a pull request with the name of the person who opened the pull request. You can use the `github` context to access the pull request information.

```yaml
name: Comment on Pull Request

on:
  pull_request:
    types:
      - opened

jobs:
  comment-on-pull-request:
    runs-on: ubuntu-latest

    steps:
    - name: Check out code
      uses: actions/checkout@v2

    - name: Comment on pull request
      uses: actions/github-script@v4
      with:
        github-token: ${{ secrets.GITHUB_TOKEN }}
        script: |
          const pullRequestAuthor = github.context.payload.pull_request.user.login;
          github.issues.createComment({
            issue_number: github.context.payload.pull_request.number,
            owner: github.context.repo.owner,
            repo: github.context.repo.repo,
            body: `Thanks, @${pullRequestAuthor}, for opening this pull request!`
          });
```

In this example, the `github.context.payload.pull_request.user.login` expression accesses the login name of the user who opened the pull request. This context information is used to customize the comment message.

Contexts allow you to make your workflows more dynamic and adaptable based on the runtime environment and the specific events triggering the workflow. They help you leverage essential information to automate tasks effectively.


**Sample yaml file with comments explaining different contexts in Workflow**

```yaml
# Set the name of the workflow
name: context demo

# Define the events that trigger the workflow
on:
  # Manually trigger the workflow with a text input
  workflow_dispatch:
    inputs:
      text:
        description: 'enter the word you want to print'
        default: 'Hello'
        required: true
        type: string

# Define environment variables
env:
  # Define a variable 'firstName' with the value 'Amuthan'
  firstName: 'Amuthan'
  # Define a variable 'website' with the value 'testing mini bytes'
  website: 'testing mini bytes'

# Define jobs to be executed
jobs:
  # Job named 'contexts-demo'
  contexts-demo:
    timeout-minutes: 5
    continue-on-error: false
    # Use a Docker container as the job's environment
    container:
      image: alpine:latest
    # Specify the operating system for the job to run on
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest]
    steps:
      # Print the input text provided when manually triggering the workflow
      - run: echo ${{ inputs.text }}
      # Print the input text using GitHub event context
      - run: echo ${{ github.event.inputs.text }}
      # Print the GitHub actor (user who triggered the workflow)
      - run: echo ${{ github.actor }}
      # Print a message with the value of the 'firstName' environment variable
      - run: echo 'Hi ${{ env.firstName }}'
      # Print a message with the value of the 'website' environment variable
      - run: echo 'website - ${{ env.website }}'
      # Print the status of the current job
      - run: echo ${{ job.status }}
      # Print the operating system of the runner
      - run: echo ${{ runner.os }}
      # Print the value of a secret named 'PASSWORD' and the value of the 'firstName' environment variable (overridden)
      - run: echo ${{ secrets.PASSWORD }} ${{ env.firstName }}
        env:
          # Override the 'firstName' environment variable for this step
          firstName: 'Testing'

  # Job named 'contexts-demo-2' that depends on the 'contexts-demo' job
  contexts-demo-2:
    needs: [contexts-demo]
    runs-on: ubuntu-latest
    steps:
      # Print a message indicating that this job is running after the 'contexts-demo' job
      - run: echo 'contexts-demo-2 running after contexts-demo'

  # Job named 'job3'
  job3:
    runs-on: ubuntu-latest
    # Condition to run this job always
    if: ${{ always() }}
    # This job depends on the 'contexts-demo' job
    needs: [contexts-demo]
    steps:
      # Print a message indicating that this is 'job3'
      - run: echo 'job3'

  # Job named 'job4'
  job4:
    runs-on: ubuntu-latest
    # Condition to run this job when the previous job (contexts-demo) fails
    if: ${{ failure() }}
    # This job depends on the 'contexts-demo' job
    needs: [contexts-demo]
    steps:
      # Print a message indicating that this is 'job4'
      - run: echo 'job4'

```

## Jobs and Steps

A workflow run is made up of one or more jobs which run in parallel by default. To run jobs sequentially, you can define dependencies on other jobs using the needs keyword.Jobs are composed of one or more number of steps.
