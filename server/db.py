import sqlite3
from sqlite3 import Error


db_file = "myapp.db"


def db_init():
    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
        exit(1)
    cur = conn.cursor()
    q = """\
        create table if not exists g_table(
            img_id varchar(50) primary key,\
            img_name varchar(50),\
            img_date date\
        )\
    """
    cur.execute(q)
    cur.execute("""
        create table if not exists clu_table(
            clu_id varchar(30) primary key,
            clu_name varchar(50)
        )
    """)
    cur.execute(""" 
        create table if not exists g_to_clu_rel(
            id INTEGER primary key AUTOINCREMENT,
            clu_id varchar(30),
            img_id varchar(30),
            foreign key(clu_id)references clu_table(clu_id) ON DELETE CASCADE,
            foreign key(img_id) references g_table(img_id) ON DELETE CASCADE
        )
    """)
    print(cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall())
    conn.commit
    if conn:
        conn.close()


def make_id():
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    data = cur.execute("SELECT * FROM g_to_clu_rel").fetchall()
    cur.execute(
        """create table if not exists uniq_face as select * from g_to_clu_rel where 1=2 """)
    cur.execute("delete from uniq_face")
    uniqid = set()
    for row in data:
        if(row[1] in uniqid):
            continue
        uniqid.add(row[1])
        cur.execute("insert into uniq_face values(?,?,?)", row)
    print(cur.execute("select * from uniq_face").fetchall())
    con.commit()
    con.close()


# make_id()
