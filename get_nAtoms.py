import sys
import glob
import openbabel
import pybel

def get_max_nAtom(atomNumber):
    nAtoms = []
    fin = glob.glob("*.xyz")
    for f in fin:
        Atom = 0
        for mol in pybel.readfile("xyz", f):
            for a in mol.atoms:
                if int(a.OBAtom.GetAtomicNum()) == atomNumber:
                    Atom +=1
            nAtoms.append(Atom)
    return str(max(nAtoms))


if __name__ == "__main__":
    dicAtoms = {1:'H', 6:'C', 7:'N', 8:'O', 9:'F', 15:'P', 16:'S', 17:'Cl', 35:'Br', 46:'Pd'}

    for key, value in dicAtoms.iteritems():
        print value + "\t" + get_max_nAtom(key) 
