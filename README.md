# Introduction

Polland is a simple polling system geared towards facilitating the information gathering phase of general poll-like surverys in a community. It at it's core uses Django as backend solution and is integrated with Mattermost - because as the time of writing the initial version of Polland, the main communication channel between it's users was Mattermost.

## How to compile

First make sure you have the latest version of python 3 [installed](https://realpython.com/installing-python/) and accessible in your terminal of choice.

:exclamation: *Use of python virutal environment is recommended*

In your terminal of choice, issue the following command:

`pip install -r ./requirements.txt`

## Modules

### Phase 1

* Mattermost bot capable of listing questions and marking users answers for specific question.
* Administrative Web UI for managing users/questions/answers/etc.
* Support of multiple-choice questions