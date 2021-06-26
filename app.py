import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station
# Create session from Python to DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available api routes."""
    return (f'/api/v1.0/precipitation<br>'
            f'/api/v1.0/stations<br>'
            f'/api/v1.0/tobs<br>'
            f'/api/v1.0/<start><br>'
            f'/api/v1.0/<start>/<end><br>')


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    session.close()

if __name__ == '__main__':
    app.run(debug=True)