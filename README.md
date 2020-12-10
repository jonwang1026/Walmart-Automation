# Walmart-Automation

# Instructions:

### Run this in terminal
    $ git clone https://github.com/jonwang1026/Walmart-Automation
    $ cd Walmart-Bot
    $ virtualenv venv --python=python3.8
    $ pip3 install install selenium
  

### Fill in the following information in Personal_info
    info = {
      "first_name": "",
      "last_name": "",
      "street": "",
      "phone": "",
      "city": "",
      "email": "",
      "state": "",
      "zip": "", #example: 12345
      "creditCard" : "",
      "cvv": "",
      }

### Change default url to desired item 
      web = {
          change the 
          "url": "https://www.walmart.com/ip/Sony-PlayStation-4-1TB-Slim-Gaming-Console/101507200",
          "cart": "https://www.walmart.com/checkout/#/sign-in",
      }
### Download the correct chromedriver for your os
      chromdriver: http://chromedriver.chromium.org/downloads

### Run the program
      $ python3 main.py
