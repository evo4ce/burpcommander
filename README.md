# burpcommander
Ruby command-line interface to Burp Suite's REST API

# Usage
```
usage: commander.py [-h] [-t TARGET] [-k KEY] [-p PORT] [-n NAME] [-i ID]
                    [-U USER] [-P PASSWORD] [-s SCANURL] [-T TASKID] [-m] [-I]

PyBurp REST API interface Version 1.0.1

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        [IP Address] Defaults to 127.0.0.1
  -k KEY, --key KEY     [API Key] if you require an API key specify it here
  -p PORT, --port PORT  [Port Number] Defaults to 1337
  -n NAME, --name NAME  [String] String to search for e.g. "Command Injection"
  -i ID, --id ID        [String] String to search for e.g. "1048832"
  -U USER, --user USER  [String] username for auth scan e.g. "admin"
  -P PASSWORD, --password PASSWORD
                        [String] password for auth scan e.g. hunter1
  -s SCANURL, --scanurl SCANURL
                        [String] URL to scan e.g. "http://mysite.com"
  -T TASKID, --taskid TASKID
                        [Integer] Returns progress for a given scanid
  -m, --metrics         Returns metrics for a given taskid
  -I, --issues          [Optional Integer] Returns the issue_events for a
                        given task_id

```

# Generic Example
 python3.7 commander.py --name "Command Injection"

## Command Output
<p>Operating system command injection vulnerabilities arise when an application incorporates user-controllable data into a command that is processed by a shell command interpreter. If the user data is not strictly validated, an attacker can use shell metacharacters to modify the command that is executed, and inject arbitrary further commands that will be executed by the server.</p> 
<p>OS command injection vulnerabilities are usually very serious and may lead to compromise of the server hosting the application, or of the application's own data and functionality. It may also be possible to use the server as a platform for attacks against other systems. The exact potential for exploitation depends upon the security context in which the command is executed, and the privileges that this context has regarding sensitive resources on the server.</p>                                

# Launch a Scan
	python3.7 commander.py --scanurl http://localhost:8081

	Successfuly initiated task_id: 22 against http://localhost:8081


# Query Scan Information
Get the scan_metrics of a given scan.

	python3.7 commander.py --taskid 18 --metrics


```
{'crawl_requests_made': 1400, 'crawl_requests_queued': 0, 'audit_queue_items_completed': 27, 'audit_queue_items_waiting': 0, 'audit_requests_made': 10190, 'audit_network_errors': 37, 'issue_events': 0}
```

