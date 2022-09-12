import os
from flask_sqlalchemy import SQLAlchemy
from GD import db
from GD import creat_app


config_name=os.getenv("flask_config","development")
application=creat_app(config_name)

# Hi this is vijay add pull request

if __name__=="__main__":
    application.run(debug=True,port=2000)