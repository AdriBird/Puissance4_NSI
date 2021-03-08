extends Node2D

var loadpion = load("res://scenes/pion_j2.tscn")

func _ready():
	pass

func _on_col1_pressed():
	var genpion = loadpion.instance()
	add_child(genpion)
	
