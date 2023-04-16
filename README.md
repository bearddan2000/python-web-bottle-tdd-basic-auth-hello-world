# python-web-bottle-tdd-basic-auth-hello-world

## Description
POC for bottle web framework and basic auth
using *test driven development* methodolgy.

Unit tests done in *pytest* then are covered to *allure test reports*.

Remotely tested with *testify*.

Requires basic authentication for endpoints.

| username | password |
| -------- | -------- |
| *user* | *pass* |

## Tech stack
- python
  - bottle
  - pytest
  - allure-pytest
  - testify
  - requests

## Docker stack
- python:latest

## To run
`sudo ./install.sh -u`
- Endpoint
  - curl -i localhost/ -u "user:pass"

## To stop (optional)
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
[Code based on](https://www.geeksforgeeks.org/creating-first-web-application-using-bottle-framework-python/?ref=rp)