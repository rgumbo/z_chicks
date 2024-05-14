from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import Qualification,ContractType, Country,Region,Town,District,Grade, Ward,Village,Grade, \
        Member,Employee,Holding,HoldingInstance,Activity,Note,Resource,OutPut,CustOrders, \
        PackType,Currency, StoreName, StockLoc, StockType, StockItem, Customer, StoreOrder, OrderItem,\
        PostCategory, PostOrigin, BlogPost

#Start Membership Admin Config

# Define the Qualification admin class
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('ql_code', 'ql_desc')

# Register the Qualification admin class with the associated model
admin.site.register(Qualification, QualificationAdmin)

# Define the Country admin class
class CountryAdmin(admin.ModelAdmin):
    list_display = ('co_code','co_name')

# Register the Country admin class with the associated model
admin.site.register(Country, CountryAdmin)

# Define the Region admin class
class RegionAdmin(admin.ModelAdmin):
    list_display = ('rg_code','rg_name','rg_co_code')

# Register the Region admin class with the associated model
admin.site.register(Region, RegionAdmin)

# Define the Town admin class
class TownAdmin(admin.ModelAdmin):
    list_display = ('to_code','to_name','to_rg_code')

# Register the Town admin class with the associated model
admin.site.register(Town, TownAdmin)

# Define the District admin class
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('dt_code','dt_to_code','dt_co_code','dt_rg_code','dt_name')

# Register the District admin class with the associated model
admin.site.register(District, DistrictAdmin)

# Define the Ward admin class
class WardAdmin(admin.ModelAdmin):
    list_display = ('wd_code','wd_dt_code','wd_to_code','wd_rg_code','wd_name','wd_chief','wd_mobile','wd_email')

# Register the Ward admin class with the associated model
admin.site.register(Ward, WardAdmin)

# Define the Village admin class
class VillageAdmin(admin.ModelAdmin):
    list_display = ('vg_code','vg_wd_code','vg_dt_code','vg_to_code','vg_rg_code','vg_name','vg_mobile','vg_email')

# Register the Village admin class with the associated model
admin.site.register(Village, VillageAdmin)


# Define the grade admin class
class GradeAdmin(admin.ModelAdmin):
    list_display = ('gd_code','gd_name','gd_min_sal','gd_max_sal')

# Register the grade admin class with the associated model
admin.site.register(Grade, GradeAdmin)

# Define the ContractType admin class
class ContractTypeAdmin(admin.ModelAdmin):
    list_display = ('ct_code','ct_desc')

# Register the ContractType admin class with the associated model
admin.site.register(ContractType, ContractTypeAdmin)

# Define the Member admin class
class MemberAdmin(admin.ModelAdmin):
    list_display = ('mm_num','mm_code','mm_trade_name','mm_name','mm_comm_date','mm_phone',
		'mm_mobile','mm_email','mm_wsite','mm_contact','mm_phone1','mm_paddress1',
		'mm_paddress2','mm_reg_date','mm_vg_code','mm_wd_code','mm_to_code','mm_dt_code','mm_rg_code','mm_co_code')

# Register the Member admin class with the associated model
admin.site.register(Member, MemberAdmin)

# Define the Employee admin class
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('ee_num','ee_mm_num','ee_fname','ee_onames','ee_initials','ee_sname','ee_nid',
		'ee_pp_num','ee_dl_num','ee_ss_num','ee_dob','ee_date_joined','ee_gender',
		'ee_salute','ee_gd_code','ee_ql_code','ee_ct_code','ee_status')

# Register the Employee admin class with the associated model
admin.site.register(Employee, EmployeeAdmin)

#Registration of farming Models
# Define the Holding admin class
class HoldingAdmin(admin.ModelAdmin):
    list_display = ('hd_num','hd_code','hd_trans_date','hd_name','hd_mm_num','hd_vg_code','hd_wd_code',
                    'hd_dt_code','hd_rg_code','hd_type','hd_desc','hd_status')

# Register the Holding admin class with the associated model
admin.site.register(Holding, HoldingAdmin)

# Define the HoldingInstance admin class
class HoldingInstanceAdmin(admin.ModelAdmin):
    list_display = ('hi_num','hi_code','hi_days','hi_trans_date','hi_hd_num','hi_use_type','hi_desc','hi_size',
                    'hi_start_date','hi_end_date','hi_pprice','hi_aprice','hi_psize', 'hi_asize','hi_tqty',
                    'hi_aqty','hi_status')

# Register the HoldingInstance admin class with the associated model
admin.site.register(HoldingInstance, HoldingInstanceAdmin)

# Define the Activity admin class
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('ac_num','ac_hi_num','ac_type','ac_desc','ac_pstart_date','ac_pend_date','ac_astart_date','ac_aend_date','ac_status','ac_remark')

# Register the Activity admin class with the associated model
admin.site.register(Activity, ActivityAdmin)

# Define the Note admin class
class NoteAdmin(admin.ModelAdmin):
    list_display = ('nt_num','nt_ac_num','nt_comment','nt_remark','nt_trans_date','nt_type','nt_status')

# Register the Note admin class with the associated model
admin.site.register(Note, NoteAdmin)

# Define the Resource admin class
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('rs_num','rs_ac_num','rs_unit','rs_desc','rs_required','rs_provided','rs_date_provided','rs_req_date','rs_approved','rs_status')

# Register the Resource admin class with the associated model
admin.site.register(Resource, ResourceAdmin)

# Define the OutPut admin class
class OutPutAdmin(admin.ModelAdmin):
    list_display = ('op_num','op_hi_num','op_qty','op_unit','op_grade','op_description','op_trans_date','op_status_date','ot_status')

# Register the OutPut admin class with the associated model
admin.site.register(OutPut, OutPutAdmin)

# Define the CustOrders admin class
class CustOrdersAdmin(admin.ModelAdmin):
    list_display = ('od_num','od_hi_num','od_Custname','od_phone','od_item','od_qty','od_unit_p',
		'od_unit','od_grade','od_notes','od_trans_date','od_status_date','ot_status','ot_paid')

# Register the CustOrders admin class with the associated model
admin.site.register(CustOrders, CustOrdersAdmin)

#Stores Admin starts here

# Define the PackType admin class
class PackTypeAdmin(admin.ModelAdmin):
    list_display = ('pt_code','pt_name','pt_desc','pt_status')

# Register the PackType admin class with the associated model
admin.site.register(PackType, PackTypeAdmin)

# Define the Currency admin class
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('cu_num','cu_code','cu_name','cu_base','cu_rate','cu_valid_from','cu_status')

# Register the Currency admin class with the associated model
admin.site.register(Currency, CurrencyAdmin)

# Define the StoreName admin class
class StoreNameAdmin(admin.ModelAdmin):
    list_display = ('sn_code','sn_name','sn_remark','sn_resp','sn_to_code','sn_rg_code','sn_phone',
'sn_email','sn_paddress','sn_status')

# Register the StoreName admin class with the associated model
admin.site.register(StoreName, StoreNameAdmin)

# Define the StockLoc admin class
class StockLocAdmin(admin.ModelAdmin):
    list_display = ('sl_code','sl_name','sl_sn_code','sl_desc','sl_resp','sl_phone','sl_status')

# Register the StockLoc admin class with the associated model
admin.site.register(StockLoc, StockLocAdmin)

# Define the StockType admin class
class StockTypeAdmin(admin.ModelAdmin):
    list_display = ('st_code','st_name','st_sl_code','st_desc','st_status','st_sn_code')

# Register the StockType admin class with the associated model
admin.site.register(StockType, StockTypeAdmin)

# Define the StockItem admin class
class StockItemAdmin(admin.ModelAdmin):
    list_display = ('si_code','si_name','si_st_code','si_pt_code','si_desc','si_qty','si_reord_qty',
		'si_std_cost','si_avg_cost','si_price_b','si_price_1','si_price_2','si_cu_id_b','si_cu_id_1',
		'si_cu_id_2','si_tax','si_disc','si_status','si_sn_code')

# Register the StockItem admin class with the associated model
admin.site.register(StockItem, StockItemAdmin)

# Define the Customer admin class
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cs_num','cs_code','cs_sn_code','cs_fname','cs_sname','cs_type','cs_mobile','cs_email','cs_contact',
		'cs_paddress','cs_reg_date','cs_to_code','cs_status')

# Register the Customer admin class with the associated model
admin.site.register(Customer, CustomerAdmin)

# Define the StoreOrder admin class
class StoreOrderAdmin(admin.ModelAdmin):
    list_display = ('so_num','so_code','so_type','so_p_s','so_mobile','so_email','so_contact',
						'so_paddress','so_ord_date','so_del_date','so_to_code','so_status','so_received',
						'so_rec_date','so_invoiced','so_inv_date','so_sn_code','so_trans_amnt','so_base_amnt',
                      'so_tax_amnt','so_disc_amnt','so_tot_amnt')

# Register the StoreOrder admin class with the associated model
admin.site.register(StoreOrder, StoreOrderAdmin)

# Define the OrderItem admin class
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('oi_num','oi_so_num','oi_si_code','oi_so_p_s','oi_pt_code','oi_cu_id','oi_ord_qty',
                      'oi_rec_qty','oi_uprice','oi_tax','oi_disc','oi_ucost','oi_trans_amnt','oi_base_amnt',
                        'oi_tax_amnt','oi_disc_amnt','oi_tot_amnt','oi_rate','oi_status') #'oi_so_p_s',

# Register the OrderItem admin class with the associated model
admin.site.register(OrderItem, OrderItemAdmin)

# Define the PostCategory admin class
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('ct_code','ct_desc','ct_seo_title','ct_seo_desc','slug')

# Register the admin class with the PostCategory model
admin.site.register(PostCategory, PostCategoryAdmin )

# Define the PostOrigin admin class
class PostOriginAdmin(admin.ModelAdmin):
    list_display = ('po_num','po_name','po_position')

# Register the admin class with the PostOrigin model
admin.site.register(PostOrigin, PostOriginAdmin)

# Define the BlogPost admin class
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('bp_heading', 'slug', 'bp_status','bp_date')
    list_filter = ("bp_status",)
    search_fields = ['bp_heading', 'bp_body']
    prepopulated_fields = {'slug': ('bp_heading',)}

# Register the admin class with the BlogPost model
admin.site.register(BlogPost, BlogPostAdmin)

# Define the PostContribution admin class
class PostContributionAdmin(admin.ModelAdmin):
    list_display = ('pc_contributor', 'pc_contribution', 'pc_bp_num', 'ad_date_c', 'pc_active')
    list_filter = ('pc_active', 'ad_date_c')
    search_fields = ('pc_contributor', 'pc_email', 'pc_contribution')
    actions = ['approve_contributions']

    def approve_contributions(self, request, queryset):
        queryset.update(pc_active=True)
