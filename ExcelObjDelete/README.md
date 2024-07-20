# 对于Excel文件中数量未知的“对象”导致的难以打开或超级卡顿问题，使用Python脚本删除“对象”

当打开某个Excel文件（xls格式或xlsx格式）时，有时会因为某种未知原因，导致①打不开②闪退③打开过程特别缓慢 <br /> <br />
而出现这种现象的原因又已知绝对不是因为数据量（数据量没有达到那种程度） <br /> <br />
一般情况下，我们认为是因为Excel文件中存在数量极大的“对象”所导致的 <br /> <br />

解决办法就是，删除这些对象。其实一般情况下，最佳方案是 <br />
（1）利用Excel里面的定位功能，筛选所有对象，再Ctrl+A，再Delete <br />
（2）利用Excel里面的选择窗格+选择对象，再Ctrl+A，再Delete <br />
（3）利用VBA进行操作 <br /> <br />

但在这里，由于难以打开目标Excel文件或者打开过程、操作过程极其卡顿，我们采用Python处理的方法 <br /><br />

若需封装成跨平台的exe可执行文件，请在cmd执行:pyinstaller --onefile --windowed ExcelObjDelete_GUI.py <br /><br />

![image](https://github.com/user-attachments/assets/73812f27-1742-4d47-9cc9-0db22810dcd6)<br />


