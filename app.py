from flask import Flask, render_template, request,redirect,url_for,session
import sqlite3,hashlib
import datetime as dt
app = Flask(__name__)

def get_db():
  conn = sqlite3.connect('todo.db')
  return conn

dateNow = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

TAGS = [
    "Personal",
    "Work",
    "Study",
    "Shopping",
    "Finance",
    "Calls",
    "Messages",

    "Urgent",
    "Soon",
    "Later",
    "Recurring",
    "Today",
    "This Week",

    "Goal",
    "Self Development",
    "Skill",
    "Learning",
    "Focus",
    "Project",

    "Health",
    "Nutrition",
    "Sleep",
    "Meditation",
    "Exercise",

    "Programming",
    "Python",
    "Web",
    "Experiment",
    "Bug",
    "Deployment",

    "Games",
    "Movies",
    "Music",
    "Reading",
    "Design",
]
db = get_db()
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS user_credentials(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL,
            PASSWORD TEXT NOT NULL,
            CREATED_AT TEXT NOT NULL
  )""")


Login_Success = False
@app.route("/login",methods=["GET","POST"])
def login():
  global Login_Success
  if request.method == "GET":
    return render_template("login.html",
                            title='LOGIN PAGE')
  elif request.method == "POST":
    username = request.form.get("username")
    password = hashlib.sha256(request.form.get("password").encode())
    password = password.hexdigest()
    
    conn = get_db()
    cr = conn.cursor()
    
    cr.execute("SELECT * FROM user_credentials WHERE user_name=?",(username,))
    result = cr.fetchone()
    if result:
      if result[2] == password:
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
      else:
        Login_Success = True
        return redirect(url_for("login"))
    elif result == None:
      return redirect(url_for("register"))


@app.route("/register",methods=["GET","POST"])
def register():
  global Login_Success
  if request.method == "GET":
    return render_template("register.html",
                            title= "REGISTER PAGE")
  elif request.method == "POST":
    username = request.form.get("username")
    password = hashlib.sha256(request.form.get("password").encode())
    password = password.hexdigest()
    conn = get_db()
    cr = conn.cursor()
    
    cr.execute("SELECT * FROM user_credentials WHERE user_name=?",(username,))
    
    if cr.fetchone():
      return "User Arleady Exists"
    elif not cr.fetchone():
      cr.execute("INSERT INTO user_credentials(user_name,PASSWORD,CREATED_AT) VALUES(?,?,?)",(
        username,password,dateNow
      ))
      conn.commit()
      conn.close()
      Login_Success = True
      return redirect(url_for("home"))

@app.route("/",methods=["GET","POST"])

def home():
  # connect to the database and fetch all todo items
  conn = get_db()
  cr = conn.cursor()
  if not Login_Success :
    return redirect("/login")
  # Get all todo items from the database
  elif Login_Success:
    if request.method == "GET":
      cr.execute("SELECT * FROM todo")
      TodoItems = cr.fetchall()
      return render_template('add.html',
                              TodoItems=TodoItems,
                              dateNow=dateNow,
                              custom_css = "add.css",
                              title="Todo List Add Page",
                              Tags=TAGS)
    elif request.method == "POST":
      
      title = request.form.get('title')
      description = request.form.get('description')
      date = request.form.get('date')
      status = request.form.get('status')
      priority = request.form.get('priority')
      tag = request.form.get('Tag')
      cr.execute("INSERT INTO todo (title,description,status,priority,Tags,CREATED_AT) VALUES (?,?,?,?,?,?)",
                  (title, description, status,priority,tag,date))
      cr.execute("SELECT * FROM todo")
      TodoItems = cr.fetchall()
      conn.commit()
      conn.close()
      return render_template('add.html',
                              TodoItems=TodoItems,
                              dateNow=dateNow,
                              custom_css = "add.css",
                              title="Todo List Add Page")
    
    
@app.route("/delete/<int:id>", methods=["POST", "GET"])
def delete(id):
  conn = get_db()
  cr = conn.cursor()
  if not Login_Success :
    return redirect("/login")
  cr.execute("DELETE FROM todo WHERE id=?", (id,))
  if Login_Success:
    cr.execute("SELECT * FROM todo")
    TodoItems = cr.fetchall()
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/update/<int:id>",methods=["POST", "GET"])
def update(id):
  conn = get_db()
  cr = conn.cursor()
  if not Login_Success :
    return redirect("/login")
  if Login_Success:
    if request.method == "GET":
      cr.execute("SELECT * FROM todo WHERE id=?", (id,))
      todo = cr.fetchone()
      return render_template('update.html',
                              title_value=todo[1],
                              description_value=todo[2],
                              status_value=todo[3],
                              dateNow=dateNow,
                              custom_css = "update.css",
                              title="Update Todo",
                              Tags=TAGS,
                              id=id)
    elif request.method == "POST":
      title = request.form.get('title')
      description = request.form.get('description')
      date = request.form.get('date')
      status = request.form.get('status')
      priority = request.form.get('priority')
      tag = request.form.get('Tag')
      cr.execute("UPDATE todo SET title=?, description=?, status=?,priority=?,Tags=?,  CREATED_AT=? WHERE id=?",
                  (title, description, status,priority,tag, date, id))
      cr.execute("SELECT * FROM todo")
      TodoItems = cr.fetchall()
      conn.commit()
      conn.close()
      return redirect("/")


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0',port=9090)




