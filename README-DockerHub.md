# VeraDemo - Blab-a-Gag

### Notice

This project is intentionally vulnerable! It contains known vulnerabilities and security errors in its code and is meant as an example project for software security scanning tools such as Veracode. Please do not report vulnerabilities in this project; the odds are they’re there on purpose :) .

## About

Blab-a-Gag is a fairly simple forum type application which allows:

- Users can post a one-liner joke.
- Users can follow the jokes of other users or not (listen or ignore).
- Users can comment on other users messages (heckle).

### URLs

- `/feed` shows the jokes/heckles that are relevant to the current user.
- `/blabbers` shows a list of all other users and allows the current user to listen or ignore.
- `/profile` allows the current user to modify their profile.
- `/login` allows you to log in to your account
- `/register` allows you to create a new user account
- `/tools` shows a tools page that shows a fortune or lets you ping a host.

## Run

Download and run the image with:

    docker run -p 8080:8080 veracode/vulnerable-verademo-java

Navigate to: `http://127.0.0.1:8080`, register as a new user, login, add some feeds and blabs.

## Other Notes

The source for this image is hosted [here](https://github.com/veracode-demo-labs/verademo-java), and within that repo are additional files that will cover both how to exploit this application and how to build this application for various CI systems.

### Exploitation Demos

See the [DEMO_NOTES](https://github.com/veracode-demo-labs/verademo-java/blob/main/DEMO_NOTES.md) file for information on using this application with the various Veracode scan types.

Also see the `docs` folder for in-depth explanations of the various exploits exposed in this application.

### CI System Demos

There are build files for various CI systems included as part of this application. Often there are several sample build files for each CI system, but there will always be at least an 'essentials' file that shows the basic steps to get the application packaged and scanned with Veracode's technology.

Note that there are some secrets that need to get set in the build files. These might vary a bit between CI systems, but generally:

- `VERACODE_API_ID` & `VERACODE_API_KEY`: The API credentials of the Veracode user account used to run the scan. See [here](https://docs.veracode.com/r/c_api_credentials3).
- `SRCCLR_API_TOKEN`: The token needed for the agent-based SCA scanner. See [here](https://docs.veracode.com/r/Integrate_Veracode_SCA_Agent_Based_Scanning_with_Your_CI_Projects).

| CI System     | "Essentials" File                                                  |
| ------------- | ------------------------------------------------------------------ |
| GitHub        | `.github/workflows/the-essentials.yml`                             |
| Azure Dev Ops | `azure-pipelines.yml`                                              |
| Jenkins       | `Jenkinsfile`                                                      |
| GitLab        | `.gitlab-ci.yml`                                                   |
| AWS           | `AWS-CodeStar.md` (directions for configuring AWS CodeStar builds) |

### Technologies Used

- Spring boot
- MariaDB

### Development

To build the container run this:

    docker pull mariadb:10.6.2
    docker build --no-cache -t verademo .

To run the container for local development run this:

    docker run --rm -p 8080:8080 --name verademo verademo

Then register as a new user and add some feeds
