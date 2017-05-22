# -*- coding = utf-8 -*-
#!/usr/bin/env python
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('cover.html')


if __name__ == "__main__":
    app.run(debug = True)   
