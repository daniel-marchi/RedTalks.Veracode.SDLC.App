# CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') in VeraDemo
VeraDemo uses untrusted data concatenation of SQL queries. This leaves the application vulnerable to malicious users injecting their own SQL components.

# Mitigate
* Utilize a whitelist to ensure data contains alphanumeric characters

# Remediate 
* Query data using prepared statements

# Resources 
* [CWE-89](https://cwe.mitre.org/data/definitions/89.html)