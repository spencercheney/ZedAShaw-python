import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('/home/spencercheney/Documents/PythonPractice/ZedAShaw-python/exercises41-51/gothonweb/templates/')

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Stranger", greet="Hello")
        greeting = "%s, %s" %(form.greet, form.name)
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()