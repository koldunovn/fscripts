import os
import glob
import sys

try:
    path = sys.argv[1]
    variable = sys.argv[2]
except:
    raise ValueError("provide path and name of the variable")

#variable = 'salt'
#path = '/work/ollie/qigao001/output/awiesm-2.1-wiso/pi_final_qg/outdata/fesom/'

print (path)
print(variable)

ll = glob.glob(f'{path}/{variable}*')

for l in ll:
    filename = os.path.basename(l)
    #dirname = os.path.dirname(l)
    var, rname, year_wrong, mon, _ = filename.split('.')
    year_right = year_wrong[:4]
    oname = f'{var}.{rname}.{year_right}.nc'
    #ofile = os.path.join(dirname, oname)
    os.system(f'ln -s {l} ./{oname}')
