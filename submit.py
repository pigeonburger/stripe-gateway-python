# Stripe Payment Gateway - Python CGI Implementation
# By Pigeonburger (https://github.com/pigeonburger)
#########################
# Translated into Python from the PHP script found here: https://financesonline.com/how-to-do-payment-gateway-integration-in-php-java-and-c/

import cgi, stripe, datetime, mysql.connector
form = cgi.FieldStorage()

# POST Values
token = form.getvalue('stripeToken')
name = form.getvalue('name')
email = form.getvalue('email')
card_num = form.getvalue('card_num')
card_cvc = form.getvalue('cvc')
card_exp_month = form.getvalue('exp_month')
card_exp_year = form.getvalue('exp_year')

# Put your Stripe API Secret Key here
stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

# Customer Info
customer = stripe.Customer.create(email=email, source=token)

# Product Info
itemName = "Pigeonburger's Python Stripe Payment"
itemNumber = "12345654321"
itemPrice = 20 * 100 # Convert $20 to cents
currency = 'usd'
orderID = "SKA92712382139"

charge = stripe.Charge.create(customer=customer['id'], amount=itemPrice, currency=currency, description=itemName, metadata={'order_id': orderID})

# If the transaction was successful
if charge["amount_refunded"] == 0 and charge['failure_code'] == None and charge['paid'] == 1 and charge['captured'] == 1:

    # Get various data from the Charge response.
    amount = charge['amount']
    balance_transaction = charge['balance_transaction']
    currency = charge['currency']
    status = charge['status']
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create MySQL query
    mysql_query = f"INSERT INTO orders(name,email,card_num,card_cvc,card_exp_month,card_exp_year,item_name,item_number,item_price,item_price_currency,paid_amount,paid_amount_currency,txn_id,payment_status,created,modified) VALUES ('{name}','{email}','{card_num}','{card_cvc}','{card_exp_month}','{card_exp_year}','{itemName}','{itemNumber}','{itemPrice}','{currency}','{amount}','{currency}','{balance_transaction}','{status}','{date}','{date}')"

    # Connect to database and execute the query above (then commit changes)
    mysqldb = mysql.connector.connect(host="localhost", user="database_username", password="database_password", database="stripepayments")
    mysqlcursor = mysqldb.cursor()
    mysqlcursor.execute(mysql_query)
    mysqldb.commit()

    # Get the ID of this latest order
    last_insert_id = mysqlcursor.lastrowid

    if last_insert_id and status == 'succeeded':
        statusmsg = f'<h2>The Transaction was successful</h2><h4>Order ID: {last_insert_id}</h4>'
    else:
        statusmsg = 'Transaction Failed.'
else:
    statusmsg = 'Transaction Failed.'

# Print the status (before using this in production, I'd do a 303 redirect to a static HTML page so they can't keep submitting this every time they reload)
print("Content-type: text/html")
print()
print(statusmsg)