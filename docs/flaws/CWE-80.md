# CWE-80: Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) in VeraDemo
Verademo mixes untrusted data with HTML, which leads to the possibility of an attacker injecting their own HTML which gives them full control over the page.

# Mitigate
* Validate input utilizing a whitelist.

# Remediate
* Encode data using an encoder project.

# Resources
* [CWE-80](https://cwe.mitre.org/data/definitions/80.html)
