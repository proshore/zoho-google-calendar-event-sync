<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Zoho and Google Calendar Sync</h3>
  <p align="center">
    A Light weight system that helps to sync approved leaves from the Zoho People to Google Calendar.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]()

The project is about syncing all the approved leave will the leave type to google calendar of the organization. In order for the leave to appear in the Google Calendar the leave must be approved by all the stakeholder. This project uses Google Calendar API and webhook of Zoho People for approval in order to function properly. 

Here's why the project is created:
* Previously, when a leave was approved, it require manual entry for the leaves in the calendar 
* Time delay in entry of the leave resulted in a situation where critical meetings scheduled had to be shifted with clients


### Built With
[![Python]][Python-url]

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

For the project to run you will need to have the following:
1. Requires `credentials.json` file. [Follow here for details](#create-credentials.json)

### Installation

To locally run the project, follow the step below
1. Clone the repo
   ```sh
   git clone git@github.com:proshore/zoho-google-calandar-event-sync.git
   ```
2. Run the docker compose command, this will install all the necessary dependency and runs the docker container.
   ```sh
   docker-compose up
   ```
3. Follow the url on the output terminal to access the application, Default url should be http://127.0.0.1:5000


***
## Create credentials.json
### Enable the API
Before using Google APIs, you need to turn them on in a Google Cloud project. You can turn on one or more APIs in a single Google Cloud project.
In the Google Cloud console, enable the Google Calendar API.

[Go here to enable the API](https://console.cloud.google.com/flows/enableapi?apiid=calendar-json.googleapis.com)

### Configure the OAuth consent screen
If you're using a new Google Cloud project to complete this quickstart, configure the OAuth consent screen and add yourself as a test user. If you've already completed this step for your Cloud project, skip to the next section.

1. In the Google Cloud console, go to **Menu menu** > **APIs & Services** > **OAuth consent screen**.
[Go to OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent)

2. For **User type** select **Internal**, then click **Create**.
3. Complete the app registration form, then click **Save and Continue**.
4. For now, you can skip adding scopes and click **Save and Continue**. In the future, when you create an app for use outside of your Google Workspace organization, you must change the User type to External, and then, add the authorization scopes that your app requires.
5. Review your app registration summary. To make changes, click **Edit**. If the app registration looks OK, click **Back to Dashboard**.

### Authorize credentials for a desktop application
To authenticate end users and access user data in your app, you need to create one or more OAuth 2.0 Client IDs. A client ID is used to identify a single app to Google's OAuth servers. If your app runs on multiple platforms, you must create a separate client ID for each platform.
1. In the Google Cloud console, go to Menu > **APIs & Services** > **Credentials**. [Go to Credentials](https://console.cloud.google.com/apis/credentials)
2. Click **Create Credentials** > **OAuth client ID**.
3. Click **Application type** > **Desktop app**.
4. In the **Name** field, type a name for the credential. This name is only shown in the Google Cloud console.
5. Click **Create**. The OAuth client created screen appears, showing your new Client ID and Client secret.
6. Click **OK**. The newly created credential appears under **OAuth 2.0 Client IDs**.
7. Save the downloaded JSON file as `credentials.json`, and move the file to your working directory.


***
<!-- USAGE EXAMPLES -->
## Usage

The project also contains a postman collection in the root, that helps to understand the API properly. 

### Generate authentication token
To generate the authentication token, Please visit the following link
````
   {{baseurl}}/generate-token
````
An example can be for local development can be
````
   http://localhost:5000/generate-token
````

This token will be used to create the calendar event and the owner of the event will be the account that has generated the link. 

**Note:** _In order for the event to be created the account needs to have the proper access for creation of events._

### Create Event

_**Prerequisite:** Token must be present on the root of the project_

A post request with the following parameter must be sent to the url provided below

````
 Post |  {{baseurl}}/zoho-calendar-sync
````

| Parameters | Type   | Required | Note             |
|------------|--------|----------|------------------|
| firstName    | String | Yes      |                  | 
| lastName   | String    | Yes      |                  |
| leavesFrom      | String   | Yes      | Format:    d-M-Y |
| leaveTo      | String   | Yes      | Format:    d-M-Y |
| leaveType      | String   | Yes      |                  |
| source      | String   | No       | If not sent will take the default id from the service.py page |


<!-- USAGE EXAMPLES -->
## Deploy to PythonAnywhere

Go to the PythonAnywhere 
Select Web on the main menu
Select Flask app for the deployment
Upload the files to the server created 

Notice
On PythonAnywhere, environment variables need to be explicitly set in your web app's configuration. You cannot use a .env file directly as you might do locally unless you explicitly load it within your application using a library like python-dotenv.


_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/product-image.png
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/