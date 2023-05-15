# Adventures in Python

This repo is meant to be the foundation for the CSD class offered by **Falk Kühnel** and **Björn Jensen** of **Jensen und Komplizen**. 

## Preparation
In order to be able to follow this tutorial you need to have to install the following things:

- Python 3.x 
- PIP

## Step 01 - Local Setup Instructions

1. Install Python version 3.11
2. Run `python3 -m venv venv` to create the virtualenv
3. Activate venv: `source venv/bin/activate`
4. Install needed dependencies (venv activated) by running: `pip install -r requirements.txt`
5. Run local flask development server: `flask run` (if you get any "used port"-error, you can change the port by setting the `--port=XXXX` argument like i.e. `flask run --port=5001`)
