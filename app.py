
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# reflect an existing database into a new model
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)


Precipitation = Base.classes.precipitation
measurement = Base.classes.measurement
Station = Base.classes.station
Station_Activity = Base.classes.measurement.station

app = Flask(__name__)


@app.route("/")
def home():
    return (
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Connecting Session from python to DB
    session = Session(engine)
    precipitation_dict = {"Date": "Precipitation"}
    session.close()

    return precipitation_dict


@app.route("/api/v1.0/stations")
def jsonified():
    session = Session(engine)
 # Create a dictionary from the row data and append to a list of all_activity
    all_activity = []
    for Station, Station_Activity in Station:
        station_dict = {}
        station_dict["station"] = Station
        station_dict["Station Activity"] = Station_Activity
    session.close()

    return jsonify(all_activity)


@app.route("/api/v1.0/Tobs")
def Tobs():
    session = Session(engine)

    latest = session.query(measurement.date).order_by(
        measurement.date.desc()).first()
    latestdate = dt.datetime.strptime(latest[0], '%Y-%m-%d')
    querydate = dt.date(latestdate.year - 1, latestdate.month, latestdate.day)

    queryresult = session.query(measurement.tobs).\
        filter(measurement.station == 'USC00519281').\
        filter(measurement.date >= querydate).all()
    session.close()
    # Convert list of tuples into normal list
    all_Tobs = list(np.ravel(queryresult))

    return all_Tobs


@app.route('/api/v1.0/<start>')
def get_t_start(earliest):
    session = Session(engine)

    queryresult = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= earliest).all()
    session.close()

    all_Tobs = []
    for min, avg, max in queryresult:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max

        all_Tobs.append(tobs_dict)

    return jsonify(all_Tobs)


@app.route('/api/v1.0/<start>/<end>')
def get_t_earliest_latest(earliest, latest):
    session = Session(engine)

    earliest = session.query(measurement.date).order_by(
        measurement.date).first()
    latest = session.query(measurement.date).order_by(
        measurement.date.desc()).first()
    latestdate = dt.datetime.strptime(latest[0], '%Y-%m-%d')

    queryresult = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= earliest).filter(
            measurement.date <= latestdate).all()
    session.close()

    all_Tobs = []
    for min, avg, max in queryresult:
        tobs_dict = {}
        tobs_dict["Min"] = min
        tobs_dict["Average"] = avg
        tobs_dict["Max"] = max
        all_Tobs.append(tobs_dict)

    return jsonify(all_Tobs)


if __name__ == "__main__":
    app.run(debug=True)
