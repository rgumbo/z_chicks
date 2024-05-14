from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView, name='homepage'),
    path('members', views.EmpHomeView, name='members'),
    path('geoparams', views.GeoHomeView, name='geoparams'),
    path('genparams', views.ParaHomeView, name='genparams'),
    path('trans', views.TransHomeView, name='trans'),
    path('farmproj', views.FarmProjHomeView, name='farmproj'),

#urls for Store app

    path('mystore', views.MyStoreView, name='mystore'),
    path('sparams', views.StoreParamView, name='sparams'),
    path('strans', views.StoreTransView, name='strans'),

    path('addpacktype', views.PackTypeView, name='addpacktype'),
    path('packtypedetail/str<pk>/', views.PackTypeDetailView.as_view(), name='packtypedetail'),
    path('editpacktype/<str:pk>/', views.EditPackType, name='editpacktype'),
    path('packtype/', views.PackTypeIndexView.as_view(), name='packtype'),
    path('deletepacktype/<str:pk>/', views.DeletePackType, name='deletepacktype'),

    path('addcurrency', views.CurrencyView, name='addcurrency'),
    path('currencydetail/str<pk>/', views.CurrencyDetailView.as_view(), name='currencydetail'),
    path('editcurrency/<str:pk>/', views.EditCurrency, name='editcurrency'),
    path('currency/', views.CurrencyIndexView.as_view(), name='currency'),
    path('deletecurrency/<str:pk>/', views.DeleteCurrency, name='deletecurrency'),

    path('addstorename', views.StoreNameView, name='addstorename'),
    path('storenamedetail/str<pk>/', views.StoreNameDetailView.as_view(), name='storenamedetail'),
    path('editstorename/<str:pk>/', views.EditStoreName, name='editstorename'),
    path('storename/', views.StoreNameIndexView.as_view(), name='storename'),
    path('storename1<str:pk>/', views.StoreName1IndexView.as_view(), name='storename1'),
    path('deletestorename/<str:pk>/', views.DeleteStoreName, name='deletstorename'),

    path('addstockloc/str<pk>/', views.StockLocView, name='addstockloc'),
    path('addstockloc_a/', views.StockLocView1, name='addstockloc_a'),
    path('stocklocdetail/str<pk>/', views.StockLocDetailView.as_view(), name='stocklocdetail'),
    path('editstockloc/<str:pk>/', views.EditStockLoc, name='editstockloc'),
    path('stockloc<str:pk>/', views.StockLocIndexView.as_view(), name='stockloc'),
    path('stocklocall/', views.StockLocAllIndexView.as_view(), name='stocklocall'),
    path('deletestockloc/<str:pk>/', views.DeleteStockLoc, name='deletestockloc'),

    path('addstocktype/str<pk>/', views.StockTypeView, name='addstocktype'),
    path('addstocktype_a/', views.StockTypeView1, name='addstocktype_a'),
    path('stocktypedetail/str<pk>/', views.StockTypeDetailView.as_view(), name='stocktypedetail'),
    path('editstocktype/<str:pk>/', views.EditStockType, name='editstocktype'),
    path('stocktype<str:pk>/', views.StockTypeIndexView.as_view(), name='stocktype'),
    path('deletestocktype/<str:pk>/', views.DeleteStockType, name='deletestocktype'),

    path('addstockitem/str<pk>/', views.StockItemView, name='addstockitem'),
    path('addstockitem_a/', views.StockItemView1, name='addstockitem_a'),
    path('stockitemdetail/str<pk>/', views.StockItemDetailView.as_view(), name='stockitemdetail'),
    path('editstockitem/<str:pk>/', views.EditStockItem, name='editstockitem'),
    path('stockitem<str:pk>/', views.StockItemIndexView.as_view(), name='stockitem'),
    path('deletestockitem/<str:pk>/', views.DeleteStockItem, name='deletestockitem'),

    path('addcustomer/str<pk>/', views.CustomerView, name='addcustomer'),
    path('addcustomer_a/', views.CustomerView1, name='addcustomer_a'),
    path('customerdetail/str<pk>/', views.CustomerDetailView.as_view(), name='customerdetail'),
    path('editcustomer/<str:pk>/', views.EditCustomer, name='editcustomer'),
    path('customer<str:pk>/', views.CustomerIndexView.as_view(), name='customer'),
    path('customerall<str:pk>/', views.CustomerAllIndexView.as_view(), name='customerall'),
    path('deletecustomer/<str:pk>/', views.DeleteCustomer, name='deletecustomer'),

    path('addstoreorder_p/str<pk>/', views.StoreOrderPView, name='addstoreorder_p'),
    path('addstoreorder_s/str<pk>/', views.StoreOrderSView, name='addstoreorder_s'),

    path('storeorderdetail/str<pk>/', views.StoreOrderDetailView.as_view(), name='storeorderdetail'),
    path('editstoreorder/<str:pk>/', views.EditStoreOrder, name='editstoreorder'),
    path('storeorder<str:pk>/', views.StoreOrderIndexView.as_view(), name='storeorder'),
    path('deletestoreorder/<str:pk>/', views.DeleteStoreOrder, name='deletestoreorder'),

    path('addorderitem/str<pk>/str<so_p_s>/', views.OrderItemView, name='addorderitem'),
    path('addorderitem/str<pk>/str<oi_so_p_s>/', views.OrderItemOiView, name='addorderitemoi'),
    path('addorderitem_a/', views.OrderItemView1, name='addorderitem_a'),
    path('orderitemdetail/str<pk>/', views.OrderItemDetailView.as_view(), name='orderitemdetail'),
    path('editorderitem/<str:pk>/', views.EditOrderItem, name='editorderitem'),
    path('orderitem<str:pk>/', views.OrderItemIndexView.as_view(), name='orderitem'),
    path('deleteorderitem/<str:pk>/', views.DeleteOrderItem, name='deleteorderitem'),

     # End Stores app

    path('addqualification', views.QualificationView, name='addqualification'),
    path('qualificationdetail/str<pk>/', views.QualificationDetailView.as_view(), name='qualificationdetail'),
    path('editqualification/<str:pk>/', views.EditQualification, name='editqualification'),
    path('qualification/', views.QualificationIndexView.as_view(), name='qualification'),
    path('deletequalification/<str:pk>/', views.DeleteQualification, name='deletequalification'),

    path('addcountry', views.CountryView, name='addcountry'),
    path('countrydetail/str<pk>/', views.CountryDetailView.as_view(), name='countrydetail'),
    path('editcountry/<str:pk>/', views.EditCountry, name='editcountry'),
    path('country/', views.CountryIndexView.as_view(), name='country'),
    path('deletecountry/<str:pk>/', views.DeleteCountry, name='deletecountry'),

    path('addregion/str<pk>/', views.RegionView, name='addregion'),
    path('addregion_a/', views.RegionView1, name='addregion_a'),
    path('regiondetail/str<pk>/', views.RegionDetailView.as_view(), name='regiondetail'),
    path('editregion/<str:pk>/', views.EditRegion, name='editregion'),
    path('region/<str:pk>/', views.RegionIndexView.as_view(), name='region'),
    path('deleteregion/<str:pk>/', views.DeleteRegion, name='deleteregion'),

    path('addtown/str<pk>/', views.TownView, name='addtown'),
    path('addtown_a/', views.TownView1, name='addtown_a'),
    path('towndetail/str<pk>/', views.TownDetailView.as_view(), name='towndetail'),
    path('edittown/<str:pk>/', views.EditTown, name='edittown'),
    path('town<str:pk>/', views.TownIndexView.as_view(), name='town'),
    path('deletetown/<str:pk>/', views.DeleteTown, name='deletetown'),

    path('adddistrict/str<pk>/', views.DistrictView, name='adddistrict'),
    path('adddistrict_a/', views.DistrictView1, name='adddistrict_a'),
    path('districtdetail/str<pk>/', views.DistrictDetailView.as_view(), name='districtdetail'),
    path('editdistrict/<str:pk>/', views.EditDistrict, name='editdistrict'),
    path('district/<str:pk>/', views.DistrictIndexView.as_view(), name='district'),
    path('deletedistrict/<str:pk>/', views.DeleteDistrict, name='deletedistrict'),

    path('addward/str<pk>/', views.WardView, name='addward'),
    path('addward_a/', views.WardView2, name='addward_a'),
    path('warddetail/str<pk>/', views.WardDetailView.as_view(), name='warddetail'),
    path('editward/<str:pk>/', views.EditWard, name='editward'),
    path('ward/<str:pk>/', views.WardIndexView.as_view(), name='ward'),
    path('deleteward/<str:pk>/', views.DeleteWard, name='deleteward'),

    path('addvillage/str<pk>/', views.VillageView, name='addvillage'),
    path('addvillage_a/', views.VillageView, name='addvillage_a'),
    path('villagedetail/str<pk>/', views.VillageDetailView.as_view(), name='villagedetail'),
    path('editvillage/<str:pk>/', views.EditVillage, name='editvillage'),
    path('village/<str:pk>/', views.VillageIndexView.as_view(), name='village'),
    path('deletevillage/<str:pk>/', views.DeleteVillage, name='deletevillage'),

    path('addgrade', views.GradeView, name='addgrade'),
    path('gradedetail/str<pk>/', views.GradeDetailView.as_view(), name='gradedetail'),
    path('editgrade/<str:pk>/', views.EditGrade, name='editgrade'),
    path('grade/', views.GradeIndexView.as_view(), name='grade'),
    path('deletegrade/<str:pk>/', views.DeleteGrade, name='deletegrade'),

    path('addcontracttype', views.ContractTypeView, name='addcontracttype'),
    path('contracttypedetail/str<pk>/', views.ContractTypeDetailView.as_view(), name='contracttypedetail'),
    path('editcontracttype/<str:pk>/', views.EditContractType, name='editcontracttype'),
    path('contracttype/', views.ContractTypeIndexView.as_view(), name='contracttype'),
    path('deletecontracttype/<str:pk>/', views.DeleteContractType, name='deletecontracttype'),

    path('addmember', views.MemberView, name='addmember'),
    path('memberdetail/str<pk>/', views.MemberDetailView.as_view(), name='memberdetail'),
    path('editmember/<str:pk>/', views.EditMember, name='editmember'),
    path('member/', views.MemberIndexView.as_view(), name='member'),
    path('deletemember/<str:pk>/', views.DeleteMember, name='deleteMember'),

    path('addemployee/str<pk>/', views.EmployeeView, name='addemployee'),
    path('employeedetail/str<pk>/', views.EmployeeDetailView.as_view(), name='employeedetail'),
    path('editemployee/<str:pk>/', views.EditEmployee, name='editemployee'),
    path('employee/', views.EmployeeIndexView.as_view(), name='employee'),
    path('deleteemployee/<str:pk>/', views.DeleteEmployee, name='deleteemployee'),

    path('addholding', views.HoldingView, name='addholding'),
    path('holdingdetail/str<pk>/', views.HoldingDetailView.as_view(), name='holdingdetail'),
    path('editholding/<str:pk>/', views.EditHolding, name='editholding'),
    path('holding/', views.HoldingIndexView.as_view(), name='holding'),
    path('deleteholding/<str:pk>/', views.DeleteHolding, name='deleteholding'),

    path('addholdinginstance/str<pk>/', views.HoldingInstanceView, name='addholdinginstance'),
    path('holdinginstancedetail/str<pk>/', views.HoldingInstanceDetailView.as_view(), name='holdinginstancedetail'),
    path('editholdinginstance/<str:pk>/', views.EditHoldingInstance, name='editholdinginstance'),
    path('holdinginstance/str<pk>/', views.HoldingInstanceIndexView.as_view(), name='holdinginstance'),
    path('holdinginstance_o/', views.HoldingInstanceIndexView_o.as_view(), name='holdinginstance_o'),
    path('deleteholdinginstance/<str:pk>/', views.DeleteHoldingInstance, name='deleteholdinginstance'),

    path('addactivity/str<pk>/', views.ActivityView, name='addactivity'),
    path('activitydetail/str<pk>/', views.ActivityDetailView.as_view(), name='activitydetail'),
    path('editactivity/<str:pk>/', views.EditActivity, name='editactivity'),
    path('activity/<str:pk>/', views.ActivityIndexView.as_view(), name='activity'),
    path('activity_r/<str:pk>/', views.ActivityIndexView_r.as_view(), name='activity_r'),
    path('activity_n/', views.ActivityIndexView_r.as_view(), name='activity_n'),
    path('deleteactivity/<str:pk>/', views.DeleteActivity, name='deleteactivity'),

    path('addnote/str<pk>/', views.NoteView, name='addnote'),
    path('notedetail/str<pk>/', views.NoteDetailView.as_view(), name='notedetail'),
    path('editnote/<str:pk>/', views.EditNote, name='editnote'),
    path('note/str<pk>/', views.NoteIndexView.as_view(), name='note'),
    path('deletenote/<str:pk>/', views.DeleteNote, name='deletenote'),

    path('addresource/str<pk>/', views.ResourceView, name='addresource'),
    path('resourcedetail/str<pk>/', views.ResourceDetailView.as_view(), name='resourcedetail'),
    path('editresource/<str:pk>/', views.EditResource, name='editresource'),
    path('resource/str<pk>/', views.ResourceIndexView.as_view(), name='resource'),
    path('deleteresource/<str:pk>/', views.DeleteResource, name='deleteresource'),

    path('addoutput/str<pk>/', views.OutPutView, name='addoutput'),
    path('outputdetail/str<pk>/', views.OutPutDetailView.as_view(), name='outputdetail'),
    path('editoutput/<str:pk>/', views.EditOutPut, name='editoutput'),
    path('output/', views.OutPutIndexView.as_view(), name='output'),
    path('deleteoutput/<str:pk>/', views.DeleteOutPut, name='deleteoutput'),

    path('addcustorders/', views.CustOrdersView, name='addcustorders'),
    path('custordersdetail/str<pk>/', views.CustOrdersView, name='custordersdetail'),
    path('editcustorders/<str:pk>/', views.EditCustOrders, name='editcustorders'),
    path('custorders/', views.CustOrdersIndexView.as_view(), name='custorders'),
    path('deletecustorders/<str:pk>/', views.DeleteCustOrders, name='deletecustorders'),

#Reports

    path('s_flash', views.SpotFlashView1, name='s_flash'),

    path('g_position_tab', views.MyOrdersView, name='g_position_tab'),
    path('g_position_tab1', views.OrdersHTMxTableView.as_view(), name='g_position_tab1'),
    #path('memberrecord_htmx', views.TransHTMxTable1, name='memberrecord_htmx'),

#Store Reports
    path('orderitem', views.OrderItemRepView, name='orderitem'),
    path('storeorders', views.StoreOrderSalesView, name='storeorders'),
    path('storeorderp', views.StoreOrderPurView, name='storeorderp'),
    path('storeorderf', views.StoreSalesFlash1View, name='storeorderf'),
    path('storeorderm', views.MonthlySalesFlash1View, name='storeorderm'),

#Blog URLs

    path('bloghome', views.PostList.as_view(), name='bloghome'),
    path('blogadmin', views.PostListAdmin.as_view(), name='blogadmin'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='postdetail'),
    path('post_detail/<slug>/', views.Post_Detail, name='post_detail'),
    path('post_new/', views.post_new, name='post_new'),
    #path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post_edit/<slug>/', views.post_edit, name='post_edit'),
    path('post_remove/<slug>/', views.post_remove, name='post_remove'),
    path('cont_approve/<int:pk>/', views.cont_approve, name='cont_approve'),
    path('cont_remove/<int:pk>/', views.cont_remove, name='cont_remove'),
 ]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
 ]
