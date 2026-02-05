def classify_contract(text):
    text = text.lower()

    scores = {
        "Employment Contract": 0,
        "Vendor Agreement": 0,
        "Lease Agreement": 0,
        "Partnership Deed": 0,
        "Service Agreement": 0
    }

    employment_keywords = [
        "employee", "employer", "salary", "wages",
        "employment", "notice period", "termination"
    ]

    vendor_keywords = [
        "vendor", "supplier", "supply",
        "purchase order", "delivery", "invoice"
    ]

    lease_keywords = [
        "lease", "rent", "lessee", "lessor",
        "premises", "monthly rent"
    ]

    partnership_keywords = [
        "partner", "profit sharing",
        "capital contribution", "partnership deed"
    ]

    service_keywords = [
        "service", "consultant", "fees",
        "scope of work", "service provider"
    ]

    for word in employment_keywords:
        if word in text:
            scores["Employment Contract"] += 1

    for word in vendor_keywords:
        if word in text:
            scores["Vendor Agreement"] += 1

    for word in lease_keywords:
        if word in text:
            scores["Lease Agreement"] += 1

    for word in partnership_keywords:
        if word in text:
            scores["Partnership Deed"] += 1

    for word in service_keywords:
        if word in text:
            scores["Service Agreement"] += 1

    return max(scores, key=scores.get)
