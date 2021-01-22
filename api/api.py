import logging
import pymysql
from flask import jsonify, request
from flask_app import app
from db_config import mysql

# Retrieve All Entries
@app.route("/entry")
def entry():
    """Returns all current blog entries

    Returns:
        Response: Flask Reponse object containing blog entries
    """
    log_message = "GET /entry"
    query = "SELECT * FROM tbl_entry;"
    result = db_read(query)

    if not result:
        app.logger.info(log_message + " " + str(500))
        return create_response("Failed to retrieve entries!", 500)

    app.logger.info(log_message + " " + str(200))
    return result


# Create Entry
@app.route("/add", methods=["POST"])
def create_entry():
    """Creates a blog entry with provided parameters from a given request.

    Returns:
        Response: Flask Response object containing resulting message and code.
    """
    _json = request.json
    _title = _json["title"]
    _date = _json["date"]
    _content = _json["content"]
    log_message = "POST /add with title=%s date=%s content=%s " % (
        _title,
        _date,
        _content,
    )

    if _title and _date and _content and request.method == "POST":
        query = "INSERT INTO tbl_entry VALUES(%s, %s, %s, %s)"
        params = (None, _title, _date, _content)
        result = db_write(query, params)

        if not result:
            app.logger.error(log_message + " " + str(500))
            resp = create_response("Entry failed to create!", 500)
        else:
            app.logger.info(log_message + " " + str(201))
            resp = create_response("Entry created successfully!", 201)
        return resp
    else:
        app.logger.error(log_message + " " + str(404))
        return not_found()


# Read Entry
@app.route("/entry/<int:id>")
def read_entry(_id=None):
    """Retrieves blog post using provided _id. Returns all entries if no _id.

    Args:
        _id (int): Blog Post ID

    Returns:
        Response: Flask Reponse object containing blog entry(s)
    """
    log_message = "GET /entry with id=%s" % _id

    if id:
        query = "SELECT * FROM tbl_entry WHERE entry_id=%s;"
        result = db_read(query, _id)

        if not result:
            app.logger.error(log_message + " " + str(500))
            return create_response("Failed to retrieve entry!", 500)

        app.logger.info(log_message + " " + 200)
        return result

    return entry()


# Update Entry
@app.route("/edit", methods=["PUT"])
def update_entry():
    """Updates a blog entry with provided parameters from a given request.

    Returns:
        Response: Flask Response object containing resulting message and code.
    """
    _json = request.json
    _id = _json["id"]
    _title = _json["title"]
    _content = _json["content"]
    log_message = "PUT /edit with id=%s title=%s content=%s " % (_id, _title, _content)

    if _id and _title and _content and request.method == "PUT":
        query = (
            "UPDATE tbl_entry SET entry_title=%s, entry_content=%s WHERE entry_id=%s"
        )
        params = (_title, _content, _id)
        result = db_write(query, params)

        if not result:
            app.logger.error(log_message + " " + str(500))
            resp = create_response("Entry failed to update!", 500)
        else:
            app.logger.info(log_message + " " + str(200))
            resp = create_response("Entry updated successfully!", 200)
        return resp
    else:
        app.logger.error(log_message + " " + str(404))
        return not_found()


# Delete Entry
@app.route("/delete/<int:id>")
def delete_entry(_id=None):
    """Deletes blog post using provided _id.

    Args:
        _id (int): Blog Post ID

    Returns:
        Response: Flask Reponse object containing result message and status code
    """
    log_message = "DELETE /delete with id=%s " % _id

    if id:
        query = "DELETE FROM tbl_entry WHERE entry_id=%s;"
        result = db_write(query, _id)

        if not result:
            app.logger.error(log_message + " " + str(500))
            resp = create_response("Entry failed to delete!", 500)
        else:
            app.logger.info(log_message + " " + str(200))
            resp = create_response("Entry deleted successfully!", 200)
        return resp
    else:
        app.logger.error(log_message + " " + str(404))
        return not_found()


@app.errorhandler(404)
def not_found():
    """Creates Flask Response object containing 404 Not Found error

    Returns:
        Response: Flask Reponse object containing 404 Not Found
    """
    message = {"status": 404, "message": "Not Found: " + request.url}
    app.logger.error("404. Not Found")

    return create_response(message, 404)


def db_read(query, params=None):
    """Database utility function uses provided query and parameters to read database items.

    Args:
        query (str): SQL query to run on database
        params (optional): SQL query parameters. Defaults to None.

    Returns:
        Response: Flask Reponse object containing resulting blog entry
    """
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        rows = cursor.fetchall()

        return create_response(rows, 200)
    except Exception as exception:
        app.logger.error(exception)
        return False
    finally:
        cursor.close()
        conn.close()


def db_write(query, params=None):
    """Database utility function uses provided query and parameters to create and modify
    database items.

    Args:
        query (str): SQL query to run on database
        params (optional): SQL query parameters. Defaults to None.

    Returns:
        bool: True if successfully executed. False if exception occurred.
    """
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()

        return True
    except Exception as exception:
        app.logger.error(exception)
        return False
    finally:
        cursor.close()
        conn.close()


def create_response(message="", status_code=""):
    """Utility function that wraps provided input as Flask Response object.

    Args:
        message (str, optional): Input to wrap as Flask Response object. Defaults to "".
        status_code (str, optional): Associated status code. Defaults to "".

    Returns:
        [type]: [description]
    """
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
