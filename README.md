## 📌 Description
transfer data between grids with different schemas (reblock).  
can make grid cells smaller or larger, while preserving the values.
## 📸 Screenshot
![screenshot1](https://github.com/pemn/assets/blob/main/vtk_merge_grid1.png?raw=true)
## 📝 Parameters
name|optional|description
---|---|------
source_grid|❎|grid with data which will be transfered to another grid
target_grid|❎|another grid or a number with new cell size
output|☑️|save the result to a vtk file
display||show results in a 3d voxel chart
## 📓 Notes
The result will be a grid with a different dimensions and spacing but with the source data in the same relative position.
## 📚 Examples
### reducing grid cell size
![screenshot2](https://github.com/pemn/assets/blob/main/vtk_merge_grid2.png?raw=true)
### increasing grid cell size
![screenshot3](https://github.com/pemn/assets/blob/main/vtk_merge_grid3.png?raw=true)
The above images only show the new cell sizes. But ene important point that is not illustrated is that array data in both cell and point arrays are preserved!
## 🧩 Compatibility
distribution|status
---|---
![winpython_icon](https://github.com/pemn/assets/blob/main/winpython_icon.png?raw=true)|✔
![vulcan_icon](https://github.com/pemn/assets/blob/main/vulcan_icon.png?raw=true)|❌
![anaconda_icon](https://github.com/pemn/assets/blob/main/anaconda_icon.png?raw=true)|❌
## 🙋 Support
Any question or problem contact:
 - paulo.ernesto
## 💎 License
Apache 2.0
Copyright ![vale_logo_only](https://github.com/pemn/assets/blob/main/vale_logo_only_r.svg?raw=true) Vale 2023
