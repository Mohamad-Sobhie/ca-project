import os
import json
import requests

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
<<<<<<< HEAD
<<<<<<< HEAD
USERNAME = 'nimaeivazzadeh'
=======
USERNAME = 'hassansamat'
PASSWORD = os.environ['GITHUB_PASSWORD']
>>>>>>> d85b0f274176c29ca1e705798a1ce3d776bc8612
=======
<<<<<<< HEAD
USERNAME = 's336378'
EXPORT_PASSWORD = os.environ['GITHUB_PASSWORD']
=======
USERNAME = 'Mohamad-Sobhie'
>>>>>>> 120801921d771d2f92f2d3f5896c8c359ae336a2
PASSWORD = os.environ['GITHUB_PASSWORD']
>>>>>>> 113b53c3bd4d6455c4e7f3c7f17b314bbb2c9131
>>>>>>> 22c8f5905dd1ce86aad69f61b1eda7aa4bce2d9d


# The repository to add this issue to
REPO_OWNER = 'Mohamad-Sobhie'
REPO_NAME = 'ca-project'


def make_github_issue(title, body=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    # Create our issue
    issue = {'title': title,
             'body': body,
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print 'Successfully created Issue "%s"' % title
    else:
        print 'Could not create Issue "%s"' % title
        print 'Response:', r.content

make_github_issue('Enable Waffle', 'Setup Waffle and close this issue', ['task'])
make_github_issue('Investigate Python dependencies', 'Fill out requirements.txt', ['task'])
make_github_issue('Install python dependencies', 'Using pip, may require sudo', ['task'])
make_github_issue('Familiarize yourself with CoDe Chan', '', ['task'])
make_github_issue('Create Dockerfile', 'Create a Dockerfile, based on ubuntu and installing pip, requirements and running the run.py', ['task'])
make_github_issue('Build Docker image', '', ['task'])
make_github_issue('Run the app using the docker container', '', ['task'])
make_github_issue('Setup a Jenkins master', '', ['task'])
make_github_issue('Setup a pipeline for CI', '', ['task'])
make_github_issue('Run the tests in the pipeline', '', ['task'])
make_github_issue('Create a script for local', '', ['task'])
make_github_issue('Augment script to hit multiple deploy targets', '', ['task'])
make_github_issue('Use Jenkins and deploy to testing', '', ['task'])
make_github_issue('Test in testing environment', '', ['task'])
make_github_issue('Display test results in Jenkins', '', ['task'])
make_github_issue('Deploy to production if test passes', '', ['task'])
make_github_issue('Allow rollbacks', '', ['task'])
make_github_issue('Setup ELK for monitoring', '', ['task'])
