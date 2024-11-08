# 让我们写的程序支持服务访问
# 需要一个web框架
from flask import Flask,render_template,request
from random import randint
app = Flask(__name__)

hero = ['德玛西亚之力','影流之主','盲僧','迅捷斥候','皮城女警','堕落天使','德邦总管','光辉女郎','永恒梦魇','九尾妖狐','暗裔剑魔','皎月女神',
        '刀锋之影','机械公敌','虚空行者','诺克萨斯之手','复仇之矛','沙漠皇帝','爆破鬼才']


@app.route('/index')
def index():
    return render_template('index.html',hero=hero)

@app.route('/choujiang')
def choujiang():
    num = randint(0,len(hero)-1)
    return render_template('index.html',hero=hero,h=hero[num])

app.run(debug=True)