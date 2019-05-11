import re

text = """ActiveNfe, ApplicableIncome, Bank, BankBillDesk, Country, Exemption, 
            GIINExemption, GetHoldingNature, UBO, TaxStatus, TransactionType, State, SourceWealth,
            PaymentMechanism, PANExemptCategory, Occupation, Location, IDType"""

model_names = re.split(r",\s+", text)
# ['ActiveNfe', 'ApplicableIncome', 'Bank', 'BankBillDesk', 'Country', 'Exemption', 'GIINExemption', 'GetHoldingNature', 'UBO', 'TaxStatus', 'TransactionType', 'State', 'SourceWealth', 'PaymentMechanism', 'PANExemptCategory', 'Occupation', 'Location', 'IDType']

p = re.compile(r"[A-Z]+")
for model_name in model_names:
    model_name_saved = model_name
    itr = p.finditer(model_name)
    # print(model_name)
    add = 0
    for match in itr:
        # print(match.end(), match.start())
        if match.start() == 0:
            if match.end() - match.start() == 1:
                model_name = model_name[match.start() + add: match.end() + add].lower() + model_name[match.end() + add:]
            else:
                model_name = model_name[match.start() + add: match.end() + add - 1].lower() + model_name[match.end() + add - 1:]
            # print("0 - ", model_name)
        else:
            if match.end() - match.start() == 1:
                model_name = model_name[:match.start() + add] +  "_" + model_name[match.start() + add: match.end() + add].lower() + model_name[match.end() + add:]
                add += 1
            else:
                model_name = model_name[:match.start() + add] +  "_" + model_name[match.start() + add: match.end() + add - 1].lower() + model_name[match.end() +add - 1:]
                add += 1
            # print("1 - ", model_name)

    print("\"" + model_name + "\": " + model_name_saved  + "," )

"""

    "active_nfe": ActiveNfe,
    "applicable_income": ApplicableIncome,
    "bank": Bank,
    "bank_bil_lDesk": BankBillDesk,
    "country": Country,
    "exemption": Exemption,
    "giinexemption": GIINExemption,
    "get_holdin_gNature": GetHoldingNature,
    "ubo": UBO,
    "tax_status": TaxStatus,
    "transaction_type": TransactionType,
    "state": State,
    "source_wealth": SourceWealth,
    "payment_mechanism": PaymentMechanism,
    "panexempt_category": PANExemptCategory,
    "occupation": Occupation,
    "location": Location,
    "idtype": IDType,

"""