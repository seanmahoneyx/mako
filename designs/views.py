from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index_page(request):
    req_designs = request.user.requested_designs.all().order_by('design_num')
    context = {'designs': req_designs}
    return render(request, "designs/index.html", context)