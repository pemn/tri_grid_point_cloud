# tri_grid_point_cloud
Generic script to create grids and surfaces from dense point clouds (ie.: filter points).  
The idea is to reduce a large number of points by creating cells/voxels which will have the value of the median of all points inside.  
This not only allows for a much smaller data, but also smoothes outliers that otherwise would create very visible noise in the surface.  
This script does not require any proprietary software to run, but some inputs/outputs require Maptek Vulcan.  

## input
Accepts multiple input formats:  
 - LAS (a drone lidar proprietary format, requires Vulcan)
 - CSV
 - Microsoft Excel XLSX
 - ASC (Asciit point cloud)

## output
The resulta can be saved in multiple formats:  
 - CSV
 - 00g (proprietary grid, requires Vulcan)
 - 00t (proprietary triangulation, requires Vulcan)

## screenshots
![screenshot1](./assets/screenshot1.png?raw=true)  
![screenshot2](./assets/screenshot2.png?raw=true)  
![screenshot3](./assets/screenshot3.png?raw=true)  
## License
Apache 2.0
