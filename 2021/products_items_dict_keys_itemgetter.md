[https://stackoverflow.com/questions/68510295/multiple-key-in-dictionary/68510522?noredirect=1#comment121078200_68510522](multiple-key-in-dictionary)


```bash
In [18]: def list_prod_category(sort_by="category"): 
    ...:     for index, product in enumerate(sorted(products, key=itemgetter(sort_by))): 
    ...:         print(f"{index + 1}. {product['name']} (${product['price']})") 
    ...:                                                                                                                                                                              

In [19]: list_prod_category("price") # Sort by price                                                                                                                              
1. SAMSUNG 64GB GALAXY TAB ($372)
2. HUAWEI HW-BAH3 LTE ($372)
3. APPLE 10.2-INCH IPAD ($456)
4. NINTENDO SWITCH CONSOLE ($457)
5. SONY PLAYSTATION 5 ($560)
6. MICROSOFT XBOX CONSOLE ($653)
7. LENOVO IP 3 ($1308)
8. APPLE MACBOOK AIR ($1345)
9. ASUS S533EQ 15.6 ($1448)

In [20]: list_prod_category("name") # Sory by name (Alphabetically)                                                                                                               
1. APPLE 10.2-INCH IPAD ($456)
2. APPLE MACBOOK AIR ($1345)
3. ASUS S533EQ 15.6 ($1448)
4. HUAWEI HW-BAH3 LTE ($372)
5. LENOVO IP 3 ($1308)
6. MICROSOFT XBOX CONSOLE ($653)
7. NINTENDO SWITCH CONSOLE ($457)
8. SAMSUNG 64GB GALAXY TAB ($372)
9. SONY PLAYSTATION 5 ($560)

In [21]: list_prod_category("category") # Sort by category                                                                                                                                         
1. NINTENDO SWITCH CONSOLE ($457)
2. SONY PLAYSTATION 5 ($560)
3. MICROSOFT XBOX CONSOLE ($653)
4. APPLE MACBOOK AIR ($1345)
5. ASUS S533EQ 15.6 ($1448)
6. LENOVO IP 3 ($1308)
7. SAMSUNG 64GB GALAXY TAB ($372)
8. APPLE 10.2-INCH IPAD ($456)
9. HUAWEI HW-BAH3 LTE ($372)

In [22]:  
```