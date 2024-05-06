from flask import Flask, render_template, request

app = Flask(__name__)

# Define your math functions
def solve_math_problem(input_data):
    # Your math solving logic here
    result = input_data * 2
    return result

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    input_data = int(request.form['input_data'])
    result = solve_math_problem(input_data)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
