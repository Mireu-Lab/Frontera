import sqlite3

class write:
    def account(email, name, kakaoid):
        sqldata = sqlite3.connect("Data/Diary_API.sqlite3")
        data = sqldata.cursor()
        sqlline = """INSERT INTO userdb (email, kakaoid) VALUES (?, ?, ?);"""
        data.execute(sqlline, (email, kakaoid))
        sqldata.commit()
        data.close()
        sqldata.close()

class read:
    def account(email, kakaoid):
        sqldata = sqlite3.connect("Data/Diary_API.sqlite3")
        data = sqldata.cursor()
        sqlline = """select email, kakaoid from userdb where email='{}' and kakaoid = '{}';""".format(email, kakaoid)
        
        try:
            data.execute(sqlline)
            sqljson = data.fetchall()
            return sqljson
        
        except:
            return {}

        sqldata.clone()

    def confirmation(kakaoid):
        sqldata = sqlite3.connect("Data/Diary_API.sqlite3")
        data = sqldata.cursor()
        sqlline = """select kakaoid from userdb where kakaoid='{}';""".format(kakaoid)
        data.execute(sqlline)
        sqljson = data.fetchall()
        return sqljson
        sqldata.clone()

class delete:
    def account(email, kakaoid):
        sqldata = sqlite3.connect("Data/Diary_API.sqlite3")
        data = sqldata.cursor()
        sqlline = """delete from userdb where email = ? and kakaoid = ?;"""
        data.execute(sqlline, (email, kakaoid))
        sqldata.commit()
        data.close()
        sqldata.close()