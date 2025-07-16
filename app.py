from flask import Flask, render_template

app = Flask(__name__, template_folder='static/templates')

@app.route('/lesson')
def lesson():
    return render_template('Limits_and_Continuity.html')

if __name__ == '__main__':
    app.run(debug=True) 