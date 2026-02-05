def detect_risk(clause):
    clause_lower = clause.lower()

    if "penalty" in clause_lower or "fine" in clause_lower:
        return "High", "Penalty clause detected"

    if "terminate" in clause_lower and "only" in clause_lower:
        return "High", "Unilateral termination"

    if "non compete" in clause_lower or "non-compete" in clause_lower:
        return "High", "Non-compete clause"

    if "indemnify" in clause_lower:
        return "Medium", "Indemnity obligation"

    return "Low", "No major risk detected"
