from flask import render_template
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

'''
Previously the html was explicitly defined
However this is inefficient.
The functionality can be segregated through use of templates
'''
# @app.route('/page')
# def test2():
#     user = {'username':'Tommo'}
#     return '''
#     <html>
#     <head>
#         <title> Home page </title>
#     </head>
#     <body>
#         <h1> Hello ''' + user['username'] + '''! </h1>
#     </body>
#     </html>'''

@app.route('/page')
def test2():
    user = {
        'username':'Thomas'
    }
    return render_template('index.html', title='Testing template', user=user)
