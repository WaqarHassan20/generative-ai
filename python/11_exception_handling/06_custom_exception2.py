class outOfIngredientsError(Exception):
    pass


def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise outOfIngredientsError("Cannot make chai: Missing ingredients!")
    print("Chai is ready!")
    
    
make_chai(1, 0)