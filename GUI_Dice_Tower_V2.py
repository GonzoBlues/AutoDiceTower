import tkinter
import tkinter.messagebox
import customtkinter
from PIL import ImageTk, Image
import os

#changes directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    dicetypes=["D4","D6","D8","D10","D12"]
    currentDice = 0
    DiceTypeVAL="D4"
    DamageModVAL = 0
    AttackModVAL = 0



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

        #numbers for the 3 Values
        self.dicetypeValLable = customtkinter.CTkLabel(
            self.sidebar_frame,
            text=self.DiceTypeVAL,
            font=("Times",-30)
        )
        self.dicetypeValLable.grid(row=2,column=2)

        self.DamageModValLable = customtkinter.CTkLabel(
            self.sidebar_frame,
            text=self.DamageModVAL,
            font=("Times",-30)
        )
        self.DamageModValLable.grid(row=6,column=2)

        self.AttackModValLable = customtkinter.CTkLabel(
            self.sidebar_frame,
            text=self.AttackModVAL,
            font=("Times",-30)
        )
        self.AttackModValLable.grid(row=4,column=2)

        #Dice Image
        DiceTypeImage = customtkinter.CTkImage(light_image=Image.open(os.path.join("D4.png")), size=(60 , 60))
        self.DiceTypeImageLable = customtkinter.CTkLabel(self.sidebar_frame,image=DiceTypeImage, text='')
        self.DiceTypeImageLable.grid(column=4, row=2,pady=10,padx=10,)

        
        # set default values

        #Button commands
    def DiceTypeIncButton(self):
        if (self.currentDice) >= 4:
            self.currentDice = 0
        else:
            self.currentDice += 1
        self.dicetypeValLable.configure(text=(self.dicetypes[self.currentDice]))

    def DiceTypeDecButton(self):
        if (self.currentDice) <= 0:
            self.currentDice = 4
        else:
            self.currentDice -= 1
        self.dicetypeValLable.configure(text=(self.dicetypes[self.currentDice]))


    def AttackModIncButton(self):
        self.AttackModVAL += 1
        if self.AttackModVAL > 0:
            self.AttackModValLable.configure(text="+" + str(self.AttackModVAL))
        else:
            self.AttackModValLable.configure(text=self.AttackModVAL)

    def AttackModDecButton(self):
        self.AttackModVAL -= 1
        if self.AttackModVAL > 0:
            self.AttackModValLable.configure(text="+" + str(self.AttackModVAL))
        else:
            self.AttackModValLable.configure(text=self.AttackModVAL)


    def DamageModIncButton(self):
        self.DamageModVAL += 1
        if self.DamageModVAL > 0:
            self.DamageModValLable.configure(text="+" + str(self.DamageModVAL))
        else:
            self.DamageModValLable.configure(text=self.DamageModVAL)

    def DamageModDecButton(self):
        self.DamageModVAL -= 1
        if self.DamageModVAL > 0:
            self.DamageModValLable.configure(text="+" + str(self.DamageModVAL))
        else:
            self.DamageModValLable.configure(text=self.DamageModVAL)

if __name__ == "__main__":
    app = App()
    app.mainloop()