To populate this directory with the necessary

### Configure Oauth 2.0 Client ID
Create a Project and Oauth Client. Follow:
* [Create Project](https://developers.google.com/workspace/guides/create-project) 
* [Create Oauth Client ID](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid) 

You will need to save the `client_secret.json` output and add it to the `/credentials` directory.

Make sure to enable the Google Cloud Resource Manager API for your project, and add the appropriate redirect URIs for running locally
```
http://localhost and http://localhost:8080
```

### Run Auth File & Generate credentials.json
With your newly added `client_secret.json` file in Step 3, run `get_api_services.py` and give Oauth consent. 

This will generate a new file, `credentials.json`, in the credentials directory and complete the Oauth flow. 