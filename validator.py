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

def uri_type(obj):
    if obj["_"] == "[Account]":
        return "customers"
    elif obj["_"] == "[Order]":
        return "orders"
    elif obj["_"] == "[OrderItem]":
        return "order-items"
    elif obj["_"] == "[Case]":
        return "ticket?type=case"
    elif obj["_"] == "[Call_Summary__c]":
        return "ticket?type=call-summary"
    elif obj["_"] == "[Customer_Files__c]":
        return "ticket?type=file"
    elif obj["_"] == "[Task]":
        return "ticket?type=task"
    elif obj["_"] == "[WorkOrder]":
        return "ticket?type=work-order"
    elif obj["_"] == "[Invoice__c]":
        return "invoice-data"
    elif obj["_"] == "[Refund_Status__c]":
        return "refund-data"
    elif obj["_"] == "[Voucher_Detail__c]":
        return "ticket?type=egc"
    elif obj["_"] == "[Contact]":
        return "contacts"
    else:
        return None

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