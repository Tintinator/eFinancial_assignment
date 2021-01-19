import pymysql
from flask_app import app
from db_config import mysql
from flask import jsonify, flash, request

# Retrieve All Entries
@app.route("/entry")
def entry():

    query = "SELECT * FROM tbl_entry;"
    resp = db_read(query)

    return resp


# Create Entry
@app.route("/add", methods=["POST"])
def create_entry():

    _json = request.json
    _title = _json["title"]
    _date = _json["date"]
    _content = _json["content"]

    if _title and _date and _content and request.method == "POST":
        query = "INSERT INTO tbl_entry VALUES(%s, %s, %s, %s)"
        params = (None, _title, _date, _content)
        temp = db_write(query, params)
        resp = jsonify("Entry added successfully!")
        resp.status_code = 200

        return resp
    else:
        return not_found()


# Read Entry
@app.route("/entry/<int:id>")
def read_entry(id):
    query = "SELECT * FROM tbl_entry WHERE entry_id=%s;"
    resp = db_read(query, id)

    return resp


# Update Entry
@app.route("/edit", methods=["POST"])
def update_entry():
    # try:
    _json = request.json
    _id = request.form.get("id")
    _title = request.form.get("title")
    _date = request.form.get("date")
    _content = request.form.get("content")
    if _id and _title and _date and _content and request.method == "POST":
        query = "UPDATE tbl_entry SET entry_title=%s, entry_date=%s, entry_content=%s WHERE entry_id=%s"
        data = (_title, _date, _content, _id)
        db_write(query, data)
        # resp = jsonify("Entry updated successfully!")
        # resp.status_code = 200

        return resp
    else:
        return not_found()


# Delete Entry
@app.route("/delete/<int:id>")
def delete_entry(id):
    query = "DELETE FROM tbl_entry WHERE entry_id=%s;"
    db_write(query, id)
    resp = jsonify("Entry deleted successfully")
    resp.status_code = 200

    return resp


@app.errorhandler(404)
def not_found(error=None):
    message = {"status": 404, "message": "Not Found: " + request.url}
    resp = jsonify(message)
    resp.status_code = 404

    return resp


def db_read(query, params=None):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200

        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def db_write(query, params=None):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()

        return params
    except Exception as e:
        print(e)

        return False
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run(debug=True)
