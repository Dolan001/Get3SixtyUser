from flask import Flask
from auth import authentication
from homeRequest import homeReq
from product import buy_pro

app = Flask(__name__)

app.register_blueprint(authentication)
app.register_blueprint(homeReq)
app.register_blueprint(buy_pro)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    app.run(debug=True)
