import random

def GISimple(impSpd=(1,9), golemSpd=(3,5), headStart=5, exitPosition=50):
    imp_min = int(impSpd[0])
    imp_max = int(impSpd[1])
    gol_min = int(golemSpd[0])
    gol_max = int(golemSpd[1])
    golem_step = 0
    imp_step = headStart
    while True:
        golem_step = golem_step + random.randint(gol_min, gol_max)
        imp_step = imp_step + random.randint(imp_min, imp_max)
        # the imp escapes
        if golem_step >= imp_step:
            return True
            break
        # the golem catches the imp
        elif imp_step >= exitPosition:
            return False
            break
        # the chase continues
        else:
            continue