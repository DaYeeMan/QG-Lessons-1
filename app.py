from flask import Flask, render_template

app = Flask(__name__, template_folder='static/templates/level3')

@app.route('/lesson')
def lesson():
    return render_template('Stationary_Distributions.html')

if __name__ == '__main__':
    app.run(debug=True) 