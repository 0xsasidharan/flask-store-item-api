import uuid
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from db import items , stores
from schemas import ItemSchema ,ItemUpdateSchema




blp = Blueprint("Item" , __name__ , description="Operation on Items ")



@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except:
            abort(404 , message = "Item not found")
        

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)

    def put(self ,  item_data , item_id):
        try:
            item = items[item_id]
            item |= item_data
            return item

        except:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted successfully."}, 200
        except:
            abort(404 , message = "Item not found")

@blp.route("/item")
class Item(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()


    @blp.arguments(ItemSchema)
    @blp.response(201 , ItemSchema)
    def post(self , item_data):

        for item in items.values():
            if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message="item already exist")

        if item_data["store_id"] not in stores:  
            abort(404 , message = "Store not found")



        item_id =uuid.uuid4().hex
        item = {**item_data , "id": item_id}
        items[item_id] = item



        return item 