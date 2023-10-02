from flask import Flask, render_template

app = Flask(__name__)
app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)

# For Task 4.1
@app.route('/')
def index():
    return render_template('index.html')

app.run()
