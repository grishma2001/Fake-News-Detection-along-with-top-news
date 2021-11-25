from flask import render_template, Blueprint, request, flash
views = Blueprint("views", __name__)


@views.route("/", methods=["POST", "GET"])
@views.route("/home", methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        news = request.form.get("news")
        print(news)
        from flask import flash
        import pandas as pd
        import numpy as np
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.model_selection import train_test_split
        from sklearn.naive_bayes import MultinomialNB
        from GoogleNews import GoogleNews

        data = pd.read_csv("./fake_news.csv")
        print(data.head())
        x = np.array(data["title"])
        y = np.array(data["label"])

        cv = CountVectorizer()
        x = cv.fit_transform(x)
        xtrain, xtest, ytrain, ytest = train_test_split(
        x, y, test_size=0.2, random_state=42)
        model = MultinomialNB()
        p=model.fit(xtrain, ytrain)

        news_headline = news


        data = cv.transform([news_headline]).toarray()
        result = model.predict(data)

        print(result)
        if result == ['FAKE']:
            print("fake")
            flash("The news is fake!", category='error')
        elif result == ['REAL']:
            print("true")
            flash("The news is \n real Trust me!", category='sucess')

    return render_template("home.html")

@views.route("/chart")
def chart():
    return render_template("chart.html")


@views.route("/news",methods=["POST", "GET"])
def news():
    c=""
    i=0
    if request.method == 'POST':
        import numpy as np
        from GoogleNews import GoogleNews
        news = request.form.get("news")
        print(news)
        news_headline = news
        googlenews = GoogleNews()
        googlenews = GoogleNews('en', 'd')

        googlenews.search(news_headline)
        googlenews.get_news(news_headline)
        googlenews.getpage(1)

        googlenews.result()
        a=googlenews.gettext()
        b=np.asarray(a)
        print(type(b))

        c=b[0:6]
    return render_template("news.html",c=c,i=i)