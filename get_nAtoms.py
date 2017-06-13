import sys
import glob
import openbabel
import pybel

def get_max_nAtom(atomNumber):
    ''' get the overall max number of atoms
    '''
    nAtoms = []
    fin = glob.glob("*.xyz")
    
    # loop throug xyz files
    for f in fin:
        Atom = 0
        # loop through molecules
        for mol in pybel.readfile("xyz", f):
            # loop through atoms and count them
            for a in mol.atoms:
                if int(a.OBAtom.GetAtomicNum()) == atomNumber:
                    Atom +=1
            nAtoms.append(Atom)
    return str(max(nAtoms))

if __name__ == "__main__":
    # dictionary for atomTypes and atomNumbers
    dicAtoms = {1:'H', 6:'C', 7:'N', 8:'O', 9:'F', 15:'P', 16:'S', 17:'Cl', 35:'Br', 46:'Pd'}

    # loop through atom Types to count them
    for key, value in dicAtoms.iteritems():
        print value + "\t" + get_max_nAtom(key) 
