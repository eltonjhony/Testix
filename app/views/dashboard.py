from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from app.views.constants.general import AppConstants
from app.views.utils.context import ContextUtils
from app.views.utils.loader import Template


@login_required
def index(request):
    return HttpResponse(Template.DASHBOARD.render(
        ContextUtils.put_context(title=AppConstants.DASHBOARD_TITLE),
        request))
