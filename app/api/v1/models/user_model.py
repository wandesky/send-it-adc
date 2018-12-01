class User(object):
    '''User class'''
    users = []

    def __init__(self, firstname, lastname, othernames, email, username, registered, isAdmin ):
        self.user_id = len(User.users)
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.username = username
        self.registered = registered
        self.isAdmin = isAdmin

    def get_all_users(self = None):
        return User.users

    def post_parcel(self):
        User.users.append(
            {
                "id":len(User.users),
                "firstname": self.firstname,
                "lastname": self.lastname,
                "othernames": self.othernames,
                "email": self.email,
                "username": self.username,
                "registered": self.registered,
                "isAdmin": self.isAdmin
            }
        )
        return "success"
        