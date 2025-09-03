e = 1.6e-19 # Elementary charge
k = 8.99e9

# Q = n*e
def eletricChargeModule(n):
    """
        Q = n*e                 \n
        Q = Eletric charge      \n
        n = Number of elements  \n
        e = Elementary charge   \n
    """
    return n*e

def electrostaticForce(q1,q2,d):
    """
        F = k* (q1*q2)/(d*d)                    \n
        F = Electrostatic force (N)             \n
        k = Coulomb's constant (8.99e9 ....)    \n
        q1, q2 = Eletric charges (C, coulombs)  \n
        d = Distance between the charges (m)    \n
    """
    return (k*q1*q2)/d**2

def eletricField_PointCharge(q1,d):
    """
        
        Point charge formula: E = k* (q1)/(d*d) \n
        E = Electric field vector (N/C)         \n
        k = Coulomb's constant (8.99e9 ....)    \n
        q1 = Eletric charges (C, coulombs)      \n
        d = Distance from the charge (m)        \n
    """
    return k*q1/d**2

def eletricDipoleMoment(q,d):
    """
        p = q * d \n
        p = Electric dipole moment (C·m) \n
        q = Charge magnitude \n
        d = Distance between charges \n
    """
    return q*d



