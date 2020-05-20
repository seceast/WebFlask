# coding=utf-8
# 代码文件：chapter19/ch19.7.3-1.py

import wx
import wx.grid

data = [['0036', '高等数学', '李放', '人民邮电出版社', '20000812', '1'],
        ['0004', 'FLASH精选', '刘扬', '中国纺织出版社', '19990312', '2'],
        ['0026', '软件工程', '牛田', '经济科学出版社', '20000328', '4'],
        ['0015', '人工智能', '周未', '机械工业出版社', '19991223', '3'],
        ['0037', '南方周末', '邓光明', '南方出版社', '20000923', '3'],
        ['0008', '新概念3', '余智', '外语出版社', '19990723', '2'],
        ['0019', '通讯与网络', '欧阳杰', '机械工业出版社', '20000517', '1'],
        ['0014', '期货分析', '孙宝', '飞鸟出版社', '19991122', '3'],
        ['0023', '经济概论', '思佳', '北京大学出版社', '20000819', '3'],
        ['0017', '计算机理论基础', '戴家', '机械工业出版社', '20000218', '4'],
        ['0002', '汇编语言', '李利光', '北京大学出版社', '19980318', '2'],
        ['0033', '模拟电路', '邓英才', '电子工业出版社', '20000527', '2'],
        ['0011', '南方旅游', '王爱国', '南方出版社', '19990930', '2'],
        ['0039', '黑幕', '李仪', '华光出版社', '20000508', '14'],
        ['0001', '软件工程', '戴国强', '机械工业出版社', '19980528', '2'],
        ['0034', '集邮爱好者', '李云', '人民邮电出版社', '20000630', '1'],
        ['0031', '软件工程', '戴志名', '电子工业出版社', '20000324', '3'],
        ['0030', '数据库及应用', '孙家萧', '清华大学出版社', '20000619', '1'],
        ['0024', '经济与科学', '毛波', '经济科学出版社', '20000923', '2'],
        ['0009', '军事要闻', '张强', '解放军出版社', '19990722', '3'],
        ['0003', '计算机基础', '王飞', '经济科学出版社', '19980218', '1'],
        ['0020', '现代操作系统', '王小国', '机械工业出版社', '20010128', '1'],
        ['0025', '计算机体系结构', '方丹', '机械工业出版社', '20000328', '4'],
        ['0010', '大众生活', '许阳', '电子出版社', '19990819', '3'],
        ['0021', '网络基础', '王大尉', '北京大学出版社', '20000617', '1'],
        ['0006', '世界杯', '柳飞', '世界出版社', '19990412', '2'],
        ['0028', '高级语言程序设计', '寇国华', '清华大学出版社', '20000117', '3'],
        ['0038', '十大旅游胜地', '潭晓明', '南方出版社', '20000403', '2'],
        ['0018', '编译原理', '郑键', '机械工业出版社', '20000415', '2'],
        ['0007', 'JAVA程序设计', '张余', '人民邮电出版社', '19990613', '1'],
        ['0013', '幽灵', '钱力华', '华光出版社', '19991008', '1'],
        ['0022', '万紫千红', '丛丽', '北京大学出版社', '20000702', '3'],
        ['0027', '世界语言大观', '候丙辉', '经济科学出版社', '20000814', '2'],
        ['0029', '操作系统概论', '聂元名', '清华大学出版社', '20001028', '1'],
        ['0016', '数据库系统概念', '吴红', '机械工业出版社', '20000328', '3'],
        ['0005', 'java基础', '王一', '电子工业出版社', '19990528', '3'],
        ['0032', 'SQL使用手册', '贺民', '电子工业出版社', '19990425', '2']]

column_names = ['书籍编号', '书籍名称', '作者', '出版社', '出版日期', '库存数量']


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='网格控件', size=(550, 500))
        self.Centre()  # 设置窗口居中
        self.grid = self.CreateGrid(self)
        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.OnLabelLeftClick)

    def OnLabelLeftClick(self, event):
        print("RowIdx：{0}".format(event.GetRow()))
        print("ColIdx：{0}".format(event.GetCol()))
        print(data[event.GetRow()])
        event.Skip()

    def CreateGrid(self, parent):
        grid = wx.grid.Grid(parent)
        grid.CreateGrid(len(data), len(data[0]))

        for row in range(len(data)):
            for col in range(len(data[row])):
                grid.SetColLabelValue(col, column_names[col])
                grid.SetCellValue(row, col, data[row][col])
        # 设置行和列自定调整
        grid.AutoSize()

        return grid


class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()  # 进入主事件循环
