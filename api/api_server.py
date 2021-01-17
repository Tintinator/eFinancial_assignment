import pymysql
from flask_app import app
from db_config import mysql
from flask import jsonify, flash, request

# Retrieve All Entries
@app.route("/entry")
def entry():
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT entry_id, entry_title, entry_date FROM tbl_entry;")
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200

        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


# Create Entry
@app.route("/add", methods=["POST"])
def create_entry():
    try:
        _json = request.json
        _title = _json["title"]
        _date = _json["date"]
        _content = _json["content"]
        if _name and _email and _password and request.method == "POST":
            # save edits
            insert_query = "INSERT INTO tbl_entry VALUES(%s, %s, %s, %s)"
            data = (None, _title, _date, _content)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(insert_query, data)
            conn.commit()
            resp = jsonify("Entry added successfully!")
            resp.status_code = 200

            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Read Entry
@app.route("/entry/<int:id>")
def read_entry(id):
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM tbl_entry WHERE entry_id=%s;", id)
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200

        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


# Update Entry
@app.route("/edit", methods=["POST"])
def update_entry():
    try:
        _json = request.json
        _id = _json["id"]
        _title = _json["title"]
        _date = _json["date"]
        _content = _json["content"]
        if _name and _email and _password and request.method == "POST":
            # save edits
            insert_query = "UPDATE tbl_entry SET entry_title=%s, entry_date=%s, entry_content=%s WHERE entry_id=%s"
            data = (_title, _date, _content, _id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(insert_query, data)
            conn.commit()
            resp = jsonify("Entry added successfully!")
            resp.status_code = 200

            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# Delete Entry
@app.route("/delete/<int:id>")
def delete_entry(id):
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("DELETE FROM tbl_entry WHERE entry_id=%s;", id)
        conn.commit()
        resp = jsonify("Entry deleted successfully")
        resp.status_code = 200

        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {"status": 404, "message": "Not Found: " + request.url}
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run()
