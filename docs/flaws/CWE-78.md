# CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection)
VeraDemo has a page called Tools, which is available at http://localhost:8080/tools

The purpose of this page is to give the user functionality to check the uptime of a host or show a fortune (literature or riddle). 


# Mitigate 
* Validate both ping and fortune functions (for validation for input)

# Remediate
* Create validation for host and use a whitelist for fortune files.

# Resources
* [CWE-78] (https://cwe.mitre.org/data/definitions/78.html)
