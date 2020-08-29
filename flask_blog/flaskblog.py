from flask import Flask,render_template,url_for
app=Flask(__name__)
# initializing flask


posts=[
    {
        'author':"Asmita Gauri",
        'title':"BLog Post 1",
        'content':"First BLog Post",
        'date_posted':"August 29th 2020"
    },
    {
        'author':"Gauri Asmita",
        'title':"BLog Post 2",
        'content':"Second BLog Post",
        'date_posted':"August 30th 2020"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html',title='About')

if __name__=='__main__':
    app.run(debug=True)