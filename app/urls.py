from flask import request
from app.user import login_user,register_user
from app.templates import create_template, get_all_templates, get_template, update_template, delete_template
from app.token_utils import token_required

TEMPLATES='/template/<template_id>'

def register_routes(app):
    # User routes
    app.add_url_rule('/register', 'register', register_user, methods=['POST'])
    app.add_url_rule('/login', 'login', login_user, methods=['POST'])

    # Template routes
    app.add_url_rule('/template', 'create_template', create_template, methods=['POST'])
    app.add_url_rule('/template', 'get_all_templates', get_all_templates, methods=['GET'])

    app.add_url_rule(TEMPLATES, 'get_template', get_template, methods=['GET'])
    app.add_url_rule(TEMPLATES, 'update_template', update_template, methods=['PUT'])
    app.add_url_rule(TEMPLATES, 'delete_template', delete_template, methods=['DELETE'])

    app.view_functions['create_template'] = token_required(app.view_functions['create_template'])
    app.view_functions['get_all_templates'] = token_required(app.view_functions['get_all_templates'])
    app.view_functions['get_template'] = token_required(app.view_functions['get_template'])
    app.view_functions['update_template'] = token_required(app.view_functions['update_template'])
    app.view_functions['delete_template'] = token_required(app.view_functions['delete_template'])
