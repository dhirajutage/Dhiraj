import cx_Oracle
class manoj :
    user_name = 'hr'
    password = 'hr'
    connection_str =  'localhost:1521/orcl'
    def __init__(self, frist_name , surname=None, age=None, sex=None):
        self.frist_name = frist_name
        self.surname = surname
        self.age = age
        self.sex  = sex

    def make_db_connection(self):
        conncetion = cx_Oracle.connect(manoj.user_name,manoj.password, manoj.connection_str)
        print("Database connection made successfully")
        return conncetion

    def insert_statement(self ,conncetion):
        ab = conncetion.cursor()
        sql = f"Insert into person values('{self.frist_name}','{self.surname}',{self.age},'{self.sex}')"
        print(sql)
        ab.execute(sql)
        ab.close()
        conncetion.commit()
        conncetion.close()
        print("database connection closed successfully")
    def delete_add(self, conncetion):
        ab = conncetion.cursor()
        sql = f"delete from person where upper(first_name) = upper('{self.frist_name}')"
        print(sql)
        ab.execute(sql)
        ab.close()
        conncetion.commit()
        conncetion.close()
        print("Record deleted successfully from Table")


if __name__ == "__main__":
    while True:
        try:
            #print("Enter your choice insert or delete or search--Insert(I),Deleted(D) Seach(S) ")
            choice= str(input("Enter your choice insert or delete or search--Insert(I),Deleted(D) Seach(S) "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break

    if choice == 'I':
        first_name = input("Enter First Name")
        last_name  = input("Enter Surname")
        age = int(input("Enter your age"))
        sex = input("Enter your Sex")
        abc = manoj(str(first_name),str(last_name),str(age),str(sex))
        conn = abc.make_db_connection()
        abc.insert_statement(conn)
    elif choice == 'D':
         inp = input("Enter First_name")
         abc= manoj(str(inp))
         conn = abc.make_db_connection()
         abc.delete_add(conn)

print("Programme completed successfully")
