import pygame
import random
from pygame.locals import *
import copy
pygame.init()

click1 = pygame.mixer.Sound('./resources/click1-2.ogg')
click2 = pygame.mixer.Sound('./resources/click3.ogg')
click3 = pygame.mixer.Sound('./resources/select2.ogg')
music = pygame.mixer.Sound('./resources/redbattlemusic.ogg')
pikachu_cry = pygame.mixer.Sound('./resources/pikachu.ogg')
chespin_cry = pygame.mixer.Sound('./resources/chespin.ogg')
froakie_cry = pygame.mixer.Sound('./resources/froakie.ogg')
fennekin_cry = pygame.mixer.Sound('./resources/fennekin.ogg')


def update():
    pygame.display.update()

# SET UP GAME

battlebgimg = pygame.image.load('./resources/background2.png')
battlebgimgRect = battlebgimg.get_rect()
announcement_panel = pygame.image.load('./resources/announcementpanel.png')
announcement_panelRect = announcement_panel.get_rect()
announcement_panel.set_alpha(95)
arrow = pygame.image.load('./resources/arrow.png')
arrowRect = arrow.get_rect()

SCREEN_WIDTH = battlebgimg.get_width()
SCREEN_HEIGHT = 560


def wait():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_RETURN:
                click1.play()
                waiting = False

#COLORS
highlighter_color = (64, 64, 64)
basic_color = (0, 0, 0)
announcement_panel_color = (64, 64, 64)
text_color = (255, 255, 255)

pygame.display.set_caption('Ultimate Deathmatch')
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
screen.fill(basic_color)
screen.blit(battlebgimg, (0, 94))


# TEXT DISPLAY POSITIONS
## 26 btwn lines
left_margin = 15
right_margin = 470
topleft1 = (left_margin, 12)
topleft2 = (left_margin, 38)
topleft3 = (left_margin, 64)
topright1 = (right_margin, 12)
topright2 = (right_margin, 38)
topright3 = (right_margin, 64)
bottom1 = (left_margin, 416 + 34)
bottom2 = (left_margin, 442 + 34)
bottom3 = (left_margin, 468 + 34)
bottom4 = (left_margin, 494 + 34)
inpanel = (left_margin, (438 - 50) + 17)

def animate_attack(playerimg, enemyimg, user):
    if user == "player":
        for num in range(10):
            player.playerx += 10
            draw_scene(playerimg, enemyimg)
            update()
        for num in range(10):
            player.playerx -= 10
            draw_scene(playerimg, enemyimg)
            update()
        """
        for num in range(4):
            for num in range(100):
                enemyimg.set_alpha(100-num)
                draw_scene(playerimg, enemyimg)
                update()
            for num in range(100):
                enemyimg.set_alpha(num)
                draw_scene(playerimg, enemyimg)
                update()
        """
    else: # user = enemy
        for num in range(10):
            enemy.enemyx -= 10
            draw_scene(playerimg, enemyimg)
            update()
        for num in range(10):
            enemy.enemyx += 10
            draw_scene(playerimg, enemyimg)
            update()
        """
        for num in range(4):
            for num in range(100):
                playerimg.set_alpha(100-num)
                draw_scene(playerimg, enemyimg)
                update()
            for num in range(100):
                playerimg.set_alpha(num)
                draw_scene(playerimg, enemyimg)
                update()
        """
def draw_scene(playerimg, enemyimg):
    screen.blit(battlebgimg, (0, 94))
    screen.blit(playerimg, (player.playerx, player.y))
    screen.blit(enemyimg, (enemy.enemyx, enemy.y))
    clear_options_panel()

def draw_scene_no_enemy(playerimg):
    screen.blit(battlebgimg, (0, 94))
    screen.blit(playerimg, (player.playerx, player.y))
    clear_options_panel()

def draw_text(string, surface, place):
    font = pygame.font.SysFont('Arial', 20)
    text_display = font.render(string, 1, text_color)
    text_rect = text_display.get_rect()
    text_rect.topleft = place
    surface.blit(text_display, text_rect)

def announce(string):
    screen.blit(announcement_panel, (0, 388))
    draw_text(string, screen, inpanel)
    screen.blit(arrow, (665, 420))
    update()

def ask(string):
    screen.blit(announcement_panel, (0, 388))
    draw_text(string, screen, inpanel)
    update()

def update_statboard():
    clear_statboard()
    draw_text(player.capsname, screen, topleft1)
    draw_text(enemy.capsname, screen, topright1)
    draw_text("HP: " + str(player.hp) + "/" + str(player.mhp), screen, topleft2)
    draw_text("Status: " + str(player.status), screen, topleft3)
    draw_text("HP: " + str(enemy.hp) + "/" + str(enemy.mhp), screen, topright2)
    draw_text("Status: " + str(enemy.status), screen, topright3)
    update()

def clear_statboard():
    statboard = pygame.Rect(0, 0, 700, 94)
    pygame.draw.rect(screen, basic_color, statboard)

def display_options(option1, option2, option3, option4):
    draw_text(option1, screen, bottom1)
    draw_text(option2, screen, bottom2)
    draw_text(option3, screen, bottom3)
    draw_text(option4, screen, bottom4)

def clear_options_panel():
    options_panel = pygame.Rect(0, 438, SCREEN_WIDTH, 122)
    pygame.draw.rect(screen, basic_color, options_panel)

def update_options_panel(option1, option2, option3, option4, highlighted):
    clear_options_panel()
    highlight(highlighted)
    display_options(option1, option2, option3, option4)
    update()

# HIGHLIGHTER

hlx = 0
hly1 = 446
hly2 = 472
hly3 = 498
hly4 = 524
hlwidth = SCREEN_WIDTH
hlheight = 25

def highlight(pos):
    if pos == 1:
        highlighter = pygame.Rect(hlx, hly1, hlwidth, hlheight)
    elif pos == 2:
        highlighter = pygame.Rect(hlx, hly2, hlwidth, hlheight)
    elif pos == 3:
        highlighter = pygame.Rect(hlx, hly3, hlwidth, hlheight)

    elif pos == 4:
        highlighter = pygame.Rect(hlx, hly4, hlwidth, hlheight)
    pygame.draw.rect(screen, highlighter_color, highlighter)

def select():
    waiting = True
    select = False
    while waiting:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    click3.play()
                    select = True
                    waiting = False
                elif event.key == K_DOWN:
                    click2.play()
                    select = False
                    waiting = False
                elif event.key == K_UP:
                    click2.play()
                    select = False
                    waiting = False
    return select

def choose(option1, option2, option3, option4):
    highlighted = 1
    update_options_panel(option1, option2, option3, option4, highlighted)
    selected = select()
    while not selected:
        for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        if highlighted == 1:
                            highlighted = 2
                        elif highlighted == 2:
                            highlighted = 3
                        elif highlighted == 3:
                            highlighted = 4
                        elif highlighted == 4:
                            highlighted = 1
                        update_options_panel(option1, option2, option3, option4, highlighted)
                        selected = select()
                    elif event.key == K_UP:
                        if highlighted == 2:
                            highlighted = 1
                        elif highlighted == 3:
                            highlighted = 2
                        elif highlighted == 4:
                            highlighted = 3
                        elif highlighted == 1:
                            highlighted = 4
                        update_options_panel(option1, option2, option3, option4, highlighted)
                        selected = select()
    clear_options_panel()
    pygame.time.wait(500)
    return highlighted


#-----

# CLASSES

class Character:

    def __init__(self, title, name, capsname, mhp, atk, spatk, df, spdf, agil, focus, morale, status, attacks, greeting, taunt, playerx, enemyx, y, img_right, img_left, sound):
        self.title = title
        self.name = name
        self.capsname = capsname
        self.mhp = mhp
        self.hp = mhp
        self.atk = atk
        self.spatk = spatk
        self.df = df
        self.spdf = spdf
        self.agil = agil
        self.focus = focus
        self.morale = morale
        self.status = status
        self.attacks = attacks
        self.greeting = greeting
        self.taunt = taunt
        self.healthpotions = 2
        self.mysticalpotions = 1
        self.catposters = 1
        self.img_left = img_left
        self.img_right = img_right
        self.playerx = playerx
        self.enemyx = enemyx
        self.y = y
        self.sound = sound

    def attackprocedure(self, user, attack, player, enemy):

        if user == "player":
            opp_name = enemy.name
            opp_hp = enemy.hp
            opp_atk = enemy.atk
            opp_spatk = enemy.spatk
            opp_df = enemy.df
            opp_spdf = enemy.spdf
            opp_agil = enemy.agil
            opp_focus = enemy.focus
            opp_morale = enemy.morale
            opp_status = enemy.status

        else:   # user is enemy
            opp_name = player.name
            opp_hp = player.hp
            opp_atk = player.atk
            opp_spatk = player.spatk
            opp_df = player.df
            opp_spdf = player.spdf
            opp_agil = player.agil
            opp_focus = player.focus
            opp_morale = player.morale
            opp_status = player.status

        hesitate = self.check_morale(attack.name) # does low morale cause hesitation?
        if hesitate:
            return True # end turn if hesitant

        hindered = self.check_prestatus() # does status condition hinder character?
        if hindered:
            return True # end turn if hindered

        draw_scene(playerimg, enemyimg)
        announce(self.name + " used " + attack.name + "!")
        wait()

        if attack.pwr != 0: # if attack is damage dealing
            successval = random.randrange(0, 101) ## hit or miss?
            if successval > attack.acc:
                succeed = False
            else:
                succeed = True
            if succeed:

                animate_attack(playerimg, enemyimg, user)
                if attack.kind == "physical":
                    damage = attack.use(self.name, opp_name, self.atk, opp_df, self.focus)
                elif attack.kind == "special":
                    damage = attack.use(self.name, opp_name, self.spatk, opp_spdf, self.focus)
                opp_hp -= damage
                if user == "player":
                    enemy.hp = opp_hp
                else: # user is enemy
                    player.hp = opp_hp
                draw_scene(playerimg, enemyimg)
                announce("The attack did " + str(damage) + " damage.")
                update_statboard()
                wait()

                if attack.stateffect != "none":
                    if attack.target == "opp":
                        attack.apply_stateffect(opp_name, opp_atk, opp_spatk, opp_df, opp_spdf, opp_hp)
                    else:
                        attack.apply_stateffect(self.name, self.atk, self.spatk, self.df, self.spdf, self.hp)
                    update_statboard()

                if attack.othereffect != "none":
                    if attack.target == "opp":
                        if user == "player":
                            enemy.status = attack.apply_othereffect(enemy.name)
                        else: # user is enemy
                            player.status = attack.apply_othereffect(player.name)
                    else:
                        self.status = attack.apply_othereffect(self.name)
                    update_statboard()
            else: ## if missed
                draw_scene(playerimg, enemyimg)
                announce("The attack missed.")
                wait()

        if user == "player":
            battling = enemy.check_health()
        else: # user is enemy
            battling = player.check_health()

        return battling

    def take_turn(self, player, enemy): # for enemy only - enemy makes choice and acts on it - self = enemy

        enemy_choice = random.randrange(0, 9)

        if enemy_choice == 0 or 1 or 2 or 3 or 4 or 5 : # attack
            enemy_choice = random.randrange(0, 4)
            attack = enemy_attacklist[enemy_choice]
            battling = self.attackprocedure("enemy", attack, player, enemy)
            update_statboard()

        elif enemy_choice == 6: # items

            if self.healthpotions != 0 or self.mysticalpotions != 0 or self.catposters != 0:
                if self.hp < (self.mhp / 2):
                    enemy_choice = 1
                elif self.status != "none":
                    enemy_choice = 2
                elif self.morale < 80:
                    enemy_choice = 3
                else:
                    enemy_choice = 1
                self.use_item(enemy_choice)

            else:
                draw_scene(playerimg, enemyimg)
                announce(self.name + "has no items.")
                wait()

            battling = True

        elif enemy_choice == 7: # taunt
            self.say_taunt(player.name, player.atk, player.focus, player.morale)
            battling = True

        elif enemy_choice == 8: # forfeit
            draw_scene(playerimg, enemyimg)
            announce(self.name + " tried to forfeit, but couldn't!")
            wait()
            battling = True

        return battling

    def use_item(self, user_choice):

        if user_choice == 1:
            if self.healthpotions != 0:
                draw_scene(playerimg, enemyimg)
                announce(self.name + " drank a health potion.")
                self.healthpotions -= 1
                wait()
                if self.hp != self.mhp:
                    draw_scene(playerimg, enemyimg)
                    announce(self.name + "'s HP was restored.")
                    self.hp += 20
                    if self.hp > self.mhp:
                        self.hp = self.mhp
                    update_statboard()
                    wait()
                else:
                    draw_scene(playerimg, enemyimg)
                    announce(self.name + " is already at full health!")
                    wait()
            else:
                draw_scene(playerimg, enemyimg)
                announce(self.name + " doesn't have that item.")
                wait()

        elif user_choice == 2:
            if self.mysticalpotions != 0:
                draw_scene(playerimg, enemyimg)
                announce(self.name + " drank a mystical potion.")
                self.mysticalpotions -= 1
                wait()
                if self.status != "none":
                    draw_scene(playerimg, enemyimg)
                    announce(self.name + " is no longer " + self.status + ".")
                    self.status = "none"
                    update_statboard()
                    wait()
                else:
                    draw_scene(playerimg, enemyimg)
                    announce(self.name + " has no status conditions to heal!")
                    wait()
            else:
                draw_scene(playerimg, enemyimg)
                announce(self.name + " doesn't have that item.")
                wait()

        elif user_choice == 3:
            if self.catposters != 0:
                draw_scene(playerimg, enemyimg)
                announce(self.name + " stared at a cat poster for a few seconds.")
                wait()
                draw_scene(playerimg, enemyimg)
                announce(self.name + "'s morale was boosted!")
                wait()
                draw_scene(playerimg, enemyimg)
                announce("The poster evaporated in the heat of battle.")
                wait()
                self.catposters -= 1
                self.morale += 10
            else:
                draw_scene(playerimg, enemyimg)
                announce(self.name + " doesn't have that item.")
                wait()
        elif user_choice == 4:
            draw_scene(playerimg, enemyimg)
            announce(player.name + " scanned the battlefield.")
            wait()
            draw_scene(playerimg, enemyimg)
            announce(player.capsname + "'s stats:")
            wait()
            draw_scene(playerimg, enemyimg)
            announce("ATK: " + str(player.atk))
            wait()
            draw_scene(playerimg, enemyimg)
            announce("SPATK: " + str(player.spatk))
            wait()
            draw_scene(playerimg, enemyimg)
            announce("DEF: " + str(player.df))
            wait()
            draw_scene(playerimg, enemyimg)
            announce("SPDEF: " + str(player.spdf))
            wait()
            draw_scene(playerimg, enemyimg)
            announce("FOCUS: " + str(player.focus))
            wait()
            draw_scene(playerimg, enemyimg)
            announce("MORALE: " + str(player.morale))
            wait()
            draw_scene(playerimg, enemyimg)
            announce(enemy.capsname + "'s stats:")
            wait()
            draw_scene(playerimg, enemyimg)
            announce("ATK: " + str(enemy.atk))
            wait()
            draw_scene(playerimg, enemyimg)
            announce("SPATK: " + str(enemy.spatk))
            wait()
            draw_scene(playerimg, enemyimg)
            announce("DEF: " + str(enemy.df))
            wait()
            draw_scene(playerimg, enemyimg)
            announce("SPDEF: " + str(enemy.spdf))
            wait()
            draw_scene(playerimg, enemyimg)
            announce("FOCUS: " + str(enemy.focus))
            wait()
            draw_scene(playerimg, enemyimg)
            announce("MORALE: " + str(enemy.morale))
            wait()
            draw_scene(playerimg, enemyimg)
            announce("The scanner disengaged.")
            wait()

    def say_taunt(self, opp_name, opp_morale, opp_focus, opp_atk): # taunt the opponent
        draw_scene(playerimg, enemyimg)
        announce(self.capsname + ": " + self.taunt)
        wait()
        opp_morale -= int(opp_morale * (1/10))
        opp_focus -= int(opp_focus * (1/10))
        opp_atk += int(opp_atk * (2/10))
        draw_scene(playerimg, enemyimg)
        announce(opp_name + " became angry.")
        wait()
        draw_scene(playerimg, enemyimg)
        announce(opp_name + "'s morale fell!")
        wait()
        draw_scene(playerimg, enemyimg)
        announce(opp_name + "'s focus fell!")
        wait()
        draw_scene(playerimg, enemyimg)
        announce(opp_name + "'s attack was sharply raised!")
        wait()

    def check_health(self): # is character defeated?
        if self.hp <= 0:
            self.hp = 0
            draw_scene(playerimg, enemyimg)
            ask(self.name + " is unable to battle!")
            return False
        return True

    def check_prestatus(self): # does character have a status condition that effects them at the beginning of the turn?
        if self.status != "none":
            recoverval = random.randrange(0, 10) ## does character recover?
            if recoverval == 0: ## does not recover
                draw_scene(playerimg, enemyimg)
                announce(self.name + " is no longer " + self.status + ".")
                self.status = "none"
                update_statboard()
                wait()
                return False
            else: ## does not recover
                draw_scene(playerimg, enemyimg)
                announce(self.name + " is " + self.status + ".")
                if self.status == "paralyzed":
                    hinderval = random.randrange(0, 5)
                    if hinderval == 0:
                        draw_scene(playerimg, enemyimg)
                        announce(self.name + " can't move.")
                        wait()
                        return True
                elif self.status == "asleep":
                    draw_scene(playerimg, enemyimg)
                    announce(self.name + " is asleep.")
                    wait()
                    return True

    def check_poststatus(self): # does character have a status condition that effects them at the end of the turn?
        if self.status != "none":
            recoverval = random.randrange(0, 5) ## does character recover?
            if recoverval == 0:
                if self.status == "asleep":
                    draw_scene(playerimg, enemyimg)
                    announce(self.name + " woke up.")
                else:
                    draw_scene(playerimg, enemyimg)
                    announce(self.name + " is no longer " + self.status + ".")
                self.status = "none"
                update_statboard()
                wait()
            else: ## does not recover
                draw_scene(playerimg, enemyimg)
                announce(self.name + " is " + self.status + ".")
                wait()
                if self.status == "poisoned":
                    draw_scene(playerimg, enemyimg)
                    announce(self.name + " was hurt by poison!")
                    self.hp -= 8
                    update_statboard()
                    wait()

    def check_morale(self, attack_name): ## does character hesitate?
        hesitateval = random.randrange(0, 101)
        if hesitateval >= self.morale:
            draw_scene(playerimg, enemyimg)
            announce(self.name + " tried to use " + attack_name + ", but hesitated.")
            wait()
            return True

class Attack:

    def __init__(self, name, kind, pwr, acc, stateffect, stateffect_strength, othereffect, target, message):
        self.name = name
        self.kind = kind
        self.pwr = pwr
        self.acc = acc
        self.stateffect = stateffect
        self.stateffect_strength = stateffect_strength
        self.othereffect = othereffect
        self.target = target
        self.message = message

    def use(self, user_name, opp_name, user_atk, opp_df, user_focus): # deal damage
        announce(self.message)
        criticalval = random.randrange(0, 101) ## critical hit?
        if criticalval < user_focus:
            critical = True
        else:
            critical = False
        if critical:
            damage = (0.44 * user_atk/opp_df * self.pwr + 2) * 1.5 ##old: self.pwr + user_atk - opp_df + self.pwr/3
            draw_scene(playerimg, enemyimg)
            announce("It's a critical hit!")
            wait()
        else:
            damage = (0.44 * user_atk/opp_df * self.pwr + 2) ##old: self.pwr + user_atk - opp_df
        if damage <= 0:
            damage = 1
        return int(damage)

    def apply_stateffect(self, target_name, target_atk, target_spatk, target_df, target_spdf, target_hp): # stat changes ex. atk stat increase
            if self.stateffect == "+atk":
                target_atk += int(target_atk * (self.stateffect_strength/10))
                draw_scene(playerimg, enemyimg)
                announce(target_name + "'s attack rose!")
            elif self.stateffect == "-atk":
                target_atk -= int(target_atk * (self.stateffect_strength/10))
                draw_scene(playerimg, enemyimg)
                announce(target_name + "'s attack fell!")
            elif self.stateffect == "+spatk":
                target_spatk += int(target_spatk * (self.stateffect_strength/10))
                draw_scene(playerimg, enemyimg)
                announce(target_name + "'s special attack rose!")
            elif self.stateffect == "-spatk":
                target_spatk -= int(target_spatk * (self.stateffect_strength/10))
                draw_scene(playerimg, enemyimg)
                announce(target_name + "'s special attack fell!")
            elif self.stateffect == "+df":
                target_df += int(target_df * (self.stateffect_strength/10))
                draw_scene(playerimg, enemyimg)
                announce(target_name + "'s defense rose!")
            elif self.stateffect == "-df":
                target_df -= int(target_df * (self.stateffect_strength/10))
                draw_scene(playerimg, enemyimg)
                announce(target_name + "'s defense fell!")
            elif self.stateffect == "+spdf":
                target_spdf += int(target_spdf * (self.stateffect_strength/10))
                draw_scene(playerimg, enemyimg)
                announce(target_name + "'s special defense rose!")
            elif self.stateffect == "-spdf":
                target_spdf -= int(target_spdf * (self.stateffect_strength/10))
                draw_scene(playerimg, enemyimg)
                announce(target_name + "'s special defense fell!")
            elif self.stateffect == "+hp":
                target_hp += int(target_hp * (self.stateffect_strength/10))
                draw_scene(playerimg, enemyimg)
                announce(target_name + "'s HP was restored!")
                update_statboard()
            if target_name == enemy.name:
                enemy.atk = target_atk
                enemy.spatk = target_atk
                enemy.df = target_df
                enemy.spdf = target_spdf
                enemy.hp = target_hp
            else: # target = player
                player.atk = target_atk
                player.spatk = target_atk
                player.df = target_df
                player.spdf = target_spdf
                player.hp = target_hp
            wait()

    def apply_othereffect(self, target_name): # status conditions ex. paralysis
        if self.othereffect == "paralysis":
            draw_scene(playerimg, enemyimg)
            announce(target_name + " was paralyzed!")
            update_statboard()
            wait()
            return "paralyzed"
        elif self.othereffect == "poison":
            draw_scene(playerimg, enemyimg)
            announce(target_name + " was poisoned!")
            update_statboard()
            wait()
            return "poisoned"
        elif self.othereffect == "sleep":
            draw_scene(playerimg, enemyimg)
            announce(target_name + " fell asleep!")
            update_statboard()
            wait()
            return "asleep"

# CHOOSE CHARACTER (enemy automatically assigned)

## name = Character(title, name, capsname, mhp, atk, spatk, df, spdf, agil, focus, morale, status, attacks, greeting, taunt, img)

characterlist = []
pikachu = Character("Pocket Monster", "Pikachu", "PIKACHU", 120, 80, 80, 70, 80, 120, 20, 99, "none", [0,1,2,3], "I can't believe you didn't choose me...!", "You went obsolete in 2008!", 50, 450, 120, './resources/pikachu-right2.png', './resources/pikachu-left2.png', pikachu_cry)
characterlist.append(pikachu)
kacheek = Character("Neopian", "Kacheek", "KACHEEK", 140, 80, 70, 80, 85, 100, 20, 99, "none", [4,5,6,7], "I'm just HTML and I'll still kick your butt!", "You don't even own any mall items!", 80, 470, 160, './resources/kacheek-right2.png', './resources/kacheek-left2.png', chespin_cry)
characterlist.append(kacheek)
cockerspaniel = Character("Webkinz", "Cocker Spaniel", "COCKER SPANIEL", 190, 70, 50, 100, 90, 90, 10, 99, "none", [8,9,10,11], "*waves*", "*mocking emoticons*", 100, 490, 190, './resources/cockerspaniel-right.png', './resources/cockerspaniel-left.png', fennekin_cry)
characterlist.append(cockerspaniel)
puffle = Character("Pet", "Puffle", "PUFFLE", 110, 80, 50, 70, 70, 150, 15, 99, "none", [12,13,14,15], "Don't take your eyes off me!", "Torsos are overrated!", 100, 490, 210, './resources/puffle-right2.png', './resources/puffle-left2.png', froakie_cry)
characterlist.append(puffle)

ask("Which character do you want to play as?")
player_choice = choose(str(characterlist[0].name), str(characterlist[1].name), str(characterlist[2].name), str(characterlist[3].name))

playerID = player_choice - 1
player = characterlist[playerID]

playerimg = pygame.image.load(player.img_right)
playerimgRect = playerimg.get_rect()

characterlist.pop(playerID)
enemy = characterlist[random.randrange(0, len(characterlist))]
enemyimg = pygame.image.load(enemy.img_left)
enemyimgRect = enemyimg.get_rect()


# name = Attack(name, kind, pwr, acc, stateffect, stateffect_strength, othereffect, target, (user_name + " ??? " + opp_name + " ???."))
def make_all_attacks(user_name, opp_name):
    all_attacks = []
    thunderwave = Attack("Thunder Wave", "special", 0, 100, "none", 0, "paralysis", "opp", (user_name + " shocked " + opp_name + " lightly."))
    all_attacks.append(thunderwave)
    thunderbolt = Attack("Thunderbolt", "special", 90, 100, "none", 0, "none", "opp", (user_name + " shocked " + opp_name + " with a blast of lightning."))
    all_attacks.append(thunderbolt)
    growl = Attack("Growl", "special", 0, 100, "-atk", 1, "none", "opp", (user_name + " growled menacingly."))
    all_attacks.append(growl)
    charge = Attack("Charge", "special", 0, 100, "+spatk", 1, "none", "user", (user_name + " charged electricity in its body."))
    all_attacks.append(charge)
    magicblast = Attack("Magic Blast", "special", 90, 90, "none", 0, "none", "opp", (user_name + " blasted " + opp_name + " with a mysterious glowing light."))
    all_attacks.append(magicblast)
    dropkick = Attack("Drop Kick", "physical", 70, 90, "none", 0, "none", "opp", (user_name + " drop kicked " + opp_name + "."))
    all_attacks.append(dropkick)
    callafriend = Attack("Call a Friend", "physical", 70, 100, "none", 0, "none", "opp", (user_name + " sicced a petpet on " + opp_name + "."))
    all_attacks.append(callafriend)
    soupkitchen = Attack("Soup Kitchen", "special", 0, 100, "+hp", 0, "none", "user", (user_name + " took a quick field trip to the local soup kitchen."))
    all_attacks.append(soupkitchen)
    tackle = Attack("Tackle", "physical", 50, 100, "none", 0, "none", "opp", (user_name + " lunged at " + opp_name + "."))
    all_attacks.append(tackle)
    resourcedrain = Attack("Resource Drain", "special", 30, 95, "+hp", 0, "none", "user", (user_name + " drained " + opp_name + "'s money -- and their HP!"))
    all_attacks.append(resourcedrain)
    snuggle = Attack("Snuggle", "physical", 0, 100, "none", 0, "sleep", "opp", (user_name + " snuggled up to " + opp_name + "."))
    all_attacks.append(snuggle)
    gak = Attack("Gak", "special", 40, 90, "none", 0, "poison", "opp", (user_name + " convinced " + opp_name + " to try a horribly failed recipe."))
    all_attacks.append(gak)
    headbutt = Attack("Headbutt", "physical", 70, 100, "none", 0, "none", "opp", (user_name + " lunged headfirst at " + opp_name + "."))
    all_attacks.append(headbutt)
    implore = Attack("Implore", "special", 0, 100, "-atk", 1, "none", "opp", (user_name + " gazed at " + opp_name + " with wide, sad eyes."))
    all_attacks.append(implore)
    bounce = Attack("Bounce", "physical", 40, 100, "+atk", 2, "none", "user", (user_name + " began bouncing, gaining momentum."))
    all_attacks.append(bounce)
    multiply = Attack("Multiply", "physical", 50, 100, "none", 0, "paralysis", "opp", (user_name + " drowned " + opp_name + " in a sea of puffles."))
    all_attacks.append(multiply)
    #return copy.deepcopy(all_attacks)
    return all_attacks


""""
player_attacklist = make_all_attacks(player.name, enemy.name)

for item in range (len(player_attacklist)): # - (len(player_attacklist) - len(player.attacks)
    if item not in player.attacks:
        player_attacklist.pop(item)

enemy_attacklist = make_all_attacks(enemy.name, player.name)

for item in range (len(enemy_attacklist) - (len(enemy_attacklist) - len(enemy.attacks))):
    if item not in enemy.attacks:
        enemy_attacklist.pop(item)

"""
player_attacklist = make_all_attacks(player.name, enemy.name)

fillerlist = []
for item in range (len(player_attacklist)):
    if item not in player.attacks:
        player_attacklist.pop(item)
        player_attacklist.insert(item, str(item))
        fillerlist.append(item)
for item in range (len(player_attacklist)):
    if str(item) in fillerlist:
        player_attacklist.pop(item)

enemy_attacklist = make_all_attacks(enemy.name, player.name)

fillerlist = []
for item in range (len(enemy_attacklist)):
    if item not in enemy.attacks:
        enemy_attacklist.pop(item)
        enemy_attacklist.insert(item, str(item))
        fillerlist.append(item)
for item in range (len(enemy_attacklist)):
    if str(item) in fillerlist:
        enemy_attacklist.pop(item)

clear_options_panel()
draw_scene_no_enemy(playerimg)
announce(player.name + " is ready for battle!")
update()
player.sound.play()
wait()

draw_scene(playerimg, enemyimg)
announce(enemy.name + " challenges " + player.name + "!")
update()
enemy.sound.play()
wait()
draw_scene(playerimg, enemyimg)
announce(enemy.capsname + ": " + enemy.greeting)
update()
music.play()
wait()

update_statboard()

battling = True

# GAME LOOP

while battling:

    draw_scene(playerimg, enemyimg)
    ask("What will " + player.name + " do?")
    player_choice = choose("Attack", "Items", "Taunt", "Forfeit")

    if player_choice == 1: # attack

        draw_scene(playerimg, enemyimg)
        ask("Which attack will " + player.name + " use?")
        player_choice = choose(player_attacklist[0].name, player_attacklist[1].name, player_attacklist[2].name, player_attacklist[3].name)
        attack = player_attacklist[player_choice - 1]

        if player.agil > enemy.agil: # who goes first

            battling = player.attackprocedure("player", attack, player, enemy) ## player goes
            update_statboard()

            battling = enemy.take_turn(player, enemy) ## enemy goes
            update_statboard()

        else:

            battling = enemy.take_turn(player, enemy) ## enemy goes
            update_statboard()

            battling = player.attackprocedure("player", attack, player, enemy) ## player goes
            update_statboard()

        player.check_poststatus()
        update_statboard
        enemy.check_poststatus()
        update_statboard

    elif player_choice == 2: # items

        if player.healthpotions != 0 or player.mysticalpotions != 0 or player.catposters != 0:
            draw_scene(playerimg, enemyimg)
            ask("Inventory:")
            player_choice = choose("[x " + str(player.healthpotions) + "]  Health Potion  --  + 20 HP", "[x " + str(player.mysticalpotions) + "]  Mystical Potion  --  heals status conditions", "[x " + str(player.catposters) + "]  Cat Poster  --  + 20 morale", "[unl.]  Scanner --  displays statistics")
            player.use_item(player_choice)

        else:
            draw_scene(playerimg, enemyimg)
            announce(player.name + " has no items.")
            wait()

        update_statboard()

        battling = enemy.take_turn(player, enemy)
        update_statboard()

        player.check_poststatus()
        update_statboard
        enemy.check_poststatus()
        update_statboard

    elif player_choice == 3: # taunt

        player.say_taunt(enemy.name, enemy.atk, enemy.focus, enemy.morale)

        battling = enemy.take_turn(player, enemy)
        update_statboard()

        player.check_poststatus()
        update_statboard
        enemy.check_poststatus()
        update_statboard

    elif player_choice == 4: # forfeit

        draw_scene(playerimg, enemyimg)
        ask(player.name + " threw in the towel.")
        wait()
        battling = False

pygame.mixer.stop()
pygame.quit()