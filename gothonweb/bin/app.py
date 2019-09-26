import web
from gothonweb import map
from gothonweb import action

# web.config.debug = False

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
    '/blaster', 'Blaster',
    '/knive', 'Knive',
    '/dodge', 'Dodge',
    '/left', 'Left',
    '/right', 'Right',
    '/one', 'One',
    '/not_one', 'Not_One'
)

app = web.application(urls, globals())

#little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None})

    web.config._session = session
else:
    session = web.config._session

render = web.template.render('/home/spencercheney/Documents/PythonPractice/ZedAShaw-python/gothonweb/templates/', base="layout")

class Index(object):
    def GET(self):
        #this is used to "setup" the session with starting values
        session.room = map.START
        # return str(session.room.name)
        web.seeother("/game")


class GameEngine(object):
    
    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            #why is this here? do you need it
            return render.you_died()

class Blaster(object):
    def GET(self):
        if action.FIGHT.Blaster():
            if session.room.move_on():
                session.room = session.room.next
        else:
            session.room = map.DEATH
        web.seeother("/game")

class Knive(object):
    def GET(self):
        if action.FIGHT.Knive():
            if session.room.move_on():
                session.room = session.room.next
        else:
            session.room = map.DEATH
        web.seeother("/game")

class Dodge(object):
    def GET(self):
        if action.FIGHT.Dodge():
            if session.room.move_on():
                session.room = session.room.next
        else:
            session.room = map.DEATH
        web.seeother("/game")

class Left(object):
    def GET(self):
        session.room.add_action("L")
        if session.room.move_on():
                session.room = session.room.next
        web.seeother("/game")

class Right(object):
    def GET(self):
        session.room.add_action("R")
        if session.room.move_on():
                session.room = session.room.next
        web.seeother("/game")

class One(object):
    def GET(self):
        session.room = session.room.next
        web.seeother("/game")

class Not_One(object):
    def GET(self):
        session.room = map.DEATH
        web.seeother("/game")

if __name__ == "__main__":
    app.run()