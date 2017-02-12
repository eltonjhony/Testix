from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from constants.view_constants import AppConstants
from utils.context import ContextUtils
from utils.loader import Template


@login_required
def index(request):
    return HttpResponse(Template.DASHBOARD.render(
        ContextUtils.put_context(title=AppConstants.DASHBOARD_TITLE),
        request))
