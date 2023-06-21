## Routine for Managing Firebase Projects

### Prerequisites
- Git repository with multiple branches, each corresponding to a Firebase project.
- `google-services.json` file containing the `project_id` value for each branch.
- Firebase credentials with appropriate access to manage projects and access the Firebase Management API.

### Steps
0. **Define standards**
    - appDomain is the name of the branch of the base project
    - crossDomain is the name of the `project_id` under `google-services.json` in the base project
    - firebaseProject is the is the id of a project under the firebase account
    - patternDomain is the firebase package_name of a android app under the firebase project
1. **Switch Git Branch**
    - Use Git commands to loop through to all branch except selected one such as main, hmg, dev.

2. **Get the crossDomain**
    - Read the contents of the `google-services.json` file from the base project to extract the current `project_id` value.

3. **Access Firebase Management API and Get the firebaseProject list**
    - Make an HTTP request to the Firebase Management API to retrieve a list of all Firebase projects associated with your account.
        - API Endpoint: `GET /v1beta1/projects`

4. **Iterate over Projects**
    - Iterate over the firebaseProject list returned by the step 3 and compare with crossDomain.
    - Find the matching firebaseProject and set as selected identified one.

5. **Check Android App Domain**
    - Make another API call to Firebase to retrieve the list of Android apps registered under the identified project from step 4.
      - API Endpoint: `GET /v1beta1/{project}/androidApps`

6. **Verify App Domain Registration**
    - Iterate over the list of Android apps and check if the crossDomain is registered for any of them under the app nickname.
    - Compare it against the (firebase app_nickname) to determine if the git branch name is present.

7. **Perform Filter Action**
    - Check in the (firebase package_name) structure if the appDomain came first or at the end and determine if it's V4 or V5.
        - for example if it's `bercarioescolacrescerkids.terasmart.terabytesolucoes.com.br` or `br.com.terabytesolucoes.terasmart.bercarioescolacrescerkids` in this case the first is V5 and the second V4.
8. **Build the answer**
    - Construct a dictiorary where each branch is a key and the value is a list of dictionary pair where each of the pairs is a crossDomain and the version type.
9. **Check the goal**
    - the goal is to find ambiguity such as 
    -   ```python
        {'bercarioescolacrescerkids' : [{'escolar-manager-smart':'V5'}, {'escolar-manager-smart-3':'V4'}]} 
        #or
        {'bercarioescolacrescerkids' : [{'escolar-manager-smart':'V5'}, {'escolar-manager-smart-3':'V5'}]}
        ```
### Language and Tools
- Programming Language: Python
- Libraries and Tools: Git commands, Python's `requests` library for HTTP requests, `json` module for JSON parsing, and any other necessary dependencies.