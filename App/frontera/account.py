from .sql import account_sql
from .file import delete
import hashlib

def signin(email, phone, password):
    email_hash = email+str(phone)
    email_hash = hashlib.sha256(email_hash.encode()).hexdigest()
    password = hashlib.sha256(password.encode()).hexdigest()

    data = account_sql.read.account(email, email_hash)

    try:
        if data[0][0] == email:
            if data[0][3] == password:
                return data[0][2]
            else:
                return False
        else:
            return False
    except:
        return "No such account"

def signup(email, name, phone, password):
    email_hash = email+str(phone)
    email_hash = hashlib.sha256(email_hash.encode()).hexdigest()
    password = hashlib.sha256(password.encode()).hexdigest()

    data = account_sql.read.account(email, email_hash)

    print(type(data))
    print(data)

    try:
        if data[0][0] != email:
            if data[0][1] != str(phone):
                if data[0][2] != email_hash:
                    account_sql.write.account(email, phone, name, password, email_hash)
                    return email_hash
                else:
                    return False
            else:
                return False
        else:
            return False
    except:
        account_sql.write.account(email, phone, name, password, email_hash)
        return email_hash

def secession(email, name, phone, password):
    email_hash = email+str(phone)
    email_hash = hashlib.sha256(email_hash.encode()).hexdigest()
    password = hashlib.sha256(password.encode()).hexdigest()

    data = account_sql.read.account(email, email_hash)

    if data[0][0] == email:
        if data[0][1] == phone:
            if data[0][2] == email_hash:
                delete.account(email, phone)
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
