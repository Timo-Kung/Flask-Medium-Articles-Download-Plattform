from common.database import Database


class Article(object):
    def __init__(self, account, title, link, image):
        self.account = account
        self.title = title
        self.link = link
        self.image = image

    def save_to_db(self):
        Database.insert_one(collection='articles', data=self.json())

    def json(self):
        return {
            "account": self.account,
            "title": self.title,
            "link ": self.link,
            "image": self.image
        }

    def find_article(account):
        user_article = Database.find(collection='articles', query={"account": account})
        return user_article

    def delete_article(account):
        Database.drop(collection='articles')
