from tkinter import *
favicon = "favicon.ico"
def contact():
    contact_form_toplevel = Toplevel()
    contact_form_toplevel.iconbitmap(favicon)
    contact_form_toplevel.title("Hello!")
    contact_form_toplevel.geometry("300x540")
    contact_form_toplevel.resizable(0, 0)
    contact_form_toplevel.configure(bg="#d3d3d3")
    fcolo = "#f08080"
    contact_frame = Frame(contact_form_toplevel, height=520, width=280, bg=fcolo)
    contact_frame.pack(padx=10, pady=10, fill="both", expand=True)
    contact_frame.pack_propagate(False)

    contact_label = Label(contact_frame, text="Contact Us", font=("Helvetica", 20, "bold underline"), fg="white", bg=fcolo)
    contact_label.pack(padx=10, pady=(10, 5))

    contact_para = Label(contact_frame,
                         text="e-mail:\nsupport@aexior.com\n\nCall: \n+91 8320 53 9455 \n\nor DM us on Instagram: \n\n@aexior",
                         font=("Helvetica", 13),
                         fg="white",
                         bg=fcolo,
                         )
    contact_para.pack(padx=10)

    about_label = Label(contact_frame, text="About", font=("Helvetica", 20, "bold underline"), fg="white", bg=fcolo)
    about_label.pack(padx=10, pady=(10, 5))

    about_para = Label(contact_frame,
                       text="This is a licensed distribution of the markOS\nversion 2.0 solely developed and \ndistributed by the Aexior.\nAexior holds the copyrights to all the versions \nand distributions of markOS™ and \nSideView™ programs and the namesake.\n\nLicense Key: TYD-798-BNS\n\n\nCopyright © 2020 Aexior. All rights reserved.",
                       font=("Helvetica", 10),
                       fg="white",
                       bg=fcolo,
                       )
    about_para.pack(padx=10)

    def more_on_us():
        more_toplevel = Toplevel(contact_form_toplevel)
        more_toplevel.geometry("300x300")
        more_toplevel.configure(bg="#d3d3d3")
        about_frame = Frame(more_toplevel, height=280, width=280, bg="#f0cb80")
        about_frame.pack(padx=10, pady=10, fill="both", expand=True)
        about_frame.pack_propagate(False)



    more_about_us_button = Button(contact_frame,
                                  text="Learn more about Aexior",
                                  fg="#f0cb80",
                                  bg="#eb5e5e",
                                  font=("Helvetica", 10),
                                  borderwidth=0,
                                  activebackground="#e73b3b",
                                  activeforeground="#f0cb80",
                                  command=more_on_us)
    more_about_us_button.pack(pady=(15,0))



