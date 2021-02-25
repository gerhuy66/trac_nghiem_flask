def getAllQuestion(mysql):
    conn = mysql.connect()
    cursor =conn.cursor()
    querry= "select * from exam_quest"
    cursor.execute(querry)
    return cursor.fetchall()

def getAllSubject(mysql):
    conn = mysql.connect()
    cursor =conn.cursor()
    querry= "select * from subject"
    cursor.execute(querry)
    return cursor.fetchall()

def getDapan(mysql):
	conn = mysql.connect()
	cursor = conn.cursor()
	querry = "select * from dapan"
	cursor.execute(querry)
	return cursor.fetchall()