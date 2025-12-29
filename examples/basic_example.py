"""
Basic gfxcanvas example
Demonstrates simple shapes and animations
"""

from gfxcanvas import GraphicalCanvas, AnimationType

# Create window
canvas = GraphicalCanvas(800, 600, "Basic Example", fps=60)

# Draw some shapes
circle = canvas.draw_circle(200, 300, 50, fill="#FF5722")
rect = canvas.draw_rectangle(400, 250, 100, 100, fill="#4CAF50")
star = canvas.draw_star(650, 300, 60, 30, points=5, fill="#FFD700")

# Add text
canvas.draw_text("gfxcanvas Demo", 400, 50, 
                font=("Arial", 32, "bold"), color="#FFFFFF")

# Animate circle
canvas.animate(circle, 'y', 300, 500, duration=2.0, 
              easing=AnimationType.EASE_IN_OUT)

# Animate rectangle rotation
canvas.animate(rect, 'rotation', 0, 360, duration=3.0, 
              easing=AnimationType.LINEAR)

# Run application
canvas.run()
