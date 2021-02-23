from flask import Flask, json, render_template, request, session, Response,jsonify,redirect,url_for
from flaskext.mysql import MySQL


app = Flask(__name__)

#database config
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'examdb'
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
    questions = "Cau Hoi Thu Nhat? - Cau Hoi Thu Hai? - Cau Hoi Thu Ba? - Cau Hoi Thu Tu?";

    return jsonify(questions)



if __name__ == '__main__':
    app.run(debug=True)