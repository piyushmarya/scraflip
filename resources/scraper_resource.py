from flask_restful import Resource,reqparse
from flask import request

from models.scraper import dump_to_json,read_json,validate_link,get_price,dump_price_to_json



class ScraperResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('link',
                        help="Required Field",
                        required=True)
    def get(self, email):
        header = request.headers.get('data')
        price = get_price(header)
        dump_price_to_json(email, price)
        json_data = read_json()
        return json_data[email]['price']

    def post(self, email):
        data = self.parser.parse_args()
        return_message = validate_link(data["link"])
        if return_message['message'] != 'valid_link':
            return return_message, 404
        dump_to_json({email: return_message})
        return return_message,200
