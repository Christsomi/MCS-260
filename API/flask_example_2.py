from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/webpage1', methods = ['GET'])

def html_page():
  if request.method == 'GET':
    return render_template("example.html")

if __name__=='__main__':
  app.run()
