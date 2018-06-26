import tkinter as tk
import OpenFile
import BuildDBConfig


class CreatMain:
    def __init__(self, master):
        self.root = master
        self.main_menu = tk.Menu(self.root)
        # Frame页面创建
        self.main_frm = tk.Frame(self.root)
        self.openfile_frm = OpenFile.OpenFile(self.root)
        self.builddbconfig_frm = BuildDBConfig.XML(self.root)

        self.creatMenu()
        self.creatMainFrm()
        # 默认显示主页面Frame
        self.main_frm.pack()

    # 主页切换菜单显示

    def creatMenu(self):
        self.file_menu = tk.Menu(self.main_menu)
        self.file_menu.add_command(
            label='主页', command=lambda: self.showFrm(self.main_frm))
        self.file_menu.add_command(
            label='打开文件', command=lambda: self.showFrm(self.openfile_frm))

        self.xml_menu = tk.Menu(self.main_menu)
        self.xml_menu.add_command(
            label="BuildDBConfig", command=lambda: self.showFrm(self.builddbconfig_frm))

        self.main_menu.add_cascade(label="文件", menu=self.file_menu)
        self.main_menu.add_cascade(label="XML文件生成", menu=self.xml_menu)
        self.root.config(menu=self.main_menu)

    # 主页面Frame视图

    def creatMainFrm(self):
        tk.Label(self.main_frm, text="软件说明").grid()

    # Frame切换函数
    def showFrm(self, frame):
        # 所有生成的Frame页面
        self.frames = [self.main_frm,
                       self.openfile_frm, self.builddbconfig_frm]
        self.frames.remove(frame)
        for f in self.frames:
            f.pack_forget()
        frame.pack()


'''
废弃的frame显示切换方法
    def _mainFrm(self):
        self.main_frm.pack()
        self.openfile_frm.pack_forget()
        self.builddbconfig_frm.pack_forget()

    def _openFile(self):
        self.main_frm.pack_forget()
        self.openfile_frm.pack()
        self.builddbconfig_frm.pack_forget()

    def _builddbconfigFrm(self):
        self.main_frm.pack_forget()
        self.openfile_frm.pack_forget()
        self.builddbconfig_frm.pack()
'''

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Tool Set")
    width = 600
    height = 660
    root.geometry(
        '%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth() - width)/2,
                         (root.winfo_screenheight() - height)/2))
    CreatMain(root)
    root.mainloop()
