class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://mysql:mysql@localhost/test1'
    SECRET_KEY = 'something very secret'

    ### FLASK-SECURITY ###
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'

