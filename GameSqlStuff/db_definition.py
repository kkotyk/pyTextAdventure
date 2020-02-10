import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn
 
def select_val(conn, select_action_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(select_action_sql)

        rows = c.fetchall()
        return rows
    except Error as e:
        print(e)
 
 
def main():
    database = r"C:\Users\Reggi\Documents\Keith Game\GameSqlStuff\szdb.db"

    select_action = """SELECT * FROM Option WHERE frame_num = 1;"""
    get_option_list_sql = """select O.option_id from Option O LEFT JOIN FrameOption FO on O.option_id = FO.option_id WHERE FO.frame_num = 1;"""
 
    # create a database connection
    conn = create_connection(database)
 
    # create tables
    if conn is not None:
        # create projects table
        #create_table(conn, sql_create_projects_table)
        option_list = select_val(conn, get_option_list_sql)
        for o in option_list:
            print('option:' + str(o[0]))
            get_flag_for_option_sql = """select F.value 
                                        from Flag F 
                                        LEFT JOIN FlagOption FO on F.flag_id = FO.flag_id 
                                        LEFT JOIN Action A on FO.action = A.action_id
                                        WHERE FO.option_id = {} and A.action_id = 2""".format(o[0])
            flags_for_option = select_val(conn, get_flag_for_option_sql)
            get_item_for_option_sql = """select I.value 
                                        from Item I 
                                        LEFT JOIN ItemOption IO on I.item_id = IO.item_id 
                                        LEFT JOIN Action A on IO.action = A.action_id
                                        WHERE IO.option_id = {} and A.action_id = 2""".format(o[0])
            items_for_option = select_val(conn, get_item_for_option_sql)
            print('flag:' + str(flags_for_option))
            print('item:' + str(items_for_option))
    else:
        print("Error! cannot create the database connection.")
 
 
if __name__ == '__main__':
    main()

