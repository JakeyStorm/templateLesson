from flask import  Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    context = {
        'author':'NoName',
        'books': [
            {
                'title': 'warcraft',
                'pages': 420
            },
            {
              'title': 'warcraft 2',
                'pages': 570
            },

        ]
    }
    return render_template('home.html',**context)

@app.route('/books/')
def books():
    book_name = 'warcraft'
    return render_template('books.html', book_name=book_name)


@app.route('/contact/')
def contact(phone=None):
    if phone is None:
        phone = '655655'
    return'my phone' + phone

if __name__ == '__main__':
    app.run(debug=True,port=8001)