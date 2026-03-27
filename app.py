from flask import Flask, render_template

# every python file has a built-in variable called __name__ and its value depends on how the file is run
app = Flask(__name__)

@app.route('/')

def index():
    # function knows to look at templates folder
    return render_template('index.html')

# checks if the file is being run directly or being imported --> if we run this file directly, the code inside this block executes, but if we import this file into another Python file, the code inside does not run

if __name__ == "__main__":
    app.run(debug=True)