import pygame
pygame.init()

display_width = 640
display_height = 480
COLS_GAME = 7
ROWS_GAME = 6
WHITE = (255, 255, 255)


board_imgs = [pygame.image.load('assets/slot.png'),pygame.image.load('assets/red.png'),pygame.image.load('assets/black.png')] 
for x in range(3):
	temp = board_imgs[x]
	temp = pygame.transform.scale(temp, (50, 50))
	board_imgs[x] = temp
screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
tops = [ROWS_GAME-1, ROWS_GAME-1, ROWS_GAME-1, ROWS_GAME-1, ROWS_GAME-1, ROWS_GAME-1,ROWS_GAME-1]
turn = 0

def draw_board():
	for x in range(ROWS_GAME):
		for y in range(COLS_GAME):
			l = 100+y*50
			t = 100+x*50
			if board[x][y]!=0:
				screen.blit(board_imgs[board[x][y]],(l,t))
			screen.blit(board_imgs[0],(l,t))

def play_move(col):
	if tops[col]==-1:
		return
	global turn, board, tops
	board[tops[col]][col] = turn%2 + 1
	tops[col]-=1
	turn+=1

while True:
	mx,my = 0,0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.MOUSEBUTTONUP:
			mx,my = event.pos
			if mx>=100 and mx<=450 and my>=100 and my<=400:
				play_move(int((mx-100)/50))
	screen.fill(WHITE)
	draw_board()
	pygame.display.flip()
	clock.tick(60)
