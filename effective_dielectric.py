from numpy import linspace
import matplotlib.pyplot as plt

print "A program to calculate the effective dielectric constant of crystals packed in a dielectric medium."
# Based on effective medium theory (Bruggeman 1935)

print "Ruth Lunt 2013\nDate last edited: 17/07/2013"

#dielectric constant of material A
e1 = raw_input("What is the dielectric constant of the bulk crystal?")
e1 = float(e1)

#dielectric constant of material B
e2 = raw_input("What is the dielectric constant of the medium? (Hint: H2O = 80)")
e2 = float(e2)

#dimension 
d = 3

void_fraction = 0.4764

def effective_dielectric(e1, e2, void_fraction, d):
    #volume fraction of bulk crystal
    p1 = 1 - void_fraction
    #volume fraction of medium
    p2 = void_fraction
    eps = p1*e1 + p2*e2
    #e = effective dielectric constant    
    e = (1./(2*(d-1)))*(d*eps - e1 - e2 + ((d*eps - e1 - e2)**2 + 4*(d - 1)*e1*e2)**0.5)
    return e


print "The results depending on the crystal packing, i.e. the volume fraction"

print "Packing density:\t\t" + "Effective dielectric:"
void_fraction_list = linspace(0.4764, 0.2595, 100)
effective_dielectric_list = []
packing_density_list = []
for void_fraction in void_fraction_list:
    packing_density = 1 - void_fraction
    print "{0:6.3f}\t\t\t".format(packing_density) +  "{0:6.3f}".format(effective_dielectric(e1, e2, void_fraction, d))
    packing_density_list.append(packing_density)
    effective_dielectric_list.append(effective_dielectric(e1, e2, void_fraction, d))
    

plt.plot(packing_density_list, effective_dielectric_list)
plt.axis([0.5236, 0.7405, effective_dielectric_list[-1], effective_dielectric_list[-0]])
plt.xlabel('packing density')
plt.ylabel('effective dielectric')
plt.show()
