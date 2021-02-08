from setuptools import setup, find_packages

setup(
        name='flaskr',
        description='Simple microblog example using Flask',
        packages=find_packages(),
        entry_points='''
                [flask.commands]
                initdb=flaskr.flaskr:initdb_command
        ''',
)
export FLASK_APP=flaskr