
class Settings:

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "postgresql://main:main@controller-db/main"

    CELERY_RESULT_BACKEND = 'redis://controller-redis:6379'

    CELERY_BROKER_URL = 'redis://controller-redis:6379'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
