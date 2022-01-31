from .sql import file_sql
import os
import hashlib
import markdown
import datetime
import xmltodict
import html_to_json

def add(kakaoid, text):
    global userid
    time = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))

    file_name = kakaoid+time
    file_name = hashlib.md5(file_name.encode()).hexdigest()

    with open("Data/md_file/"+file_name+'.md', "a+", encoding='UTF-8') as file_work:
        file_work.write(text)
        file_work.close()

    file_sql.write.file(kakaoid, file_name, time)
    return markdown.markdown(text)

def delete(fileid):
    global userid

    file = 'Data/md_file/{}.md'.format(fileid)

    if os.path.isfile(file):
        file_sql.delete.file(fileid)
        os.remove(file)
        return True
    else:
        return False

def all_delete(kakaoid):
    

    for file_url in file_sql.read.file(kakaoid):
        file = 'Data/md_file/{}.md'.format(file_url[0])

        if os.path.isfile(file):
            file_sql.delete.file(file_url[0])
            os.remove(file)
            return True
        else:
            return False

def list(kakaoid):
    return file_sql.read.file(kakaoid)

def file_read(fileid, type):
    file = 'Data/md_file/{}.md'.format(fileid)

    if os.path.isfile(file):
        md_text = open("Data/md_file/"+fileid+'.md', "r", encoding='UTF-8')
        html_text = markdown.markdown(md_text.read())
        json_text = html_to_json.convert(html_text)

        if type == True:
            return xmltodict.unparse(json_text, pretty=True)
        elif type == False:
            return json_text

    else:
        return {"message" : False}