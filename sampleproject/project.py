from flask import Flask, render_template, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home2.html')


if __name__ == '__main__':
    app.run()