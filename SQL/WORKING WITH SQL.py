import pymysql


def gather_columns(column, all_column):
    for dic in column:
        all_column.append(dic[0])
    return all_column


def gather_values(column, records):
    for heads in column:
        values = input(heads)
        records.append(values)
    return records


def login():
    try:
        db = pymysql.connect(host=input("host name="), user=input("user name="), password=input("password="),
                             database=input("database name="))
        print("connection successful")
        return db
    except:
        print("connection error.try loging in again")
        login()


def insert(database,curser, table):
    # getting columns
    curser.execute("show columns from table1")
    columns = curser.fetchall()

    # gathering values for insert statement
    all_values = []
    all_columns = []
    all_columns = gather_columns(columns, all_columns)
    all_values = gather_values(all_columns, all_values)
    columns = ""
    for col in all_columns:
        columns += col + ','

    # execute
    curser.execute(str("INSERT INTO " + table + "(" + str(columns)[0:-1] + ")VALUES(" + str(all_values)[1:-1] + ")"))
    database.commit()


def update(database):
    table = input("table name")
    curser = database.cursor()
    try:
        curser.execute(str("show columns from " + table))
    except:
        print("table not found.\n Please enter a valid table name")
        update(curser)
    options = input('OPTIONS:\n'
                    '1.INSERT ROW\n'
                    '2.DELETE ROW\n'
                    )
    if options == "1":
        insert(database,curser, table)


def show_all_tables(db,cursor):
    cursor.execute("show tables")
    tables = cursor.fetchall()
    n = 1
    for table in tables:
        print(str(n) + ".", table[0])
        n += 1
    menu(db,cursor)


def run():
    input("Welcome to SQL \n "
          "Please login to access your database")
    db = login()
    curser = db.cursor()
    menu(db,curser)


def drop(db,cursor):
    table = input("ENTER THE TABLE NAME TO DELETE")
    cursor.execute(str("drop table if exists "+str(table)))
    db.commit()


def create_new_table(db,cursor):
    table = input("ENTER THE TABLE NAME")

    num = int(input("ENTER THE NUMBERS OF COLUMNS"))
    n = 1
    columns = {}

    while n <= num:       # GETTING COLUMNS AND VALUES
        column = input("COLUMN" + str(n))
        columns[str(column)] = input("DATA TYPE")
        n += 1

    statement = ""       # GET STATEMENT FOR EXECUTION
    for key in columns:
        statement += str(key) + " " + str(columns[key]) + ","

    cursor.execute("CREATE TABLE "+str(table)+"(" + statement[:-1] + ")")
    db.commit()


def menu(db,curser):
    options = input('OPTIONS:\n'
                    '1.CREATE TABLE\n'
                    '2.UPDATE A TABLE\n'
                    '3.DELETE A TABLE\n'
                    '4.SHOW ALL TABLES\n')
    if options == "1":
        create_new_table(db,curser)
    if options == "2":
        update(db)
    if options == "3":
        drop(db,curser)
    if options == "4":
        show_all_tables(db,curser)


run()
