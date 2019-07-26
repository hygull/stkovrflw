```python
>>> l = [
...     "Order", "OrderItem", "TransactionType", "SystematicDetail", "SystematicDetailOther",
...     "PortfolioType", "Portfolio", "Revenue", "RtaMissing", "Holdings"]
>>> 
>>> for item in l:
...     print('admin.site.register(' + item + ', ' + item + 'Admin)' )
... 
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(TransactionType, TransactionTypeAdmin)
admin.site.register(SystematicDetail, SystematicDetailAdmin)
admin.site.register(SystematicDetailOther, SystematicDetailOtherAdmin)
admin.site.register(PortfolioType, PortfolioTypeAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Revenue, RevenueAdmin)
admin.site.register(RtaMissing, RtaMissingAdmin)
admin.site.register(Holdings, HoldingsAdmin)
```



```python
>>> for item in l:
...     code = "class " + item + "Admin(admin.ClientBaseAdmin):\n"
...     code += "    list_display = []\n"
...     code += "    list_filter = []\n"
...     code += "    search_fields = []\n"
...     print(code , '\n')
... 
class OrderAdmin(admin.ClientBaseAdmin):
    list_display = []
    list_filter = []
    search_fields = []
 

class OrderItemAdmin(admin.ClientBaseAdmin):
    list_display = []
    list_filter = []
    search_fields = []
 

class TransactionTypeAdmin(admin.ClientBaseAdmin):
    list_display = []
    list_filter = []
    search_fields = []
 

class SystematicDetailAdmin(admin.ClientBaseAdmin):
    list_display = []
    list_filter = []
    search_fields = []
 

class SystematicDetailOtherAdmin(admin.ClientBaseAdmin):
    list_display = []
    list_filter = []
    search_fields = []
 

class PortfolioTypeAdmin(admin.ClientBaseAdmin):
    list_display = []
    list_filter = []
    search_fields = []
 

class PortfolioAdmin(admin.ClientBaseAdmin):
    list_display = []
    list_filter = []
    search_fields = []
 

class RevenueAdmin(admin.ClientBaseAdmin):
    list_display = []
    list_filter = []
    search_fields = []
 

class RtaMissingAdmin(admin.ClientBaseAdmin):
    list_display = []
    list_filter = []
    search_fields = []
 

class HoldingsAdmin(admin.ClientBaseAdmin):
    list_display = []
    list_filter = []
    search_fields = []
 

>>> 
```