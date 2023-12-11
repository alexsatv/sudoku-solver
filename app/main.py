import pygame
from solver import SudokuSolver
from typing import Tuple

class GUI():
    def __init__(self) -> None:
        self._running = True
        self.screen = None
        self.size = self.width, self.height = 500, 600
        self.dif = 500 / 9
        self.font1 = None
        self.font2 = None
        self.current_cell = None
        self.highlight = False
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.button_width = 150
        self.button_height = 50
        self.button_x = (self.width - self.button_width) // 2
        self.button_y = self.height - 75
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.keys = {
            pygame.K_1: 1,
            pygame.K_2: 2,
            pygame.K_3: 3,
            pygame.K_4: 4,
            pygame.K_5: 5,
            pygame.K_6: 6,
            pygame.K_7: 7,
            pygame.K_8: 8,
            pygame.K_9: 9
        }

    def on_init(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((500, 600))
        pygame.font.init()
        self.font1 = pygame.font.SysFont("comicsans", 40)
        self.font2 = pygame.font.SysFont("comicsans", 20)
        self._running = True

    def on_event(self, event: pygame.event) -> None:
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos_x, pos_y = pos
            if self.button_x <= pos_x <= self.button_x + self.button_width and self.button_y <= pos_y <= self.button_y + self.button_height:
                self.solve()
            else:
                column, row = self.get_coordinate(pos)
                self.current_cell = (column, row)
                self.highlight = True
        if event.type == pygame.KEYDOWN:
            if self.current_cell != None:
                if event.key in self.keys:
                    pressed_number = self.keys[event.key]
                    self.board[self.current_cell[0]][self.current_cell[1]] = pressed_number
                if event.key == pygame.K_BACKSPACE:
                    self.board[self.current_cell[0]][self.current_cell[1]] = 0

    def on_loop(self) -> None:
        pass

    def on_render(self) -> None:
        self.screen.fill((255, 255, 255))
        if self.highlight == True and self.current_cell is not None:
            pygame.draw.rect(self.screen, (167, 235, 194), (self.current_cell[0] * self.dif, self.current_cell[1] * self.dif, self.dif + 1, self.dif + 1))
        self.draw()
        solve_button = pygame.draw.rect(self.screen, self.BLACK, (self.button_x, self.button_y, self.button_width, self.button_height))
        text = self.font1.render('Solve', True, self.WHITE)
        text_rect = text.get_rect(center=solve_button.center)
        self.screen.blit(text, text_rect)
        pygame.display.update()

    def on_cleanup(self) -> None:
        pygame.quit()
 
    def on_execute(self) -> None:
        if self.on_init() == False:
            self._running = False
 
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def get_coordinate(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        x = pos[0] // self.dif
        y = pos[1] // self.dif
        return int(x), int(y)

    def draw(self) -> None:
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    text1 = self.font1.render(str(self.board[i][j]), 1, (0, 0, 0))
                    text_rect = text1.get_rect(center=(i * self.dif + self.dif / 2, j * self.dif + self.dif / 2))
                    self.screen.blit(text1, text_rect)

        for i in range(10):
            thick = 7 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.dif), (500, i * self.dif), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i * self.dif, 0), (i * self.dif, 500), thick)

    def solve(self) -> None:
        solver = SudokuSolver(self.board)
        solution = solver.solved
        if solution == "Couldn't find solution":
            print(solution)
        else:
            self.board = solution

if __name__ == "__main__" :
    program = GUI()
    program.on_execute()