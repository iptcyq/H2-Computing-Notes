from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("postreq.html")

@app.route('/request', methods=["post"])
def req():
    username = request.form["uname"]
    connection = sqlite3.connect("social_media.db")
    query = '''SELECT User.UserID, User.Name, Post.PostText, Tag.Tag
            FROM Post
            INNER JOIN User ON User.UserID = Post.UserID
            LEFT JOIN PostTag ON PostTag.PostID = Post.PostID
            LEFT JOIN Tag ON Tag.TagID = PostTag.TagID
            WHERE User.Name = ?'''
    unfiltered_posts = connection.execute(query, (username,)).fetchall()
    connection.close()

    if len(unfiltered_posts) <= 0:
        return "Error: name not found"

    filtered_posts = [list(unfiltered_posts[0][:3])+[[unfiltered_posts[0][3]]]]
    for i in range(1,len(unfiltered_posts)): 
        if unfiltered_posts[i][0] == unfiltered_posts[i-1][0] and unfiltered_posts[i][2] == unfiltered_posts[i-1][2]:
            filtered_posts[-1][3].append(unfiltered_posts[i][3])
        elif unfiltered_posts[i][3] == None:
            filtered_posts.append(list(unfiltered_posts[i]) )
            print("no tag")
        else:
            print("new post")
            filtered_posts.append(list(unfiltered_posts[i][:3])+[[unfiltered_posts[i][3]]])

    return render_template("result.html", uname=username, posts=filtered_posts)
    
if __name__ == "__main__":
    app.run()
