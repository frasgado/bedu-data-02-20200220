
PRICING = [12, 123, 234, 90, 1289, 1289, 1289, 82, 62, 78, 89, 50]

def apply_taxes(number):
    return number * 1.16

pricing_with_taxes = list(map(apply_taxes, PRICING))
print(pricing_with_taxes) 

def convert_number_to_boolean(number):
    return number % 2 == 0
    
'''    
    if number % 2 == 0:
        return True
    else:
        return False
'''

pricing_to_boolean = list(map(convert_number_to_boolean, PRICING))
print(pricing_to_boolean)