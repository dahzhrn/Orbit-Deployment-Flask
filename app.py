'''
	Membuat CV Web Static dengan Flask
'''

# =[Modules dan Packages]========================
from flask import Flask, render_template

# =[Variabel Global]=============================
app   = Flask(__name__, static_url_path='/static')

# =[Routing]=====================================
@app.route("/")
def beranda():
    return render_template('index.html')

# =[Main]========================================
if __name__ == '__main__':
	app.run(host="localhost", port=5000, debug=True)