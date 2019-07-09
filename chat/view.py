from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Report
from .models import Heat_map
# from .models import Predictions
# from .models import Tickers
# from .models import Models


def home_view(request):
	heat_map = Heat_map.objects.all()
	report = Report.objects.filter( ticker_db='GARAN_TI_EQUITY').values('report_content')
	return render(request, 'index.html',{'heat_maps':heat_map,'report':report})