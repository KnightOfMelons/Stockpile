from django.db.models import Avg, Max, Min, Sum, F
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Roll
from .forms import RollForm
from django.views.generic import ListView, DeleteView
from datetime import datetime


class RollsListView(ListView):
    model = Roll
    template_name = 'stockpile/index.html'


class DELETEDRollsListView(ListView):
    model = Roll
    template_name = 'stockpile/deleted.html'


class ROLLDelete(DeleteView):
    model = Roll
    template_name = 'stockpile/deleted.html'
    success_url = reverse_lazy('deleted')


def change_delete_time(request, pk):
    x = Roll.objects.get(id=pk)
    x.date_removed = datetime.now()
    x.save()

    return redirect('main')

# ================================== ДОБАВЛЕНИЕ ==================================

def add_roll(request):
    if request.method == 'POST':
        form = RollForm(request.POST)
        if form.is_valid():
            roll = form.save(commit=False)
            roll.date_added = datetime.now()
            roll.save()
            return redirect('main')
    else:
        form = RollForm()
    return render(request, 'stockpile/add_roll.html', {'form': form})


# ================================== ПОИСК ==================================
def search_rolls(request):
    if request.method == 'GET':
        min_id = request.GET.get('min_id')
        max_id = request.GET.get('max_id')

        if min_id is not None and max_id is not None:
            rolls = Roll.objects.filter(id__range=(min_id, max_id))
            return render(request, 'stockpile/search/ID/search_resultsID.html', {'rolls': rolls})

    return render(request, 'stockpile/search/ID/search_form.html')


def search_rollsLENGTH(request):
    if request.method == 'GET':
        min_length = request.GET.get('min_length')
        max_length = request.GET.get('max_length')

        if min_length is not None and max_length is not None:
            rolls = Roll.objects.filter(length__range=(min_length, max_length))
            return render(request, 'stockpile/search/LENGTH/search_resultsLENGTH.html', {'rolls': rolls})

    return render(request, 'stockpile/search/LENGTH/search_formLENGTH.html')


def search_rollsWEIGHT(request):
    if request.method == 'GET':
        min_weight = request.GET.get('min_weight')
        max_weight = request.GET.get('max_weight')

        if min_weight is not None and max_weight is not None:
            rolls = Roll.objects.filter(weight__range=(min_weight, max_weight))
            return render(request, 'stockpile/search/WEIGHT/search_resultsWEIGHT.html', {'rolls': rolls})

    return render(request, 'stockpile/search/WEIGHT/search_formWEIGHT.html')


def search_rollsDATEADDED(request):
    if request.method == 'GET':
        min_dateadded = request.GET.get('min_dateadded')
        max_dateadded = request.GET.get('max_dateadded')

        if min_dateadded is not None and max_dateadded is not None:
            rolls = Roll.objects.filter(date_added__range=(min_dateadded, max_dateadded))
            return render(request, 'stockpile/search/DATEADDED/search_resultsDATEADDED.html', {'rolls': rolls})

    return render(request, 'stockpile/search/DATEADDED/search_formDATEADDED.html')


def search_rollsDATEDELETED(request):
    if request.method == 'GET':
        min_datedeleted = request.GET.get('min_datedeleted')
        max_datedeleted = request.GET.get('max_datedeleted')

        if min_datedeleted is not None and max_datedeleted is not None:
            rolls = Roll.objects.filter(date_removed__range=(min_datedeleted, max_datedeleted))
            return render(request, 'stockpile/search/DATEDELETED/search_resultsDATEDELETED.html', {'rolls': rolls})

    return render(request, 'stockpile/search/DATEDELETED/search_formDATEDELETED.html')


# ================================== СТАТИСТИКА ==================================
def stats(request):
    return render(request, 'stockpile/statistic/stats.html')


def total_rolls(request):
    total_rolls = Roll.objects.count()
    context = {
        'rolls': total_rolls,
    }
    return render(request, 'stockpile/statistic/ADDED/staticADDED.html', context)


def total_rolls_DELETED(request):
    total_rolls = Roll.objects.filter(date_removed__isnull=False).count()
    context = {
        'rolls': total_rolls,
    }
    return render(request, 'stockpile/statistic/DELETED/staticDELETED.html', context)


def average_of_length_and_weight(request):
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if start_date is not None and end_date is not None:
            average_length = Roll.objects.filter(date_added__range=(start_date, end_date)).aggregate(Avg('length'))
            average_weight = Roll.objects.filter(date_added__range=(start_date, end_date)).aggregate(Avg('weight'))

            return render(request, 'stockpile/statistic/AVERAGE/staticAVERAGE.html', {'average_len': average_length,
                                                                                      'average_weig': average_weight})

    return render(request, 'stockpile/statistic/AVERAGE/staticAVERAGEform.html')


def maximum_and_minimum(request):
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if start_date is not None and end_date is not None:
            max_length = Roll.objects.filter(date_added__range=(start_date, end_date)).aggregate(Max('length'))
            max_weight = Roll.objects.filter(date_added__range=(start_date, end_date)).aggregate(Max('weight'))

            min_length = Roll.objects.filter(date_added__range=(start_date, end_date)).aggregate(Min('length'))
            min_weight = Roll.objects.filter(date_added__range=(start_date, end_date)).aggregate(Min('weight'))

            return render(request, 'stockpile/statistic/MAXMIN/staticMAXMIN.html', {'max_len': max_length,
                                                                                    'max_weig': max_weight,
                                                                                    'min_len': min_length,
                                                                                    'min_weig': min_weight})

    return render(request, 'stockpile/statistic/MAXMIN/staticMAXMINform.html')


def sum_all_rolls(request):
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if start_date is not None and end_date is not None:
            summa = Roll.objects.filter(date_added__range=(start_date, end_date)).aggregate(Sum('weight'))

            return render(request, 'stockpile/statistic/SUM/staticSUM.html', {'sum': summa})

    return render(request, 'stockpile/statistic/SUM/staticSUMform.html')


def interval_max_min(request):
    result = Roll.objects.aggregate(
        max_duration=Max(F('date_removed') - F('date_added')),
        min_duration=Min(F('date_removed') - F('date_added'))
    )

    max_duration = result['max_duration']
    min_duration = result['min_duration']

    return render(request, 'stockpile/statistic/INTERVAL/staticINTERVAL.html', {'max_d': max_duration,
                                                                              'min_d': min_duration})

def search_main_page(request):
    return render(request, 'stockpile/search/search_main.html')
