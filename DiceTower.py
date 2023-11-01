#random is imported to simulate a dice roll during the early
#stages of development, before computer vision is implemented.
#At later and complete stages random will be replaced by the library we use for CV.
import random

#This class runs the back end for the GUI.
class DiceTower:
        def __init__(self, DiceType=0, AttackMod=0, DamageMod=0, NatAttack=1, NatDamage=1):
                self.DiceType = DiceType
                self.AttackMod = AttackMod
                self.DamageMod = DamageMod
                self.NatAttack = NatAttack
                self.NatDamage = NatDamage
                self.AttackRoll = 1
                self.DamageRoll = 1
                self.DiceNum = [4,6,8,10,12]
        
        @property
        def DiceType(self):
                return self._DiceType

        @DiceType.setter
        def DiceType(self, x):
                self._DiceType = x
        
        @property
        def AttackMod(self):
                return self._AttackMod

        @AttackMod.setter
        def AttackMod(self, Mod):
                self._AttackMod = Mod
        
        @property
        def DamageMod(self):
                return self._DamageMod
        
        @DamageMod.setter
        def DamageMod(self, Mod):
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
        def DamageRoll(self, x = 0):
                if x < 0:
                        self._DamageRoll = 0
                else:
                        self._DamageRoll = x
        
        def GetRoll(self):
                self.NatAttack = random.randint(1,21)
                self.NatDamage = random.randint(1,self.DiceNum[self.DiceType])
                self.AttackRoll = self.NatAttack + self.AttackMod
                self.DamageRoll = self.NatDamage + self.DamageMod

        def IncDamDie(self):
                self.DiceType += 1
                x = self.DiceType
                if x > 4:
                        self.DiceType = 0

        def DeIncDamDie(self):
                self.DiceType -= 1
                x = self.DiceType
                if x < 0:
                        self.DiceType = 4
        
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
                return ("Nat Attack: {}\n\nNat Damage: {}\n\nAttack Roll: {}\n\nDamage Roll: {}".format(self.NatAttack,self.NatDamage,self.AttackRoll,self.DamageRoll))
'''
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
'''
