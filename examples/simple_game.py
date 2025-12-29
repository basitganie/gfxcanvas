"""
Simple game example
A bouncing ball game with keyboard controls
"""

from gfxcanvas import GraphicalCanvas, Vector2

# Create window
canvas = GraphicalCanvas(800, 600, "Simple Game", fps=60)

# Create player
player = canvas.create_entity(400, 550, 60, 20, color="#2196F3")

# Create ball
ball = canvas.create_entity(400, 100, 30, 30, 
                           sprite_type='circle', 
                           color="#FF5722")
canvas.set_entity_velocity(ball, 200, 200)

# Score
score = 0
score_text = canvas.draw_text(f"Score: {score}", 400, 30, 
                             font=("Arial", 24, "bold"))

# Game loop
def update(dt):
    global score
    
    # Player movement
    player_pos = canvas.get_entity_position(player)
    speed = 400
    
    if canvas.is_key_pressed('Left') or canvas.is_key_pressed('a'):
        canvas.set_entity_velocity(player, -speed, 0)
    elif canvas.is_key_pressed('Right') or canvas.is_key_pressed('d'):
        canvas.set_entity_velocity(player, speed, 0)
    else:
        canvas.set_entity_velocity(player, 0, 0)
    
    # Update entities
    canvas.update_entity(player, dt)
    canvas.update_entity(ball, dt)
    
    # Keep player on screen
    px, py = canvas.get_entity_position(player)
    if px < 0:
        canvas.set_entity_position(player, 0, py)
    elif px > 740:
        canvas.set_entity_position(player, 740, py)
    
    # Ball collision with walls
    bx, by = canvas.get_entity_position(ball)
    vx, vy = canvas.entities[ball]['velocity']
    
    if bx <= 15 or bx >= 785:
        canvas.set_entity_velocity(ball, -vx, vy)
    if by <= 15:
        canvas.set_entity_velocity(ball, vx, -vy)
    
    # Ball collision with player
    if canvas.check_collision(ball, player):
        canvas.set_entity_velocity(ball, vx, -abs(vy))
        score += 1
        canvas.update_text(score_text, f"Score: {score}")
    
    # Game over
    if by >= 600:
        canvas.pause()
        canvas.draw_text("Game Over!", 400, 300, 
                        font=("Arial", 48, "bold"), color="#FF0000")

# Start game
canvas.start_game_loop(update_callback=update)
canvas.run()
