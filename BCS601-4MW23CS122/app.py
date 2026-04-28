from flask import Flask, request, render_template

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

@app.route('/', methods=['GET', 'POST'])
def home():
    result = {}
    if request.method == 'POST':
        num = int(request.form['number'])

        result['even_odd'] = "Even" if num % 2 == 0 else "Odd"
        result['prime'] = "Prime" if is_prime(num) else "Not Prime"
        result['factorial'] = factorial(num)
        result['sum_digits'] = sum(map(int, str(num)))

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)