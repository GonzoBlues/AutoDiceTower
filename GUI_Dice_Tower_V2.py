import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{480}x{800}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=110, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1)

        #Side bar buttons

        #Dicetype
        self.dicetypedec = customtkinter.CTkButton(
            self.sidebar_frame,
            command=self.DiceTypeDecButton,
            text="<",
            width=50,
            height=20,
            font=("Times",-50)
            )
        self.dicetypedec.grid(row=2,column=1, padx=10,pady=0)
        self.dicetypeinc = customtkinter.CTkButton(
            self.sidebar_frame,
            command=self.DiceTypeIncButton,
            text=">",
            width=50,
            height=20,
            font=("Times",-50)
            )
        self.dicetypeinc.grid(row=2,column=3, padx=10,pady=0)

        #Attackmod
        self.AttackModdec = customtkinter.CTkButton(
            self.sidebar_frame,
            command=self.AttackModDecButton,
            text="<",
            width=50,
            height=20,
            font=("Times",-50)
            )
        self.AttackModdec.grid(row=4,column=1, padx=10,pady=0)
        self.AttackModinc = customtkinter.CTkButton(
            self.sidebar_frame,
            command=self.AttackModIncButton,
            text=">",
            width=50,
            height=20,
            font=("Times",-50)
            )
        self.AttackModinc.grid(row=4,column=3, padx=10,pady=0)

        #Damagemod
        self.DamageModdec = customtkinter.CTkButton(
            self.sidebar_frame,
            command=self.DamageModDecButton,
            text="<",
            width=50,
            height=20,
            font=("Times",-50),
            anchor="e"
            )
        self.DamageModdec.grid(row=6,column=1, padx=10,pady=0)
        self.DammafeModinc = customtkinter.CTkButton(
            self.sidebar_frame,
            command=self.DamageModIncButton,
            text=">",
            width=50,
            height=20,
            font=("Times",-50),
            anchor="w"
            )
        self.DammafeModinc.grid(row=6,column=3, padx=10,pady=0)

        #sidebartext
        #spacers
        self.spacerLable = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="",
            )
        self.spacerLable.grid(row=0,column=0,pady=20)
        self.spacerLeftSideLable = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="",
            )
        self.spacerLeftSideLable.grid(row=0,column=4,padx=10,rowspan=6)
        self.spacerRightSideLable = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="",
            )
        self.spacerRightSideLable.grid(row=0,column=0,padx=10,rowspan=6)
        #dicetype
        self.DiceTypeLable = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="Damage Dice",
            anchor="s",
            font=("Times",-30)
            )
        self.DiceTypeLable.grid(row=1,column=1,pady=0,columnspan=3)

        #Attack modifer
        self.AttackModLable = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="Attack Modifer",
            anchor="s",
            font=("Times",-30)
            )
        self.AttackModLable.grid(row=3,column=1,pady=0,columnspan=3)

        #Damage modifer
        self.DamageModLable = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="Damage Modifer",
            anchor="s",
            font=("Times",-30)
            )
        self.DamageModLable.grid(row=5,column=1,pady=0,columnspan=3)  
        dicetypeVAL="D4"
        #numbers for the 3 Values
        self.dicetypeValLable = customtkinter.CTkLabel(
            self.sidebar_frame,
            text=dicetypeVAL,
            font=("Times",-30)
        )
        self.dicetypeValLable.grid(row=2,column=2)
        # set default values

        #Button commands
    def DiceTypeIncButton(slef):
        print("DiceTypeInc")
        #work on this next
        ##



        ##
    def DiceTypeDecButton(slef):
        print("DiceTypeDec")
    def AttackModIncButton(slef):
        print("AttackModInc")
    def AttackModDecButton(slef):
        print("AttackModDec")
    def DamageModIncButton(self):
        print("DamageModInc")
    def DamageModDecButton(self):
        print("DamageModDec")

if __name__ == "__main__":
    app = App()
    app.mainloop()