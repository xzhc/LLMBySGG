"""
This case demonstrates procedural programming, functional programming, and object-oriented programming.
Prepare to cook the following 3 dishes, and describe the cooking process of each dish through the program.
Northeast Chinese jelly Noodles (Dongbei DAlan pi)
Northeast Stew (Dongbei Daluan Dun)
Crispy Pork (Xiao Su Rou)
"""

#Object-oriented programming
class Dish:
    def __init__(self, name):
        self.name = name
    def wash(self, ingredient):
        print(f"{self.name}: wash {ingredient}")
    def cut(self, ingredient):
        print(f"{self.name}: cut {ingredient}")
    def mix(self, *ingredients):
        print(f"{self.name}: mix {ingredients}")
    def stew(self, *ingredients):
        print(f"{self.name}: stew {ingredients}")
    def fry(self, ingredient):
        print(f"{self.name}: fry {ingredient}")
    def serve(self):
        print(f"{self.name}: serve the fish")

dlp = Dish('Northeast Chinese Jelly Noodles (Dongbei Dala pi)')

dlp.wash("cucumber")
dlp.wash(('Jelly noodles'))
dlp.cut('cucumber')
dlp.mix('cucumber', 'Jelly noodles', 'seasoning')
dlp.serve()

"""
Functional programming approach
def northeast_chinese_jelly_noodles(func):
    wash("cucumber")
    wash("jelly noodles")
    cut("cucumber")
    mix("cucumber", "jelly noodles", "seasoning")
    serve("Northeast Chinese Jelly Noodles (Dongbei Dala Pi)")

def northeast_stew():
    wash("cabbage")
    wash("cowpea")
    wash("potato")
    cut("meat")
    stew("cabbage", "potato", "cowpea", "meat", "corn", "vermicelli", "seasoning")
    serve("Northeast Stew (Dongbei Dalun Dun)")
    
    def crispy_pork():
    wash("meat")
    cut("meat")
    mix("meat", "starch")
    fry("meat")
    serve("Crispy Pork (Xiao Su Rou)")
    print("~" * 30)
    
northeast_chinese_jelly_noodles()
northeast_stew()
crispy_pork()
"""

"""
Procedural programming approach
    Suitable for simple processes and steps, not ideal for complex business logic
# Northeast Chinese Jelly Noodles (Dongbei Dala Pi)
wash("cucumber")
wash("jelly noodles")
cut("cucumber")
mix("cucumber", "jelly noodles", "seasoning")
serve("Northeast Chinese Jelly Noodles (Dongbei Dala Pi)")
print("~"*30)
# Northeast Stew (Dongbei Dalun Dun)
wash("cabbage")
wash("cowpea")
wash("potato")
cut("meat")
stew("cabbage", "potato", "cowpea", "meat", "corn", "vermicelli", "seasoning")
serve("Northeast Stew (Dongbei Dalun Dun)")
print("~"*30)
# Crispy Pork (Xiao Su Rou)
wash("meat")
cut("meat")
mix("meat", "starch")
fry("meat")
serve("Crispy Pork (Xiao Su Rou)")
print("~"*30)
"""