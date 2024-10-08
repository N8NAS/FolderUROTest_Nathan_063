import random

class Robot:
    def __init__(self, name, health, damage1, damage2):
        self.name = name
        self.health = health
        self.damage1 = damage1
        self.damage2 = damage2
    def attack(self, other):
        attack_damage = random.randint(self.damage1, self.damage2)
        other.health -= attack_damage
        print(f"{self.name} attacks {other.name} for {attack_damage} damage!")
        print(f"{other.name} has {other.health} health left\n")

class Battle:
    def start_fight(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        print("We will start the fight by choosing which robot can have the first blow")
        print("The first robot gets head and the second robot gets tails")
        print("Referee, please toss the coin")
        i = random.randint(1, 2)
        if i == 1:
            print("HEADS!!")
            print(f"{robot1.name} gets the first blow")
            while robot1.health > 0 and robot2.health > 0 :
                robot1.attack(robot2)
                if robot2.health > 0:
                    robot2.attack(robot1)
                    if robot1.health <= 0:
                        print(f"{robot1.name} is defeated")
                        print(f"{robot2.name} is the victor")
                else :
                    print(f"{robot2.name} is defeated")
                    print(f"{robot1.name} is the victor")
        else:
            print("TAILS!!")
            print(f"{robot2.name} gets the first blow")
            while robot1.health > 0 and robot2.health > 0 :
                robot2.attack(robot1)
                if robot1.health > 0 :
                    robot1.attack(robot2)
                    if robot2.health <= 0 :
                        print(f"{robot2.name} is defeated")
                        print(f"{robot1.name} is the victor")
                else :
                    print(f"{robot1.name} is defeated")
                    print(f"{robot2.name} is the victor")



class Game:

    def add_robot(self):
        nama1 = input("Berikan nama untuk robot pertama : ")
        health1 = int(input("Berikan health point untuk robot pertamamu : "))
        damage1_1 = int(input("Berikan batas bawah attack damage : "))
        damage1_2 = int(input("Berikan batas atas attack damage : "))
        nama2 = input("Berikan nama untuk robot kedua : ")
        health2 = int(input("Berikan health point untuk robot keduamu : "))
        damage2_1 = int(input("Berikan batas bawah attack damage : "))
        damage2_2 = int(input("Berikan batas atas attack damage : "))
        nama3 = input("Berikan nama untuk robot ketiga : ")
        health3 = int(input("Berikan health point untuk robot ketigamu : "))
        damage3_1 = int(input("Berikan batas bawah attack damage : "))
        damage3_2 = int(input("Berikan batas atas attack damage : "))
        RoboOne = Robot(nama1, health1, damage1_1, damage1_2)
        RoboTwo = Robot(nama2, health2, damage2_1, damage2_2)
        RoboThree = Robot(nama3, health3, damage3_1, damage3_2)
        list_of_robots = [RoboOne.name, RoboTwo.name, RoboThree.name]
        print(list_of_robots)
        robotsatu = int(input("Dari list ini, pilih satu dari dua yang akan saling berkelahi(pilih dengan angka urutan) : "))
        robotdua = int(input("Pilih robot kedua yang akan saling berkelahi(pilih dengan angka urutan) : "))
        war = Battle()
        if robotsatu == 1 and robotdua == 1 :
            war.start_fight(RoboOne, RoboOne)
        elif robotsatu == 1 and robotdua == 2 :
            war.start_fight(RoboOne, RoboTwo)
        elif robotsatu == 1 and robotdua == 3:
            war.start_fight(RoboOne, RoboThree)
        elif robotsatu == 2 and robotdua ==1:
            war.start_fight(RoboTwo, RoboOne)
        elif robotsatu == 2 and robotdua == 2:
            war.start_fight(RoboTwo, RoboTwo)
        elif robotsatu == 2 and robotdua == 3:
            war.start_fight(RoboTwo, RoboThree)
        elif robotsatu == 3 and robotdua == 1:
            war.start_fight(RoboThree, RoboOne)
        elif robotsatu == 3 and robotdua == 2:
            war.start_fight(RoboThree, RoboTwo)
        else:
            war.start_fight(RoboThree, RoboThree)
    def start_game(self):
        print("Selamat datang ke ROBOT CLASH!!!\n")
        print("Di Robot Clash, anda dapat membuat robot sendiri dengan nama, health, dan attack damage unik")
        print("Namun, jumlah robot yang dapat dibuat dibataskan pada tiga robot")
        self.add_robot()

myGame = Game()
myGame.start_game()