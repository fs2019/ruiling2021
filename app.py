from flask import Flask,request,render_template,redirect

app=Flask(__name__)

@app.route('/brand')
def brand():
    title='brand'
    return render_template('brand.html',title=title)
@app.route('/ContactUs')
def ContactUs():
    title='contactUs'
    return render_template('ContactUs.html',title=title)
@app.route('/')
def AboutUs():
    title='AboutUs'
    return render_template('AboutUs.html',title=title)
@app.route('/CompanyNews')
def CompanyNews():
    title='CompanyNews'
    return render_template('CompanyNews.html',title=title)
@app.route('/GNetwork')
def GNetwork():
    title='GNetwork'
    return render_template('GNetwork.html',title=title)
@app.route('/ASS')
def ASS():
    title='ASS'
    return render_template('ASS.html',title=title)
@app.route('/goodsIndex')
def goodsIndex():
    title='goodsIndex'
    return render_template('goodsIndex.html',title=title)
@app.route('/JiTa')
def JiTa():
    title='JiTa'
    return render_template('goods/JiTa.html',title=title)
@app.route('/layout')
def layout():
    title='layout'
    return render_template('layout.html',title=title)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=80,debug=True)
