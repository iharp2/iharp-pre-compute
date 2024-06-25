VARIABLE_NAME_long2short = {
    "2m_temperature": "t2m",
    "total_precipitation": "tp",
    "surface_pressure": "sp",
}

VARIABLE_NAME_short2long = {v: k for k, v in VARIABLE_NAME_long2short.items()}


def get_short_from_long(long_name):
    return VARIABLE_NAME_long2short.get(long_name, long_name)


def get_long_from_short(short_name):
    return VARIABLE_NAME_short2long.get(short_name, short_name)
