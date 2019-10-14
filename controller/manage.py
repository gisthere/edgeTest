import time

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app import db, app

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(host="0.0.0.0"))


@manager.command
def create_tables():
    res = False
    tries = 0
    while not res and tries < 10:
        try:
            db.create_all()
            res = True
        except Exception as e:
            print(e)
            tries += 1
            time.sleep(1)


if __name__ == '__main__':
    manager.run()

