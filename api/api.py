import pymysql
from flask_app import app
from db_config import mysql
from flask import jsonify, flash, request
import logging

# Retrieve All Entries
@app.route("/entry")
def entry():
    logMessage = "GET /entry"
    query = "SELECT * FROM tbl_entry;"
    result = db_read(query)

    if not result:
        app.logger.info(logMessage + " " + str(500))
        return createResponse("Failed to retrieve entries!", 500)
    else:
        app.logger.info(logMessage + " " + str(200))
        return result


# Create Entry
@app.route("/add", methods=["POST"])
def create_entry():
    _json = request.json
    _title = _json["title"]
    _date = _json["date"]
    _content = _json["content"]
    logMessage = "POST /add with title=%s date=%s content=%s " % (
        _title,
        _date,
        _content,
    )

    if _title and _date and _content and request.method == "POST":
        query = "INSERT INTO tbl_entry VALUES(%s, %s, %s, %s)"
        params = (None, _title, _date, _content)
        result = db_write(query, params)

        if not result:
            app.logger.error(logMessage + " " + str(500))
            resp = createResponse("Entry failed to create!", 500)
        else:
            app.logger.info(logMessage + " " + str(201))
            resp = createResponse("Entry created successfully!", 201)
        return resp
    else:
        app.logger.error(logMessage + " " + str(404))
        return not_found()


# Read Entry
@app.route("/entry/<int:id>")
def read_entry(id):
    logMessage = "GET /entry with id=%s" % id

    if id:
        query = "SELECT * FROM tbl_entry WHERE entry_id=%s;"
        result = db_read(query, id)

        if not result:
            app.logger.error(logMessage + " " + str(500))
            return createResponse("Failed to retrieve entry!", 500)
        else:
            app.logger.info(logMessage + " " + 200)
            return result
    else:
        return entry()


# Update Entry
@app.route("/edit", methods=["PUT"])
def update_entry():
    _json = request.json
    _id = _json["id"]
    _title = _json["title"]
    _content = _json["content"]
    logMessage = "PUT /edit with id=%s title=%s content=%s " % (_id, _title, _content)

    if _id and _title and _content and request.method == "PUT":
        query = (
            "UPDATE tbl_entry SET entry_title=%s, entry_content=%s WHERE entry_id=%s"
        )
        params = (_title, _content, _id)
        result = db_write(query, params)

        if not result:
            app.logger.error(logMessage + " " + str(500))
            resp = createResponse("Entry failed to update!", 500)
        else:
            app.logger.info(logMessage + " " + str(200))
            resp = createResponse("Entry updated successfully!", 200)
        return resp
    else:
        app.logger.error(logMessage + " " + str(404))
        return not_found()


# Delete Entry
@app.route("/delete/<int:id>")
def delete_entry(id):
    logMessage = "DELETE /delete with id=%s " % id

    if id:
        query = "DELETE FROM tbl_entry WHERE entry_id=%s;"
        result = db_write(query, id)

        if not result:
            app.logger.error(logMessage + " " + str(500))
            resp = createResponse("Entry failed to delete!", 500)
        else:
            app.logger.info(logMessage + " " + str(200))
            resp = createResponse("Entry deleted successfully!", 200)
        return resp
    else:
        app.logger.error(logMessage + " " + str(404))
        return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {"status": 404, "message": "Not Found: " + request.url}
    app.logger.error("404. Not Found")

    return createResponse(message, 404)


def db_read(query, params=None):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        rows = cursor.fetchall()

        return createResponse(rows, 200)
    except Exception as e:
        app.logger.error(e)
        return False
    finally:
        cursor.close()
        conn.close()


def db_write(query, params=None):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()

        return True
    except Exception as e:
        app.logger.error(e)
        return False
    finally:
        cursor.close()
        conn.close()


def createResponse(message="", status_code=""):
    resp = jsonify(message)
    resp.status_code = status_code
    return resp


if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO,
        filename="apiLog.log",
        format="[%(asctime)s] - %(levelname)s: %(message)s",
        filemode="w",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )
    app.logger.info("Flask Application Starting")

    app.run(debug=True)
