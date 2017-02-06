from django.template import loader

class Template:
    GET_STARTED = loader.get_template('testix/get-started.html')
    DASHBOARD = loader.get_template('testix/dashboard.html')
