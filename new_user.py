from common.database import Database

Database.initialize()
Database.insert_one("users", {"account": "timo@test.com", "password": "123", "name": "Timo"})
users = Database.find_one('users', {"account": "timo@test.com"})

print(users)
