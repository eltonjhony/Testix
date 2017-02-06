from django.http import HttpResponse

from app.views.constants.general import AppConstants
from app.views.utils.context import ContextUtils
from app.views.utils.loader import Template

def get_started(request):
    return HttpResponse(Template.GET_STARTED.render(
        ContextUtils.put_context(title=AppConstants.INDEX_TITLE),
        request))
