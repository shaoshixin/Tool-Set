import tkinter as tk
import tkinter.ttk as ttk
import TestUrl
import sys
import tkinter.filedialog


class TestUrlFrame(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.param1_filepath = tk.StringVar()
        self.param2_filepath = tk.StringVar()
        self.url_value = tk.StringVar()
        self.url_value.set("http://localhost:3000/login/loginSub")
        self.reqheaders_value = tk.StringVar()
        self.creatPage()

    def creatPage(self):
        tk.Label(self, text="测试URL：").grid(
            row=0, column=0, sticky='W')
        self.url_entry = tk.Entry(self, width=60, textvariable=self.url_value)
        self.url_entry.grid(row=0, column=1, sticky='W')

        tk.Label(self, text="提交方式：").grid(row=1, column=0, sticky='W')
        self.httpsub_combox = ttk.Combobox(self)
        self.httpsub_combox['values'] = ["GET", "POST"]
        self.httpsub_combox.grid(row=1, column=1, sticky='W')

        tk.Label(self, text="头部信息：").grid(row=2, column=0, sticky='W')
        # 创建文本框text，设置宽度100，high不是高度，是文本显示的行数设置为2行
        self.reqheaders_text = tk.Text(self, width=60, height=8)
        self.reqheaders_text.insert(
            1.0, {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64)"
                  "AppleWebKit/537.36 (KHTML, like Gecko)"
                  "Chrome/65.0.3325.181 Safari/537.36",
                  "Referer": "http://localhost:3000/"})
        self.reqheaders_text.grid(row=2, column=1, sticky='W')
        # 创建文本框侧边滚动条，主要方法有两个，将滚动条command方法设置为文本框的yview，将文本框['yscrollcommand']设置为滚动条的set方法
        self.sl1 = tk.Scrollbar(self, orient=tk.VERTICAL,
                                command=self.reqheaders_text.yview)
        self.sl1.grid(row=2, column=2, sticky=tk.N+tk.S)
        self.reqheaders_text['yscrollcommand'] = self.sl1.set

        self.param_frame = tk.Frame(self)
        self.param_frame.grid(row=3, column=0, columnspan=2, sticky='W')

        tk.Label(self.param_frame, text="参数1名：").grid(
            row=0, column=0, sticky='W')
        self.param1_entry = tk.Entry(self.param_frame, width=10)
        self.param1_entry.grid(row=0, column=1, sticky='W')

        tk.Label(self.param_frame, text="参数1测试值选择：",).grid(
            row=0, column=2, sticky='W')
        self.param1_entry = tk.Entry(
            self.param_frame, textvariable=self.param1_filepath, width=30)
        self.param1_entry.grid(row=0, column=3, sticky='W')

        tk.Button(self.param_frame, text="文件选择",
                  command=lambda: self.selectPath(self.param1_filepath)).grid(row=0, column=4)

        tk.Label(self.param_frame, text="参数2名：").grid(
            row=1, column=0, sticky='W')
        self.param2_entry = tk.Entry(self.param_frame, width=10)
        self.param2_entry.grid(row=1, column=1, sticky='W')

        tk.Label(self.param_frame, text="参数2测试值选择：").grid(
            row=1, column=2, sticky='W')
        self.param2_entry = tk.Entry(
            self.param_frame, textvariable=self.param2_filepath, width=30)
        self.param2_entry.grid(row=1, column=3, sticky='W')

        tk.Button(self.param_frame, text="文件选择",
                  command=lambda: self.selectPath(self.param2_filepath)).grid(row=1, column=4)

        self.btn = tk.Button(self, text="btn", width=6, command=self._go)
        self.btn.grid()

        self.res_text = tk.Text(self, width=60, height=12)
        self.res_text.grid(row=4, column=1)

    def getBack(self):

        self.url = self.url_entry.get()
        self.headers = eval(self.reqheaders_text.get('0.0', 'end'))
        print(self.param1_entry.get())
        self.f = TestUrl.ReadFile(self.param1_entry.get())
        return self.url, self.headers, self.f

    def selectPath(self, en):
        path = tkinter.filedialog.askopenfilename()
        en.set(path)

    def _go(self):

        url, headers, f = self.getBack()
        # self.url = self.url_entry.get()
        # self.headers = eval(self.reqheaders_text.get('0.0', 'end'))
        # self.f = TestUrl.ReadFile("D:/projects/python36/Tool-Set/1.json")
        ok_num = 0  # 成功用例计数
        fail_num = 0  # 失败用例计数
        ok_list = []  # 成功用例列表，若为字典的话因为值不同导致被覆盖
        fail_list = []  # 失败用例列表
        data = f.read_file()  # data为账号密码的组合
        for i in data:
            try:
                test_login = TestUrl.TLogin(url, headers, i)
                t_req = test_login.get_back()
                item = dict(t_req, **i)  # 由于字典的键为code 所以会不断进行覆盖，变成了更新而不是拼接
                if t_req["code"] == "200":
                    ok_num += 1
                    ok_list.append(item)
                else:
                    fail_num += 1
                    fail_list.append(item)
                num = ok_num + fail_num
            except:
                t = '%s%s' % ("连接错误！", sys.exc_info()[0])
                print(t)
                self.res_text.delete(1.0, "end")
                self.res_text.insert(1.0, t)
        t = '%s%s%s%s%s%s%s%s%s%s%s%s%s' % ("共测试", num, "个用例，", "\n", "其中成功",
                                            ok_num, "个，失败", fail_num, "个", "\n", "成功的用例为：", "\n", ok_list)
        self.res_text.delete(1.0, "end")
        self.res_text.insert(1.0, t)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Tool Set")
    width = 600
    height = 660
    root.geometry(
        '%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth() - width)/2,
                         (root.winfo_screenheight() - height)/2))
    frm = TestUrlFrame(root)
    frm.grid()
    root.mainloop()
