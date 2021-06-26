import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify
import datetime as dt
from datetime import datetime
from datetime import date, timedelta

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
# Home
@app.route("/")
def home():
    """List all available api routes."""
    return (f'<table><thead><tr><th>/api/v1.0/precipitation</th><th></th><th><a href="http://127.0.0.1:5000/api/v1.0/precipitation">Precipitation</a><br></th></  table>'
            f'<table><thead><tr><th>/api/v1.0/stations<br></th><th></th><th><a href="http://127.0.0.1:5000/api/v1.0/stations">Stations</a><br></th></table>'
            f'<table><thead><tr><th>/api/v1.0/tobs<br></th><th></th><th><a href="http://127.0.0.1:5000/api/v1.0/tobs">Temperature Observations</a><br></th></table>'
            f'<table><thead><tr><th>/api/v1.0/<start><br></th><th></th><th><a href="http://127.0.0.1:5000/api/v1.0/<start>">Start</a><br></th></table>'
            f'<table><thead><tr><th>/api/v1.0/<start>/<end><br></th><th></th><th><a href="http://127.0.0.1:5000/api/v1.0/<start>/<end>">Start and End</a><br></th></table>')


# Precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create session from Python to DB
    session = Session(engine)
    # Defining Last year
    max_d = session.query(measurement.date).order_by(measurement.date.desc()).first()[0]
    max_d = datetime.strptime(max_d, '%Y-%m-%d')
    last_year = max_d - timedelta(days=366)
    # Query the last 12 months precipitation
    oy_precipitation = session.query(measurement.date,measurement.prcp).filter(measurement.date >= last_year).order_by(measurement.date).all()
    session.close()
    # Convert list of tuples into normal list
    precip = []
    for date, prcp in oy_precipitation:
        p_dict = {}
        p_dict["Date"] = date
        p_dict["Precipitation"] = prcp
        precip.append(p_dict)

    return jsonify(precip)

# Stations
@app.route("/api/v1.0/stations")
def stations():
    # Create session from Python to DB
    session = Session(engine)
    # Query list of stations
    list_stations=session.query(station.station).all()
    session.close()
    # Convert list of tuples into normal list
    stations = list(np.ravel(list_stations))

    return jsonify(stations)

if __name__ == '__main__':
    app.run(debug=True)