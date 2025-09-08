customer_keys = [
    "PersonMobilePhone",
    "PersonEmail",
    "CustomerID__c"
]

order_keys = [
    "AccountId",
    "OrderNumber",
    "CustomerContactID__c",
    "OrderNo__c",
    "CRM_Customer_Hash__c"
]

uni_keys = [
    "Id"
]

imp_keys = [
    "Id"
]

ids = set()

def data_type(obj):
    if obj["_"] == "[Account]":
        imp_keys.extend(customer_keys)
    elif obj["_"] == "[Order]":
        imp_keys.extend(customer_keys)
    else:
        return

def is_valid_customer_data(data: list):
    for obj in data:
        for key in uni_keys:
            if key not in obj:
                return False
            elif key in obj and (obj[key] is None or obj[key] == ""):
                return False
            elif key in obj and obj[key] in ids:
                return False
            else:
                ids.add(obj[key])

        for key in imp_keys:
            if key not in obj:
                return False

    return True