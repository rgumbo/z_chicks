
# chicks/tables.py
import django_tables2 as tables
from chicks.models import CustOrders

class CustOrdersHTMxTable(tables.Table):
    class Meta:
        model = CustOrders
        template_name = "tables/bootstrap_htmx.html"