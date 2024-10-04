import sqlite3

import logger
from singleton import *
from logger import *
class DBExecStatus:
    ExecOK = 0
    ExecError = 1
@Singleton
class DBConnect:
    def __init__(self):
        self.dbName = None
        self.__db = None
    def CreateDBConnect(self, dbName):
        self.dbName = dbName
        self.__db = sqlite3.connect(dbName)
    def CloseDBConnect(self):
        self.__db.close()
    def createTable(self, tableName,**args):
        cur = self.__db.cursor()
        dbString = "CREATE TABLE %s("%tableName
        for name, type in args.items():
            dbString += "%s %s NOT NULL,"%(name, type)
        dbString = dbString[:-1]
        dbString += ");"
        logger.log(LogLevel.INFO, dbString)
        try:
            cur.execute(dbString)
            return DBExecStatus.ExecOK
        except Exception as e:
            logger.log(LogLevel.ERROR, str(e))
            return DBExecStatus.ExecError
        self.__db.commit()
    def execute(self,dbString):
        cur = self.__db.cursor()
        cur.execute(dbString)
        self.__db.commit()
        return cur.fetchall()