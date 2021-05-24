from flask import Flask
app = Flask(__name__)

@app.route('/test',methods = ['GET'])
def hello_world():
   return {
       "1": 1,
       "2": 2
   }

if __name__ == '__main__':
   app.run()