def getAllQuestion(mysql,eId):
    conn = mysql.connect()
    cursor =conn.cursor()
    querry= "select * from exam_quest where e_id = %s"
    cursor.execute(querry,(eId))
    return cursor.fetchall()

def getAllSubject(mysql):
    conn = mysql.connect()
    cursor =conn.cursor()
    querry= "select * from subject"
    cursor.execute(querry)
    return cursor.fetchall()

def getExamBySubject(mysql,subId):
    conn = mysql.connect()
    cursor =conn.cursor()
    querry= "select * from exam where exam.sub_id = %s"
    cursor.execute(querry,(subId))
    return cursor.fetchall()

def getDapan(mysql):
	conn = mysql.connect()
	cursor = conn.cursor()
	querry = "select * from dapan"
	cursor.execute(querry)
	return cursor.fetchall()
