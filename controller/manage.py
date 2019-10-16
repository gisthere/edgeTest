import time

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app import db, app

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(host="0.0.0.0"))  # Ковычки то двойные то одинарные


@manager.command
def create_tables():
    """
    tries = 0
    while tries < 10:
        try:
            db.create_all()
            return
        except Exception as e:
            print(e)
            tries += 1
            time.sleep(1)
    """
    res = False
    tries = 0
    while not res and tries < 10:
        try:
            db.create_all()
            res = True
        except Exception as e:
            print(e)  # Для логгирования лучше всего использовать logging API, а не пртинты
            tries += 1
            time.sleep(1)
    # Как, после завершении выполнения команды понять, что она выполнилась успешно? В случае с Exception выводится
    # сообщение, а в случае успеха - ничего

if __name__ == '__main__':
    manager.run()

