import mysql.connector

DATABASE = mysql.connector.connect(
    host='localhost',
    user='root',
    password='pass',
)

/Users/em/Library/PROGRAMMING/PYTHON/project3_467def db_exists():
    try:
        connection = CONNECTION()
        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES")
        db = cursor.fetchall()
        for data in db:
            if data in db:
                return True
            return False
    except Exception as e:
        print(str(e))
        return False


def CONNECTION():
    DB = mysql.connector.connect(
        host='localhost',
        user='root',
        password='pass',
        database='DB_NAME'
    )
    try:
        return DB
    except Exception as e:
        print(str(e))
        return False


def create_db():
    if not db_exists():
        cursor = DATABASE.cursor()
        cursor.execute('CREATE SCHEMA DB_NAME')


def table_exists(name):
    try:
        connection = CONNECTION()
        cursor = connection.cursor()
        cursor.execute(f"SHOW TABLES LIKE '{name}'")
        result = cursor.fetchone()
        return result is not None
    except Exception as e:
        print(str(e))
        return False


def create_baselight_table(collection):
    # Create a new table 'baselight'
    if db_exists():
        if not table_exists(collection):
            try:
                connection = CONNECTION()
                cursor = connection.cursor()
                sql = f'''
                                CREATE TABLE {collection} (
                                    `Path` VARCHAR(255),
                                    `Frames` VARCHAR(255)
                                )
                                '''
                cursor.execute(sql)
            except Exception as e:
                print(str(e))
    else:
        create_db()  # Create new database 'qa_db'
        create_baselight_table(collection)  # Create new table


def create_xytech_table(collection):
    # Create a new table 'xytech'
    if db_exists():
        if not table_exists(collection):
            try:
                connection = CONNECTION()
                cursor = connection.cursor()
                sql = f'''
                                CREATE TABLE {collection} (
                                    `Workorder` VARCHAR(255),
                                    'Location' VARCHAR(255),
                                    'Notes' VARCHAR(255),
                                    'Producer' VARCHAR(255),
                                    `Frames` VARCHAR(255)
                                )
                                '''
                cursor.execute(sql)
            except Exception as e:
                print(str(e))
    else:
        create_db()  # Create new database 'qa_db'
        create_xytech_table(collection)  # Create new table