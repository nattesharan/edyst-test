from flask import Flask,render_template
app = Flask(__name__)

def parse_xml(xmlstring, tag):
    start = 0
    posts = []
    while True:
        try:
            start = xmlstring.index('<%s>' % tag, start) + 2 + len(tag)
        except ValueError:
            break
        end = xmlstring.index('</%s>' % tag, start)
        item = xmlstring[start:end].strip()
        posts.append(item)
    return posts
@app.route('/<file>/<int:limit>', methods=['GET'])
def get_posts(file,limit):
    if file == 'example':
        f = open('example.xml')
    if file == 'example2':
        f = open('example2.xml')
    blog_posts = []
    data = f.read()
    posts = parse_xml(data,"item")
    for post in posts:
        blog_post = {}
        pub_date = parse_xml(post,'pubDate')
        link = parse_xml(post,"link")
        blog_post['pub_date'] = pub_date[0]
        blog_post['link'] = link[0]
        blog_posts.append(blog_post)
    return render_template('home.html',posts = blog_posts[0:limit])
@app.route('/')
def home():
    return render_template('dash.html')
if __name__=="__main__":
    app.run(port=3000, debug=True)