def format_duration(seconds):
    time_units = {"year": 365*24*60*60, "day": 24*60*60, "hour": 60*60, "minute": 60, "second": 1}
    components = []

    for unit, value in time_units.items():
        quantity = seconds // value
        if quantity > 0:
            components.append(f"{quantity} {unit}{'s' if quantity > 1 else ''}")
            seconds -= quantity * value

    if not components:
        return "now"
    elif len(components) == 1:
        return components[0]
    else:
        return ", ".join(components[:-1]) + " and " + components[-1]