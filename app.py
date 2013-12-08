from flask import Flask, render_template, url_for
from flask.ext.markdown import Markdown
import codecs

app = Flask(__name__)
Markdown(app)
app.debug = True

def get_asides():
    asides = codecs.open('static/articles/asides.txt','rb','utf-8').read().split('#!')
    counter = 0
    d = {}
    for aside in asides:
        if len(aside)<10:
            pass
        else:
            counter+=1
            out=''
            for row in aside.split('\n'):
                if row[0:3] == '#ID':
                    _id = row.split()[1]
                else:
                    out+=row
            d['AS'+_id] = out
            print d
    return d

@app.route('/')
def index():
    article_md = codecs.open('static/articles/article.md','rb', 'utf-8').read()
    asides = get_asides()
    return render_template('index.html', article_md=article_md, asides=asides)

if __name__=='__main__':
    app.run()
