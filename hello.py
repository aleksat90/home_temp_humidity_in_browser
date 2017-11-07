from flask import Flask
app = Flask(__name__)

from flask import  render_template

import sys
import Adafruit_DHT



#Deaktiviraj kad uradis release
app.debug = True


@app.route("/")
def hello():
	vlaga,temp = procitaj_DHT11()
	return render_template('hello.html',temp = temp,vlaga = vlaga )



def procitaj_DHT11():
	vlaga,temp = Adafruit_DHT.read_retry(11,4)
	return vlaga,temp




if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8080)
