from website import create_app
from flask import Flask
from website.hcode import hcode
from website.code import code

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)