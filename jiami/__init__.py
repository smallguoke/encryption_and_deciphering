# import tkinter as tk
# from tkinter import END
#
# import AES
# import SHA1
#
# # OptionList = [
# #     "AES",
# #     "DES",
# #     "HMAC",
# #     "MD5",
# #     "RSA",
# #     "SHA1"
# # ]
# #
# # app = tk.Tk()
# #
# # app.geometry('900x600')
# #
# # variable = tk.StringVar(app)
# # variable.set(OptionList[0])
# #
# # opt = tk.OptionMenu(app, variable, *OptionList)
# # opt.config(width=90, font=('Helvetica', 12))
# # opt.pack()
# #
# # app.mainloop()
#
#
# # root = tk.Tk()
# # root.title("加密解密程序")
# # root.geometry('500x500')
# # sha1 = SHA1.Sha1_a()
# # e = tk.Entry(root, show=None)
# # e.pack
# #
# # te = tk.Text(root, height=10)
# # te.pack
# #
# #
# # def but():
# #     sha1.data = e.get()
# #     miw = sha1.encrypt()
# #     te.insert('insert',miw)
# #
# #
# # bl = tk.Button(root, text='加密', width=15, height=2, command=but())
# # bl.pack
# #
# # root.mainloop()
# import tkinter as tk
#
# root = tk.Tk()  # 实例化对象
# root.title('title')  # 给窗口取名
# root.geometry("500x400")
# sha1 = SHA1.Sha1_a()
# l = tk.Label(text='明文：', font=("宋体", 15), fg='blue')
# l.grid(row=0,column=0)
# e = tk.Entry(root, show=None)
# e.grid(row=0,column=1)
#
#
# def insert_point():
#     var = e.get()
#     sha1.data = var
#     miw = sha1.encrypt()
#     t.delete(0.0, END)
#     t.insert("insert", miw)
#
#
# b1 = tk.Button(root, text='加密',
#                bg='white', font="Arial,12",
#                width=15, height=1, command=insert_point)  # 给窗口添加按钮
# b1.grid()
#
# t = tk.Text(root, height=10)
# t.grid()
#
# root.mainloop()  # 大型的while循环
