from flask import Flask, json, render_template, request, session, Response,jsonify,redirect,url_for
from flaskext.mysql import MySQL
app = Flask(__name__)

#database config
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Quangphuong156'
app.config['MYSQL_DATABASE_DB'] = 'exam_db'
app.config['MYSQL_DATABASE_Host'] = 'localhost'
mysql.init_app(app)
##################
con = mysql.connect()
cursor = con.cursor()

#Route
@app.route('/',methods=["GET"])
def home():
    return render_template('index.html')
#####

@app.route('/getQuestion',methods=["GET"])
def getQuestion():
    from service import getAllQuestion
    eId = request.args['eId']
    rs = getAllQuestion(mysql,eId)
    return jsonify(rs)

@app.route('/getSubject',methods=["GET"])
def getSubject():
    from service import getAllSubject
    rs= getAllSubject(mysql)
    return jsonify(rs)

@app.route('/getExamsBySub',methods=["GET","POST"])
def getExamBySubject():
    from service import getExamBySubject
    subId = request.args['subId']
    rs = getExamBySubject(mysql,subId)
    return jsonify(rs)
 

@app.route('/insertAnswer', methods=["GET","POST"])
def insertAnswer():
    anList = request.form
    arr = []
    for an in anList:
        cursor.execute("INSERT INTO dapan(dapancol) VALUES (%s)", ( anList[an]))
        con.commit()
    return '<h1>success</h1>'

@app.route('/score', methods=['POST'])
def score():
    from service import getAllQuestion1
    from service import getDapan
    cur = getAllQuestion1(mysql)
    cur1 = getDapan(mysql)
    mabt = request.form['mabt']
    a = 0
    for e in cur:
        for x in cur1:
            if mabt == x[2]:
                if x[1] == e[2]:
                    a = a + 1
    return str(a)          
				
if __name__ == '__main__':
    app.run(debug=True)