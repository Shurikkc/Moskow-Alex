import pygame


size = 1000, 800
screen = pygame.display.set_mode(size)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size),
                                 self.board[y][x])


    def nazatie(self, cell_coords):
        self.board[cell_coords[0]][cell_coords[1]] = -100

    def poziciya(self, mouse_pos):
        if self.left <= mouse_pos[1] < self.left + self.height * self.cell_size and self.top <= mouse_pos[
            0] < self.top + self.width * self.cell_size:
            return (int((mouse_pos[1] - self.left) / self.cell_size), int((mouse_pos[0] - self.top) / self.cell_size))
        else:
            return None

    def get_click(self, mouse_pos):
        cell = self.poziciya(mouse_pos)
        if cell != None:
            self.nazatie(cell)
        if cell == None:
            print(cell)



def main():
    board = Board(5, 7)
    board.set_view(100, 100, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render()
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()