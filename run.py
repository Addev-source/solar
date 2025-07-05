import os
import sys


# Ensure the app directory is in the Python path

sys.path.insert(0, os.path.dirname(__file__))

from app import app 

if __name__ == "__main__":
    app.run(debug=True)


# The application is configured to run in debug mode during development.
# The code imports necessary modules and sets up the application context.
# The application is structured to handle different routes and render templates accordingly.
# The application is designed to fetch currency rates and product prices from an external API.
