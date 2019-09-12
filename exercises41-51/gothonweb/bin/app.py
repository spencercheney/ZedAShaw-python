import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('/home/spencercheney/Documents/PythonPractice/ZedAShaw-python/exercises41-51/gothonweb/templates/')

class Index(object):
    def GET(self):
        greeting = "Hello World"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()