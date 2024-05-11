from django import forms
from django.forms import ModelForm

from .models import Qualification,ContractType, Country,Region,Town,District,Grade, Ward,Village,Grade,\
        Member,Employee, Holding,HoldingInstance,Activity,Note,Resource,OutPut,CustOrders, \
        PackType,Currency, StoreName, StockLoc, StockType, StockItem, Customer, StoreOrder, OrderItem

from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
from django import forms

#Form for running the orders graphs

class OrdRunForm(forms.Form):
    ord_choices = (("S","Sales Orders"),("P","Purchase Orders"))
    go = forms.ChoiceField(choices=ord_choices)

# Create the Country form class
class CountryForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Country
        # specify fields to be used
        fields = ['co_code','co_name']

# Create the Region form class
class RegionForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Region
        # specify fields to be used
        fields = ['rg_code','rg_name']

class RegionForm_e(forms.ModelForm):
    # meta class
    class Meta:
        model = Region
        # specify fields to be used
        fields = ['rg_code','rg_name','rg_co_code']

# Create the Town form class
class TownForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Town
        # specify fields to be used
        fields = ['to_code','to_name']

class TownForm_e(forms.ModelForm):
    # meta class
    class Meta:
        model = Town
        # specify fields to be used
        fields = ['to_code','to_name','to_rg_code']

# Create the District form class
class DistrictForm(forms.ModelForm):
    # meta class
    class Meta:
        model = District
        # specify fields to be used
        fields = ['dt_code','dt_name']

class DistrictForm_e(forms.ModelForm):
    # meta class
    class Meta:
        model = District
        # specify fields to be used
        fields = ['dt_code','dt_name','dt_to_code','dt_rg_code','dt_co_code']

# Create the Ward form class
class WardForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Ward
        # specify fields to be used
        fields = ['wd_code','wd_name','wd_chief','wd_mobile','wd_email']

class WardForm_e(forms.ModelForm):
    # meta class
    class Meta:
        model = Ward
        # specify fields to be used
        fields = ['wd_code','wd_name','wd_chief','wd_mobile','wd_email','wd_dt_code','wd_rg_code','wd_to_code']

# Create the Village form class
class VillageForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Village
        # specify fields to be used
        fields = ['vg_code','vg_name','vg_mobile','vg_email']

class VillageForm_e(forms.ModelForm):
    # meta class
    class Meta:
        model = Village
        # specify fields to be used
        fields = ['vg_code','vg_name','vg_mobile','vg_email','vg_wd_code','vg_rg_code','vg_to_code','vg_dt_code']

# Create the ContractType form class
class ContractTypeForm(forms.ModelForm):
    # meta class
    class Meta:
        model = ContractType
        # specify fields to be used
        fields = ['ct_code','ct_desc']

# Create the Gradeform class
class GradeForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Grade
        # specify fields to be used
        fields = ['gd_code','gd_name','gd_min_sal','gd_max_sal']

# Create the Qualification form class
class QualificationForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Qualification
        # specify fields to be used
        fields = ['ql_code', 'ql_desc']

# Create the Member form class
class MemberForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Member
        # specify fields to be used
        fields = ['mm_num','mm_code','mm_trade_name','mm_name','mm_comm_date','mm_phone',
        'mm_mobile','mm_email','mm_wsite','mm_contact','mm_phone1','mm_paddress1',
        'mm_paddress2','mm_reg_date','mm_vg_code','mm_wd_code','mm_to_code','mm_dt_code','mm_rg_code','mm_co_code']
        widgets = {
            'mm_reg_date': widgets.DateInput(attrs={'type': 'date'}),
            'mm_comm_date': widgets.DateInput(attrs={'type': 'date'}),
         }

# Create the Employee form class
class EmployeeForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Employee
        # specify fields to be used
        fields = ['ee_num','ee_mm_num','ee_fname','ee_onames','ee_initials','ee_sname','ee_nid',
        'ee_pp_num','ee_dl_num','ee_ss_num','ee_dob','ee_date_joined','ee_gender',
        'ee_salute','ee_gd_code','ee_ql_code','ee_ct_code','ee_status']
        widgets = {
            'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
            'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         }

class EmployeeForm_e(forms.ModelForm):
    # meta class
    class Meta:
        model = Employee
        # specify fields to be used
        fields = ['ee_num','ee_mm_num','ee_fname','ee_onames','ee_initials','ee_sname','ee_nid',
        'ee_pp_num','ee_dl_num','ee_ss_num','ee_dob','ee_date_joined','ee_gender',
        'ee_salute','ee_gd_code','ee_ql_code','ee_ct_code','ee_status']
        widgets = {
            'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
            'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
                  }

class HoldingForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Holding
        # specify fields to be used
        fields =['hd_num', 'hd_code', 'hd_code', 'hd_size', 'hd_trans_date', 'hd_name', 'hd_mm_num', 'hd_vg_code',
        'hd_wd_code', 'hd_dt_code','hd_to_code',  'hd_rg_code', 'hd_type', 'hd_desc', 'hd_status']
        widgets = {
            'hd_trans_date': widgets.DateInput(attrs={'type': 'date'}),
         }

# Create the HoldingInstance form class
class HoldingInstanceForm(forms.ModelForm):
        # meta class
        class Meta:
            model = HoldingInstance
            # specify fields to be used
            fields = ['hi_num','hi_code','hi_days','hi_start_date','hi_end_date','hi_use_type',
                      'hi_desc','hi_size','hi_pprice', 'hi_aprice','hi_psize','hi_asize',
                      'hi_tqty','hi_aqty','hi_status']
            widgets = {
                'hi_start_date': widgets.DateInput(attrs={'type': 'date'}),
                'hi_end_date': widgets.DateInput(attrs={'type': 'date'}),
             }

# Create the Activity form class
class ActivityForm(forms.ModelForm):
        # meta class
        class Meta:
            model = Activity
            # specify fields to be used
            fields = ['ac_num','ac_type','ac_day','ac_date','ac_o_qty','ac_c_qty','ac_t_wqt',
                      'ac_a_wqt','ac_morlity','ac_e_cost','ac_desc','ac_pstart_date',
                        'ac_pend_date','ac_astart_date','ac_aend_date','ac_status','ac_remark']
            widgets = {
                'ac_date': widgets.DateInput(attrs={'type': 'date'}),
                'ac_pstart_date': widgets.DateInput(attrs={'type': 'date'}),
                'ac_pend_date': widgets.DateInput(attrs={'type': 'date'}),
                'ac_astart_date': widgets.DateInput(attrs={'type': 'date'}),
                'ac_aend_date': widgets.DateInput(attrs={'type': 'date'}),
             }

# Create the Note form class
class NoteForm(forms.ModelForm):
        # meta class
        class Meta:
            model = Note
            # specify fields to be used
            fields = ['nt_num', 'nt_comment', 'nt_remark', 'nt_trans_date', 'nt_type', 'nt_status']
            widgets = {
                'nt_trans_date': widgets.DateInput(attrs={'type': 'date'}),
             }

# Create the Resource form class
class ResourceForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Resource
        # specify fields to be used
        fields = ['rs_num', 'rs_unit', 'rs_desc', 'rs_required', 'rs_provided', 'rs_date_provided',
                  'rs_req_date', 'rs_approved', 'rs_status']
        widgets = {
            'rs_date_provided': widgets.DateInput(attrs={'type': 'date'}),
            'rs_req_date': widgets.DateInput(attrs={'type': 'date'}),
        }

# Create the OutPut form class
class OutPutForm(forms.ModelForm):
        # meta class
        class Meta:
            model = OutPut
            # specify fields to be used
            fields = ['op_num','op_qty','op_unit','op_grade','op_description','op_trans_date',
                      'op_status_date','ot_status']
            widgets = {
                'op_trans_date': widgets.DateInput(attrs={'type': 'date'}),
                'op_status_date': widgets.DateInput(attrs={'type': 'date'}),
             }

# Create the CustOrders form class
class CustOrdersForm(forms.ModelForm):
        # meta class
        class Meta:
            model = CustOrders
            # specify fields to be used
            fields = ['od_num','od_hi_num','od_Custname','od_phone','od_item','od_qty','od_unit_p',
        'od_unit','od_grade','od_notes','od_trans_date','od_status_date','ot_status','ot_paid']
            widgets = {
                'od_trans_date': widgets.DateInput(attrs={'type': 'date'}),
                'od_status_date': widgets.DateInput(attrs={'type': 'date'}),
             }

# Stores admin forms start here

# Create the PackType form class
class PackTypeForm(forms.ModelForm):
        # meta class
        class Meta:
            model = PackType
            # specify fields to be used
            fields = ['pt_code','pt_name','pt_desc','pt_status']
            #widgets = {
                #'od_trans_date': widgets.DateInput(attrs={'type': 'date'}),
                #'od_status_date': widgets.DateInput(attrs={'type': 'date'}),
             #}

# Create the Currency form class
class CurrencyForm(forms.ModelForm):
        # meta class
        class Meta:
            model = Currency
            # specify fields to be used
            fields = ['cu_num','cu_code','cu_name','cu_base','cu_rate','cu_valid_from','cu_status']
            widgets = {
                'cu_valid_from': widgets.DateInput(attrs={'type': 'date'}),
                #'od_status_date': widgets.DateInput(attrs={'type': 'date'}),
             }

# Create the StoreName form class
class StoreNameForm(forms.ModelForm):
        # meta class
        class Meta:
            model = StoreName
            # specify fields to be used
            fields = ['sn_code','sn_name','sn_remark','sn_resp','sn_to_code','sn_rg_code','sn_phone',
            'sn_email','sn_paddress','sn_status']
           # widgets = {
               # 'od_trans_date': widgets.DateInput(attrs={'type': 'date'}),
                #'od_status_date': widgets.DateInput(attrs={'type': 'date'}),
             #}

# Create the StockLoc form class
class StockLocForm(forms.ModelForm):
        # meta class
        class Meta:
            model = StockLoc
            # specify fields to be used
            fields = ['sl_code','sl_name','sl_desc','sl_resp','sl_phone','sl_status']
            #widgets = {
                #'od_trans_date': widgets.DateInput(attrs={'type': 'date'}),
                #'od_status_date': widgets.DateInput(attrs={'type': 'date'}),
            # }

# Create the StockType form class
class StockTypeForm(forms.ModelForm):
        # meta class
        class Meta:
            model = StockType
            # specify fields to be used
            fields = ['st_code','st_name','st_desc','st_status','st_sn_code']
            widgets = {
            'st_sn_code': forms.HiddenInput(),
                #'od_status_date': widgets.DateInput(attrs={'type': 'date'}),
             }

# Create the StockItem form class
class StockItemForm(forms.ModelForm):
        # meta class
        class Meta:
            model = StockItem
            # specify fields to be used
            fields = ['si_code','si_name','si_pt_code','si_desc','si_qty','si_reord_qty',
        'si_std_cost','si_avg_cost','si_price_b','si_price_1','si_price_2','si_cu_id_b','si_cu_id_1',
        'si_cu_id_2','si_status','si_sn_code','si_tax','si_disc']
            widgets = {
                        'si_sn_code': forms.HiddenInput(),
                #'od_status_date': widgets.DateInput(attrs={'type': 'date'}),
             }

# Create the Customer form class
class CustomerForm(forms.ModelForm):
        # meta class
        class Meta:
            model = Customer
            # specify fields to be used
            fields = ['cs_num','cs_code','cs_fname','cs_sname','cs_type','cs_mobile','cs_email','cs_contact',
        'cs_paddress','cs_reg_date','cs_to_code','cs_status']
            widgets = {
                'cs_reg_date': widgets.DateInput(attrs={'type': 'date'}),
              #  'od_status_date': widgets.DateInput(attrs={'type': 'date'}),
             }

# Create the StoreOrder form class
class StoreOrderForm(forms.ModelForm):
        # meta class
        class Meta:
            model = StoreOrder
            # specify fields to be used
            fields = ['so_num','so_code','so_type','so_p_s','so_mobile','so_email','so_contact',
                        'so_paddress','so_ord_date','so_del_date','so_to_code','so_status','so_received',
                        'so_rec_date','so_invoiced','so_inv_date','so_sn_code','so_trans_amnt','so_base_amnt',
                      'so_tax_amnt','so_disc_amnt','so_tot_amnt']
            widgets = {
                'so_ord_date': widgets.DateInput(attrs={'type': 'date'}),
                'so_del_date': widgets.DateInput(attrs={'type': 'date'}),
                'so_rec_date': widgets.DateInput(attrs={'type': 'date'}),
                'so_inv_date': widgets.DateInput(attrs={'type': 'date'}),
                'so_sn_code': forms.HiddenInput(),
             }

# Create the OrderItem form class
class OrderItemForm(forms.ModelForm):
    # meta class
    class Meta:
        model = OrderItem
        # specify fields to be used
        fields = ['oi_num', 'oi_so_num', 'oi_si_code', 'oi_pt_code',  'oi_cu_id', 'oi_ord_qty',
                  'oi_rec_qty', 'oi_uprice', 'oi_ucost', 'oi_trans_amnt', 'oi_base_amnt',
                  'oi_tax_amnt', 'oi_disc_amnt', 'oi_tot_amnt', 'oi_rate', 'oi_status', 'oi_tax', 'oi_disc','oi_so_p_s']
        widgets = {
            'oi_so_num': forms.HiddenInput(),
            'oi_base_amnt': forms.HiddenInput(),
            'oi_tax_amnt': forms.HiddenInput(),
            'oi_disc_amnt': forms.HiddenInput(),
            'oi_tot_amnt': forms.HiddenInput(),
            'oi_rate': forms.HiddenInput(),
            'oi_ucost': forms.HiddenInput(),
            'oi_trans_amnt': forms.HiddenInput(),
            'oi_uprice': forms.HiddenInput(),
            'oi_tax': forms.HiddenInput(),
            'oi_disc': forms.HiddenInput(),
            'oi_rec_qty': forms.HiddenInput(),
            'oi_so_p_s': forms.HiddenInput(),
        }

class OrderItemEditForm(forms.ModelForm):
    # meta class
    class Meta:
        model = OrderItem
        # specify fields to be used
        fields = ['oi_num','oi_so_num','oi_si_code','oi_pt_code','oi_so_p_s','oi_cu_id','oi_ord_qty',
                      'oi_rec_qty','oi_uprice','oi_ucost','oi_trans_amnt','oi_base_amnt',
                        'oi_tax_amnt','oi_disc_amnt','oi_tot_amnt','oi_rate','oi_status','oi_tax','oi_disc']
        # widgets = {
        # 'od_trans_date': widgets.DateInput(attrs={'type': 'date'}),
        # 'od_status_date': widgets.DateInput(attrs={'type': 'date'}),
        # }
