import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import flask
from flask import Flask , jsonify





engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)


@app.route("/api/v1.0/precipitation")

def precipitation():
    m_prcp = session.query(Measurement.prcp , Measurement.date).\
    filter(Measurement.date > '2016-08-23').\
    order_by(Measurement.date).all()
    prdict = {date : x for date , x in m_prcp}
    return jsonify(prdict)


@app.route("/")
def welcome():
    return (f"welcome page <br/>"
           
           f" routes <br/>"
           
           f"/api/v1.0/precipitation <br/>"
           
           f"/api/v1.0/stations <br/>"
           
           f"/api/v1.0/tobs <br/>)
           

    

@app.route("/api/v1.0/stations")

def station():
    result = session.query(Station.station).all()
    st_list = list(np.ravel(result))
    return jsonify (st_list)



@app.route("/api/v1.0/tobs")

def tobs():
    tobss = session.query(Measurement.tobs).\
            filter(Measurement.station == 'USC00519281' ).\
            filter(Measurement.date >= '2017,8,23').all()
    tobs_list = list(np.ravel(tobss))
    return jsonify (tobs_list)



@app.route ("/api/v1.0/<start>/<end>")

def temps(start,end):
    findings = session.query(Measurement).filter(Measurement.date>= start).filter(Measurement.date<=end)
    found =[] 
    for row in findings:
        found.append(row.tobs) 
    return (jsonify ({"tempmin": min(found),"tempmax": max(found),"tempavg":np.mean}))
           
            

if __name__ == "__main__":
   app.run(debug=True)