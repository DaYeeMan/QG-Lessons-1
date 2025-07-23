from flask import Flask, render_template

app = Flask(__name__, template_folder='static/templates/level2')

@app.route('/lesson')
def lesson():
    return render_template('Moment_Generating_Functions.html')

if __name__ == '__main__':
    app.run(debug=True) 