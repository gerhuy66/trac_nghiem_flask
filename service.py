def getAllQuestion(mysql):
    conn = mysql.connect()
    cursor =conn.cursor()
    querry= "select * from exam_quest"
    cursor.execute(querry)
    return cursor.fetchall()