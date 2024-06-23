# Demo Notes

Notes, tips, and hints for using the various Veracode scan types with this application.

Also see the `docs/flaws` folder for in-depth explanations of the various exploits exposed in this application.

## Static scanning

Build the app:

	cd app
	mvn clean package

The `app/target/verademo.war` file is the built app.  This is the file to be used for scanning.  Either upload this file to the Veracode platform for a Policy/Sandbox scan, or use it with the Veracode Pipeline scan.

## SCA scanning

### Upload/Scan

This will just happen as part of the Policy or Sandbox scan.

### Agent-based scan

Use either the command-line version of the SCA agent (follow the install and config instructions in the Veracode [docs center](https://docs.veracode.com/r/c_sc_what_is) ) or the IDE plugin to initiate an SCA scan.

### Vulnerable Methods

The Veracode agent-based SCA scan can also find [vulnerable methods](https://docs.veracode.com/r/Finding_and_Fixing_Vulnerabilities#fixing-vulnerable-methods).  In this app, there is a vulnerable version of the bcrypt library called from both the `User` and `UserController` classes.

### SBOM generation

SBOM generation for the application is supported after an SCA scan ([link](https://docs.veracode.com/r/Generating_a_Software_Bill_of_Materials_SBOM_for_Upload_Scans)) 

SBOM generation for the Docker container is supported by the Container/CLI scanner ([link](https://docs.veracode.com/r/veracode_sbom)).

## Veracode Fix

This application has flaws that can be fixed with [Veracode Fix](https://docs.veracode.com/r/veracode_fix).  For an example of one:

### Build the app

	cd app
	mvn clean package

### Run the Veracode Pipeline scanner

	java -jar ${path-to-pipeline-scanner}/pipeline-scan.jar -f target/verademo.war -esd true 

### Run Veracode Fix

	veracode fix src/main/java/com/veracode/verademo/controller/UserController.java

The first flaw is an SQL Injection around line 170 that can be Fixed.

To verify the fix re-build the app and re-run the Pipeline scanner. 

## Container scan

From the root of the project run the Veracode container scanner:

	veracode scan --type directory --source . --output container_results.json	