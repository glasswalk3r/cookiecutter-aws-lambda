import logging
import os
import sys


try:
    log_level = getattr(logging, os.environ['{{ cookiecutter.env_name_log_level }}'])
    log_format = os.environ['{{ cookiecutter.env_name_log_format }}']
except KeyError as e:
    msg = 'Missing the environment variable {}, aborting'.format(e)
    raise Exception(msg)

root = logging.getLogger()

if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)

logging.basicConfig(stream=sys.stdout, format=log_format,
                    level=log_level)


def {{ cookiecutter.lambda_handler_name }}(event, context):
    logger = logging.getLogger()
    logger.info('Event data: {}'.format(event))
    logger.info('Context data: {}'.format(context))
    # do some stuff
    return {'result': 'OK'}
