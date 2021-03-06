from flask import Blueprint

blueprint = Blueprint('{{ cookiecutter.identifier }}', __name__,
                      url_prefix='/{{ cookiecutter.identifier }}',
                      template_folder='templates')


@blueprint.route('/some/url')
def some_endpoint():
    return 'not implemented'
