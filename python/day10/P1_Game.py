"""
This cade demonstrates the Angry Birds game with class inheritance
"""

class Birds:
    def __init__(self, name, color, skill_description):
        self.name = name
        self.color = color
        self.skill_description = skill_description
        
    def fly(self):
        pass
    def catch(self):
        pass
    def use_skill(self):
        print(f'{self.name} uses skill: {self.skill_description}')
        
        
class RedBirds(Birds):
    def __init__(self):
        super().__init__('Red Bird', 'Red', 'Collides with obstackles ahead, inflicting massive damage.')

    def fly(self):
        print(f'{self.name} flies forward at a steady speed.')

    def call(self):
        print(f'{self.name} buzzes loudly.')

class BlueBirds(Birds):
    def __init__(self):
        super().__init__('Blue Bird', 'Blue', 'Splits into three birds to attack dispersedly.')

    def fly(self):
        print(f'{self.name} flies forward gracefully......')

    def call(self):
        print(f"{self.name} chirps chattering")

class YellowBirds(Birds):
    def __init__(self):
        super().__init__('Yellow Bird', 'Yellow', 'Accelerates rapidly to pierce through obstacles.')

    def fly(self):
        print(f'{self.name} speeds forward like a lightning bolt!')

    def call(self):
        print(f'{self.name} lets out a sharp whistle!')

class Obstacle:
    """Obstacle class"""
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def be_attacked(self, bird):
        print(f'{bird.name} launches an attack on {self.name}!')
        bird.use_skill()

        #Assign damage valuses to obstacles based on different bird type
        if isinstance(bird, RedBirds):
            damage = 80
        elif isinstance(bird, BlueBirds):
            damage = 50
        else:
            damage = 30 * 3

        #Substract the corresponding damage from the obstacle's strength
        self.strength -=damage
        if self.strength <= 0:
            print(f'{self.name} has been destroyed!')
        else:
            print(f'{self.name} has {self.strength} strength remaining.')

# Create bird objects
red_bird = RedBirds()
blue_bird = BlueBirds()
yellow_bird = YellowBirds()
# Create obstacle objects
o1 = Obstacle('Wooden Box', 100)
o2 = Obstacle('Stone Wall', 150)

o1.be_attacked(blue_bird)
o1.be_attacked(yellow_bird)
o2.be_attacked(red_bird)