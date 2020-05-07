NAME_SWITCH = {
    "ral": "RAL",
    "ral design": "RALD",
    "ral classic": "RALC",
    "ral effect": "RALE",
    "nsc": "NCS",
    "pantone": "PNT",
    "Глянцевая 80-100%": "80/100%",
    "Полулянцевая 55-80%": "55/80%", 
    "Полуматовая 30-55%": "30/55%",
    "Матовая 15-30%": "15/30%",
    "Суперматовая 1-15%": "1-15%", 
    "Шагрень": "шгр",
    "Гладкая": "гл",
    "Антик": "ант",
    "Муар": "мр",
    "Молотковая": "мтк",
    "Шелк": "шлк",
    "Не определено": "н/о",
    }
def name_switch(name):
    if name in NAME_SWITCH:
        return NAME_SWITCH[name]
    return name

if __name__ == "__main__":
    print(name_switch('RAL'))