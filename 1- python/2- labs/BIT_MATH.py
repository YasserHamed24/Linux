def SET_BIT(REG , NUM):
    result = REG | (1 << NUM)
    return result

def CLR_BIT(REG , NUM):
    result = REG & ~(1 << NUM)
    return result

def GET_BIT(REG , NUM):
    result = REG & (1 << NUM)
    result = result >> NUM
    return result

def TOG_BIT(REG , NUM):
    result = REG ^ (1 << NUM)
    return result
