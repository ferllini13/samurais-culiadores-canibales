import pygame
import sys
from pygame.locals import *

pygame.mixer.init()
pygame.mixer.music.load("sound.mp3")
back_sound= pygame.mixer.Sound("back.wav")
pygame.mixer.music.play()

BLACK = (0,0,0)
WHITE = (255, 255, 255)

#se cra la clase cursor, que es un rectangulo qeu sigue al mouse
class cursor(pygame.Rect):
	def __init__(self):
		pygame.Rect.__init__(self,0,0,1,1)#cursos inicia en coordenadas 0,0 y es de 1x1
	def update(self):#actualiza la pocision del cursos dependiendo de la del mouse
		self.left,self.top=pygame.mouse.get_pos()#capta la posicion del mouse

#se crea la clase para los button para los botones
class button(pygame.sprite.Sprite):#se crea la clase para los botones
	def __init__(self,pic1,pic2,x,y):#se define cada boton con dos imagenes y las coordenadas
		self.unselected_pic=pic1#se define como se vera la imagen sin seleccionar
		self.selected_pic=pic2 #se define como se vera la imagen seleccionada
		self.basic_pic=self.unselected_pic #se define una imagen bacica qie inicia como la no seleccionada
		self.rect=self.basic_pic.get_rect()
		self.rect.left,self.rect.top=(x,y)
<<<<<<< HEAD

	def update(self,screen,cursor):#se actializa el boton
		if cursor.colliderect(self.rect):#se define la condicion cuando el cursor se pocisione sobre el boton
			self.basic_pic=self.selected_pic
		else: self.basic_pic=self.unselected_pic #condicion del boton en stand by
		screen.blit(self.basic_pic,self.rect)#que se actualiza la pantalla dependiendo de la accion condicional

=======
>>>>>>> 93113cc4964bd9d81477beb4c7819d9bb2892434

	def update(self,screen,cursor):#se actializa el boton
		if cursor.colliderect(self.rect):#se define la condicion cuando el cursor se pocisione sobre el boton
			self.basic_pic=self.selected_pic
		else: self.basic_pic=self.unselected_pic #condicion del boton en stand by
		screen.blit(self.basic_pic,self.rect)#que se actualiza la pantalla dependiendo de la accion condicional


def sizesWin(text1,y,screen):
	#Title picture and buttons
	wallp4=pygame.image.load("wall4.jpg").convert()
	salir=pygame.image.load("play.png")
	salir2=pygame.image.load("play2.png")

	
	#Define buttons
	bexit=button(salir,salir2,500,600)
	
	#Variables
	lenghtW=0
	textBuffer = ''
	begin=True
	place=120
	cursor1=cursor()
<<<<<<< HEAD

=======
>>>>>>> 93113cc4964bd9d81477beb4c7819d9bb2892434
	pygame.init()
	
	#Events and updates
	while begin==True:
		#Updates

		screen.blit(wall4,(0,0))
		cursor1.update()
		bcrear.update(screen,cursor1)
		bsalir


		bcrear.update(screen,cursor1)
		
		back=pygame.image.load("back.png")
		back2=pygame.image.load("back2.png")
		bback=button(back,back2,10,5)
		

		#Makes the labels
		myfont= pygame.font.SysFont("monospace",25)
		myfont2= pygame.font.SysFont("monospace",16)

<<<<<<< HEAD


		labelInd= myfont.render(text1,1,WHITE)



		screen.blit(labelInd,(10,y))





=======
		labelInd= myfont.render(text1,1,WHITE)

		screen.blit(labelInd,(10,y))

>>>>>>> 93113cc4964bd9d81477beb4c7819d9bb2892434
		for event in pygame.event.get():
			#Events on keyboard, for the entry
			if event.type==pygame.KEYDOWN:
				
				#Limit the keys allowed to numbers
				if event.key<=122 and event.key>=97 and lenghtW<15*10:
					#This creates the text of the entry
					textBuffer=textBuffer+chr(event.key)
					lenghtW+=15
					place=place+15
					myfont= pygame.font.SysFont("monospace",25)
					label=myfont.render(chr(event.key),1,BLACK)
					screen.blit(label,(place,y))

<<<<<<< HEAD


=======
>>>>>>> 93113cc4964bd9d81477beb4c7819d9bb2892434
				elif event.key<=57 and event.key>=48 and lenghtW<15*10:
					#This creates the text of the entry
					textBuffer=textBuffer+chr(event.key)
					lenghtW+=15
					place=place+15
					myfont= pygame.font.SysFont("monospace",25)
					label=myfont.render(chr(event.key),1,BLACK)
					screen.blit(label,(place,y))


				#To delete the words
				elif event.key == pygame.K_BACKSPACE and len(textBuffer)>0:
					textBuffer=textBuffer[:-1]
					lenghtW-=15
					place=place-15
					myfont= pygame.font.SysFont("monospace",25)
					label=myfont.render(textBuffer,1,BLACK)
					screen.blit(wallp2,(0,0))
					bback.update(screen,cursor1)
					pygame.draw.rect(screen, WHITE, [130,120, 150, 30],)
					screen.blit(label,(130,y))


				#This saves the entry
				elif event.key==pygame.K_RETURN:
					if len(textBuffer)>0:
						begin=False
						return textBuffer
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if cursor1.colliderect(bback.rect):
					pygame.mixer.pre_init(44100, -16, 1024)
					back_sound.play()
					return main()

			#Submit button
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if cursor1.colliderect(bcrear.rect):
					if len(textBuffer)>0:
						begin=False
						return textBuffer

			#To Close the window
			elif event.type == pygame.QUIT:
				return sys.exit(0)

<<<<<<< HEAD


=======
>>>>>>> 93113cc4964bd9d81477beb4c7819d9bb2892434
		#Update the window		
		pygame.display.flip()


def main():
	pygame.init()
	screen=pygame.display.set_mode([1000,720])
	pygame.display.set_caption("PYWARS")
	wallp=pygame.image.load("wall.jpg").convert()
	wallp2=pygame.image.load("wall2.jpg").convert()
	wallp3=pygame.image.load("wall3.jpg").convert()
<<<<<<< HEAD

=======
>>>>>>> 93113cc4964bd9d81477beb4c7819d9bb2892434
	cursor1=cursor()

	#se inportan las imagenes de los botones
	play=pygame.image.load("play.png")
	play2=pygame.image.load("play2.png")
	instruc=pygame.image.load("instruc.png")
	instruc2=pygame.image.load("instruc2.png")
	salir=pygame.image.load("exit.png")
	salir2=pygame.image.load("exit2.png")
<<<<<<< HEAD
=======
	back=pygame.image.load("back.png")
	back2=pygame.image.load("back2.png")
	start=pygame.image.load("start.png")
	start2=pygame.image.load("start2.png")
	join=pygame.image.load("join.png")
	join2=pygame.image.load("join2.png")
>>>>>>> 93113cc4964bd9d81477beb4c7819d9bb2892434
	
	bplay=button(play,play2,600,200)
	binstruc=button(instruc,instruc2,650,300)
	bexit=button(salir,salir2,700,400)
<<<<<<< HEAD



	back=pygame.image.load("back.png")
	back2=pygame.image.load("back2.png")
	bback=button(back,back2,10,5)


=======
	bback=button(back,back2,10,5)
	bstart=button(start,start2,0,400)
	bjoin=button(join,join2,700,400)
>>>>>>> 93113cc4964bd9d81477beb4c7819d9bb2892434


	while True:
		screen.blit(wallp,(0,0))
		cursor1.update()

		#se actualizan los botones
		bplay.update(screen,cursor1)
		bexit.update(screen,cursor1)
		binstruc.update(screen,cursor1)
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if cursor1.colliderect(bplay.rect):
<<<<<<< HEAD
					return play_main(1)
=======
					return play_main()
>>>>>>> 93113cc4964bd9d81477beb4c7819d9bb2892434
				elif cursor1.colliderect(binstruc.rect):
					return game_instruc()
				elif cursor1.colliderect(bexit.rect):
					pygame.quit()
<<<<<<< HEAD
					sys.exit(0)
			elif event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)         
		pygame.display.flip()


		def play_main(x):
			while True:
				screen.blit(wallp2,(0,0))
				back.update(screen,cursor1)
				cursor1.update()
				for event in pygame.event.get():
					if x==1:
						pygame.draw.rect(screen, WHITE, [130,120, 150, 30],)
						usuario=sizesWin('Usuario:',120,screen)
						print('Welcome '+usuario)
					elif x==2:
						pygame.draw.rect(screen, WHITE, [130,120, 150, 30],)
						usuario=sizesWin('Usuario:',120,screen)
						pygame.draw.rect(screen, WHITE, [130,160, 150, 30],)
						juego=sizesWin('Juego',160,screen)
						print('Welcome '+usuario+' su juego es el '+juego)
					elif event.type == pygame.QUIT:
						pygame.quit()
						sys.exit(0)
					elif event.type == pygame.MOUSEBUTTONDOWN:
=======
					sys.exit()
			elif event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.flip()


		def play_main():
			while True:
				screen.blit(wallp2,(0,0))
				bback.update(screen,cursor1)
				bstart.update(screen,cursor1)
				bjoin.update(screen,cursor1)
				cursor1.update()
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN:
>>>>>>> 93113cc4964bd9d81477beb4c7819d9bb2892434
						if cursor1.colliderect(bback.rect):
							pygame.mixer.pre_init(44100, -16, 1024) 
							back_sound.play()
							return main()
<<<<<<< HEAD
=======
						elif cursor1.colliderect(bstart.rect):
							return start_game()
						elif cursor1.colliderect(bjoin.rect):
							pass
					elif event.type==pygame.QUIT:
						pygame.quit()
						sys.exit()
>>>>>>> 93113cc4964bd9d81477beb4c7819d9bb2892434
				pygame.display.flip()

		def game_instruc():
			while True:
				screen.blit(wallp3,(0,0))
				bback.update(screen,cursor1)
				cursor1.update()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
<<<<<<< HEAD
						sys.exit(0)
=======
						sys.exit()
>>>>>>> 93113cc4964bd9d81477beb4c7819d9bb2892434
					if event.type == pygame.MOUSEBUTTONDOWN:
						if cursor1.colliderect(bback.rect):
							pygame.mixer.pre_init(44100, -16, 1024) 
							back_sound.play()
							return main()
				pygame.display.flip()


<<<<<<< HEAD
=======
def start_game():
	pass


>>>>>>> 93113cc4964bd9d81477beb4c7819d9bb2892434
main()
