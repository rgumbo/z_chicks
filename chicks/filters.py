from django import forms
from .models import CustOrders,StoreOrder,OrderItem,HoldingInstance
import django_filters
#from decimal import Decimal
from django.db.models import Q

class CustOrdersFilter(django_filters.FilterSet):

    class Meta:
        model = CustOrders
        fields = ['od_hi_num', 'od_Custname', 'od_trans_date','ot_paid','ot_status']

    def search_filter(self, queryset):
        return queryset.all() #filter(mr_gr_num=l_gr_num)

class OrderItemFilter(django_filters.FilterSet):

    class Meta:
        model = OrderItem
        fields = ['oi_si_code','oi_pt_code']

    def search_filter(self, queryset):
        return queryset.all() #filter(mr_gr_num=l_gr_num)

class StoreOrderFilter(django_filters.FilterSet):

    class Meta:
        model = StoreOrder
        fields = ['so_cs_num','so_sn_code','so_type','so_ord_date','so_del_date']

    def search_filter(self, queryset):
        return queryset.all() #filter(mr_gr_num=l_gr_num)
class RegHoldingFilter(django_filters.FilterSet):

    class Meta:
        model = HoldingInstance
        fields = ['hi_hd_num__hd_rg_code']

    def search_filter(self, queryset):
        return queryset.all() #filter(mr_gr_num=l_gr_num)


#class MembAdvFilter(django_filters.FilterSet):
 #   class Meta:
       # model = InterestRecord
        #fields = ['ir_period', 'ir_gm_num']

#Filter for table

# starapp/filters.py
from decimal import Decimal
from django.db.models import Q
import django_filters
from chicks.models import CustOrders

class CustOrderFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = CustOrders
        fields = ['query']

    def universal_search(self, queryset, mr_period, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return CustOrders.objects.filter(
                Q(od_unit_p=value) | Q(od_qty=value)
            )

        return CustOrders.objects.filter(
            Q(od_Custname__icontains=value) | Q(od_hi_num=value)
        )
