#!/usr/bin/env python
import os

COV = None
if os.environ('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include="app/*")
    COV.start()

if os.path.exists('.env'):
    print("Importing environtment variables from .env")
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from app import create_app, db
from app import User, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('migrate', MigrateCommand)


@manager.command
def test():
    "Run the unit tests"
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
