import pymysql
conn = pymysql.connect(
    host="surveypythondb.c9wc8aya24by.us-east-1.rds.amazonaws.com",
    user="admin",
    password="surveypass",
    database="survey",
    port=3306
)
print("Connected!")
