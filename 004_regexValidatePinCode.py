def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6:
        return False
    if pin.isdigit():
        return True
    return False