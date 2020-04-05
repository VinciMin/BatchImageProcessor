## 介绍

我是一名视觉设计师，在日常工作中经常会遇到很多批量处理大量图片的工作。例如使用InDesign中的数据合并，或是Photoshop中的数据组功能，同时完成成千上百张设计稿中图片/文字信息的替换工作。然而对于大批量的文件处理，直接进行手动操作重命名等操作费时费力。我选择了Python3作为加持，可以进行大量且快速的批量操作。

## 文件批量重命名

对于成百上千张图片，可以使用下方的代码快速的进行重命名，并且分类到指定的文件夹。
[从Excel文件对图片重命名](https://github.com/VinciMin/BatchImageProcessor/blob/master/RenameFromExcel.py)

## 图片纵向合并

有时候我们对一张图片中的切片进行批处理，而后又希望对切片进行纵向整合，可以用这里的代码。
[图片纵向合并](https://github.com/VinciMin/BatchImageProcessor/blob/master/VerticalMergerImg.py)

## 文件夹批量合并为Zip

对于图片分类之后产生的数十个文件夹，如何分别打包为Zip文件，方便地发送给客户呢？可以使用下方代码
[文件夹批量合并为Zip](https://github.com/VinciMin/BatchImageProcessor/blob/master/MakeZip.py)

## gif文件批量转jpg

网上gif的网站大都速度慢，并且有数量限制。这种情况下不妨使用以下代码。输入文件夹路径即可把所有的gif转为jpg，还能保持文件名称不变。
[gif文件批量转jpg](https://github.com/VinciMin/BatchImageProcessor/blob/master/gif2jpg.py)
