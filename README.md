# Stripe Payment Gateway - Python Implementation
 A Simple Python CGI script for processing user payments for a website, using the <a href="https://stripe.com">Stripe</a> payment gateway.

This script was originally made in PHP (the original can be found <a href="https://financesonline.com/how-to-do-payment-gateway-integration-in-php-java-and-c/">here</a>) but was translated into Python by me. I had many extra dependencies that required me to use Python instead of PHP on my website, so I made this script.


# Requirements

- Python >= 3.6
- `stripe` and `mysql-connector-python` Python packages.
- A web server configured to run Python CGI scripts.
- A MySQL Database.
- A Stripe account with API keys.

*More detailed setup instructions are down below*


# Setup:

First, <a href="https://github.com/pigeonburger/stripe-gateway-python/releases/download/v1.0/stripe-gateway-python.zip">download</a> the Python and HTML files, extract them and put them both in the same folder somewhere in your web server directory.

<h3>Get your Stripe API keys:</h3>

1. Navigate to the *API Keys* section under *Developers* on your Stripe dashboard.

![image](https://user-images.githubusercontent.com/70826123/119243327-fd176200-bba8-11eb-8e37-de3dea68579a.png)

2. Copy your Publishable Key and Secret Key from under the "Standard keys" section. You will need them later.

![image](https://user-images.githubusercontent.com/70826123/119243393-a199a400-bba9-11eb-87bb-0f2d9690a098.png)


<h3>Install the required Python packages:</h3>

```
pip install stripe
```

```
pip install mysql-connector-python
```

<h3>Setting up the Database:</h3>

Create a new MySQL database called `stripepayments`, then run the following commands in the MySQL command-line:

```
USE stripepayments;
```

```
CREATE TABLE `orders` (
 `id` int(11) NOT NULL AUTO_INCREMENT,
 `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
 `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `card_num` bigint(20) NOT NULL,
 `card_cvc` int(5) NOT NULL,
 `card_exp_month` varchar(2) COLLATE utf8_unicode_ci NOT NULL,
 `card_exp_year` varchar(5) COLLATE utf8_unicode_ci NOT NULL,
 `item_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
 `item_number` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
 `item_price` float(10,2) NOT NULL,
 `item_price_currency` varchar(10) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'usd',
 `paid_amount` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
 `paid_amount_currency` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
 `txn_id` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
 `payment_status` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
 `created` datetime NOT NULL,
 `modified` datetime NOT NULL,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
```

<h3>Editing the Python and HTML files:</h3>

- On line 11, in `index.html`, insert your Stripe Publishable key that you got earlier.
- On line 19, in `submit.py`, insert your Stripe Secret key that you got earlier.
- On line 47, in `submit.py`, add the required details to connect to your MySQL database.

The files now have the basic working functionality, and can be further edited to suit your needs!
