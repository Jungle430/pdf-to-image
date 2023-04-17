# pdf-to-image

一个将pdf自动转化为图片的脚本

>2023-4-17

- 前几天用了[typst](https://typst.app)用来写作业和报告，感觉效果很好（主要比Latex入门容易)，但是交作业的时候需要交图片，所以写了一个pdf转图片的脚本(WPS还NMD收费，确实恶心坏了)，后续可能会继续完善本项目，比如网页转图片啥的

- 依赖环境
  - 安装PyMuPDF库：

```python
pip install PyMuPDF
```

- 使用方式
  - 将`pdf`文件移动至和`main.py`同一级文件目录
  
  - 后面接`pdf`文件名即可
  
  - 例子：
  

```shell
python .\main.py .\chapter5.pdf
```

