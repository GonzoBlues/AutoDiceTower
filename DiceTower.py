#random is imported to simulate a dice roll during the early
#stages of development, before computer vision is implemented.
#At later and complete stages random will be replaced by the library we use for CV.
import random

#This class runs the back end for the GUI.
class DiceTower:
        def __init__(self, DiceType="D4", AttackMod=0, DamageMod=0, NatAttack=1, NatDamage=1):
                self.DiceType = DiceType
                self.AttackMod = AttackMod
                self.DamageMod = DamageMod
                self.NatAttack = NatAttack
                self.NatDamage = NatDamage
                self.AttackRoll = 1
                self.DamageRoll = 1
        
        @property
        def DiceType(self):
                return self._DiceType

        @DiceType.setter
        def DiceType(self, Dice):
                if Dice == "D4":
                        self._DiceType = 4
                elif Dice == "D6":
                        self._DiceType = 6
                elif Dice == "D8":
                        self._DiceType = 8
                elif Dice == "D10":
                        self._DiceType = 10
                elif Dice == "D12":
                        self._DiceType = 12
                else:
                        self._DiceType = 4
        
        @property
        def AttackMod(self):
                return self._AttackMod

        @AttackMod.setter
        def AttackMod(self, Mod):
                if Mod > 20:
                        self._AttackMod = -20
                elif Mod < -20:
                        self._AttackMod = 20
                else:
                        self._AttackMod = Mod
        
        @property
        def DamageMod(self):
                return self._DamageMod
        
        @DamageMod.setter
        def DamageMod(self, Mod):
                if Mod > 20:
                        self._DamageMod = -20
                elif Mod < -20:
                        self._DamageMod = 20
                else:
                        self._DamageMod = Mod

        @property
        def NatDamage(self):
                return self._NatDamage

        @NatDamage.setter
        def NatDamage(self, Damage):
                self._NatDamage = Damage
        
        @property
        def NatAttack(self):
                return self._NatAttack
        
        @NatAttack.setter
        def NatAttack(self, Attack):
                self._NatAttack = Attack
        
        @property
        def AttackRoll(self):
                return self._AttackRoll
        
        @AttackRoll.setter
        def AttackRoll(self, Attack):
                self._AttackRoll = Attack
        
        @property
        def DamageRoll(self):
                return self._DamageRoll
        
        @DamageRoll.setter
        def DamageRoll(self, Damage):
                self._DamageRoll = Damage
        
        def GetRoll(self):
                self.NatAttack = random.randint(1,21)
                self.NatDamage = random.randint(1,self.DiceType)
                self.AttackRoll = self.NatAttack + self.AttackMod
                self.DamageRoll = self.NatDamage + self.DamageMod
        
        def AddAtckMod(self):
                self.AttackMod += 1
        
        def SubAtckMod(self):
                self.AttackMod -= 1
        
        def AddDamMod(self):
                self.DamageMod += 1
        
        def SubDamMod(self):
                self.DamageMod -= 1

        def ChangeDiceType(self, type):
                self.DiceType = type
        
        def __str__(self):
                return ("DT:{}\tAM:{}\tDM:{}\tNA:{}\tND:{}\tAR:{}\tDR:{}".format(self.DiceType,self.AttackMod,self.DamageMod,self.NatAttack,self.NatDamage,self.AttackRoll,self.DamageRoll))

#Code pass this point just test the class and makes the code usable in text input form.
g1 = DiceTower()
while True:
        print("AM:{}".format(g1.AttackMod))
        x = input("Up or Down: ")
        if x == "Up":
                g1.AddAtckMod()
                x = ""
        elif x == "Down":
                g1.SubAtckMod()
                x = ""
        else:
                x = ""
                pass
        print("DM:{}".format(g1.DamageMod))
        x = input("Up or Down: ")
        if x == "Up":
                g1.AddDamMod()
                x = ""
        elif x == "Down":
                g1.SubDamMod()
                x = ""
        else:
                x = ""
                pass
        x = input("Dice Type? D4-12: ")
        g1.ChangeDiceType(x)
        x = ""
        g1.GetRoll()
        print(g1)
        print("")
