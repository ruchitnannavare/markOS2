import requests
import json
from requests import ConnectionError
from tkinter import *
try:
    url = "https://api.telegram.org/bot1339449529%3AAAFv9IMnjFl7I6zXwnTrqgM_CcVam-MpXk0/getUpdates"
    dic = requests.get(url)
    new = json.loads(dic.content)
    result_list = new["result"]
    list = []
    for dict in result_list:
        from_person = dict["message"]["from"]
        first_name = from_person["first_name"]
        last_name = from_person["last_name"]
        chat_id = from_person["id"]
        data_tuple = (first_name, last_name, chat_id)
        list.append(data_tuple)
    print(list)
    list_2 = [("First Name", "Last Name", "Unique ID")]
    final_list = list_2 + list


    class Mytable:
        def __init__(self, show_test_root):
            for i in range(totalrows):
                for j in range(totalcolumns):
                    self.e = Entry(show_test_root, width=20, fg="black", font=("Arial", 11))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, final_list[i][j])
                    self.e.configure(state="readonly")
    totalrows = len(final_list)
    totalcolumns = len(final_list[1])
    show_test_root = Tk()
    show_test_root.title("SideView")
    show_test_root.resizable(0, 0)
    mt = Mytable(show_test_root)
    show_test_root.mainloop()
except ConnectionError as e:
    print(e)
