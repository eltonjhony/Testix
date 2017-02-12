from django.http import HttpResponse

from constants.view_constants import AppConstants
from utils.context import ContextUtils
from utils.loader import Template

def get_started(request):
    return HttpResponse(Template.GET_STARTED.render(
        ContextUtils.put_context(title=AppConstants.INDEX_TITLE),
        request))
