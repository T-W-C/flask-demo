from app import app


# links the URL given as a argument to the function
# two decorator below: /, /index
# when these URL's are reqursted flask invokes the function and pass the return value back to the browser as a result

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
# above is a view function

@app.route('/')
@app.route('/test')
def test():
    return "Hello, Bob!"
# above is a view function