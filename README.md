# cookiecutter-aws-lambda

A [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template to
generate boleirplate Python 3 code for an
[AWS Lambda](https://aws.amazon.com/lambda/?nc1=h_ls).

## Introduction

There are many different Cookiecutter templates for Lambda out there. Many.

Some mixes programming language code with configuration management tools (like
Terraform, CloudFormation and Ansible). Some of them implement fancy
configurations for your code too.

This is **not** what you're going to get from this repository: if you're looking
for a simple way to jump start your AWS Lambda code with Python 3 interpreter,
then you're in the right place.

This is what you're going to get:

1. A directory with the Lambda name.
2. Within the directory, a single file called `main.py`, that will contain an
AWS Lambda handler name of your choice.
3. Basic assertion of your environment variables configuration.
4. Basic logging configuration to start with.

That's all!

Here is an example, result of using all standard values proposed:

```python
import logging
import os
import sys


try:
    log_level = getattr(logging, os.environ['LOG_LEVEL'])
    log_format = os.environ['LOG_FORMAT']
except KeyError as e:
    msg = 'Missing the environment variable {}, aborting'.format(e)
    raise Exception(msg)

root = logging.getLogger()

if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)

logging.basicConfig(stream=sys.stdout, format=log_format,
                    level=log_level)


def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.info('Event data: {}'.format(event))
    logger.info('Context data: {}'.format(context))
    # do some stuff
    return {'result': 'OK'}

```

## How to use

You should first visit the Cookiecutter documentation page to understand how the
tool works. I'm assuming that you already know how to program in Python 3.X and
how to create AWS Lambdas.

After that, it is just a matter to answer the questions. Picking up the default
values should be enough in most cases.

Here is a short explanation of the keywords available for configuration:

* `env_name_log_level`: the name of the environment variable that will contain
the configuration of the logging level. Valid values are those described in the
standard
[logging framework documentation](https://docs.python.org/3/library/logging.html).
* `env_name_log_format`: the name of the environment variable that will contain
the configuration of the logging format. Valid values are those described in the
standard
[logging framework documentation](https://docs.python.org/3/library/logging.html).
* `lambda_handler_name`: the handler name you want to use to handle the AWS
Lambda requests.
* `lambda_name`: the Lambda name you want to give.
