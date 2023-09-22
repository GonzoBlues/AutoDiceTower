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

    #photos Import
    DiceTypeImageD4 = customtkinter.CTkImage(light_image=Image.open(os.path.join("D4.png")), size=(60 , 60))
    DiceTypeImageD6 = customtkinter.CTkImage(light_image=Image.open(os.path.join("D6.png")), size=(60 , 60))
    DiceTypeImageD8 = customtkinter.CTkImage(light_image=Image.open(os.path.join("D8.png")), size=(60 , 60))
    DiceTypeImageD10 = customtkinter.CTkImage(light_image=Image.open(os.path.join("D10.png")), size=(60 , 60))
    DiceTypeImageD12 = customtkinter.CTkImage(light_image=Image.open(os.path.join("D12.png")), size=(60 , 60))

    #Dice Dic
    dice_image_dic = {"D4":DiceTypeImageD4,"D6": DiceTypeImageD6,"D8": DiceTypeImageD8,"D10": DiceTypeImageD10,"D12": DiceTypeImageD12}


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
        self.sidebarFrame = customtkinter.CTkFrame(self, width=110, corner_radius=0)
        self.sidebarFrame.grid(row=0, column=0, rowspan=7, sticky="nsew")
        self.sidebarFrame.grid_rowconfigure(7, weight=1)

        #creat Title Bar
        self.TitleBar = customtkinter.CTkFrame(self, height= 70,width=480,fg_color="black",corner_radius=0)
        self.TitleBar.grid(row=0,column = 0,columnspan = 7,sticky ="n")
        self.TitleBarLable = customtkinter.CTkLabel(self.TitleBar,text_color= "Blue",text ="Auto Dice Tower",height=70,width=480,font=("Times",-60))
        self.TitleBarLable.grid(row=0,column = 0,columnspan = 7,sticky ="n")
        #Side bar buttons

        #Dicetype
        self.dicetypedec = customtkinter.CTkButton(
            self.sidebarFrame,
            command=self.DiceTypeDecButton,
            text="<",
            width=50,
            height=20,
            font=("Times",-50)
            )
        self.dicetypedec.grid(row=2,column=1, padx=10,pady=0)
        self.dicetypeinc = customtkinter.CTkButton(
            self.sidebarFrame,
            command=self.DiceTypeIncButton,
            text=">",
            width=50,
            height=20,
            font=("Times",-50)
            )
        self.dicetypeinc.grid(row=2,column=3, padx=10,pady=0)

        #Attackmod
        self.AttackModdec = customtkinter.CTkButton(
            self.sidebarFrame,
            command=self.AttackModDecButton,
            text="<",
            width=50,
            height=20,
            font=("Times",-50)
            )
        self.AttackModdec.grid(row=4,column=1, padx=10,pady=0)
        self.AttackModinc = customtkinter.CTkButton(
            self.sidebarFrame,
            command=self.AttackModIncButton,
            text=">",
            width=50,
            height=20,
            font=("Times",-50)
            )
        self.AttackModinc.grid(row=4,column=3, padx=10,pady=0)

        #Damagemod
        self.DamageModdec = customtkinter.CTkButton(
            self.sidebarFrame,
            command=self.DamageModDecButton,
            text="<",
            width=50,
            height=20,
            font=("Times",-50),
            anchor="e"
            )
        self.DamageModdec.grid(row=6,column=1, padx=10,pady=0)
        self.DammafeModinc = customtkinter.CTkButton(
            self.sidebarFrame,
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
            self.sidebarFrame,
            text="",
            )
        self.spacerLable.grid(row=0,column=0,pady=20)
        self.spacerLeftSideLable = customtkinter.CTkLabel(
            self.sidebarFrame,
            text="",
            )
        self.spacerLeftSideLable.grid(row=0,column=4,padx=10,rowspan=6)
        self.spacerRightSideLable = customtkinter.CTkLabel(
            self.sidebarFrame,
            text="",
            )
        self.spacerRightSideLable.grid(row=0,column=0,padx=10,rowspan=6)
        #dicetype
        self.DiceTypeLable = customtkinter.CTkLabel(
            self.sidebarFrame,
            text="Damage Dice",
            anchor="s",
            font=("Times",-30)
            )
        self.DiceTypeLable.grid(row=1,column=1,pady=0,columnspan=3)

        #Attack modifer
        self.AttackModLable = customtkinter.CTkLabel(
            self.sidebarFrame,
            text="Attack Modifer",
            anchor="s",
            font=("Times",-30)
            )
        self.AttackModLable.grid(row=3,column=1,pady=0,columnspan=3)

        #Damage modifer
        self.DamageModLable = customtkinter.CTkLabel(
            self.sidebarFrame,
            text="Damage Modifer",
            anchor="s",
            font=("Times",-30)
            )
        self.DamageModLable.grid(row=5,column=1,pady=0,columnspan=3)  

        #numbers for the 3 Values
        self.dicetypeValLable = customtkinter.CTkLabel(
            self.sidebarFrame,
            text=self.DiceTypeVAL,
            font=("Times",-30)
        )
        self.dicetypeValLable.grid(row=2,column=2)

        self.DamageModValLable = customtkinter.CTkLabel(
            self.sidebarFrame,
            text=self.DamageModVAL,
            font=("Times",-30)
        )
        self.DamageModValLable.grid(row=6,column=2)

        self.AttackModValLable = customtkinter.CTkLabel(
            self.sidebarFrame,
            text=self.AttackModVAL,
            font=("Times",-30)
        )
        self.AttackModValLable.grid(row=4,column=2)

        #Dice Image
        #Set Start
        self.DiceTypeImageLable = customtkinter.CTkLabel(self.sidebarFrame,image=self.DiceTypeImageD4, text='')
        self.DiceTypeImageLable.grid(column=4, row=2,pady=10,padx=10,)

        #Dice Changer
    def Change_diceimg(self,newDice):
            # Check if newDice is in the dictionary
        if newDice in self.dice_image_dic:
                # Configure diceImage_label with the corresponding image
            self.DiceTypeImageLable.configure(image=self.dice_image_dic[newDice])
        else:
            print("Error: Invalid dice type")
            self.DiceTypeImageLable.configure(image=self.DiceTypeImageD4)  # Fallback to D4 image
                    #Add an error image?
    
        #Button commands
    def DiceTypeIncButton(self):
        if (self.currentDice) >= 4:
            self.currentDice = 0
        else:
            self.currentDice += 1
        newdice = self.dicetypes[self.currentDice]
        self.dicetypeValLable.configure(text = (newdice))
        self.Change_diceimg(self.dicetypes[self.currentDice])

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