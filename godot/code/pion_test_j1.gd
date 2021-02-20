extends KinematicBody2D

var vel = Vector2()
const gravity = 800



func _physics_process(delta):
	vel.y += gravity * delta
	move_and_slide(vel)
