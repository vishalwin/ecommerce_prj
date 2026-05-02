def get_user_name(db, user_id):
    user = db.get_user(user_id)
    return user.name


#db is database not ready``