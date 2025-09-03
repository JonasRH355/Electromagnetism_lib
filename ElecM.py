e = 1.6e-19 # Elementary charge
k = 8.99e9

# Q = n*e
def eletricChargeModule(n):
    """
        Q = n*e
        Q = Eletric charge
        n = Number of elements
        e = Elementary charge
    """
    return n*e

def ElectrostaticForce(q1,q2,d):
    """
        F = k* (q1*q2)/(d*d)
        F = Electrostatic force (N)
        k = Coulomb's constant (8.99e9 ....)
        q1, q2 = Eletric charges (C, coulombs)
        d = Distance between the charges (m)
    """
    return (k*q1*q2)/d**2


