from pyramid.config import Configurator
from pyramid_mailer import Mailer


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    mailer = Mailer()
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    
    config.registry['mailer'] = Mailer.from_settings(settings)
    #config.include('pyramid_mailer')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/jinventory/')
    config.add_route('request', '/jinventory/request/')
    config.add_route('laptops','/jinventory/laptops/')
    config.add_route('release','/jinventory/release/')
    config.add_route('accept','/jinventory/accept/')
    config.scan()
    return config.make_wsgi_app()
