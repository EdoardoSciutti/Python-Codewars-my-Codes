def printer_error(s):
    errors = sum(1 for c in s if c > 'm')
    return f"{errors}/{len(s)}"