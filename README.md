## 📌 Description
transfer data between grids with different schemas (reblock)
## 📸 Screenshot
![screenshot1](../../code/pandoc_index/assets/vtk_merge_grid1.png)
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
![screenshot2](../../code/pandoc_index/assets/vtk_merge_grid2.png)
## 🧩 Compatibility
distribution|status
---|---
![winpython_icon](../../code/pandoc_index/assets/winpython_icon.png)|✔
![vulcan_icon](../../code/pandoc_index/assets/vulcan_icon.png)|❌
![anaconda_icon](../../code/pandoc_index/assets/anaconda_icon.png)|❌
## 🙋 Support
Any question or problem contact:
 - paulo.ernesto
## 💎 License
Apache 2.0
Copyright ![vale_logo_only](../../code/pandoc_index/assets/vale_logo_only_r.svg) Vale 2023
