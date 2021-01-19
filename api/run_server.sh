#!/bin/bash

echo "setting up flask_app.py..."
py flask_app.py

echo "setting up db_config.py..."
py db_config.py

echo "setting up api.py..."
py api.py

echo "server started"