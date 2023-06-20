## Routine for Managing Firebase Projects

### Prerequisites
- Git repository with multiple branches, each corresponding to a Firebase project.
- `google-services.json` file containing the `project_id` value for each branch.
- Firebase credentials with appropriate access to manage projects and access the Firebase Management API.

### Steps

1. **Switch Git Branch**
    - Use Git commands to switch to the desired branch corresponding to the Firebase project you want to manage.

2. **Read `google-services.json`**
    - Read the contents of the `google-services.json` file to extract the current `project_id` value.

3. **Access Firebase Management API**
    - Make an HTTP request to the Firebase Management API to retrieve a list of all Firebase projects associated with your account.
        - API Endpoint: `GET /v1beta1/projects`

4. **Iterate over Projects**
    - Iterate over the projects returned by the API and compare the `project_id` from `google-services.json` with the `project_id` of each Firebase project.
    - Find the matching project based on your criteria (e.g., name or pattern matching).

5. **Check Android App Domain**
    - Make another API call to Firebase to retrieve the list of Android apps registered under the identified project.
      - API Endpoint: `GET /v1beta1/{project}/androidApps`

6. **Verify App Domain Registration**
    - Iterate over the list of Android apps and check if the desired app domain is registered for any of them under the app nickname.
    - Compare it against the registered domains to determine if the app domain is present.

7. **Perform Filter Action**
    - Check if in the (firebase project_code) and (google-services.json project_id) is equals
    - Check in the (firebase package_name) structure if the (google-services.json project_id) came first or at the end and determine if it's V4 or V5.
        - for example if it's `bercarioescolacrescerkids.terasmart.terabytesolucoes.com.br` or `br.com.terabytesolucoes.terasmart.bercarioescolacrescerkids` in this case the first is V5 and the second V4.

### Language and Tools
- Programming Language: Python
- Libraries and Tools: Git commands, Python's `requests` library for HTTP requests, `json` module for JSON parsing, and any other necessary dependencies.