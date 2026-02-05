def explain_clause(clause, risk):
    text = clause.lower()

    if "terminate" in text or "termination" in text:
        return "This clause explains how the contract can be ended. If the conditions are strict or one-sided, it may be risky for the business."

    if "penalty" in text or "fine" in text:
        return "This clause includes penalties. The business may have to pay money if conditions are not met."

    if "indemnify" in text or "indemnity" in text:
        return "This clause transfers legal or financial responsibility to one party, which can be risky."

    if "non-compete" in text:
        return "This clause restricts the business from engaging in similar work and may limit future opportunities."

    if risk == "HIGH":
        return "This is a high-risk clause and should be reviewed carefully before signing."

    elif risk == "MEDIUM":
        return "This clause has moderate risk and should be understood clearly."

    else:
        return "This clause is standard and generally safe for small businesses."
