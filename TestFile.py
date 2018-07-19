from graphics import *
from vlc import *
import random
import time

class Menu(object):
    def __init__(self, image, night, win):
        self.night = str(night.readNight())
        self.image = Image(Point(win.getWidth() / 2, win.getHeight() / 2), image)
        self.nightmare = Image(Point(373, 838), "nightmare.png")
        self.extra = Image(Point(290, 940), "extra.png")
        self.extras = Image(Point(1100, 800), "extras.png")
        self.background = Image(Point(win.getWidth() / 2, win.getHeight() / 2), "Background.png")
        self.job = Image(Point(win.getWidth() / 2, win.getHeight() / 2), "JOB.png")
        self.star1 = Image(Point(1825, 100), "star.png")
        self.star2 = Image(Point(1675, 100), "star.png")
        self.star3 = Image(Point(1525, 100), "star.png")
        self.circ1 = Circle(Point(1300, 670), 10)
        self.circ1.setFill("Red")
        self.circ2 = Circle(Point(1050, 760), 10)
        self.circ2.setFill("Red")
        self.circ3 = Circle(Point(1270, 850), 10)
        self.circ3.setFill("Red")
        self.circ4 = Circle(Point(1200, 940), 10)
        self.circ4.setFill("Red")
        self.pos = win.checkMouse()
        self.menuMusic = MediaPlayer("Audio/Menu Music.mp3")
        self.newNight = MediaPlayer("Audio/New Night.mp3")
        self.fastNight = False
        self.radar = False
        self.agressive = False
        self.noErrors = False

    def __str__(self):
        string = "Night: " + str(self.night) + "\n"
        string += "FastNight: " + str(self.fastNight) + "\n"
        string += "Radar: " + str(self.radar) + "\n"
        string += "Agressive: " + str(self.agressive) + "\n"
        string += "NoErrors: " + str(self.noErrors)
        return string

    def runMenu(self, gameover):
        """displays the menu screen"""
        if gameover:
            self.image.draw(win)
            text = Text(Point(669, 738), str(night.readNight()))
            text.setTextColor("White")
            text.setSize(36)
            text.setFace("times roman")
            text.setStyle("bold italic")
            text.draw(win)
            if int(night.readStar()) >= 1:
                self.star1.draw(win)
                self.nightmare.draw(win)
            if int(night.readStar()) >= 2:
                self.star2.draw(win)
                self.extra.draw(win)
            if int(night.readStar()) >= 3:
                self.star3.draw(win)
            self.menuMusic.play()
            clicked = False
            reset = False
            while clicked == False:
                win.update()
                self.pos = win.checkMouse()
                if self.pos != None:
                    if self.pos.getX() > 175 and self.pos.getX() < 600 and self.pos.getY() > 600 and self.pos.getY() < 675:
                        night.reset()
                        self.night = 1
                        self.job.draw(win)
                        reset = True
                        time.sleep(8)
                        clicked = True
                    elif self.pos.getX() > 175 and self.pos.getX() < 650 and self.pos.getY() > 700 and self.pos.getY() < 775:
                        clicked = True
                    elif self.pos.getX() > 175 and self.pos.getX() < 650 and self.pos.getY() > 800 and self.pos.getY() < 875 and int(night.readStar()) >= 1:
                        clicked = True
                        self.night = "6"
                    elif self.pos.getX() > 175 and self.pos.getX() < 650 and self.pos.getY() > 900 and self.pos.getY() < 975 and int(night.readStar()) >= 2:
                        self.extras.draw(win)
                        if self.fastNight == True:
                            self.circ1.draw(win)
                        if self.radar == True:
                            self.circ2.draw(win)
                        if self.agressive == True:
                            self.circ3.draw(win)
                        if self.noErrors == True:
                            self.circ4.draw(win)
                        x = 0
                        y = 0
                        click = False
                        while click == False:
                            win.update()
                            self.pos = win.checkMouse()
                            if self.pos != None:
                                x = self.pos.getX()
                                y = self.pos.getY()
                                if 1474 >= x >= 1417 and 623 >= y >= 596:
                                    click = True
                                elif 1255 >= x >= 768 and 701 >= y >= 630:
                                    if self.fastNight == False:
                                        self.fastNight = True
                                        self.circ1.draw(win)
                                    else:
                                        self.fastNight = False
                                        self.circ1.undraw()
                                    print(self.fastNight)
                                elif 1006 >= x >= 768 and 785 >= y >= 726:
                                    if self.radar == False:
                                        self.radar = True
                                        self.circ2.draw(win)
                                    else:
                                        self.radar = False
                                        self.circ2.undraw()
                                    print(self.radar)
                                elif 1232 >= x >= 768 and 875 >= y >= 817:
                                    if self.agressive == False:
                                        self.agressive = True
                                        self.circ3.draw(win)
                                    else:
                                        self.agressive = False
                                        self.circ3.undraw()
                                    print(self.agressive)
                                elif 1166 >= x >= 768 and 969 >= y >= 907:
                                    if self.noErrors == False:
                                        self.noErrors = True
                                        self.circ4.draw(win)
                                    else:
                                        self.noErrors = False
                                        self.circ4.undraw()
                                    print(self.noErrors)
                        self.circ1.undraw()
                        self.circ2.undraw()
                        self.circ3.undraw()
                        self.circ4.undraw()
                        self.extras.undraw()
                time.sleep(.01)
            self.image.undraw()
            self.nightmare.undraw()
            self.star1.undraw()
            self.star2.undraw()
            self.star3.undraw()
            self.extra.undraw()
            self.menuMusic.stop()
            if reset:
                self.job.undraw()
            text.undraw()
        if self.pos.getX() > 175 and self.pos.getX() < 650 and self.pos.getY() > 800 and self.pos.getY() < 875 and int(night.readStar()) >= 1:
            self.night = "6"
        else:
            self.night = str(night.readNight())

        self.newNight.play()
        self.background.draw(win)
        text = Text(Point(win.getWidth() // 2, win.getHeight() // 2), "Night " + str(self.night))
        text.setTextColor("White")
        text.setSize(36)
        text.setFace("times roman")
        text.setStyle("bold italic")
        text.draw(win)
        for i in range(400):
            time.sleep(.01)
        text.undraw()
        self.background.undraw()
        self.newNight.stop()

class Room(object):
    def __init__(self, image, speed, animatronic, win: GraphWin):
        self.x = win.getWidth() / 2
        self.y = win.getHeight() / 2
        self.image = Image(Point(self.x,self.y), image)
        self.springtrapAtTheWindow = Image(Point(self.x + 5000, self.y), "CAM Springtrap/Springtrap at the Window.png")
        self.springtrapAtTheDoor = Image(Point(self.x + 5000, self.y), "CAM Springtrap/Springtrap at the Door.png")
        self.image.draw(win)
        self.springtrapAtTheWindow.draw(win)
        self.springtrapAtTheDoor.draw(win)
        self.balloonBoyJumpscare = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Jumpscares/Balloon Boy.png")
        self.chicaJumpscare = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Jumpscares/Chica.png")
        self.foxyJumpscare = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Jumpscares/Foxy.png")
        self.freddyJumpscare = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Jumpscares/Freddy.png")
        self.mangleJumpscare = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Jumpscares/Mangle.png")
        self.puppetJumpscare = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Jumpscares/Puppet.png")
        self.springtrapJumpscare = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Jumpscares/Springtrap.png")
        self.sixAM = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "6 AM.png")
        self.gameOver = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Game Over.png")
        self.night5End = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Good Ending.png")
        self.night6End = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Night 6 Ending.png")
        self.speed = speed
        self.moveTime = 0
        self.ambience = MediaPlayer("Audio/Ambience.mp3")
        self.ambience.play()
        self.nightAudio = ["Audio/Night 1 Call.mp3", "Audio/Night 2 Call.mp3", "Audio/Night 3 Call.mp3",
                           "Audio/Night 4 Call.mp3", "Audio/Night 5 Call.mp3", "Audio/Night 6 Call.mp3"]
        self.nightCall = MediaPlayer(self.nightAudio[int(menu.night) - 1])
        self.nightCall.play()
        self.goodEnding = MediaPlayer("Audio/End of Night 5.wav")
        self.night6Ending = MediaPlayer("Audio/End of Night 6.wav")
        self.jumpscare = MediaPlayer("Audio/Jumpscare Sound.mp3")
        self.mangle = MediaPlayer("Audio/Phantom Mangle.mp3")
        self.puppet = MediaPlayer("Audio/Phantom Puppet.mp3")
        self.alarm = MediaPlayer("Audio/Alarm.wav")
        self.sixAMAudio = MediaPlayer("Audio/6 AM.mp3")
        self.gameOverAudio = MediaPlayer("Audio/Game Over.wav")
        self.breathing = MediaPlayer("Audio/Breathing Sound.mp3")
        self.ventilationOn = MediaPlayer("Audio/Ventilation On.mp3")
        self.ventilationOff = MediaPlayer("Audio/Ventilation Off.mp3")
        self.nightText = Text(Point(100, 30), "Night " + str(menu.night))
        self.nightText.setTextColor("White")
        self.nightText.setSize(36)
        self.nightText.setFace("times roman")
        self.nightText.setStyle("bold italic")
        self.nightText.draw(win)
        self.clock = "12"
        self.timer = 0
        self.timeText = Text(Point(85, 80), self.clock + " AM")
        self.timeText.setTextColor("White")
        self.timeText.setSize(36)
        self.timeText.setFace("times roman")
        self.timeText.setStyle("bold italic")
        self.timeText.draw(win)
        self.waring1 = Polygon(Point(250, 20), Point(280, 86), Point(220, 86))
        self.waring1.setFill("Yellow")
        self.waring1.setOutline("Black")
        self.waring1.setWidth(3)
        self.waring2 = Text(Point(250, 60), "!")
        self.waring2.setTextColor("Black")
        self.waring2.setSize(36)
        self.waring2.setFace("times roman")
        self.waring2.setStyle("bold")
        self.moved = False
        self.at0 = False
        self.at16 = False
        self.phantom = False
        self.lights = True
        self.phantomTimer = 0
        self.jumpscareTimer = 0
        self.fastNight = 1
        self.agressive = 0
        if menu.fastNight == True:
            self.fastNight = 3
        if menu.agressive == True:
            self.agressive = 500

    def __str__(self):
        string = "Active: " + str(self.active) + "\n"
        string += "Time: " + str(self.clock) + " AM" + "\n"
        string += "Pos: " + "(" + str(self.x) + "," + str(self.y) + ")"
        return string

    def moveRight(self):
        """moves the image right"""
        self.x -= self.speed
        self.image.move(self.speed, 0)
        self.springtrapAtTheWindow.move(self.speed, 0)
        self.springtrapAtTheDoor.move(self.speed, 0)

    def moveLeft(self):
        """moves the image left"""
        self.x += self.speed
        self.image.move(-self.speed, 0)
        self.springtrapAtTheWindow.move(-self.speed, 0)
        self.springtrapAtTheDoor.move(-self.speed, 0)

    def move(self, pos):
        if pos.getX() < win.getWidth() / 4 and self.x > 540:
            self.moveRight()
        elif pos.getX() > win.getWidth() * 3 / 4 and self.x < 1470:
            self.moveLeft()
        self.moveCounter()
        if self.phantom == True:
            self.jumpscareTimer += 1
        if self.jumpscareTimer >= 200 - (int(menu.night) - 1) * 20 and self.phantom:
            self.phantom = False
            self.phantomTimer = 0
            self.jumpscareTimer = 0
            if random.randrange(2) == 0:
                if menu.noErrors == False:
                    reboot.ventilationTimer = 8999 - 750 * (int(menu.night) - 1)
                    reboot.ventilation = False
                room.jumpscare.stop()
                room.jumpscare.play()
                room.foxyJumpscare.draw(win)
                for i in range(100):
                    room.moveCounter()
                    if i == 50:
                        room.breathing.stop()
                        room.breathing.play()
                    time.sleep(.01)
                room.foxyJumpscare.undraw()
            else:
                if menu.noErrors == False:
                    reboot.ventilationTimer = 8999 - 750 * (int(menu.night) - 1)
                    reboot.ventilation = False
                room.jumpscare.stop()
                room.jumpscare.play()
                room.freddyJumpscare.draw(win)
                for i in range(100):
                    room.moveCounter()
                    if i == 50:
                        room.breathing.stop()
                        room.breathing.play()
                    time.sleep(.01)
                room.freddyJumpscare.undraw()
            self.waring1.undraw()
            self.waring2.undraw()
        time.sleep(.01)

    def moveCounter(self):
        """determines when the animatronic can move and is used for some timers"""
        if self.moveTime > 1500 - 100 * (int(menu.night) - 1) - self.agressive and random.randrange(20) == 0:
            animatronic.move()
            self.moveTime = 0
            self.moved = True
        else:
            self.moved = False
        self.phantomTimer += 1
        if self.phantomTimer == 9000 - 1000 * (int(menu.night) - 1):
            self.phantom = True
        if self.phantomTimer == 10000 - 1000 * (int(menu.night) - 1):
            self.phantom = False
            self.phantomTimer = 0
            self.jumpscareTimer = 0
            self.waring1.undraw()
            self.waring2.undraw()
        if self.jumpscareTimer == 1:
            self.waring1.draw(win)
            self.waring2.draw(win)
        self.moveTime += 1
        reboot.audioTimer += 1
        if menu.noErrors == False:
            if reboot.ventilationTimer <= 11000 - 750 * (int(menu.night) - 1) and self.lights:
                reboot.ventilationTimer += 1
            if reboot.ventilationTimer == 9000 - 750 * (int(menu.night) - 1) and self.lights:
                reboot.ventilation = False
            elif reboot.ventilationTimer == 9800 - 750 * (int(menu.night) - 1) and self.lights:
                self.alarm.stop()
                self.alarm.play()
            elif reboot.ventilationTimer == 10300 - 750 * (int(menu.night) - 1) and self.lights:
                self.ventilationOff.stop()
                self.ventilationOff.play()
                self.lights = False
                for vent in Vent.vents:
                    vent.is_closed = False
                self.image.move(5000, 0)
                self.springtrapAtTheDoor.move(5000, 0)
                self.springtrapAtTheWindow.move(5000, 0)
        if self.timer == 36000 / self.fastNight:
            self.timeText.undraw()
            self.clock = "6"
            self.timeText = Text(Point(85, 80), self.clock + " AM")
            self.timeText.setTextColor("White")
            self.timeText.setSize(36)
            self.timeText.setFace("times roman")
            self.timeText.setStyle("bold italic")
            self.timeText.draw(win)
        elif self.timer == 30000 / self.fastNight:
            self.timeText.undraw()
            self.clock = "5"
            self.timeText = Text(Point(85, 80), self.clock + " AM")
            self.timeText.setTextColor("White")
            self.timeText.setSize(36)
            self.timeText.setFace("times roman")
            self.timeText.setStyle("bold italic")
            self.timeText.draw(win)
        elif self.timer == 24000 / self.fastNight:
            self.timeText.undraw()
            self.clock = "4"
            self.timeText = Text(Point(85, 80), self.clock + " AM")
            self.timeText.setTextColor("White")
            self.timeText.setSize(36)
            self.timeText.setFace("times roman")
            self.timeText.setStyle("bold italic")
            self.timeText.draw(win)
        elif self.timer == 18000 / self.fastNight:
            self.timeText.undraw()
            self.clock = "3"
            self.timeText = Text(Point(85, 80), self.clock + " AM")
            self.timeText.setTextColor("White")
            self.timeText.setSize(36)
            self.timeText.setFace("times roman")
            self.timeText.setStyle("bold italic")
            self.timeText.draw(win)
        elif self.timer == 12000 / self.fastNight:
            self.timeText.undraw()
            self.clock = "2"
            self.timeText = Text(Point(85, 80), self.clock + " AM")
            self.timeText.setTextColor("White")
            self.timeText.setSize(36)
            self.timeText.setFace("times roman")
            self.timeText.setStyle("bold italic")
            self.timeText.draw(win)
        if self.timer == 6000 / self.fastNight:
            self.timeText.undraw()
            self.clock = "1"
            self.timeText = Text(Point(85, 80), self.clock + " AM")
            self.timeText.setTextColor("White")
            self.timeText.setSize(36)
            self.timeText.setFace("times roman")
            self.timeText.setStyle("bold italic")
            self.timeText.draw(win)
        if animatronic.pos == 16 and self.moved:
            self.springtrapAtTheWindow.move(-5000, 0)
            self.image.move(5000, 0)
            self.at16 = True
        elif self.at16 and self.moved:
            self.springtrapAtTheWindow.move(5000, 0)
            self.image.move(-5000, 0)
            self.at16 = False
        if animatronic.pos == 0 and self.moved:
            self.springtrapAtTheDoor.move(-5000, 0)
            self.image.move(5000, 0)
            self.at0 = True
        elif self.at0 and self.moved:
            self.springtrapAtTheDoor.move(5000, 0)
            self.image.move(-5000, 0)
            self.at0 = False
        self.timer += 1

    def closeRoom(self):
        """undiplays the room image and disables any attributes associated with it"""
        self.image.undraw()
        self.springtrapAtTheWindow.undraw()
        self.springtrapAtTheDoor.undraw()
        self.waring1.undraw()
        self.waring2.undraw()
        self.nightText.undraw()
        self.timeText.undraw()
        self.ambience.stop()
        self.nightCall.stop()
        self.jumpscare.stop()
        self.mangle.stop()
        self.puppet.stop()
        self.breathing.stop()
        self.ventilationOff.stop()
        self.ventilationOn.stop()

class Camera(object):

    def __init__(self, image, animatronic, reboot, room, win):
        self.image = Image(Point(1315, 375), image)
        self.toggleCamera = False
        self.camPOINTS = [[1400, 620], [1674, 588], [1776, 535], [1776, 452], [1568, 473], [1392, 481], [1392, 399],
                  [1525, 370], [1610, 318], [1746, 362]]
        self.ventPOINTS = [[1398, 279], [1484, 425], [1589, 512], [1704, 407], [1735, 588]]
        self.imagesNone = ["CAM None\CAM_01.png", "CAM None\CAM_02.png", "CAM None\CAM_03.png", "CAM None\CAM_04.png", "CAM None\CAM_05.png",
                           "CAM None\CAM_06.png", "CAM None\CAM_07.png", "CAM None\CAM_08.png", "CAM None\CAM_09.png", "CAM None\CAM_10.png",
                           "CAM None\CAM_11.png", "CAM None\CAM_12.png", "CAM None\CAM_13.png", "CAM None\CAM_14.png", "CAM None\CAM_15.png"]
        self.imagesSpringtrap = ["CAM Springtrap\CAM_01 X.png", "CAM Springtrap\CAM_02 X.png", "CAM Springtrap\CAM_03 X.png", "CAM Springtrap\CAM_04 X.png", "CAM Springtrap\CAM_05 X.png",
                                 "CAM Springtrap\CAM_06 X.png", "CAM Springtrap\CAM_07 X.png", "CAM Springtrap\CAM_08 X.png", "CAM Springtrap\CAM_09 X.png", "CAM Springtrap\CAM_10 X.png",
                                 "CAM Springtrap\CAM_11 X.png", "CAM Springtrap\CAM_12 X.png", "CAM Springtrap\CAM_13 X.png", "CAM Springtrap\CAM_14 X.png", "CAM Springtrap\CAM_15 X.png"]
        self.imagesPhantom = ["CAM Phantom\CAM_01 Y.png", "CAM Phantom\CAM_02 Y.png", "CAM Phantom\CAM_03 Y.png", "CAM Phantom\CAM_04 Y.png", "CAM Phantom\CAM_05 Y.png",
                              "CAM Phantom\CAM_06 Y.png", "CAM Phantom\CAM_07 Y.png", "CAM Phantom\CAM_08 Y.png", "CAM Phantom\CAM_09 Y.png", "CAM Phantom\CAM_10 Y.png"]
        self.imagesError = ["CAM Error\CAM_01 Z.png", "CAM Error\CAM_02 Z.png", "CAM Error\CAM_03 Z.png", "CAM Error\CAM_04 Z.png", "CAM Error\CAM_05 Z.png",
                            "CAM Error\CAM_06 Z.png", "CAM Error\CAM_07 Z.png", "CAM Error\CAM_08 Z.png", "CAM Error\CAM_09 Z.png", "CAM Error\CAM_10 Z.png",
                            "CAM Error\CAM_11 Z.png", "CAM Error\CAM_12 Z.png", "CAM Error\CAM_13 Z.png", "CAM Error\CAM_14 Z.png", "CAM Error\CAM_15 Z.png"]
        self.openingCamera = MediaPlayer("Audio/Open Camera.wav")
        self.closingCamera = MediaPlayer("Audio/Close Camera.wav")
        self.closeVent = MediaPlayer("Audio/Close Vent.mp3")
        self.switchCamera = MediaPlayer("Audio/Switch Camera.mp3")
        self.audio1 = MediaPlayer("Audio/Balloon Boy Sound 1.wav")
        self.audio2 = MediaPlayer("Audio/Balloon Boy Sound 2.wav")
        self.audio3 = MediaPlayer("Audio/Balloon Boy Sound 3.wav")
        self.audio = self.audio1
        self.AUDIOS = [self.audio1, self.audio2, self.audio3]
        self.lastCamera = 2
        self.currentCamera = 2
        self.currentVent = 11
        self.cam = Image(Point(1315, 375), self.imagesNone[self.lastCamera - 1])
        self.ventText = Text(Point(1375, 60), "Press Enter to Close a Vent")
        self.ventText.setTextColor("White")
        self.ventText.setSize(20)
        self.ventText.setFace("times roman")
        self.audioText = Text(Point(815, 60), "Audio Error")
        self.audioText.setTextColor("Red")
        self.audioText.setSize(20)
        self.audioText.setFace("times roman")
        self.cameraText = Text(Point(815, 90), "Video Error")
        self.cameraText.setTextColor("Red")
        self.cameraText.setSize(20)
        self.cameraText.setFace("times roman")
        self.ventilationText = Text(Point(844, 120), "Ventilation Error")
        self.ventilationText.setTextColor("Red")
        self.ventilationText.setSize(20)
        self.ventilationText.setFace("times roman")
        self.radar = Text(Point(780, 680), str(animatronic.pos))
        self.radar.setTextColor("Red")
        self.radar.setSize(36)
        self.radar.setFace("times roman")
        self.phantom = False
        self.jumpscareTimer = 0

    def __str__(self):
        string = "Current camera: " + str(self.currentCamera) + "\n"
        string += "Current vent: " + str(self.currentVent) + "\n"
        string += "Last camera: " + str(self.lastCamera) + "\n"
        return string

    def checkCamera(self, pos, room, win):
        """checks if the mouse is over the camera button"""
        if pos.getX() > win.getWidth() * 7 / 8 and pos.getY() < win.getHeight() / 2 and room.x > 1450:
            self.openCamera(pos, win)

    def openCamera(self, pos, win):
        """opens the camera screen"""
        self.closingCamera.stop()
        self.openingCamera.play()
        self.image.draw(win)
        self.cam.draw(win)
        if reboot.audio == False:
            self.audioText.draw(win)
        if reboot.camera == False:
            self.cameraText.draw(win)
        if reboot.ventilation == False:
            self.ventilationText.draw(win)
        if menu.radar == True:
            self.radar.draw(win)
        while pos.getX() > win.getWidth() / 4 and animatronic.alive == True and room.clock != "6":
            win.update()
            pos = win.getCurrentMouseLocation()
            self.checkButtons(win)
            room.moveCounter()
            if reboot.cameraTimer <= 7500 - 750 * (int(menu.night) - 1) and menu.noErrors == False:
                reboot.cameraTimer += 1
            if reboot.cameraTimer == 7500 - 750 * (int(menu.night) - 1) and menu.noErrors == False:
                reboot.camera = False
            if reboot.camera == False and reboot.cameraTimer == 7500 - 750 * (int(menu.night) - 1) and menu.noErrors == False:
                self.cam.undraw()
                self.ventText.undraw()
                self.audioText.undraw()
                self.cameraText.undraw()
                self.ventilationText.undraw()
                self.radar.undraw()
                self.cam = Image(Point(1315, 375), self.imagesError[self.lastCamera - 1])
                self.cam.draw(win)
                if reboot.audio == False:
                    self.audioText.draw(win)
                if reboot.camera == False:
                    self.cameraText.draw(win)
                if reboot.ventilation == False:
                    self.ventilationText.draw(win)
                if menu.radar == True:
                    self.radar = Text(Point(780, 680), str(animatronic.pos))
                    self.radar.setTextColor("Red")
                    self.radar.setSize(36)
                    self.radar.setFace("times roman")
                    self.radar.draw(win)
            elif animatronic.pos != self.lastCamera and room.moved:
                self.cam.undraw()
                self.ventText.undraw()
                self.audioText.undraw()
                self.cameraText.undraw()
                self.ventilationText.undraw()
                self.radar.undraw()
                if reboot.camera == False:
                    self.cam = Image(Point(1315, 375), self.imagesError[self.lastCamera - 1])
                    self.cam.draw(win)
                else:
                    self.cam = Image(Point(1315, 375), self.imagesNone[self.lastCamera - 1])
                    self.cam.draw(win)
                if self.lastCamera >= 11:
                    self.ventText.draw(win)
                if reboot.audio == False:
                    self.audioText.draw(win)
                if reboot.camera == False:
                    self.cameraText.draw(win)
                if reboot.ventilation == False:
                    self.ventilationText.draw(win)
                if menu.radar == True:
                    self.radar = Text(Point(780, 680), str(animatronic.pos))
                    self.radar.setTextColor("Red")
                    self.radar.setSize(36)
                    self.radar.setFace("times roman")
                    self.radar.draw(win)
            elif animatronic.pos == self.lastCamera and room.moved:
                self.cam.undraw()
                self.ventText.undraw()
                self.audioText.undraw()
                self.cameraText.undraw()
                self.ventilationText.undraw()
                self.radar.undraw()
                if reboot.camera == False:
                    self.cam = Image(Point(1315, 375), self.imagesError[self.lastCamera - 1])
                    self.cam.draw(win)
                else:
                    self.cam = Image(Point(1315, 375), self.imagesSpringtrap[self.lastCamera - 1])
                    self.cam.draw(win)
                if self.lastCamera >= 11:
                    self.ventText.draw(win)
                if reboot.audio == False:
                    self.audioText.draw(win)
                if reboot.camera == False:
                    self.cameraText.draw(win)
                if reboot.ventilation == False:
                    self.ventilationText.draw(win)
                if menu.radar == True:
                    self.radar = Text(Point(780, 680), str(animatronic.pos))
                    self.radar.setTextColor("Red")
                    self.radar.setSize(36)
                    self.radar.setFace("times roman")
                    self.radar.draw(win)
            time.sleep(.01)
        self.closeCamera()

    def checkButtons(self, win):
        """changes the camera image based on a click"""
        pos = win.checkMouse()
        if pos != None:
            if self.toggleCamera == False:
                cameraNum = 0
                if pos.getX() > 1185 and pos.getX() < 1369 and pos.getY() > 494 and pos.getY() < 577 and reboot.audio and reboot.audioTimer > 700:
                    self.audio.stop()
                    self.audio = random.choice(self.AUDIOS)
                    self.audio.play()
                    animatronic.distract(self.currentCamera)
                    room.moveTime = 9000
                    reboot.audioTimer = 0
                    if menu.noErrors == False:
                        reboot.audioLimit -= 1
                        if reboot.audioLimit <= 0:
                            reboot.audio = False
                elif pos.getX() > 1185 and pos.getX() < 1369 and pos.getY() > 587 and pos.getY() < 674:
                    self.toggleCamera = True
                    self.ventText.undraw()
                    self.audioText.undraw()
                    self.cameraText.undraw()
                    self.ventilationText.undraw()
                    self.radar.undraw()
                    self.cam.undraw()
                    self.phantom = False
                    self.jumpscareTimer = 0
                    self.switchCamera.stop()
                    self.switchCamera.play()
                    if reboot.camera == False:
                        self.lastCamera = self.currentVent
                        self.cam = Image(Point(1315, 375), self.imagesError[self.lastCamera - 1])
                        self.cam.draw(win)
                    elif self.currentVent == animatronic.pos:
                        self.lastCamera = self.currentVent
                        self.cam = Image(Point(1315, 375), self.imagesSpringtrap[self.currentVent - 1])
                        self.cam.draw(win)
                    else:
                        self.lastCamera = self.currentVent
                        self.cam = Image(Point(1315, 375), self.imagesNone[self.currentVent - 1])
                        self.cam.draw(win)
                    self.ventText.draw(win)
                    if reboot.audio == False:
                        self.audioText.draw(win)
                    if reboot.camera == False:
                        self.cameraText.draw(win)
                    if reboot.ventilation == False:
                        self.ventilationText.draw(win)
                    if menu.radar == True:
                        self.radar = Text(Point(780, 680), str(animatronic.pos))
                        self.radar.setTextColor("Red")
                        self.radar.setSize(36)
                        self.radar.setFace("times roman")
                        self.radar.draw(win)
                else:
                    for point in self.camPOINTS:
                        x = point[0]
                        y = point[1]
                        if pos.getX() > x and pos.getX() < x + 85 and pos.getY() > y and pos.getY() < y + 58:
                            self.switchCamera.stop()
                            self.switchCamera.play()
                            self.cam.undraw()
                            self.ventText.undraw()
                            self.audioText.undraw()
                            self.cameraText.undraw()
                            self.ventilationText.undraw()
                            self.radar.undraw()
                            self.phantom = False
                            self.jumpscareTimer = 0
                            if reboot.camera == False:
                                self.lastCamera = cameraNum + 1
                                self.currentCamera = cameraNum + 1
                                self.cam = Image(Point(1315, 375), self.imagesError[self.lastCamera - 1])
                                self.cam.draw(win)
                            elif cameraNum + 1 == animatronic.pos:
                                self.lastCamera = cameraNum + 1
                                self.currentCamera = cameraNum + 1
                                self.cam = Image(Point(1315, 375), self.imagesSpringtrap[self.currentCamera - 1])
                                self.cam.draw(win)
                            elif random.randrange(32 - int(menu.night)) * 2 == 0:
                                self.jumpscareTimer = 0
                                self.phantom = True
                                self.lastCamera = cameraNum + 1
                                self.currentCamera = cameraNum + 1
                                self.cam = Image(Point(1315, 375), self.imagesPhantom[self.currentCamera - 1])
                                self.cam.draw(win)
                            else:
                                self.lastCamera = cameraNum + 1
                                self.currentCamera = cameraNum + 1
                                self.cam = Image(Point(1315, 375), self.imagesNone[self.currentCamera - 1])
                                self.cam.draw(win)
                            if reboot.audio == False:
                                self.audioText.draw(win)
                            if reboot.camera == False:
                                self.cameraText.draw(win)
                            if reboot.ventilation == False:
                                self.ventilationText.draw(win)
                            if menu.radar == True:
                                self.radar = Text(Point(780, 680), str(animatronic.pos))
                                self.radar.setTextColor("Red")
                                self.radar.setSize(36)
                                self.radar.setFace("times roman")
                                self.radar.draw(win)
                        cameraNum += 1
            else:
                cameraNum = 0
                if pos.getX() > 1185 and pos.getX() < 1369 and pos.getY() > 587 and pos.getY() < 674:
                    self.switchCamera.stop()
                    self.switchCamera.play()
                    self.toggleCamera = False
                    self.cam.undraw()
                    self.ventText.undraw()
                    self.audioText.undraw()
                    self.cameraText.undraw()
                    self.ventilationText.undraw()
                    self.radar.undraw()
                    self.phantom = False
                    self.jumpscareTimer = 0
                    if reboot.camera == False:
                        self.lastCamera = self.currentCamera
                        self.cam = Image(Point(1315, 375), self.imagesError[self.lastCamera - 1])
                        self.cam.draw(win)
                    elif self.currentCamera == animatronic.pos:
                        self.lastCamera = self.currentCamera
                        self.cam = Image(Point(1315, 375), self.imagesSpringtrap[self.currentCamera - 1])
                        self.cam.draw(win)
                    elif random.randrange(32 - int(menu.night)) * 2 == 0:
                        self.jumpscareTimer = 0
                        self.phantom = True
                        self.lastCamera = self.currentCamera
                        self.cam = Image(Point(1315, 375), self.imagesPhantom[self.currentCamera - 1])
                        self.cam.draw(win)
                    else:
                        self.lastCamera = self.currentCamera
                        self.cam = Image(Point(1315, 375), self.imagesNone[self.currentCamera - 1])
                        self.cam.draw(win)
                    if reboot.audio == False:
                        self.audioText.draw(win)
                    if reboot.camera == False:
                        self.cameraText.draw(win)
                    if reboot.ventilation == False:
                        self.ventilationText.draw(win)
                    if menu.radar == True:
                        self.radar = Text(Point(780, 680), str(animatronic.pos))
                        self.radar.setTextColor("Red")
                        self.radar.setSize(36)
                        self.radar.setFace("times roman")
                        self.radar.draw(win)
                else:
                    for point in self.ventPOINTS:
                        x = point[0]
                        y = point[1]
                        if pos.getX() > x and pos.getX() < x + 85 and pos.getY() > y and pos.getY() < y + 58:
                            self.switchCamera.stop()
                            self.switchCamera.play()
                            self.cam.undraw()
                            self.ventText.undraw()
                            self.audioText.undraw()
                            self.cameraText.undraw()
                            self.ventilationText.undraw()
                            self.radar.undraw()
                            self.phantom = False
                            self.jumpscareTimer = 0
                            if reboot.camera == False:
                                self.lastCamera = cameraNum + 11
                                self.currentVent = cameraNum + 11
                                self.cam = Image(Point(1315, 375), self.imagesError[self.lastCamera - 1])
                                self.cam.draw(win)
                            elif cameraNum + 11 == animatronic.pos:
                                self.lastCamera = cameraNum + 11
                                self.currentVent = cameraNum + 11
                                self.cam = Image(Point(1315, 375), self.imagesSpringtrap[self.currentVent - 1])
                                self.cam.draw(win)
                            else:
                                self.lastCamera = cameraNum + 11
                                self.currentVent = cameraNum + 11
                                self.cam = Image(Point(1315, 375), self.imagesNone[self.currentVent - 1])
                                self.cam.draw(win)
                            self.ventText.draw(win)
                            if reboot.audio == False:
                                self.audioText.draw(win)
                            if reboot.camera == False:
                                self.cameraText.draw(win)
                            if reboot.ventilation == False:
                                self.ventilationText.draw(win)
                            if menu.radar == True:
                                self.radar = Text(Point(780, 680), str(animatronic.pos))
                                self.radar.setTextColor("Red")
                                self.radar.setSize(36)
                                self.radar.setFace("times roman")
                                self.radar.draw(win)
                        cameraNum += 1
        if win.checkKey() == "Return" and self.toggleCamera == True and room.lights:
            self.closeVent.stop()
            self.closeVent.play()
            Vent.vents[self.currentVent - 11].open_close()
        if self.phantom == True:
            self.jumpscareTimer += 1
        if self.jumpscareTimer >= 120 - (int(menu.night) - 1) * 20:
            self.phantom = False
            self.jumpscareTimer = 0
            if self.lastCamera == 4:
                if menu.noErrors == False:
                    reboot.audio = False
                room.mangle.stop()
                room.mangle.play()
                room.mangleJumpscare.draw(win)
                for i in range(100):
                    room.moveCounter()
                    if i == 50:
                        room.breathing.stop()
                        room.breathing.play()
                    time.sleep(.01)
                room.mangleJumpscare.undraw()
            elif self.lastCamera == 7:
                if menu.noErrors == False:
                    reboot.ventilationTimer = 8999 - 750 * (int(menu.night) - 1)
                    reboot.ventilation = False
                room.jumpscare.stop()
                room.jumpscare.play()
                room.chicaJumpscare.draw(win)
                for i in range(100):
                    room.moveCounter()
                    if i == 50:
                        room.breathing.stop()
                        room.breathing.play()
                    time.sleep(.01)
                room.chicaJumpscare.undraw()
            elif self.lastCamera == 8:
                room.puppet.stop()
                room.puppet.play()
                room.puppetJumpscare.draw(win)
                for i in range(1000):
                    room.moveCounter()
                    time.sleep(.01)
                room.puppetJumpscare.undraw()
            else:
                if menu.noErrors == False:
                    reboot.ventilationTimer = 8999 - 750 * (int(menu.night) - 1)
                    reboot.ventilation = False
                room.jumpscare.stop()
                room.jumpscare.play()
                room.balloonBoyJumpscare.draw(win)
                for i in range(100):
                    room.moveCounter()
                    if i == 50:
                        room.breathing.stop()
                        room.breathing.play()
                    time.sleep(.01)
                room.balloonBoyJumpscare.undraw()
            self.cam.undraw()
            self.ventText.undraw()
            self.audioText.undraw()
            self.cameraText.undraw()
            self.ventilationText.undraw()
            self.radar.undraw()
            if reboot.camera == False:
                self.cam = Image(Point(1315, 375), self.imagesError[self.lastCamera - 1])
                self.cam.draw(win)
            elif self.lastCamera == animatronic.pos:
                self.cam = Image(Point(1315, 375), self.imagesSpringtrap[self.currentCamera - 1])
                self.cam.draw(win)
            else:
                self.cam = Image(Point(1315, 375), self.imagesNone[self.currentCamera - 1])
                self.cam.draw(win)
            if reboot.audio == False:
                self.audioText.draw(win)
            if reboot.camera == False:
                self.cameraText.draw(win)
            if reboot.ventilation == False:
                self.ventilationText.draw(win)
            if menu.radar == True:
                self.radar = Text(Point(780, 680), str(animatronic.pos))
                self.radar.setTextColor("Red")
                self.radar.setSize(36)
                self.radar.setFace("times roman")
                self.radar.draw(win)

    def closeCamera(self):
        """undraws the camera"""
        self.cam.undraw()
        self.ventText.undraw()
        self.audioText.undraw()
        self.cameraText.undraw()
        self.ventilationText.undraw()
        self.radar.undraw()
        self.image.undraw()
        self.openingCamera.stop()
        self.closingCamera.play()
        self.closeVent.stop()
        self.switchCamera.stop()
        self.audio.stop()

class RebootScreen(object):
    """The screen with the reboot"""
    def __init__(self, pos:tuple, room, night, animatronic, win:GraphWin):
        self.pos = pos
        self.screen = Image(Point(pos[0],pos[1]),"reboot screen.png")
        self.isActive = False
        self.audio = True
        self.camera = True
        self.ventilation = True
        self.audioLimit = 8 - int(night.readNight())
        self.audioTimer = 700
        self.cameraTimer = 0
        self.ventilationTimer = 0
        self.rebootingTimer = 0
        self.systems = [self.camera, self.ventilation, self.audio]
        self.errors = [Image(Point(self.pos[0] + 192, self.pos[1] - 124),"error.png"),Image(Point(self.pos[0] + 192, self.pos[1] -48),"error.png"),Image(Point(self.pos[0] + 192, self.pos[1] + 35),"error.png")]
        self.openingReboot = MediaPlayer("Audio/Open Reboot.wav")
        self.closingReboot = MediaPlayer("Audio/Close Reboot.wav")
        self.rebooting = MediaPlayer("Audio/Rebooting.mp3")
        self.POINTS = [[306, 515], [306, 600], [306, 685], [306, 825]]

    def fixProblem(self, number, pos, room, win):
        """fixes a specific error"""
        self.rebooting.play()
        self.rebootingTimer = 0
        reboot = True
        while self.rebootingTimer < 500 and reboot:
            win.update()
            room.moveCounter()
            if animatronic.alive == False or room.clock == "6":
                self.undisplayScreen()
                reboot = False
            self.rebootingTimer += 1
            time.sleep(.01)
        self.rebooting.stop()
        if reboot:
            if number == 0:
                if camera.lastCamera == animatronic.pos:
                    camera.cam = Image(Point(1315, 375), camera.imagesSpringtrap[camera.lastCamera - 1])
                else:
                    camera.cam = Image(Point(1315, 375), camera.imagesNone[camera.lastCamera - 1])
                self.camera = True
                self.cameraTimer = 0
                self.errors[1].undraw()
            elif number == 1:
                self.ventilation = True
                self.ventilationTimer = 0
                self.errors[2].undraw()
                if room.lights == False:
                    room.ventilationOff.stop()
                    room.ventilationOn.stop()
                    room.ventilationOn.play()
                    room.image.move(-5000, 0)
                    room.springtrapAtTheWindow.move(-5000, 0)
                    room.springtrapAtTheDoor.move(-5000, 0)
                    room.lights = True
            elif number == 2:
                self.audio = True
                self.audioLimit = 8 - int(night.readNight())
                self.errors[0].undraw()
    def fixAll(self, pos, room, win):
        """fixes all the errors"""
        self.rebooting.play()
        self.rebootingTimer = 0
        reboot = True
        while self.rebootingTimer < 800 and reboot:
            win.update()
            room.moveCounter()
            if animatronic.alive == False or room.clock == "6":
                self.undisplayScreen()
                reboot = False
            self.rebootingTimer += 1
            time.sleep(.01)
        self.rebooting.stop()
        if reboot:
            self.audio = True
            self.audiolimit = 8 - int(night.readNight())
            self.camera = True
            self.cameraTimer = 0
            if camera.lastCamera == animatronic.pos:
                camera.cam = Image(Point(1315, 375), camera.imagesSpringtrap[camera.lastCamera - 1])
            else:
                camera.cam = Image(Point(1315, 375), camera.imagesNone[camera.lastCamera - 1])
            self.ventilation = True
            if room.lights == False:
                room.ventilationOff.stop()
                room.ventilationOn.stop()
                room.ventilationOn.play()
                room.image.move(-5000, 0)
                room.springtrapAtTheWindow.move(-5000, 0)
                room.springtrapAtTheDoor.move(-5000, 0)
                room.lights = True
            counter = 0
            for i in self.systems:
                i = True
                self.errors[counter].undraw()
                counter += 1
    def displayScreen(self):
        """adds the reboot screen and errors to the window"""
        self.screen.draw(win)
        self.isActive = True
        if self.audio == False:
            self.errors[0].draw(win)
        if self.camera == False:
            self.errors[1].draw(win)
        if self.ventilation == False:
            self.errors[2].draw(win)
    def undisplayScreen(self):
        """removes the reboot screen and errors from the window"""
        self.isActive = False
        for i in self.errors:
            i.undraw()
        self.openingReboot.stop()
        self.closingReboot.play()
        self.rebooting.stop()
        self.screen.undraw()

    def checkReboot(self, pos, room, win):
        """displays the reboot screen when the mouse is on it"""
        if pos.getX() < win.getWidth() * 2 / 3 and pos.getX() > win.getWidth() / 3 and pos.getY() > win.getHeight() * 3 / 4 and room.x < 1000:
            self.closingReboot.stop()
            self.openingReboot.play()
            self.displayScreen()
            while pos.getX() < win.getWidth() * 3 / 4 and animatronic.alive and room.clock != "6":
                win.update()
                pos = win.getCurrentMouseLocation()
                self.checkButtons(pos, room, win)
                room.moveCounter()
                time.sleep(.01)
            self.undisplayScreen()

    def checkButtons(self, pos, room, win):
        """checks if a system has been clicked"""
        pos = win.checkMouse()
        counter = 0
        if pos != None:
            for point in self.POINTS:
                counter += 1
                x = point[0]
                y = point[1]
                if pos.getX() > x and pos.getX() < x + 415 and pos.getY() > y and pos.getY() < y + 50:
                    if counter == 1:
                        self.fixProblem(2, pos, room, win)
                    if counter == 2:
                        self.fixProblem(0, pos, room, win)
                    if counter == 3:
                        self.fixProblem(1, pos, room, win)
                    if counter == 4:
                        self.fixAll(pos, room, win)

class Vent(object):
    vents = []
    def __init__(self, name):
        self.name = name
        self.is_closed = False
        Vent.vents.append(self)

    def __str__(self):
        string = ""
        for i in Vent.vents:
            string += str(i.name) + ": " + i.is_closed
        return string

    def open_close(self):
        """opens the vent if closed, closes the vent if open"""
        for vent in Vent.vents:
            if vent.is_closed:
                vent.is_closed = False
        self.is_closed = True

vent1 = Vent("vent1")
vent2 = Vent("vent2")
vent3 = Vent("vent3")
vent4 = Vent("vent4")
vent5 = Vent("vent5")

class Animatronic(object):
    def __init__(self):
        self.alive = True
        self.pos = random.randint(7, 9)
        self.target = 0

    def __str__(self):
        string = "Pos: " + str(self.pos)
        return string

    def distract(self, num):
        """sets springtraps target to be something other than the office"""
        self.target = num

    def move(self):
        """changes springTrap's position"""
        camera = self.pos
        if camera == 1:
            self.pos = 0
        elif camera == 2:
            if self.target == (3 or 4 or 5):
                chance = random.randrange(10)
                if chance != 0:
                    self.pos = self.target
                else:
                    if vent5.is_closed == True:
                        chance = random.randint(0, 100)
                        if chance <= 11:
                            self.pos = 15
                        elif chance <= 25:
                            self.pos = 3
                        elif 25 < chance <= 50:
                            self.pos = 4
                        elif 50 < chance <= 75:
                            self.pos = 5
                        elif 75 < chance <= 100:
                            self.pos = 16
                    else:
                        self.pos = 15
            else:
                if vent5.is_closed == True:
                    chance = random.randint(0, 100)
                    if chance <= 11:
                        self.pos = 15
                    elif chance <= 25:
                        self.pos = 3
                    elif 25 < chance <= 50:
                        self.pos = 4
                    elif 50 < chance <= 75:
                        self.pos = 5
                    elif 75 < chance <= 100:
                        self.pos = 16
                else:
                    self.pos = 15
            self.target = 0

        elif camera == 3:
            if self.target == (3 or 4):
                chance = random.randrange(10)
                if chance != 0:
                    self.pos = self.target
                else:
                    chance = random.randint(1, 4)
                    if chance == 1:
                        self.pos = 4
                    else:
                        self.pos = 2
            else:
                chance = random.randint(1, 4)
                if chance == 1:
                    self.pos = 4
                else:
                    self.pos = 2
            self.target = 0

        elif camera == 4:
            if self.target == (2 or 3 or 5):
                chance = random.randrange(10)
                if chance != 0:
                    self.pos = self.target
                else:
                    chance = random.randint(0, 1)
                    if chance == 0:
                        self.pos = 3
                    else:
                        self.pos = 5
            else:
                chance = random.randint(0, 1)
                if chance == 0:
                    self.pos = 3
                else:
                    self.pos = 5
            self.target = 0
        elif camera == 5:
            if self.target == (2 or 3 or 4 or 6 or 8):
                chance = random.randrange(10)
                if chance != 0:
                    self.pos = self.target
                else:
                    if vent3.is_closed == True:
                        chance = random.randint(0, 100)
                        if chance <= 11:
                            self.pos = 13
                        elif chance <= 50:
                            self.pos = 6
                        elif 50 < chance <= 75:
                            self.pos = 8
                        else:
                            self.pos = 4
                    else:
                        self.pos = 13
            if vent3.is_closed == True:
                chance = random.randint(0, 100)
                if chance <= 11:
                    self.pos = 13
                elif chance <= 50:
                    self.pos = 6
                elif 50 < chance <= 75:
                    self.pos = 8
                else:
                    self.pos = 4
            else:
                self.pos = 13
            self.target = 0
        elif camera == 6:
            if self.target == (5 or 7 or 8):
                chance = random.randrange(10)
                if chance != 0:
                    self.pos = self.target
                else:
                    chance = random.randint(0, 1)
                    if chance == 0:
                        self.pos = 5
                    else:
                        self.pos = 7
            else:
                chance = random.randint(0, 1)
                if chance == 0:
                    self.pos = 5
                else:
                    self.pos = 7
            self.target = 0
        elif camera == 7:
            if self.target == (5 or 6 or 8):
                chance = random.randrange(10)
                if chance != 0:
                    self.pos = self.target
                else:
                    if vent2.is_closed == True:
                        chance = random.randint(0, 100)
                        if chance <= 11:
                            self.pos = 12
                        elif chance <= 50:
                            self.pos = 6
                        else:
                            self.pos = 8
                    else:
                        self.pos = 12

            else:
                if vent2.is_closed == True:
                    chance = random.randint(0, 100)
                    if chance <= 11:
                        self.pos = 12
                    elif chance <= 50:
                        self.pos = 6
                    else:
                        self.pos = 8
                else:
                    self.pos = 12
            self.target = 0
        elif camera == 8:
            if self.target == (5 or 7 or 9):
                chance = random.randrange(10)
                if chance != 0:
                    self.pos = self.target
                else:
                    chance = random.randint(1, 3)
                    if chance == 1:
                        self.pos = 5
                    elif chance == 2:
                        self.pos = 9
                    else:
                        self.pos = 7
            else:
                chance = random.randint(1, 3)
                if chance == 1:
                    self.pos = 5
                elif chance == 2:
                    self.pos = 9
                else:
                    self.pos = 7
            self.target = 0
        elif camera == 9:
            if self.target == (8 or 10):
                chance = random.randrange(10)
                if chance != 0:
                    self.pos = self.target
                else:
                    if vent1.is_closed == True:
                        chance = random.randint(0, 100)
                        if chance <= 11:
                            self.pos = 11
                        elif chance <= 50:
                            self.pos = 10
                        else:
                            self.pos = 8
                    else:
                        self.pos = 11
            else:
                if vent1.is_closed == True:
                    chance = random.randint(0, 100)
                    if chance <= 11:
                        self.pos = 11
                    elif chance <= 50:
                        self.pos = 10
                    else:
                        self.pos = 8
                else:
                    self.pos = 11
            self.target = 0
        elif camera == 10:
            if self.target == 9:
                chance = random.randrange(10)
                if chance != 0:
                    self.pos = self.target
                else:
                    if vent4.is_closed == True:
                        chance = random.randint(0, 100)
                        if chance <= 11:
                            self.pos = 14
                        else:
                            self.pos = 9
                    else:
                        self.pos = 9
            else:
                if vent4.is_closed == True:
                    chance = random.randint(0, 100)
                    if chance <= 11:
                        self.pos = 14
                    else:
                        self.pos = 9
                else:
                    self.pos = 9
            self.target = 0

        elif camera == 11:
            if vent1.is_closed == True:
                self.pos = 9
            else:
                if self.target != 9:
                    self.pos = 1
                else:
                    chance = random.randrange(4)
                    if chance != 0:
                        self.pos = 9
                    else:
                        self.pos = 1
            self.target = 0
        elif camera == 12:
            if vent2.is_closed == True:
                self.pos = 7
            else:
                if self.target != 7:
                    self.pos = 1
                else:
                    chance = random.randrange(4)
                    if chance != 0:
                        self.pos = 7
                    else:
                        self.pos = 1
            self.target = 0
        elif camera == 13:
            if vent3.is_closed == True:
                self.pos = 5
            else:
                if self.target != 5:
                    self.pos = 16
                else:
                    chance = random.randrange(4)
                    if chance != 0:
                        self.pos = 5
                    else:
                        self.pos = 16
            self.target = 0
        elif camera == 14:
            if vent4.is_closed == True:
                self.pos = 10
            else:
                if self.target != 10:
                    self.pos = 17
                else:
                    chance = random.randrange(4)
                    if chance != 0:
                        self.pos = 10
                    else:
                        self.pos = 17
            self.target = 0
        elif camera == 15:
            if vent5.is_closed == True:
                self.pos = 2
            else:
                if self.target != 2:
                    self.pos = 17
                else:
                    chance = random.randrange(4)
                    if chance != 0:
                        self.pos = 2
                    else:
                        self.pos = 17
            self.target = 0
        elif camera == 16:  # at the window
            if self.target != 2:
                self.pos = 1
            else:
                chance = random.randrange(10)
                if chance != 0:
                    self.pos = 2
                else:
                    self.pos = 1
            self.target = 0

        elif camera == 0:  # at the doorway
            if self.target == 1:
                chance = random.randrange(10)
                if chance != 0:
                    self.pos = 1
                else:
                    self.alive = False
            else:
                self.alive = False
            self.target = 0

        elif camera == 17:  # to the right
            if self.target == 2:
                chance = random.randrange(10)
                if chance != 0:
                    self.pos = 2
                else:
                    self.alive = False
            elif self.target == 10:
                chance = random.randrange(10)
                if chance != 0:
                    self.pos = 10
                else:
                    self.alive = False
            else:
                self.alive = False


class Night(object):
    def __init__(self):
        try: # checks if nightInfo file exists
            self.file = open("nightInfo", "r")
        except FileNotFoundError:
            self.file = open("nightInfo", "w")  # creates the night file
            self.file.close()
        if self.readNight() != "": #checks if the file is blank
            self.night = self.readNight()
        else:
            self.night = 1
            self.file = open('nightInfo',"w")
            self.file.write(str(self.night))
            self.file.close()
        try: # checks if star file exists
            self.file = open("starInfo","r")
        except FileNotFoundError:
            self.file = open("starInfo","w")
            self.file.close()
        if self.readStar() != "":
            self.star = self.readStar()
        else:
            self.star = 0
            self.file = open("starInfo","w")
            self.file.write(str(self.star))
            self.file.close()

    def __str__(self):
        string = "Night: " + str(self.night) + "\n"
        string += "Star: " + str(self.star)
        return string

    def saveNight(self):
        """increases the night by 1 and saves it to NightInfo"""
        self.night = str(int(self.night) + 1)
        nightInfo = open("nightInfo","w")
        nightInfo.write(self.night)
        nightInfo.close()

    def readNight(self):
        """returns what night you're on from NightInfo"""
        nightInfo = open("nightInfo","r")
        night = nightInfo.read()
        nightInfo.close()
        return night

    def saveStar(self):
        """increases the star count by 1 and saves it"""
        self.star = str(int(self.star) + 1)
        starInfo = open("starInfo","w")
        starInfo.write(self.star)
        starInfo.close()

    def readStar(self):
        """returns the number of stars"""
        starInfo = open("starInfo","r")
        star = starInfo.read()
        return star

    def reset(self):  # happens when you make a new game
        """resets the night count"""
        self.night = 1
        nightInfo = open("nightInfo","w")
        nightInfo.write(str(self.night))
        nightInfo.close()

win = GraphWin("FNAF 3", 1920, 1080)
win.setBackground('Black')
gameover = True
night = Night()
menu = Menu("menu.png", night, win)
while not win.closed:
    menu.runMenu(gameover)
    gameover = False
    animatronic = Animatronic()
    room = Room("Room.png", 15, animatronic, win)
    reboot = RebootScreen((630, 660), room, night, animatronic, win)
    camera = Camera("camera2None.png", animatronic, reboot, room, win)

    while animatronic.alive and room.clock != "6":
        win.update()
        pos = win.getCurrentMouseLocation()
        room.move(pos)
        camera.checkCamera(pos, room, win)
        reboot.checkReboot(pos, room, win)
    room.closeRoom()
    if not animatronic.alive:
        gameover = True
        room.springtrapJumpscare.draw(win)
        room.jumpscare.stop()
        room.jumpscare.play()
        timer = 0
        while timer < 200:
            timer += 1
            time.sleep(.01)
        room.springtrapJumpscare.undraw()
        room.gameOver.draw(win)
        room.gameOverAudio.play()
        timer = 0
        while timer < 1500:
            timer += 1
            time.sleep(.01)
        room.gameOver.undraw()
        room.gameOverAudio.stop()
        room.jumpscare.stop()
    if gameover == False and int(menu.night) < 5:
        night.saveNight()
        room.sixAM.draw(win)
        room.sixAMAudio.play()
        timer = 0
        while timer < 1000:
            timer += 1
            time.sleep(.01)
        room.sixAM.undraw()
        room.sixAMAudio.stop()
    elif gameover == False and int(menu.night) == 5 and int(night.readStar()) == 0:
        night.saveStar()
    elif gameover == False and int(menu.night) == 6 and int(night.readStar()) == 1:
        night.saveStar()
    elif gameover == False and int(menu.night) == 6 and int(night.readStar()) == 2 and menu.fastNight == False and menu.radar == False and menu.agressive == True and menu.noErrors == False:
        night.saveStar()
    if gameover == False and int(menu.night) == 5:
        gameover = True
        room.sixAM.draw(win)
        room.sixAMAudio.play()
        timer = 0
        while timer < 1000:
            timer += 1
            time.sleep(.01)
        room.sixAM.undraw()
        room.night5End.draw(win)
        room.goodEnding.play()
        timer = 0
        while timer < 2000:
            timer += 1
            time.sleep(.01)
        room.night5End.undraw()
        room.goodEnding.stop()
    elif gameover == False and int(menu.night) == 6:
        gameover = True
        room.sixAM.draw(win)
        room.sixAMAudio.play()
        timer = 0
        while timer < 1000:
            timer += 1
            time.sleep(.01)
        room.sixAM.undraw()
        room.night6End.draw(win)
        room.night6Ending.play()
        click = None
        timer = 0
        while timer < 2000:
            timer += 1
            time.sleep(.01)
        room.night6End.undraw()
        room.night6Ending.stop()
