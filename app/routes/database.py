from flask import Blueprint,request
import sqlite3
import os
from dbconnect import DBConnect,DBExecStatus
bp = Blueprint("database",__name__)
basedir = os.getcwd()
@bp.route("/create_class")
def create_class():
    class_name = request.args.get("class_name")
    dbc = DBConnect()
    dbc.CreateDBConnect(f"{basedir}/db/{class_name}.db")
    for days in ["Mon","Tue","Wed","Thu","Fri"]:
        ct_status = dbc.createTable(days,name="TEXT",start="TEXT",end='TEXT',split="INT")
        if ct_status == DBExecStatus.ExecError:
            dbc.CloseDBConnect()
            return {"code":1,"message":"班级已创建"}
    dbc.CloseDBConnect()
    return {"code":0,"message":""}
@bp.route("/get_day")
def get_day():
    class_name = request.args.get("class_name")
    day_name = request.args.get("day_name")
    dbc = DBConnect()
    dbc.CreateDBConnect(f"{basedir}/db/{class_name}.db")
    classes = dbc.execute(f"SELECT * FROM {day_name}")
    classes_json = []
    for cls in classes:
        classes_json.append({"name":cls[0],"start":cls[1],"end":cls[2],"split":cls[3]})
    dbc.CloseDBConnect()
    return classes_json
@bp.route("/get_allday")
def get_allday():
    class_name = request.args.get("class_name")
    dbc = DBConnect()
    dbc.CreateDBConnect(f"{basedir}/db/{class_name}.db")
    alldays = {}
    for days in ["Mon","Tue","Wed","Thu","Fri"]:
        classes = dbc.execute(f"SELECT * FROM {days}")
        classes_json = []
        for cls in classes:
            classes_json.append({"name": cls[0], "start": cls[1], "end": cls[2], "split": cls[3]})
        alldays[days] = classes_json
    dbc.CloseDBConnect()
    return alldays