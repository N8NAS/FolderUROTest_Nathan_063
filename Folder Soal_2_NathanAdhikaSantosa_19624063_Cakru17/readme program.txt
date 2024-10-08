ikuti #___1___# - #___n___# sehingga mengetahui alur program (mulai dari bawah)
# # sebagai penjelasan dari alur program
@@@ sebagai penjelasan diluar alur program


import random @@@ import module random sehingga dapat menggunakna random.randint()

class Robot:
    def __init__(self, name, health, damage1, damage2): @@@ untuk menyimpan data robot yang dibuat oleh user
        self.name = name
        self.health = health
        self.damage1 = damage1
        self.damage2 = damage2
    def attack(self, other): @@@ jika terpanggil maka
        damage = random.randint(self.damage1, self.damage2)

        @@@ yg menyerang memiliki damage random tergantung input batas atas dan bawah user

        other.health -= damage

        @@@ robot lain yang menyerang, healthnya akan berkurang sebesar damage robot yang menyerang

        print(f"{self.name} attacks {other.name} for {damage} damage!")

        @@@ print nama robot yang menyerang + attacks + nama robot lain + for + damage robot yang menyerang + damage!

        print(f"{other.name} has {other.health} health left")

        @@@ print nama robot lain + has + health robot lain + health left

class Battle:

    #___4___#

    def start_fight(self, robot1, robot2):
        # mendefinisikan self dengan parameter robot1 sebagai parameter robot 1 dan begitu juga dengan robot 2#

        self.robot1 = robot1
        self.robot2 = robot2

        # print apa yang di dalam ("")#

        print("We will start the fight by choosing which robot can have the first blow")
        print("The first robot gets head and the second robot gets tails")
        print("Referee, please toss the coin")

        # mendefinisikan variabel local i sebagai angka random 1 sampai 2#

        i = random.randint(1, 2)

        #jika mendapatkan i = 1 maka robot1 menyerang dulu #

        if i == 1:
            print("HEADS!!") #print teks di dalam#
            print(f"{robot1.name} gets the first blow") # print nama robot1 + gets the first blow#
            while robot1.health > 0 and robot2.health > 0 : # selama syarat terpenuhi maka fungsi di dalam akan bekerja terus #
                robot1.attack(robot2) #memanggil method attack di class Robot untuk menyerang robot2#
                if robot2.health > 0: #jika health robot2 tidak nol maka robot2 memanggil method dan class sama untuk menyerang robot1#
                    robot2.attack(robot1)
                    if robot1.health <= 0: #jika health robot1 nol maka akan print kode yang di bawah#
                        print(f"{robot1.name} is defeated")
                        print(f"{robot2.name} is the victor")
                else : # jika health robot 2 habis maka robot1 menang dan akan print yang di bawah#
                    print(f"{robot2.name} is defeated")
                    print(f"{robot1.name} is the victor")

        #hal yang terjadi di bawah ini sama namun robot2 dapat menyerang terlebih dahulu sehingga urutan robot1 dan robot2 dibalikan#

        else:
            print("TAILS!!")
            print(f"{robot2.name} gets the first blow")
            while robot2.health > 0 and robot1.health > 0 :
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

    def add_robot(self): #___3___#
        # nama1 hingga damage3_2 merupakan variabel dimana nilai variabel tergantung dengan input dari user.
        input yang diberi oleh user sesuai perintah yang diberi di dalam input(" "). Variabel dengan nama health dan
        damage di depannya, input dari user akan diubah tipenya dari string menjadi integer atau angka tanpa koma#
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

        # variabel-variabel dibawah ini memanggil class Robot dan parameternya di isi sesuai input user pada variabel-
        variable sebelumnya#
        RoboOne = Robot(nama1, health1, damage1_1, damage1_2)
        RoboTwo = Robot(nama2, health2, damage2_1, damage2_2)
        RoboThree = Robot(nama3, health3, damage3_1, damage3_2)

        # dibuat sebuah daftar nama robot, nama robotnya tergantung oleh input dari user. RoboOne.name berarti memanggil
        class Robot dengan memasukkan parameter lalu memanggil atribut nama yang di input oleh user.#
        list_of_robots = [RoboOne.name, RoboTwo.name, RoboThree.name]

        #print atau menampilkan daftar nama robot
        print(list_of_robots)

        #variabel dibawah meminta input dari user dalam bentuk angka(karena int(input("")) ), input tersebut meminta
        pilihan user dalam robot mana saja yang akan saling berkelahi
        robotsatu = int(input("Dari list ini, pilih satu dari dua yang akan saling berkelahi(pilih dengan angka urutan) : "))
        robotdua = int(input("Pilih robot kedua yang akan saling berkelahi(pilih dengan angka urutan) : "))

        #mendefinikasikan variabel war sebagai memanggil class Battle dengan self sebagai parameter #
        war = Battle()

        #if, elif(else if), dan else statement dibawah ini digunakan untuk mengubah input user di atas(robotsatu dan robot
        dua) yang berupa angka menjadi robot yang dipilih user (RoboOne/RoboTwo/RoboThree). Robot yang dipilih user dipakai
        sebagai parameter untuk method start_fight pada class Battle #
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

    def start_game(self): #___2___# method ini dipanggil #
        print("Selamat datang ke ROBOT CLASH!!!\n") # print apa yang terdapat di dalam " " #
        print("Di Robot Clash, anda dapat membuat robot sendiri dengan nama, health, dan attack damage unik") # print apa yang terdapat di dalam " " #
        print("Namun, jumlah robot yang dapat dibuat dibataskan pada tiga robot") # print apa yang terdapat di dalam " " #
        self.add_robot() # memanggil class Game atau self dan method add_robot() @

#___1___# varibel myGame mendefinisikan class Game dengan parameter self #
myGame = Game()
# memanggil class Game dan method #
myGame.start_game()