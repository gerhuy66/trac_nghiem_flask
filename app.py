from flask import Flask, json, render_template, request, session, Response,jsonify,redirect,url_for
from flaskext.mysql import MySQL
app = Flask(__name__)

#database config
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'exam_db'
app.config['MYSQL_DATABASE_Host'] = 'localhost'
mysql.init_app(app)
##################



#Route
@app.route('/',methods=["GET"])
def home():
    return render_template('index.html')
#####

@app.route('/getQuestion',methods=["GET"])
def getQuestion():
    from service import getAllQuestion
    rs = getAllQuestion(mysql)
    return jsonify(rs)

@app.route('/getSubject',methods=["GET"])
def getSubject():
    from service import getAllSubject
    rs= getAllSubject(mysql)
    return jsonify(rs)


if __name__ == '__main__':
    app.run(debug=True)