def split_clauses(text):
    lines = text.split("\n")
    clauses = []
    for line in lines:
        if len(line.strip()) > 30:
            clauses.append(line.strip())
    return clauses
