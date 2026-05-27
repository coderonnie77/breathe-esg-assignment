UNIT_CONVERSIONS = {
    'gallon_to_liter': 3.78541,
    'mwh_to_kwh': 1000,
    'mile_to_km': 1.60934,
}


def normalize_unit(quantity, unit):

    unit = unit.lower()

    if unit == 'gallon':
        return quantity * UNIT_CONVERSIONS['gallon_to_liter'], 'liter'

    if unit == 'mwh':
        return quantity * UNIT_CONVERSIONS['mwh_to_kwh'], 'kwh'

    if unit == 'mile':
        return quantity * UNIT_CONVERSIONS['mile_to_km'], 'km'

    return quantity, unit