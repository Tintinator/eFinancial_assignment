from flask_app import app
from config_data import user, password, mysqlDB, host
from flaskext.mysql import MySQL

mysql = MySQL()

# print(user)
# print(password)
# print(mysqlDB)
# print(host)

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = user
app.config["MYSQL_DATABASE_PASSWORD"] = password
app.config["MYSQL_DATABASE_DB"] = mysqlDB
app.config["MYSQL_DATABASE_HOST"] = host
mysql.init_app(app)
