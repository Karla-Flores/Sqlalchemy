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
    return (f'/api/v1.0/precipitation <br>'
            f'/api/v1.0/stations<br>'
            f'/api/v1.0/tobs<br>'
            f'api/v1.0/&lt;start&gt;<br>'
            f'/api/v1.0/&lt;start&gt;/&lt;end&gt;<br>')


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

# Tobs
@app.route("/api/v1.0/tobs")
def tobs():
    # Create session from Python to DB
    session = Session(engine)
    # Query most active station
    high_tempobs = session.query(measurement.station, func.count(measurement.tobs)).group_by(measurement.station).order_by(func.count(measurement.tobs).desc()).all()
    high_tempobs_station = high_tempobs[0][0]
    # Defining Last year
    max_d = session.query(measurement.date).order_by(measurement.date.desc()).first()[0]
    max_d = datetime.strptime(max_d, '%Y-%m-%d')
    last_year = max_d - timedelta(days=366)
    # Query the last 12 months of temperature observation data for this station
    t_obs = session.query(measurement.tobs).filter(measurement.station == high_tempobs_station).filter(measurement.date >= last_year).order_by(measurement.date).all()  
    session.close()
    # Convert list of tuples into normal list
    yt_obs = list(np.ravel(t_obs))

    return jsonify(yt_obs)

@app.route('/api/v1.0/<start>')
def start(start = None):
    # Create session from Python to DB
    session = Session(engine)
    # Selection
    start_select = session.query(measurement.date, func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start).group_by(measurement.date).all()
    start_select = list(start_select)
    return jsonify(start_select)

@app.route('/api/v1.0/<start>/<end>')
def end(start = None, end = None):
    # Create session from Python to DB
    session = Session(engine)
    # Selection
    end_select = session.query(measurement.date, func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start, measurement.date <= end).group_by(measurement.date).all()
    end_select  = list(end_select )
    return jsonify(end_select)

if __name__ == '__main__':
    app.run(debug=True)