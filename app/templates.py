from flask import request, jsonify
from app.models import Template, User
from bson import ObjectId


TEMPLATES='Template not found'

def create_template(current_user):
    data = request.get_json()

    required_fields = ['template_name', 'subject', 'body']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({'message': f'Missing required fields: {", ".join(missing_fields)}'}), 400

    user = User.objects(id=current_user.id).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    new_template = Template(
        template_name=data['template_name'],
        subject=data['subject'],
        body=data['body'],
        user=user
    )

    new_template.save()

    return jsonify({"message": "Template created successfully"}), 201



def get_all_templates(current_user):

    user_id = request.args.get('user_id', current_user.id)

    templates = Template.objects(user=user_id)

    if not templates:
        return jsonify({'message': 'No templates found for this user'}), 404

    return jsonify([template.to_json() for template in templates]), 200


def get_template(current_user, template_id):

    try:
        template = Template.objects(id=ObjectId(template_id)).first()
    except Exception as e:
        return jsonify({'message': f'Invalid ObjectId: {e}'}), 400

    if not template:
        return jsonify({'message': TEMPLATES}), 404

    return jsonify(template.to_json()), 200

def update_template(current_user, template_id):
    data = request.get_json()

    template = Template.objects(id=ObjectId(template_id)).first()

    if not template:
        return jsonify({'message': TEMPLATES}), 404

    if 'template_name' in data:
        template.update(set__template_name=data['template_name'])
    
    if 'subject' in data:
        template.update(set__subject=data['subject'])
    
    if 'body' in data:
        template.update(set__body=data['body'])

    return jsonify({"message": "Template updated successfully"}), 200



def delete_template(current_user,template_id):

    template = Template.objects(id=ObjectId(template_id)).first()

    if not template:
        return jsonify({'message': TEMPLATES}), 404
    template.delete()

    return jsonify({'message': 'Template deleted successfully'}), 200
