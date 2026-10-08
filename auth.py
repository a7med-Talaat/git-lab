def authenticate_user(username, password):
    database = {"admin": "pass123", "ahmed": "gitmaster"}
    return database.get(username) == password

def get_current_user():
    return "a7med-Talaat"
