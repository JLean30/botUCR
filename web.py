from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
from pyrebase import pyrebase 

config = {
  "apiKey": "AIzaSyDLK2a5YDHZhrOduL9GmRZOeCt9RUbKCos",
  "authDomain": "botpythondb.firebaseapp.com",
  "databaseURL": "https://botpythondb.firebaseio.com",
  "storageBucket": "botpythondb.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()



# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = "http://extremetechcr.com/tienda/14-procesadores-amd"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product from the store page
containers = page_soup.findAll("div", {"class": "product-container product-block"})

# name the output file to write to local disk
#out_filename = "graphics_cards.csv"
# header of csv file to be written
headers = "brand,product_name,shipping \n"

# opens file, and writes headers
#f = open(out_filename, "w")
#f.write(headers)

# loops over each product and grabs attributes about
# each product
for container in containers:
    # Finds all link tags "a" from within the first div.
    titulo = container.div.div.img["title"]

    # Grabs the title from the image title attribute
    # Then does proper casing using .title()
  

    # Grabs the text within the second "(a)" tag from within
    # the list of queries.
    precio = container.find("div", class_="right-block").div.div.div.span.text

    # Grabs the product shipping information by searching
    # all lists with the class "price-ship".
    # Then cleans the text of white space with strip()
    # Cleans the strip of "Shipping $" if it exists to just get number
   # shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

    # prints the dataset to console

  #  print("product_name: " + product_name + "\n")
    data = {"name": titulo, "precio": precio.strip()}

    #db.child("procesadoresAmd").push(data)
proces = db.child("procesadoresAmd").order_by_child("name").get()
for proce in proces.each(): 
    print(proce.val())
  

