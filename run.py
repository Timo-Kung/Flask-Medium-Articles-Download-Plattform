from flask import Flask, render_template, request, session, redirect
from models import item
from models.users import User
from models.articles import Article
from common.database import Database

app = Flask(__name__)

app.secret_key = "Timo"


@app.before_first_request
def init_db():
    Database.initialize()


@app.route("/")
def hello():
    return render_template("base_2.html")


@app.route("/login", methods=["GET", "POST"])
def login_method():
    if request.method == "POST":
        account = request.form['InputAccount']
        password = request.form['InputPassword']
        check = User.is_login_valid(account, password)
        if check == True:
            session['account'] = account
            session['name'] = User.find_user_data(account).get('name')
            return redirect("/")
        else:
            message = "Your account or password is wrong!"
            return render_template("login.html", message=message)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register_method():
    if request.method == "POST":
        name = request.form['InputName']
        account = request.form['InputAccount']
        password = request.form['InputPassword']
        result = User.register_user(name, account, password)
        if result == True:
            session['account'] = account
            session['name'] = User.find_user_data(account).get('name')
            return redirect("/")
        else:
            message = "Your account is already register!"
            return render_template("register.html", message=message)
    else:
        return render_template("register.html")


@app.route("/logout")
def logout_method():
    session['account'] = None
    return redirect("/")


@app.route("/result")
def result():
    url = request.url
    favorite_article = []
    user_favorite = Article.find_article(session['account'])
    for article in user_favorite:
        favorite_article.append(article['title'])

    search = request.args.get('search')
    items = item.search_content(search)
    all_items = item.search_metadata(items)
    other_pages = item.page_bar(search)
    return render_template("result.html", search=search, all_items=all_items, other_pages=other_pages, url=url,
                           favorite_article=favorite_article)


@app.route("/favorite", methods=["GET", "POST"])
def favorite_method():
    if session['account']:
        if request.method == "POST":
            url = request.form['url']
            title = request.form['title']
            link = request.form['link']
            image = request.form['image']
            account = session['account']
            Article(account, title, link, image).save_to_db()
            return redirect(url)
        else:
            account = session['account']
            user_article = Article.find_article(account)
            return render_template("favorite.html", user_article=user_article)


@app.route("/delete", methods=['POST'])
def delete_method():
    link = request.form['link']
    account = session['account']
    Article.delete_article(account)
    return redirect("/favorite")


@app.route("/download")
def download():
    value = request.args.get('value')
    title = request.args.get('title_1')
    downloads = item.download(title, value)
    print(title)
    print(value)
    return render_template("download.html", value=value, downloads=downloads, title=title)


if __name__ == "__main__":
    app.run(debug=True)
