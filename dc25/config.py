import os
basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DATABASE = basedir+'/../dc25_db/testing.db'
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

PORT = 3000
DEBUG = 'True'
