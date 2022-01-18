from flask import Flask
from flask_restful import request ,Resource, Api


app = Flask(__name__)
api = Api(app)

class HeaderParser(Resource):
    def get(self):
        return {
            "ipaddres": request.remote_addr,
            "language": request.headers.get('accept-language'),
            "software": request.headers.get('user-agent')}

api.add_resource(HeaderParser, '/api/whoami')

if __name__ == '__main__':
    app.run(debug=True)