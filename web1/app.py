from flask import *

app = Flask(__name__)

foods = [
      {
        "title": "thit cho",
        "description": "rat ngon",
        "link": "https://mfa.cachefly.net/mfa/images/uploads/2018/01/1200x630/1280px-Dog_meat_in_Ninh_Binh.jpg",
        "type": "eat",
      },
      {
        "title":"bun cha",
        "description":"ngon khoong kem ngoc trinh",
        "link":"https://img.delicious.com.au/8nXC730a/w759-h506-cfill/del/2015/10/bun-cha-16771-2.jpg",
        "type":"eat",
      },
      {
        "title":"bun cha",
        "description":"ngon khoong kem ngoc trinh",
        "link":"https://img.delicious.com.au/8nXC730a/w759-h506-cfill/del/2015/10/bun-cha-16771-2.jpg",
        "type":"eat"
      },  
    ]
 
@app.route('/')
def index():
    return "hello C4E29"

@app.route('/say-hi')
def say_hi():
    return "hello anh kha"


@app.route('/say-hi/<name>')    
def say_hi_anyone(name):
    return "xin chao {}".format(name)

@app.route('/add/<int:x>/<int:y>')
def phep_cong(x,y):
    tong = x + y 
    return str(tong)

@app.route('/food')
def food():
    return render_template('food.html',foods = foods)

@app.route('/food/<int:index>')
def detail(index):
    food_detail = foods[index]
    return render_template('food_detail.html', food_detail=food_detail)


if __name__ == '__main__':
  app.run(debug=True)
 