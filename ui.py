import customtkinter
import handle
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500*350")
root.title("仪表文档生成系统")

current_path = os.getcwd()
filedir = current_path+"\\生成文件"
replace_dict = {
    # 合总目
    "拓拓拓": "",
    # 总目
    "绮绮绮": "第一采气厂2023年产建地面工程",
    # 总分目
    "梃梃梃": "煤岩气站外管线 调整设计",
    # 项目号
    "KKKK111T-0000": "CEDC015S-2023",
    # 文件号
    "拉-00000": "仪-23507",
    # 施工阶段
    "嘭嘭嘭": "施工图",
    # 日期
    "0000-12-12": "2023.07.24",
}

'''
def login():
    demo.requests_(entry1.get(),entry2.get())
    demo.get_brower(demo.reflist,entry3.get())
    entry1.delete(0,len(entry1.get()))
    entry2.delete(0, len(entry2.get()))
    demo.reflist=[]
    demo.data = {
        'newsNumber': '999999999',
        'pageSize': '20',
        'pageIndex': '1',
        'subChannelNumber': '0',
        'NewsSiteJson':'[{"paramenterlist":[{"ApplcationName":"https://cqyt.eip.cnpc/sites/d1cyc/news","ColumnEnName":"tzgg"}]}]'
        }
'''

def generate():

    #修改参数到特定的word文档里面
    replace_dict["拓拓拓"]= entry1.get()
    replace_dict["绮绮绮"] = entry2.get()
    replace_dict["梃梃梃"] = entry3.get()
    replace_dict["KKKK111T-0000"] = entry4.get()
    replace_dict["拉-00000"] = entry5.get()
    replace_dict["嘭嘭嘭"] = entry6.get()
    replace_dict["0000-12-12"] = entry7.get()

    handle.transfer(filedir,replace_dict)
    handle.kill_process()
    handle.main(replace_dict)

    #把之前存储在后台的内容清空
    entry1.delete(0, len(entry1.get()))
    entry2.delete(0, len(entry2.get()))
    entry3.delete(0, len(entry3.get()))
    entry4.delete(0, len(entry4.get()))
    entry5.delete(0, len(entry5.get()))
    entry6.delete(0, len(entry6.get()))
    entry7.delete(0, len(entry7.get()))


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label = customtkinter.CTkLabel(master=frame,text="仪表文档生成系统")
label.pack(pady=12,padx=10)

entry1 = customtkinter.CTkEntry(master=frame,placeholder_text="合总目")
entry1.pack(pady=12,padx=10)

entry2 = customtkinter.CTkEntry(master=frame,placeholder_text="总目")
entry2.pack(pady=12,padx=10)

entry3 = customtkinter.CTkEntry(master=frame,placeholder_text="总分目")
entry3.pack(pady=12,padx=10)

entry4 = customtkinter.CTkEntry(master=frame,placeholder_text="项目号")
entry4.pack(pady=12,padx=10)

entry5 = customtkinter.CTkEntry(master=frame,placeholder_text="文件号")
entry5.pack(pady=12,padx=10)

entry6 = customtkinter.CTkEntry(master=frame,placeholder_text="施工阶段")
entry6.pack(pady=12,padx=10)

entry7 = customtkinter.CTkEntry(master=frame,placeholder_text="日期")
entry7.pack(pady=12,padx=10)


button = customtkinter.CTkButton(master=frame,text="生成文档",command=generate)
button.pack(pady=12,padx=10)



'''
checkbox = customtkinter.CTkCheckBox(master=frame,text="记住账号")
checkbox.pack(pady=12,padx=10)
'''
root.mainloop()