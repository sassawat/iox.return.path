from .api import bulkConfig

def initialize_routes(api):
    api.add_resource(bulkConfig, "/api/v1/bulkConfig")
