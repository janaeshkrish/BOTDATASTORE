import mysql.connector
import sqlalchemy
import pandas as pd

def DataUpdate(name,number,email,occupation):
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='25111998',
        database='rasadb'
    )
    mycursor = db.cursor()

    #created a database
    #mycursor.execute("CREATE DATABASE rasadb")

    #create a table
    #mycursor.execute('CREATE TABLE details (name VARCHAR(50),number int,email VARCHAR(255),occupation VARCHAR(50))')

    # mycursor.execute('DESCRIBE details')
    # for i in mycursor:
    #     print(i)


    #To insert the values in database
    query = 'INSERT INTO details (name,number,email,occupation) VALUES ("{0}","{1}","{2}","{3}");'.format(name,number,email,occupation)
    mycursor.execute(query)
    db.commit()

    print(mycursor.rowcount,'Record INserted')


def DataGet(column,occup):

    engine = sqlalchemy.create_engine('mysql+pymysql://root:25111998@localhost:3306/rasadb')
    df = pd.read_sql_table('details',engine)
    data=df[column][df["occupation"]==occup]

    final = data.to_list()
    if len(final)>=1:

        return final
    else:
        return ["There is no data. "]
    
   
# if __name__=="__main__":

#     DataGet("email","software developer")

#     DataUpdate('janaeshwar','9787553774','janaesh@gmail.com','software developer')

    



