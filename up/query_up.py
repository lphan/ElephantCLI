#!/usr/bin/env python

from bbp_client.oidc.client import BBPOIDCClient
from bbp_services.client import get_services, get_environments
from bbp_client.client import Client
import json

user = ""


def parse_args(*args):
    """ parse arguments from input
        call functions. Use decorator for calling authenticate_oidc
    """
    command = args[0]
    cl = authenticate_oidc()
    # Authentication using oidc protocol
    if command == 'get_task':
        print "Calling get_task function ..."
        data = get_task_name(cl)
        print data
        # Write content of data to json-file
        filename = 'logging/'+'task.json'
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)
    elif command == 'get_all_tasks':
        data = get_all_tasks(cl)
        print data
        filename = 'logging/'+'alltask.json'
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)


def authenticate_oidc():
    """ Authentication to OIDC Service
    """
    # TODO: decorator authentication
    global user
    user = raw_input("Username of Gaspar's account ")
    services = get_services()
    env = get_environments()
    oauth_url = services['oidc_service'][env[0]]['url']
    # print oauth_url
    # TODO: try ... catch exception
    BBPOIDCClient.implicit_auth(user, oauth_url=oauth_url)
    # root token can get expired, need to login again with Gaspar-pass

    # create Client-instance
    cl = Client.new()
    return cl


def get_task(client, task_id):
    """ Query information of task base on task_id
    """
    # get task
    # task_id = 'af559194-6fca-11e4-aaa5-0050569773f6'
    l = client.get_task(task_id)

    # retrieve all properties of the task
    properties = l.info
    print "Retrieve value of task ", task_id
    print "Task-id --> All Attributes of task as json-file", properties

    # properties has format dict
    print "\n"
    key = raw_input("Input Key to get Value: ")
    result = key in properties
    if result is True:
        value = properties.get(key)
        print "\n"
        print "Task-id --> Value = ", value
    else:
        print "Input key does not exist"

    # Other way to get properties of task with task_id

    return client.task.get_task(task_id)


def get_task_name(client):
    """ Get properties of task base on task_name
    """
    task_name = raw_input("Input task_name ")
    return client.task.get_tasks(task_name)


def get_all_tasks(client):
    """ Get list of all tasks visible to user
    """
    print "\n"
    print "User "+user+" --> get list of visible all task_id"
    temp_list = []
    s = client.get_tasks()
    for i in range(len(s)):
        temp = s.pop()
        temp_list.append(temp.task_id)

    print temp_list

    # With task_id is feasible to get all information about task

    # Other way to get list of all tasks
    lt = client.task.get_tasks()
    return lt


def get_host(client):
    return client.task.host


def get_all_jobs(client):
    """ Get all jobs visible for this user
    """
    # Other way to get all jobs
    # print "4.2 All Jobs ", cl.task.get_jobs()
    return client.get_jobs()


def get_job_id(client, job_id):
    """ Get specific job name with job_id
    """
    # ex. job_id = 'a77615e6-6fcc-11e4-aaa5-0050569773f6'
    print "Job_id", job_id
    return client.get_job(job_id)

# TODO: to get result from the already done job_id"
# TODO: update a task with new properties
# TODO: save information to json-file
