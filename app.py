import os
from flask import Flask
from flask_restful import Api

from resources.scraper_resource import ScraperResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ScraperResource,'/scrape/<string:email>')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
