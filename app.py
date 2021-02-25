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
# @app.route('/score', methods=['POST'])
# def score():
# 	from service import getAllQuestion
# 	from service import getDapan
#     cur = getAllQuestion(mysql)
# 	cur1 = getDapan(mysql)
# 	for x in cauhoi:
# 		for y in dapan:
# 			if(x == y)
# 				i += 1
				
if __name__ == '__main__':
    app.run(debug=True)