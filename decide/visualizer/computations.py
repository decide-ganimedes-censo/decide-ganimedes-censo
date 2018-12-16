import statistics

# Constantes ---------------- 

AGE_RANGES = {
    (0,10) : 0,
    (10,18) : 0,
    (18,30) : 0,
    (30,45) : 0,
    (45, 60) : 0,
    (60, 80) : 0,
    (80, 200) : 0
}

# Métodos ---------------- 

def age_distribution(ages):
    """ Por cuestiones de eficiencia, este método
    devuelve en su conjunto la distribución de edades y 
    la media del conjunto de datos """

    distribution = AGE_RANGES.copy()
    tam = len(ages)
    mean = 0

    for (age, number) in ages.items():
        for (min_age, max_age) in AGE_RANGES.keys():
            if age > min_age and age <= max_age:
                distribution[(min_age,max_age)] = distribution[(min_age,max_age)] + round(100 * number/tam, 2)
                mean += age
                continue
    
    mean = None if mean == 0 else round(mean/tam, 2)

    return (distribution, mean)

def mean(data):
    return  None if not data else round(statistics.mean(data), 2)

def get_sexes_participation(votantes, sexes_participation):

        for v in votantes:
            sexes_participation[v[0].sex] = sexes_participation[v[0].sex] + 1

        return sexes_participation

def get_sexes_percentages(sexes_participation, sexes_total, sexes_empty):

        sexes_empty['W'] = round((sexes_participation['W'] / sexes_total['W']) * 100, 2)
        sexes_empty['N'] = round((sexes_participation['N'] / sexes_total['N']) * 100, 2)
        sexes_empty['M'] = round((sexes_participation['M'] / sexes_total['M']) * 100, 2)

        return sexes_empty