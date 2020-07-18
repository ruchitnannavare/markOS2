from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import json
favicon = "favicon.ico"


def update_data_function():
    update_database_root = Toplevel()
    update_database_root.geometry("300x120")
    update_database_root.title("Update")
    update_database_root.iconbitmap(favicon)
    update_database_root.resizable(0, 0)
    update_database_root.configure(background="#d3d3d3")
    update_label = Label(update_database_root, text="Prompt for updating student information.", font=("Helvetica", 10), fg="#585858", bg="#d3d3d3")
    update_label.grid(row=0, column=0, columnspan=2, ipadx=10, pady=(10, 5))
    student_roll_label = Label(update_database_root, text="Enter student's unique ID:", anchor=W, bg="#d3d3d3")
    student_roll_label.grid(row=1, column=0, padx=5, pady=5)
    student_roll_input = Entry(update_database_root, borderwidth=0)
    student_roll_input.grid(row=1, column=1, padx=5, pady=5)
    admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
    admissions_standard_dict = {admissions_standard_list[0]: "eleven_science", admissions_standard_list[1]: "twelve_science"}
    admissions_standard_dict_invert = {"eleven_science": admissions_standard_list[0],
                                       "twelve_science": admissions_standard_list[1]}
    def update_data():
        update_data_buttom = Button(update_database_root,
                                    text="Enter",
                                    font=("Helvetica", 10),
                                    width=15,
                                    borderwidth=0,
                                    bg="#45b4e7",
                                    fg="white",
                                    activeforeground="white",
                                    activebackground="#1ca0dd",
                                    command=update_data,
                                    state=DISABLED)
        update_data_buttom.grid(row=2, columnspan=2, padx=(15, 0), pady=(5, 0))
        unique_id = str(student_roll_input.get()).upper()
        with open("student_key_data.json", "r") as file:
            try:
                dictionary = json.load(file)
                found_list = dictionary[unique_id]
                permission = True
            except KeyError:
                error_message = messagebox.showerror("Student Not found!", "The mID unique key you entered isn't assigned to anyone yet.")
                if error_message == "ok":
                    pass
                student_roll_input.delete(0, END)
                update_data_buttom.configure(state=ACTIVE)
                permission = False
        if permission == True:
            print(found_list)

            def printgiven(id):
                print(id)
                connection_name = "admission_" + str(found_list[0]) + ".db"
                print(connection_name)
                connection = sqlite3.connect(connection_name)
                cursor = connection.cursor()
                xcude = admissions_standard_dict[str(found_list[1])]
                print(xcude)
                toprint = f"select * FROM {xcude} where Rollno=?"
                print(toprint)
                try:
                    cursor.execute(toprint, (id,))
                    row = cursor.fetchone()
                    print(row)
                    print(1)
                except Error as e:
                    print(e)
                    row = e

                return row
                connection.close()
                cursor.close()

            data_tuple = printgiven(unique_id)
            print(data_tuple)
            admissions_root = Toplevel()
            admissions_root.geometry("496x545")
            admissions_root.resizable(0, 0)
            admissions_root.title("Update Data")
            admissions_root.iconbitmap(favicon)
            admissions_root.configure(background="#d3d3d3")
            admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
            admissions_branch_list = ["Harni", "Karelibaug"]
            admissions_year_list = []
            for year in range(0, 79):
                year_string = "20" + str(20 + year) + "-" + str(21 + year)
                admissions_year_list.append(year_string)
            admissions_parent_relation_list = ["Mother", "Father", "Guardian"]

            # Admission prompt
            admissions_label = Label(admissions_root,
                                     text="Prompt for updating student data, fill in the details.",
                                     anchor=W,
                                     bg="#d3d3d3",
                                     fg="#585858",
                                     font=("Helevetica", 10))
            admissions_label.grid(row=0, column=0, columnspan=2, ipadx=78, pady=(15, 15))
            # Student details
            # Students first name
            admissions_firstname_label = Label(admissions_root,
                                               text="Student's First Name:",
                                               bg="#d3d3d3")
            admissions_firstname_label.grid(row=1, column=0, padx=10, sticky=W)
            firstname_var = StringVar()
            firstname_var.set(data_tuple[1])
            admissions_firstname_input = Entry(admissions_root,
                                               width=30,
                                               font=11,
                                               bg="white",
                                               borderwidth=0,
                                               textvariable=firstname_var)
            admissions_firstname_input.grid(row=1, column=1, padx=15, sticky=W)
            # Student's last name
            admissions_lastname_label = Label(admissions_root,
                                              text="Student's Last Name:",
                                              bg="#d3d3d3")
            admissions_lastname_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
            lastname_var = StringVar()
            lastname_var.set(data_tuple[2])
            admissions_lastname_input = Entry(admissions_root,
                                              width=30,
                                              font=11,
                                              bg="white",
                                              borderwidth=0,
                                              textvariable=lastname_var)
            admissions_lastname_input.grid(row=2, column=1, padx=15, pady=10, sticky=W)

            # Relation dropdown menu
            guardian_relation = StringVar()
            guardian_relation.set(data_tuple[3])
            admissions_guardian_relation_label = Label(admissions_root,
                                                       text="Guardian Relation:",
                                                       bg="#d3d3d3")
            admissions_guardian_relation_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
            admissions_relation_label = OptionMenu(admissions_root, guardian_relation, *admissions_parent_relation_list)
            admissions_relation_label.grid(row=3, column=1, padx=14, pady=10, sticky=W)

            # Guardian name input
            admissions_guardian_name_label = Label(admissions_root,
                                                   text=f"{guardian_relation.get()} Full Name:",
                                                   bg="#d3d3d3")
            admissions_guardian_name_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
            guardianname_var = StringVar()
            guardianname_var.set(data_tuple[4])
            admissions_guardian_name_input = Entry(admissions_root,
                                                   width=30,
                                                   font=11,
                                                   bg="white",
                                                   borderwidth=0,
                                                   textvariable=guardianname_var)
            admissions_guardian_name_input.grid(row=4, column=1, padx=15, pady=10, sticky=W)

            # Student Address
            admissions_student_address_label = Label(admissions_root,
                                                     text="Student Address:",
                                                     bg="#d3d3d3")
            admissions_student_address_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
            address_var = StringVar()
            address_var.set(data_tuple[5])
            admissions_student_address_input = Entry(admissions_root,
                                                     width=30,
                                                     font=(11),
                                                     bg="white",
                                                     borderwidth=0,
                                                     textvariable=address_var)
            admissions_student_address_input.grid(row=5, column=1, padx=15, pady=10, sticky=W)

            # Admission year frame
            admissions_year_frame = Frame(admissions_root, height=8, width=39, bg="#d3d3d3")
            admissions_year_frame.grid(row=6, column=0)

            admissions_year = StringVar()
            admissions_year.set(data_tuple[6])
            admissions_year_label = Label(admissions_year_frame,
                                          text="Academic Year:",
                                          bg="#d3d3d3")
            admissions_year_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

            admissions_year_scroll = OptionMenu(admissions_year_frame,
                                                admissions_year,
                                                *admissions_year_list, )
            admissions_year_scroll.grid(row=0, column=1, sticky=W)

            # Standard frame
            admissions_standard_frame = Frame(admissions_root, height=8, width=25, bg="#d3d3d3")
            admissions_standard_frame.grid(row=6, column=1)
            admissions_standard_label = Label(admissions_standard_frame,
                                              text="                              Standard:",
                                              bg="#d3d3d3")
            admissions_standard_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)

            admissions_standard = StringVar()
            admissions_standard.set(data_tuple[7])

            admissions_standard_scroll = OptionMenu(admissions_standard_frame,
                                                    admissions_standard,
                                                    *admissions_standard_list)
            admissions_standard_scroll.grid(row=0, column=1, sticky=W)

            # Branch Frame
            admissions_branch_label = Label(admissions_root,
                                            text="Branch:",
                                            bg="#d3d3d3")
            admissions_branch_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)

            admissions_branch = StringVar()
            admissions_branch.set(data_tuple[8])

            admissions_branch_scroll = OptionMenu(admissions_root,
                                                  admissions_branch,
                                                  *admissions_branch_list)
            admissions_branch_scroll.grid(row=7, column=1, padx=14, pady=10, sticky=EW)

            # parents mobile number
            admissions_parent_number_label = Label(admissions_root,
                                                   text="Guardian Phone Number:",
                                                   bg="#d3d3d3")
            admissions_parent_number_label.grid(row=8, column=0, padx=10, pady=10, sticky=W)
            parent_var = IntVar()
            parent_var.set(data_tuple[9])
            admissions_parent_number_input = Entry(admissions_root,
                                                   width=30,
                                                   font=11,
                                                   bg="white",
                                                   borderwidth=0,
                                                   textvariable=parent_var)
            admissions_parent_number_input.grid(row=8, column=1, padx=15, pady=10, sticky=W)

            # Student phone Number
            admissions_student_number_label = Label(admissions_root,
                                                    text="Student Phone Number:",
                                                    bg="#d3d3d3")
            admissions_student_number_label.grid(row=9, column=0, padx=10, pady=10, sticky=W)
            student_var = IntVar()
            student_var.set(data_tuple[10])
            admissions_student_number_input = Entry(admissions_root,
                                                    width=30,
                                                    font=11,
                                                    bg="white",
                                                    borderwidth=0,
                                                    textvariable=student_var)
            admissions_student_number_input.grid(row=9, column=1, padx=15, pady=10, sticky=W)

            # Guardian email address
            admissions_guardian_email_label = Label(admissions_root,
                                                    text="Guardian Email Address:",
                                                    bg="#d3d3d3")
            admissions_guardian_email_label.grid(row=10, column=0, padx=10, pady=10, sticky=W)
            parent_mail_var = StringVar()
            parent_mail_var.set(data_tuple[11])
            admissions_guardian_email_input = Entry(admissions_root,
                                                    width=30,
                                                    font=11,
                                                    bg="white",
                                                    borderwidth=0,
                                                    textvariable=parent_mail_var)
            admissions_guardian_email_input.grid(row=10, column=1, padx=15, pady=10, sticky=W)

            # Student email address
            admissions_student_email_label = Label(admissions_root,
                                                   text="Student Email Address:",
                                                   bg="#d3d3d3")
            admissions_student_email_label.grid(row=11, column=0, padx=10, pady=10, sticky=W)
            student_mail_var = StringVar()
            student_mail_var.set(data_tuple[12])
            admissions_student_email_input = Entry(admissions_root,
                                                   width=30,
                                                   font=(11),
                                                   bg="white",
                                                   borderwidth=0,
                                                   textvariable=student_mail_var)
            admissions_student_email_input.grid(row=11, column=1, padx=15, pady=10, sticky=W)

            # Functions for checking admission details
            def check_admission_details():
                input_list = [admissions_firstname_input, admissions_lastname_input, admissions_guardian_name_input,
                              admissions_student_address_input, admissions_parent_number_input, admissions_student_number_input,
                              admissions_guardian_email_input, admissions_student_email_input]
                input_label_list = [admissions_firstname_label, admissions_lastname_label, admissions_guardian_name_label,
                                    admissions_student_address_label, admissions_parent_number_label,
                                    admissions_student_number_label, admissions_guardian_email_label,
                                    admissions_student_email_label]
                for i in input_list:
                    if len(i.get()) == 0:
                        missing_text = input_label_list[input_list.index(i)].cget("text")
                        give_warning = messagebox.showerror("Blank is Empty", f"{missing_text} Can not be left empty!")
                        if give_warning == "ok":
                            i.delete(0, END)

            # Check Int and strings
            def check_int_str():
                variable_int_list = [admissions_student_number_input, admissions_parent_number_input]
                variable_int_list_label = [admissions_student_number_label, admissions_parent_number_label]
                for integer in variable_int_list:
                    try:
                        int(integer.get())
                    except ValueError:
                        integer_error_variable = variable_int_list_label[variable_int_list.index(integer)].cget("text")
                        integer_error = messagebox.showerror("Number Error",
                                                             f"{integer_error_variable} Can only contain numbers!")
                        if integer_error == "ok":
                            integer.delete(0, END)

                variable_str_list = [admissions_firstname_input, admissions_lastname_input, admissions_guardian_name_input]
                variable_str_list_label = [admissions_firstname_label, admissions_lastname_label,
                                           admissions_guardian_name_label]
                for string in variable_str_list:
                    string_list = list(string.get())
                    occurance = 0
                    for element in string_list:
                        for num in list(range(0, 10)):
                            if str(num) == element:
                                print(num)
                                string_error_variable = variable_str_list_label[variable_str_list.index(string)].cget("text")
                                string_error = messagebox.showerror("Character Error",
                                                                    f"{string_error_variable} Can only contain alphabetic characters.")
                                occurance += 1
                                if string_error == "ok":
                                    string.delete(0, END)
                        if occurance >= 1:
                            break

            # Submit button function
            def update_submit():
                global data_tuple_2
                check_admission_details()
                check_admission_details()
                check_int_str()
                admissions_confirmation = messagebox.askyesno("Confirm Update",
                                                              "All the details are filled in!\nClick YES to update your markOS database.",
                                                              master=admissions_root)
                data_tuple_2 = (str(admissions_firstname_input.get()).upper(),
                                str(admissions_lastname_input.get()).upper(),
                                str(guardian_relation.get().upper()),
                                str(admissions_guardian_name_input.get()).upper(),
                                str(admissions_student_address_input.get()).upper(),
                                str(admissions_year.get()),
                                str(admissions_standard.get()),
                                str(admissions_branch.get()).upper(),
                                int(admissions_parent_number_input.get()),
                                int(admissions_student_number_input.get()),
                                str(admissions_guardian_email_input.get()),
                                str(admissions_student_email_input.get()))
                print(data_tuple_2)
                if admissions_confirmation == True:
                    password_window = Toplevel()
                    password_window.attributes('-topmost', 'true')
                    password_window.geometry("200x130")
                    password_window.iconbitmap(favicon)
                    password_window.configure(background="#d3d3d3")
                    password_window.resizable(0, 0)
                    password_window_label = Label(password_window, width=25,
                                                  text="Please enter master password\nto edit your markOS database.",
                                                  bg="#d3d3d3")
                    password_window_label.pack(pady=(10, 0))
                    password_window_input = Entry(password_window, borderwidth=0, show="*", width=25, font=("Times", 9, "bold"))
                    password_window_input.pack(pady=(15, 0))

                    def update_successfull():
                        print(password_window_input.get())
                        if str(password_window_input.get()) == "1234":
                            admissions_root.attributes('-topmost', 'false')
                            password_window.attributes('-topmost', 'false')

                            admission_succesfull_message = messagebox.showinfo("Update Successful!",
                                                                               f"Update process has been succesfull.")


                            if admission_succesfull_message == "ok":
                                def update_given(Rollno, sfn, sln, gr, gfn, sa, ay, std, branch, gpn, spn, gea, sea):
                                    connection_name = "admission_" + str(found_list[0]) + ".db"
                                    print(connection_name)
                                    xcude = admissions_standard_dict[str(found_list[1])]
                                    print(xcude)
                                    connection = sqlite3.connect(connection_name)
                                    cursor = connection.cursor()

                                    updategiven = f"""update {xcude} set
                                                   first='%s',
                                                   last='%s',
                                                   gr='%s',
                                                   guardian='%s',
                                                   address='%s',
                                                   year='%s',
                                                   standard='%s',
                                                   branch='%s',
                                                   g_no='%s',
                                                   s_no='%s',
                                                   g_em='%s',
                                                   s_em='%s'
                                                   where rollno='%s' """
                                    args = (sfn, sln, gr, gfn, sa, ay, std, branch, gpn, spn, gea, sea, Rollno)

                                    try:
                                        cursor.execute(updategiven % args)
                                        connection.commit()
                                        out = "Done."

                                    except Error as e:
                                        connection.rollback()
                                        print(e)
                                        out = e
                                    return out
                                    connection.close()
                                    cursor.close()
                                admissions_root.destroy()
                                password_window.destroy()
                                update_given(str(unique_id)[:4],
                                             data_tuple_2[0],
                                             data_tuple_2[1],
                                             data_tuple_2[2],
                                             data_tuple_2[3],
                                             data_tuple_2[4],
                                             data_tuple_2[5],
                                             data_tuple_2[6],
                                             data_tuple_2[7],
                                             data_tuple_2[8],
                                             data_tuple_2[9],
                                             data_tuple_2[10],
                                             data_tuple_2[11])
                                update_database_root.destroy()
                        else:
                            messagewarning = messagebox.showwarning("Incorrect Password",
                                                                    "The Password you have entered is incorrect,\nplease try again.")
                            if messagewarning == "ok":
                                password_window_input.delete(0, END)

                    password_window_confirmation_button = Button(password_window,
                                                                 text="Enter Admission",
                                                                 font=("Helvetica", 9),
                                                                 width=15,
                                                                 borderwidth=0,
                                                                 bg="#67e867",
                                                                 fg="white",
                                                                 activeforeground="white",
                                                                 activebackground="#35e035",
                                                                 command=update_successfull)
                    password_window_confirmation_button.pack(pady=(15, 0))
                else:
                    admissions_root.destroy()

            # Submit button
            update_submit_button = Button(admissions_root,
                                          text="Submit Update",
                                          width=25,
                                          borderwidth=0,
                                          font=("Helvetica", 9),
                                          bg="#45b4e7",
                                          fg="white",
                                          activeforeground="white",
                                          activebackground="#1ca0dd",
                                          command=update_submit)
            update_submit_button.grid(row=12, column=0, padx=(14, 0), pady=10, sticky=W)

    update_button = Button(update_database_root,
                           text="Enter",
                           font=("Helvetica", 10),
                           width=15,
                           borderwidth=0,
                           bg="#45b4e7",
                           fg="white",
                           activeforeground="white",
                           activebackground="#1ca0dd",
                           command=update_data)

    update_button.grid(row=2, columnspan=2, padx=(15, 0), pady=(5, 0))

def access_data_function():
    data_access_top = Toplevel()
    data_access_top.title("markOS™")
    data_access_top.geometry("350x260")
    data_access_top.iconbitmap(favicon)
    data_access_top.resizable(0, 0)
    data_access_top.attributes('-topmost', 'true')
    data_access_top.configure(background="#d3d3d3")

    send_custom_text_label = Label(data_access_top, text="Select one method.", bg="#d3d3d3", fg="#585858", font=(("Helvetica"), 10))
    send_custom_text_label.pack(anchor=W, padx=10, pady=(10, 15))

    option_frame_1 = Frame(data_access_top, bg="#bababa", height=100, width=340)
    option_frame_1.pack(side="top", fill="both", expand=True, pady=(0, 5), padx=5)
    option_frame_1.propagate(False)
    empty_label = Label(option_frame_1, bg="#bababa", width=32)
    empty_label.grid(row=0, columnspan=3)
    send_one_label = Label(option_frame_1, text="See One", font=("Helvetica", 18, "italic"), fg="#585858", bg="#bababa")
    send_one_label.grid(row=1, column=0, columnspan=2, padx=(10, 0), sticky=W)
    send_one_instruction = Label(option_frame_1, text="See data of one student in particular.", font=("Helvetica", 9), fg="#585858", bg="#bababa")
    send_one_instruction.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky=W)

    def access_data_function_for_one():
        data_access_top.attributes('-topmost', 'false')
        access_data_root = Toplevel()
        access_data_root.attributes('-topmost', 'true')
        access_data_root.geometry("300x120")
        access_data_root.title("Student Data")
        access_data_root.iconbitmap(favicon)
        access_data_root.resizable(0, 0)
        access_data_root.configure(background="#d3d3d3")
        data_access_top.destroy()
        access_data_label = Label(access_data_root, text="Prompt for accessing student information.", font=("Helvetica", 10), fg="#585858", bg="#d3d3d3")
        access_data_label.grid(row=0, column=0, columnspan=2, ipadx=10, pady=(10, 5))
        student_roll_label = Label(access_data_root, text="Enter student's unique ID:", anchor=W, bg="#d3d3d3")
        student_roll_label.grid(row=1, column=0, padx=5, pady=5)
        student_roll_input = Entry(access_data_root, borderwidth=0)
        student_roll_input.grid(row=1, column=1, padx=5, pady=5)
        admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
        admissions_standard_dict = {"11 SCIENCE": "eleven_science", "12 SCIENCE": "twelve_science"}
        admissions_standard_dict_invert = {"eleven_science": admissions_standard_list[0],
                                           "twelve_science": admissions_standard_list[1]}
        def access_data():
            access_data_button.configure(state=DISABLED)
            unique_id = str(student_roll_input.get()).upper()
            with open("student_key_data.json", "r") as file:
                try:
                    dictionary = json.load(file)
                    found_list = dictionary[unique_id]
                    access_data_root.attributes('-topmost', 'false')
                    permission = True
                except KeyError:
                    access_data_root.attributes('-topmost', 'false')
                    error_message = messagebox.showerror("Student Not found!", "The mID unique key you entered isn't assigned to anyone yet.")
                    if error_message == "ok":
                        access_data_root.attributes('-topmost', 'true')
                    access_data_root.attributes('-topmost', 'true')
                    student_roll_input.delete(0, END)
                    access_data_button.configure(state=ACTIVE)
                    permission = False
            if permission == True:
                print(found_list)

                def printgiven(id):
                    print(id)
                    connection_name = "admission_" + str(found_list[0]) + ".db"
                    print(connection_name)
                    connection = sqlite3.connect(connection_name)
                    cursor = connection.cursor()
                    xcude = admissions_standard_dict[str(found_list[1])]
                    print(xcude)
                    toprint = f"select * FROM {xcude} where Rollno=?"
                    print(toprint)
                    try:
                        cursor.execute(toprint, (id,))
                        row = cursor.fetchone()
                        print(row)
                        print(1)
                    except Error as e:
                        print(e)
                        row = e

                    return row
                    connection.close()
                    cursor.close()

                data_tuple = printgiven(unique_id)
                print(data_tuple)
                admissions_root = Toplevel()
                admissions_root.geometry("496x545")
                admissions_root.resizable(0, 0)
                admissions_root.title("Update Data")
                admissions_root.iconbitmap(favicon)
                admissions_root.configure(background="#d3d3d3")
                admissions_standard_list = ["11 SCIENCE", "12 SCIENCE"]
                admissions_branch_list = ["Harni", "Karelibaug"]
                admissions_year_list = []
                for year in range(0, 79):
                    year_string = "20" + str(20 + year) + "-" + str(21 + year)
                    admissions_year_list.append(year_string)
                admissions_parent_relation_list = ["Mother", "Father", "Guardian"]

                # Admission prompt
                admissions_label = Label(admissions_root,
                                         text="Prompt for updating student data, fill in the details.",
                                         anchor=W,
                                         bg="#d3d3d3",
                                         fg="#585858",
                                         font=("Helevetica", 10))
                admissions_label.grid(row=0, column=0, columnspan=2, ipadx=78, pady=(15, 15))
                # Student details
                # Students first name
                admissions_firstname_label = Label(admissions_root,
                                                   text="Student's First Name:",
                                                   bg="#d3d3d3")
                admissions_firstname_label.grid(row=1, column=0, padx=10, sticky=W)
                firstname_var = StringVar()
                firstname_var.set(data_tuple[1])
                admissions_firstname_input = Entry(admissions_root,
                                                   width=30,
                                                   font=11,
                                                   bg="white",
                                                   borderwidth=0,
                                                   textvariable=firstname_var)
                admissions_firstname_input.grid(row=1, column=1, padx=15, sticky=W)
                # Student's last name
                admissions_lastname_label = Label(admissions_root,
                                                  text="Student's Last Name:",
                                                  bg="#d3d3d3")
                admissions_lastname_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
                lastname_var = StringVar()
                lastname_var.set(data_tuple[2])
                admissions_lastname_input = Entry(admissions_root,
                                                  width=30,
                                                  font=11,
                                                  bg="white",
                                                  borderwidth=0,
                                                  textvariable=lastname_var)
                admissions_lastname_input.grid(row=2, column=1, padx=15, pady=10, sticky=W)

                # Relation dropdown menu
                guardian_relation = StringVar()
                guardian_relation.set(data_tuple[3])
                admissions_guardian_relation_label = Label(admissions_root,
                                                           text="Guardian Relation:",
                                                           bg="#d3d3d3")
                admissions_guardian_relation_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
                admissions_relation_label = OptionMenu(admissions_root, guardian_relation, *admissions_parent_relation_list)
                admissions_relation_label.grid(row=3, column=1, padx=14, pady=10, sticky=W)

                # Guardian name input
                admissions_guardian_name_label = Label(admissions_root,
                                                       text=f"{guardian_relation.get()} Full Name:",
                                                       bg="#d3d3d3")
                admissions_guardian_name_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
                guardianname_var = StringVar()
                guardianname_var.set(data_tuple[4])
                admissions_guardian_name_input = Entry(admissions_root,
                                                       width=30,
                                                       font=11,
                                                       bg="white",
                                                       borderwidth=0,
                                                       textvariable=guardianname_var)
                admissions_guardian_name_input.grid(row=4, column=1, padx=15, pady=10, sticky=W)

                # Student Address
                admissions_student_address_label = Label(admissions_root,
                                                         text="Student Address:",
                                                         bg="#d3d3d3")
                admissions_student_address_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
                address_var = StringVar()
                address_var.set(data_tuple[5])
                admissions_student_address_input = Entry(admissions_root,
                                                         width=30,
                                                         font=11,
                                                         bg="white",
                                                         borderwidth=0,
                                                         textvariable=address_var)
                admissions_student_address_input.grid(row=5, column=1, padx=15, pady=10, sticky=W)

                # Admission year frame
                admissions_year_frame = Frame(admissions_root, height=8, width=39, bg="#d3d3d3")
                admissions_year_frame.grid(row=6, column=0)

                admissions_year = StringVar()
                admissions_year.set(found_list[0])
                admissions_year_label = Label(admissions_year_frame,
                                              text="Academic Year:",
                                              bg="#d3d3d3")
                admissions_year_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

                admissions_year_scroll = OptionMenu(admissions_year_frame,
                                                    admissions_year,
                                                    *admissions_year_list, )
                admissions_year_scroll.grid(row=0, column=1, sticky=W)

                # Standard frame
                admissions_standard_frame = Frame(admissions_root, height=8, width=25, bg="#d3d3d3")
                admissions_standard_frame.grid(row=6, column=1)
                admissions_standard_label = Label(admissions_standard_frame,
                                                  text="                              Standard:",
                                                  bg="#d3d3d3")
                admissions_standard_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)

                admissions_standard = StringVar()
                admissions_standard.set(found_list[1])

                admissions_standard_scroll = OptionMenu(admissions_standard_frame,
                                                        admissions_standard,
                                                        *admissions_standard_list)
                admissions_standard_scroll.grid(row=0, column=1, sticky=W)

                # Branch Frame
                admissions_branch_label = Label(admissions_root,
                                                text="Branch:",
                                                bg="#d3d3d3")
                admissions_branch_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)

                admissions_branch = StringVar()
                admissions_branch.set(data_tuple[8])

                admissions_branch_scroll = OptionMenu(admissions_root,
                                                      admissions_branch,
                                                      *admissions_branch_list)
                admissions_branch_scroll.grid(row=7, column=1, padx=14, pady=10, sticky=EW)

                # parents mobile number
                admissions_parent_number_label = Label(admissions_root,
                                                       text="Guardian Phone Number:",
                                                       bg="#d3d3d3")
                admissions_parent_number_label.grid(row=8, column=0, padx=10, pady=10, sticky=W)
                parent_var = IntVar()
                parent_var.set(data_tuple[9])
                admissions_parent_number_input = Entry(admissions_root,
                                                       width=30,
                                                       font=11,
                                                       bg="white",
                                                       borderwidth=0,
                                                       textvariable=parent_var)
                admissions_parent_number_input.grid(row=8, column=1, padx=15, pady=10, sticky=W)

                # Student phone Number
                admissions_student_number_label = Label(admissions_root,
                                                        text="Student Phone Number:",
                                                        bg="#d3d3d3")
                admissions_student_number_label.grid(row=9, column=0, padx=10, pady=10, sticky=W)
                student_var = IntVar()
                student_var.set(data_tuple[10])
                admissions_student_number_input = Entry(admissions_root,
                                                        width=30,
                                                        font=11,
                                                        bg="white",
                                                        borderwidth=0,
                                                        textvariable=student_var)
                admissions_student_number_input.grid(row=9, column=1, padx=15, pady=10, sticky=W)

                # Guardian email address
                admissions_guardian_email_label = Label(admissions_root,
                                                        text="Guardian Email Address:",
                                                        bg="#d3d3d3")
                admissions_guardian_email_label.grid(row=10, column=0, padx=10, pady=10, sticky=W)
                parent_mail_var = StringVar()
                parent_mail_var.set(data_tuple[11])
                admissions_guardian_email_input = Entry(admissions_root,
                                                        width=30,
                                                        font=11,
                                                        bg="white",
                                                        borderwidth=0,
                                                        textvariable=parent_mail_var)
                admissions_guardian_email_input.grid(row=10, column=1, padx=15, pady=10, sticky=W)

                # Student email address
                admissions_student_email_label = Label(admissions_root,
                                                       text="Student Email Address:",
                                                       bg="#d3d3d3")
                admissions_student_email_label.grid(row=11, column=0, padx=10, pady=10, sticky=W)
                student_mail_var = StringVar()
                student_mail_var.set(data_tuple[12])
                admissions_student_email_input = Entry(admissions_root,
                                                       width=30,
                                                       font=11,
                                                       bg="white",
                                                       borderwidth=0,
                                                       textvariable=student_mail_var)
                admissions_student_email_input.grid(row=11, column=1, padx=15, pady=10, sticky=W)


                # Submit button
                def okay_function():
                    access_data_root.destroy()
                    admissions_root.destroy()
                okay_button = Button(admissions_root,
                                     text="Okay",
                                     width=25,
                                     borderwidth=0,
                                     font=("Helvetica", 9),
                                     bg="#45b4e7",
                                     fg="white",
                                     activeforeground="white",
                                     activebackground="#1ca0dd",
                                     command=okay_function)
                okay_button.grid(row=12, column=0, padx=(14, 0), pady=10, sticky=W)



        access_data_button = Button(access_data_root,
                                    text="Enter",
                                    font=("Helvetica", 10),
                                    width=15,
                                    borderwidth=0,
                                    bg="#45b4e7",
                                    fg="white",
                                    activeforeground="white",
                                    activebackground="#1ca0dd",
                                    command=access_data)
        access_data_button.grid(row=2, columnspan=2, padx=(15, 0), pady=(5, 0))

    one_proceed_button = Button(option_frame_1,
                                    text="See One",
                                    font=("Helvetica", 10),
                                    width=12,
                                    borderwidth=0,
                                    bg="#45b4e7",
                                    fg="white",
                                    activeforeground="white",
                                    activebackground="#1ca0dd",
                                    command=access_data_function_for_one)
    one_proceed_button.grid(row=1, rowspan=2, column=3, sticky=E, padx=(0, 10))
    option_frame_2 = Frame(data_access_top, bg="#bababa", height=100, width=340)
    option_frame_2.pack(side="top", fill="both", expand=True, pady=(0, 5), padx=5)
    option_frame_2.propagate(False)
    empty_label = Label(option_frame_2, bg="#bababa", width=32)
    empty_label.grid(row=0, columnspan=3)
    send_batch_label = Label(option_frame_2, text="See Batch", font=("Helvetica", 18, "italic"), fg="#585858", bg="#bababa")
    send_batch_label.grid(row=1, column=0, columnspan=2, padx=(10, 0), sticky=W)
    send_batch_instruction = Label(option_frame_2, text="See data of whole class.", font=("Helvetica", 9), fg="#585858", bg="#bababa")
    send_batch_instruction.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky=W)

    all_proceed_button = Button(option_frame_2, text="See Batch",
                                font=("Helvetica", 10),
                                width=12,
                                borderwidth=0,
                                bg="#45b4e7",
                                fg="white",
                                activeforeground="white",
                                activebackground="#1ca0dd")
    all_proceed_button.grid(row=1, rowspan=2, column=3, sticky=E, padx=(0, 10))