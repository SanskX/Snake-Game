#módulo
from sys import exit
import pygame
from random import randint
#submódulo
from pygame.locals import *

#criar janela
pygame.init()
l=640
a=480

#posição dos objetos
x_cobra=int(l/2)
y_cobra=int(a/2)

velocidade=10
xc=velocidade
yc=0

x_maça=randint(40,600)
y_maça=randint(50,430)

recorde=0

#texto
pontos=0
fonte=pygame.font.SysFont('georgia',30,bold=True,italic=True)

tela=pygame.display.set_mode((l,a))

#nome do jogo
pygame.display.set_caption('Snake Game')
relógio=pygame.time.Clock()
lista_cobra=[]
comprimento_i=5
morreu=False
#criando função
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela,(0,255,0),(XeY[0],XeY[1], 30, 30))
def reiniciar_jogo():
    global pontos,comprimento_i,x_cobra,y_cobra,lista_cabeça,lista_cobra,x_cobra,x_maça,y_maça,morreu
    pontos=0
    comprimento_i=5
    x_cobra=int(l/2)
    y_cobra=int(a/2)
    lista_cobra=[]
    lista_cabeça=[]
    x_maça=randint(40,600)
    y_maça=randint(50,430)
    morreu=False
#mudar taxa de frames(FPS)
while True:
    relógio.tick(30)
    tela.fill((255,255,255))

    mensagem=f'Pontos: {pontos}'
    texto_formatado=fonte.render(mensagem, False,(0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

#controle do objeto
        if event.type == KEYDOWN:
            if event.key == K_a:
                if xc== velocidade:
                    pass
                else:
                    xc= -velocidade
                    yc=0
            if event.key == K_d:
                if xc== -velocidade:
                    pass
                else:
                    xc= velocidade
                    yc=0
            if event.key == K_w:
                if yc==velocidade:
                    pass
                else:
                    yc= -velocidade
                    xc=0
            if event.key == K_s:
                if yc== -velocidade:
                    pass
                else:
                    yc=velocidade
                    xc=0
    x_cobra=x_cobra+xc
    y_cobra=y_cobra+yc

#desenhando objeto
    cobra=pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,30,30))
    maça=pygame.draw.rect(tela,(255,0,0),(x_maça,y_maça,30,30))

#colisão
    if cobra.colliderect(maça):
        x_maça=randint(40,600)
        y_maça=randint(50,430)
        pontos+=1
        comprimento_i=comprimento_i+2

#lista da cobra
    lista_cabeça=[]
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)
    lista_cobra.append(lista_cabeça)

#game over & reiniciar
    if lista_cobra.count(lista_cabeça)>1:
        fonte2=pygame.font.SysFont('arial',20,True,True)
        mensagem='Game over! Pressione R para jogar novamente'
        texto_formatado=fonte2.render(mensagem,True, (255,0,0))
        ret_texto=texto_formatado.get_rect()
        morreu=True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    exit()
                if event.type==KEYDOWN:
                    if event.key==K_r:
                        reiniciar_jogo()
            ret_texto.center=(l//2,a//2)
            tela.blit(texto_formatado,(ret_texto))
            pygame.display.update()
        ''''''

#não sumir
    if x_cobra>l:
        x_cobra=0
    if x_cobra<0:
        x_cobra=l
    if y_cobra<0:
        y_cobra=a
    if y_cobra>a:
        y_cobra=0

    if len(lista_cobra)>comprimento_i:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)


    tela.blit(texto_formatado,(440,40))
    pygame.display.update()
