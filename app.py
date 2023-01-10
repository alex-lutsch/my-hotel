from flask import Flask, request
from customer import Customer

app = Flask(__name__)
items = []

@app.route('/customers', methods=['GET'])
def list_customers():
    customer_list = ''
    for customer in items:
        customer_list += f'{customer.name}, {customer.address}, {customer.email}<br>'
    return customer_list

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        email = request.form['email']
        for customer in items:
            if customer.email == email:
                return 'Error: Customer with this email already exists.'
        customer = Customer(name, address, email)
        items.append(customer)
        return '<h2>Customer Added</h2>'
    else:
        return '''
            <html>
            <head>
            
            </head>
            <body>
                <form id="add-form" onsubmit="addCustomer(); return false;">
                    <label for="name">Name:</label><br>
                    <input id="name" name="name" placeholder="Enter your name"><br>
                    <label for="address">Address:</label><br>
                    <input id="address" name="address" placeholder="Enter your address"><br>
                    <label for="email">Email:</label><br>
                    <input id="email" name="email" placeholder="Enter your email"><br>
                    <button type="submit">Add Customer</button>
                </form>

                <form id="list-form" onsubmit="listCustomers(); return false;">
                    <button type="submit">List Customers</button>
                </form>
                <div id="customer-list"></div>
                <script>
            function addCustomer() {
                var form = document.getElementById('add-form');
                var name = form.elements['name'].value;
                var address = form.elements['address'].value;
                var email = form.elements['email'].value;

                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/');
                xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                xhr.onload = function() {
                    if (xhr.status === 200) {
                        alert(xhr.responseText);
                    }
                    else {
                        alert('Error: ' + xhr.responseText);
                    }
                };
                xhr.send(`name=${name}&address=${address}&email=${email}`);
            }

            function listCustomers() {
                var xhr = new XMLHttpRequest();
                xhr.open('GET', '/customers');
                xhr.onload = function() {
                if (xhr.status === 200) {
                    document.getElementById('customer-list').innerHTML = xhr.responseText;
                }
                 else {
                    alert('Error: ' + xhr.responseText);
                }
            };
            xhr.send();
                    }
                    </script>
                    </body>
                    </html>
            '''



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)