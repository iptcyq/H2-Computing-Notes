from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("postcreate.html")

@app.route('/create', methods=["post"])
def create():
    uID, content, tags = request.form["uID"],request.form["content"],request.form["tags"]
    connection = sqlite3.connect("social_media.db")

    # check if person exists
    res = connection.execute('''SELECT * FROM User WHERE UserID = ?''', (uID,))
    if not res:
        return "Error User ID invalid"

    # insert tags
    tags_ID = []
    res = connection.execute('''SELECT Tag FROM Tag''').fetchall()
    print(res)
    for tag in tags.split(','):
        if (tag,) not in res: # NOT DONE 
            connection.execute('''INSERT INTO Tag(Tag) VALUES (?)''', (tag,))
        tID = connection.execute('''SELECT TagID FROM Tag WHERE
            Tag = ?''', (tag,)).fetchone()
        tags_ID.append(tID[0])
    
    connection.commit()

    # insert post
    connection.execute('''INSERT INTO
    Post(UserID, PostText) VALUES (?,?)''', (uID, content))
    connection.commit()
    pID = connection.execute('''SELECT PostID FROM Post WHERE
        PostText = ?''', (content,)).fetchone()
    print(pID[0])

    # insert post tag
    for tag in tID:
        connection.execute('''INSERT INTO PostTag(PostID, TagID)
        VALUES (?,?)''', (pID[0], tag))
    
    connection.commit()
    connection.close()
    return "post done"
       
if __name__ == "__main__":
    app.run()
