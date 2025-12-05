#!/bin/bash
# Start script for Render
pip install gunicorn
exec gunicorn app:app --bind 0.0.0.0:$PORT --workers 2
