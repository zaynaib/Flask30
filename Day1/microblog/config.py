import os

#basedir is the root directory of the app packages
# os(operating system)  find absoulte path
# directory name file
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
