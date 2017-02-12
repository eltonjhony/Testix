from django.template import loader

class Template:
    GET_STARTED = loader.get_template('getstarted/get-started.html')
    DASHBOARD = loader.get_template('dashboard/dashboard.html')
