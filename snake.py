from tkinter import *
import random
import time

start_time = time.time()
GAME_WIDTH = 1200
GAME_HEIGHT = 800
SPEED = 75
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#141414"

def random_color():
    return"#%06x" % random.randint(0, 0xFFFFFF)

class Snake:
    
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        self.colors = []
        for i in range (0, BODY_PARTS):
            self.coordinates.append([0,0])
            self.colors.append(SNAKE_COLOR)  # start with one consistent color

        for (x, y), color in zip(self.coordinates, self.colors):
            square = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=color, tag="snake")
            self.squares.append(square)



class Food:
     def __init__(self):
        x = random.randint(0,int(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0,int(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]
        self.color = random_color()  # store random color for this food
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=self.color, tag="food")


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x, y))

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        # Use food's color for new body part
        color = food.color
        label.config(text="Score: {} | Last Color: {}".format(score, color))

        canvas.delete("food")

        snake.colors.insert(0, color)
        food = Food()

    else:
         # Keep previous head color if no food was eaten
        snake.colors.insert(0, snake.colors[0])
        del snake.coordinates[-1]
   
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        del snake.colors[-1]
    square = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=snake.colors[0])
    snake.squares.insert(0, square)  
   
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False
def load_high_score():
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except:
        return 0

def save_high_score(new_score):
    with open("highscore.txt", "w") as file:
        file.write(str(new_score))

def game_over():
    canvas.delete(ALL)

    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 - 40,
                       font=('Arial', 70), text="Game Over", fill="red")
    elapsed = int(time.time() - start_time)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 60,
                   font=('Arial', 30), text=f"Time: {elapsed}s", fill="white")


    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 + 20,
                       font=('Arial', 30), text=f"Final Score: {score}", fill="white")

    # Load high score
    high_score = load_high_score()
    if score > high_score:
        save_high_score(score)
        high_score = score
        canvas.delete(ALL)
        canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 - 40,
                    font=('Arial', 70), text="🎉 New High Score!", fill="gold")
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 60,
                    font=('Arial', 30), text=f"Time: {elapsed}s", fill="white")


        canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 + 20,
                       font=('Arial', 30), text=f"Final Score: {score}", fill="white")


    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2 + 100,
                       font=('Arial', 20), text=f"High Score: {high_score}", fill="white")

    # Add buttons
    play_again_btn = Button(window, text="Play Again", font=("Arial",16), command=restart_game)
    play_again_btn.pack(padx=50, pady=50)
    quit_btn = Button(window, text="Quit", font=("Arial", 16), command=window.quit)

    canvas.create_window(GAME_WIDTH / 2, GAME_HEIGHT / 2 + 160, window=play_again_btn)
    canvas.create_window(GAME_WIDTH / 2, GAME_HEIGHT / 2 + 200, window=quit_btn)

def restart_game():
    global snake, food, direction, score

    score = 0
    direction = "down"

    canvas.delete("all")
    label.config(text="Score: 0")

    snake = Snake()
    food = Food()
    next_turn(snake, food)

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text="Score: 0 | Last Color: {}".format(SNAKE_COLOR), font=("Arial", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()


window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y= int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
            

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()