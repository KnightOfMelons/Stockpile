from django.urls import path
from . import views
from .views import RollsListView, add_roll, DELETEDRollsListView, ROLLDelete, change_delete_time, search_rolls, \
    search_rollsLENGTH, search_rollsWEIGHT, search_rollsDATEADDED, search_rollsDATEDELETED, total_rolls,\
    total_rolls_DELETED, average_of_length_and_weight, maximum_and_minimum, sum_all_rolls, interval_max_min

urlpatterns = [
    path('', RollsListView.as_view(), name='main'),
    path('deleted/', DELETEDRollsListView.as_view(), name='deleted'),
    path('delete_roll/<int:pk>', ROLLDelete.as_view(), name='delete_roll'),
    path('change_roll/<int:pk>', change_delete_time, name='change_delete_time'),

    path('search', views.search_main_page, name='searchMainPage'),
    path('search/', search_rolls, name='search_rolls'),
    path('searchlength/', search_rollsLENGTH, name='searchlength'),
    path('searchweight/', search_rollsWEIGHT, name='searchweight'),
    path('searchdataADDED/', search_rollsDATEADDED, name='searchdataADDED'),
    path('searchdataDELETED/', search_rollsDATEDELETED, name='searchdataDELETED'),

    path('stats', views.stats),
    path('statsADDED/', total_rolls, name='statsADDED'),
    path('statsDELETED/', total_rolls_DELETED, name='statsDELETED'),
    path('statsAVERAGE/', average_of_length_and_weight, name='statsAVERAGE'),
    path('statsMAXMIN/', maximum_and_minimum, name='statsMAXMIN'),
    path('statsSUM/', sum_all_rolls, name='statsSUM'),
    path('statsINTERVAL/', interval_max_min, name='statsINTERVAL'),

    path('add', add_roll, name='add'),
]
