import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL: str = 'sqlite:///' + os.path.join(basedir, 'data_base.sqlite')