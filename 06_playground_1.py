# Name: Encuentra la interseccion de conjuntos 
# Link: https://platzi.com/clases/7967-python-21-dias/63512-encuentre-la-interseccion-de-conjuntos/

def find_set_intersection(sets:list[set]):
    if not sets:
        return set()
    set_intersect = sets[0]
    for i in range(len(sets)):
        set_intersect = set_intersect.intersection(sets[i])
    
    return set_intersect

# Version I found beautiful
def find_set_intersection2(sets:list[set]):
    if not sets:
        return set()
    set_intersect = sets[0].intersection(*sets[1:])
    
    return set_intersect



sets = [
    {1, 2, 3, 4},
    {2, 3, 4, 5},
    {3, 4, 5, 6}
]

print(find_set_intersection2(sets))