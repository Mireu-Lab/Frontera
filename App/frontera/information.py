from .sql import information_sql

def write(kakaoid, nickname, realname, profile_picture, hobby, job, zone, sex, birthday, times):
    information_sql.write.user_info(kakaoid, nickname, realname, profile_picture, hobby, job, zone, sex, birthday, times)

def read(kakaoid):
    return information_sql.read.user_info(kakaoid)

def delete(kakaoid):
    information_sql.delete.user_info(kakaoid)