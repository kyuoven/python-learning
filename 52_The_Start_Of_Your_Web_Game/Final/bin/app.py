import web
from Final import #enter game map here

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
)

app = web.application(urls, globals())

#little hack so that the debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.sessions.Session (app, store, initializer=['room': None])
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        #this is used to setup the sessin with starting values.
        session.room = map.START 
        web.seeother("/game")

class GameEngine(object):
    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else: 
            #do you need this?
            return render.you_died()
        
    def POST(self):
        form = web.input(action=None)

        #fix this part
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")

if __name__ == "__main__":
    app.run()