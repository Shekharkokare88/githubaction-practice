from flask import Flask, render_template
app = Flask(__name__)

return()
NNN


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
    #thus is Python code Updated

#neeeeeddddddddd
