#!/usr/bin/env python3
import argparse
import requests
import json

parser = argparse.ArgumentParser(description="PyBurp REST API interface Version 1.0.1")
parser.add_argument('-t', '--target', help='[IP Address] Defaults to 127.0.0.1')
parser.add_argument('-k', '--key', help='[API Key] if you require an API key specify it here')
parser.add_argument('-p', '--port', help='[Port Number] Defaults to 1337')
parser.add_argument('-n', '--name', help='[String] String to search for e.g. "Command Injection"')
parser.add_argument('-i', '--id', help='[String] String to search for e.g. "1048832"')
parser.add_argument('-U', '--user', help='[String] username for auth scan e.g. "admin"')
parser.add_argument('-P', '--password', help='[String] password for auth scan e.g. hunter1')
parser.add_argument('-s', '--scanurl', help='[String] URL to scan e.g. "http://mysite.com"')
parser.add_argument('-T', '--taskid', help='[Integer] Returns progress for a given scanid')
parser.add_argument('-m', '--metrics', help='Returns metrics for a given taskid', action='store_true')
parser.add_argument('-I', '--issues', help='[Optional Integer] Returns the issue_events for a given task_id', action='store_true')

args = vars(parser.parse_args())

class BurpCommander:

    def __init__(self, options):
        self.http = self.setup_http()
        self.options = options
        self.target = options['target'] if options['target'] else '127.0.0.1'
        self.port = options['port'] if options['port'] else  '1337'
        self.uri = f'http://{self.target}:{self.port}'
        self.path = f'{self.uri}/{options["key"]}/v0.1/' if options['key'] else \
            f'{self.uri}/v0.1/'
        self.issues = self.get_issues()

    def scan_progress(self):
        path = f'{self.path}scan/{self.options["taskid"]}'
        print(path)
        response = self.http.get(path).json()
        if self.options["metrics"]: return response["scan_metrics"] 

        if self.options["issues"]:
            return response["issue_events"]
        else:
            return response

    def launch_scan(self):
        path = f'{self.path}scan'
        username = self.options['user'] if self.options['user'] else ''
        password = self.options['password'] if self.options['password'] else ''
        scanurl = self.options['scanurl'] if self.options['scanurl'] else ''

        post = {
            "application_logins": [
                {
                    "username": username,
                    "password": password
                }
            ],
            "urls": [
                scanurl
            ]
        }

        post_data = json.dumps(post)
        response = self.http.post(path, post_data)

        if response.status_code == 201:
            print(f'Successfuly initiated task_id: {response.headers["location"]} against {scanurl}')
        else:
            print(f'Error launching scan against {scanurl}')

    def setup_http(self):
        request = requests
        return request
    
    def get_issues(self):
        path = f'{self.path}knowledge_base/issue_definitions'
        response = self.http.get(path).json()
        return response
    
    def issue_by_name(self, name):
        return list(filter(lambda x: name.lower() in x['name'].lower(),
            self.issues))

    def issue_by_id(self, id):
        return list(filter(lambda x: id.lower() in x['issue_type_id'].lower(),
            self.issues))

if __name__ == "__main__":
    bc = BurpCommander(args)
    print(bc.issue_by_name(args['name'])) if args['name'] else None
    print(bc.issue_by_id(args['id'])) if args['id'] else None
    bc.launch_scan() if args['scanurl'] else None
    print(bc.scan_progress()) if args['taskid'] else None
