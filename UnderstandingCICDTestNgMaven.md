# Understanding Continuous Integration, Continuous Deployment, TestNG and Maven

## Continuous Integration
Continuous Integration (CI) is a practice of continuously integrating code from multiple developers into a shared centralized repository. With CI, every code check-in or pull request is verified by an automated build process, which includes running Sonar Code Analysis,unit and integration tests. 

- **If the tests pass**, the build succeeds.
- **If the tests fail**, the build fails, providing continuous feedback to developers on their code changes.

### Example in Our Company
In our company, whenever a developer pushes their changes to our centralized repository (Azure), an automated build is triggered. This process includes:
- Running **unit tests**
- Running **integration tests**
- Performing **Sonar checks**

If all these checks pass, the build is marked as successful.

---

## Continuous Deployment
Continuous Deployment (CD) is a practice of continuously deploying any code change that passes the CI process to higher environments and ultimately to the production environment.

### Current Workflow in Our Company
In our company, we do not have a fully automated continuous deployment process. Instead, we follow these steps:

1. **Code Push or Pull Request Raised**  
   - When a developer pushes code or raises a pull request, a CI setup is triggered.  
   - This automated build process includes:
     - Running **unit tests**
     - Running **integration tests**
     - Performing **Sonar checks**
   - If all checks pass, the build is successful.

2. **Pull Request Review**  
   - Once the build is successful, the pull request undergoes a **PR review process**.  
   - After approval, the changes are merged into the `master` branch.

3. **Deployment to Dev Environment**  
   - Once changes are merged into the `master` branch, an **automated pipeline** is triggered to deploy the code to the **Dev environment**.  
   - After deployment, an **Automated Regression Pipeline** is triggered. This is configured to automatically run whenever the **release pipeline for DEV** is completed.

4. **Manual Testing and Higher Environment Deployment**  
   - After manual feature testing in the Dev environment, the code is **manually deployed** to higher environments such as **UAT** or **Prod**.  
   - On UAT, a **Sanity Regression Pipeline** is auto-triggered once the build is deployed. This is achieved by configuring a trigger to run the regression pipeline whenever the **release pipeline for UAT** is completed.

---

## TestNG
[Add TestNG-specific details here, if required.]
