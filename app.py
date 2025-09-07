from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("friends.db")
    cur = conn.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS friends (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birthday TEXT
        )
    """)
    conn.commit()
    conn.close()
init_db()

@app.route("/")
def index():
    conn = sqlite3.connect("friends.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM friends")
    friends = cur.fetchall()
    conn.close()
    return render_template("index.html", friends=friends)

@app.route("/add", methods=["POST"])
def add_friends():
    name = request.form.get("name")
    birthday=request.form.get("birthday")
    if name: 
        conn = sqlite3.connect("friends.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO friends (name,birthday) VALUES(?,?)", (name,birthday,))
        conn.commit()
        conn.close()
        return redirect("/")
    
@app.route("/remove/<int:friend_id>")
def remove_friend(friend_id):
        conn = sqlite3.connect("friends.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM friends WHERE id = ?", (friend_id,))
        conn.commit()
        conn.close()
        return redirect("/")

if __name__ == "__main__":
        app.run(debug=True)
        

                        

        
     