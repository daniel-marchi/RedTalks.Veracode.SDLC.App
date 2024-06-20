# CWE-73: External COntrol of File Name or Path in VeraDemo
VeraDemo uses untrusted data while constructing file paths. This leaves the application vulnerable to malicious users uploading their own files or exfiltrating them from the filesystem. This allows for code execution or be used as a step to compromise the system

# Mitigate
* Canonicalize the file path and check directory if it matches the image directory. Check file type to ensure the file is served as a .png

# Remediate
* Don't use external data as part of the file path. Ideally map a randomly generated file name to the user so user-controlled values are never mixed with file path information.

# Resources
* [CWE-73](https://cwe.mitre.org/data/definitions/73.html)