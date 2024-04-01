#!python
# transfer data between VTK grids with different schemas (reblock)

'''
usage: $0 source_grid*vtk target_grid*vtk output*vtk display@
'''
import sys, os.path, re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import modules from a pyz (zip) file with same name as scripts
sys.path.insert(0, os.path.splitext(sys.argv[0])[0] + '.pyz')
from _gui import usage_gui, log
import pyvista as pv

from pd_vtk import vtk_shape_ijk, vtk_array_ijk, vtk_mesh_info, vtk_spacing_fit
def vtk_merge_grid(grid0, grid1):
  d0 = vtk_shape_ijk(grid0.dimensions)
  d1 = vtk_shape_ijk(grid1.dimensions)
  t0 = np.minimum(d0, d1)
  t1 = np.maximum(d0, d1)
  print('t0 =',*t0,'| t1 =',*t1)

  spacing = vtk_spacing_fit(grid1.dimensions, grid1.spacing, np.flip(t1))
  grid = pv.ImageData(dimensions=np.flip(t1), spacing=spacing, origin=grid1.origin)

  n1 = np.transpose(np.meshgrid(*[np.linspace(0, d0[_], t1[_], False, dtype=np.int_) for _ in range(len(d0))]), (2,1,3,0))

  for name in grid0.array_names:
    data = None
    s0 = None
    s1 = None
    if grid0.get_array_association(name) == pv.FieldAssociation.CELL:
      c0 = np.maximum(np.subtract(d0, 1), 1)
      c1 = np.maximum(np.subtract(t1, 1), 1)
      s0 = np.reshape(grid0.get_array(name), c0)
      s1 = np.empty(c1, dtype=s0.dtype)
      data = grid.cell_data
    else:
      s0 = np.reshape(grid0.get_array(name), d0)
      s1 = np.empty(t1, dtype=s0.dtype)
      data = grid.point_data

    it = np.nditer(s1, ['multi_index'])
    while not it.finished:
      s1[it.multi_index] = s0[tuple(n1[it.multi_index])]
      it.iternext()
    data[name] = s1.flat

  return grid

def main(source_grid, target_grid, output, display):
  grid0 = pv.read(source_grid)
  grid1 = None
  if re.fullmatch(r'[\d\.\-,;_~]+', target_grid):
    dims = None
    spacing = np.resize(np.asfarray(re.split('[,_]', target_grid)), 3)
    origin = None
    if grid0.GetDataObjectType() == 2:
      b = np.reshape(grid0.bounds, (3,2))
      dims = np.maximum(np.add(np.ceil(np.divide(b[:, 1] - b[:, 0], spacing)), 1), 1).astype(np.int_)
      origin = b[:, 0]
    else:
      dims = np.maximum(np.ceil(np.divide(np.multiply(grid0.dimensions, grid0.spacing), spacing)), 1).astype(np.int_)
      origin = grid0.origin
    grid1 = pv.ImageData(dimensions=dims, spacing=spacing, origin=origin)
  else:
    grid1 = pv.read(target_grid)

  grid = vtk_merge_grid(grid0, grid1)
  grid.set_active_scalars(grid0.active_scalars_name)

  print(vtk_mesh_info(grid))
  if grid is not None and output:
    grid.save(output)

  if int(display):
    name = grid.active_scalars_name
    if not name:
      name = None
    s0 = vtk_array_ijk(grid0, name, True)
    s1 = vtk_array_ijk(grid, name, True)

    cmap = plt.get_cmap()
    plt.subplot(121, projection='3d')
    if name is not None:
      plt.title(name)
    plt.gca().voxels(s0, facecolors=cmap(s0))

    plt.subplot(122, projection='3d')
    if name is not None:
      plt.title(name)
    plt.gca().voxels(s1, facecolors=cmap(s1))

    plt.show()

if __name__=="__main__":
  usage_gui(__doc__)
