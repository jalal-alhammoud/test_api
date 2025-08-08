from fastapi import FastAPI, HTTPException



app = FastAPI(
    title="Recommendation System API",
    description="A comprehensive API for product recommendations using various algorithms",
    version="1.0.0",
    openapi_tags=[{
        "name": "Recommendations",
        "description": "Endpoints for different recommendation algorithms"
    }]
)



@app.get("/health", tags=["System"])
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy", "version": "1.0.0"}



# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

# import sys

# # add your project directory to the sys.path
# project_home = '/home/jalalAlhammoud/mysite'
# if project_home not in sys.path:
#     sys.path = [project_home] + sys.path

# # import flask app but need to call it "application" for WSGI to work
# from flask_app import app as application  # noqa
