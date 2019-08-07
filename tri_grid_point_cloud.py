#!python
# create a surface/grid of a point cloud
# input_path: file in one of the supported formats. x and y MUST be the first columns
# cell_size: all points inside each cell of this size will be merged
# output_path: result will be saved on this path with the format based on extension
# v1.0 11/2017 paulo.ernesto
# Copyright 2019 Vale
# License: Apache 2.0
"""
usage: $0 input_path*asc,csv,las,xlsx cell_size=1,2,5,10,25,50 output_path*00t,00g,csv
"""

import sys, os.path
import numpy as np
import pandas as pd

# import modules from a pyz (zip) file with same name as scripts
sys.path.insert(0, os.path.splitext(sys.argv[0])[0] + '.pyz')

from _gui import usage_gui, pd_load_dataframe

from voxelspace import VoxelSpace

def pd_load_asc_grid(input_path):
  f = open(input_path)
  nrow = int(f.readline())
  ncol = None
  r = None 
  for i in range(nrow):
    row = f.readline().split(' ')
    if ncol is None:
      ncol = len(row)
      r = np.ndarray((int(nrow), ncol), dtype=np.float32)
    elif len(row) != ncol:
      continue

    r[i] = row

  return pd.DataFrame(r, columns=['x','y','z','w','v'])


# convert a vulcan surface to a vulcan solid
def tri_grid_point_cloud(input_path, cell_size, output_path):
  cell_size = float(cell_size)

  df = None
  if input_path.lower().endswith('.las'):
    las_asc=input_path + ".asc"
    os.system('las2txt.exe "%s" "%s"' % (input_path, las_asc))
    df = pd_load_asc_grid(las_asc)
    os.remove(las_asc)
  elif input_path.lower().endswith('.asc'):
    df = pd_load_asc_grid(input_path)
  else:
    df = pd_load_dataframe(input_path)

  vs = VoxelSpace(df, [cell_size, cell_size])

  vs.calculate_mean_xyz('z')
  if output_path.lower().endswith('.00t'):
    output_grid = output_path + '.00g'
    vs.save_vulcan_grid(output_grid)
    os.system('trigrid "%s" "%s"' % (output_grid, output_path))
    os.remove(output_grid)
  elif output_path.lower().endswith('.00g'):
    vs.save_vulcan_grid(output_path)
  elif output_path.lower().endswith('.csv'):
    import csv
    with open(output_path, 'w', newline='') as csvfile:
      cw = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
      cw.writerow('xyz')
      for i in range(vs.get_dx()):
        for j in range(vs.get_dy()):
          cw.writerow([i,j,vs[i,j]])

main = tri_grid_point_cloud

if __name__=="__main__":
  usage_gui(__doc__)
