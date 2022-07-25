import pygame

pygame.init()

screen = pygame.display.set_mode((800, 728))  # configura a tela do jogo

running = True
pygame.display.set_caption("RPG center")  # muda o nome da tela do jogo

icone = pygame.image.load('rpg.png')  # carrega a imagem pro programa

pygame.display.set_icon(icone)  # muda o icone perto do nome do jogo

p = input("nome da imagem:")
playerX = 400
playerY = 300
trocaX = 0
trocaY = 0
mover_mouseX = 0
mover_mouseY = 0
backX = 0
backY = 0



player1 = pygame.image.load('sword.png')

background = pygame.image.load('Mapa.jpeg')


def player(X, Y):
    screen.blit(player1, (X, Y))

botao1 = pygame.Rect(100,10,50,30)
botao2 = pygame.Rect(200,10,50,30)

while running:
    x, y = pygame.mouse.get_pos()
    botao_mouse = pygame.mouse.get_pressed(3)
    screen.fill((0, 0, 0))  # adiciona cor em RGB
    screen.blit(background, (backX, backY))
    pygame.draw.rect(screen, (255,255,255),botao1)
    pygame.draw.rect(screen, (255, 255, 255), botao2)
    mover_mouseX, mover_mouseY = pygame.mouse.get_rel() # pega o quanto o mouse deslocou

    if botao_mouse[0] == True:# move o mapa e acionar os botões
        if botao1.collidepoint(x, y):
            print("botão 1 pressionado")
        elif botao2.collidepoint(x,y):
            print("botão 2 pressionado")
        else:
            backX = mover_mouseX + backX
            backY = mover_mouseY + backY
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # pygame.QUIT cria e possibilita o botão X de sair do jogo
            running = False
        if evento.type == pygame.KEYDOWN:
            print("key apertada")
            if evento.key == pygame.K_LEFT:
                trocaX -= 0.3
                print("Key esquerda")
            if evento.key == pygame.K_RIGHT:
                trocaX += 0.3
                print("Key direita")
            if evento.key == pygame.K_DOWN:
                trocaY += 0.3
            if evento.key == pygame.K_UP:
                trocaY -= 0.3
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                trocaX = 0
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_UP:
                trocaY = 0

    #print(botao_mouse)

    playerX = playerX + trocaX
    playerY = playerY + trocaY
    if playerX >= 740:
        playerX = 740
    if playerX <= 0:
        playerX = 0
    player(playerX, playerY)
    # print(botao_mouse[0])
    pygame.display.update()
