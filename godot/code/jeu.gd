extends Node2D


func _ready():
	pass

func _on_col1_pressed():
	var loadpion = load("res://scenes/pion_j2.tscn")
	var genpion = loadpion.instance()
	add_child(genpion)
	Global.posi_pion = get_node("boutons/col1").rect_position.x + 30
	get_node("pion_j2").position.x = get_node("boutons/col1").rect_position.x + 30
	
	


func _on_col2_pressed():
	var loadpion = load("res://scenes/pion_j2.tscn")
	var genpion = loadpion.instance()
	add_child(genpion)
	get_node("pion_j2").position.x = get_node("boutons/col2").rect_position.x


func _on_col3_pressed():
	var loadpion = load("res://scenes/pion_j2.tscn")
	var genpion = loadpion.instance()
	add_child(genpion)
	get_node("pion_j2").position.x = get_node("boutons/col3").rect_position.x


func _on_col4_pressed():
	var loadpion = load("res://scenes/pion_j2.tscn")
	var genpion = loadpion.instance()
	add_child(genpion)
	get_node("pion_j2").position.x = get_node("boutons/col4").rect_position.x


func _on_col5_pressed():
	var loadpion = load("res://scenes/pion_j2.tscn")
	var genpion = loadpion.instance()
	add_child(genpion)
	get_node("pion_j2").position.x = get_node("boutons/col5").rect_position.x


func _on_col6_pressed():
	var loadpion = load("res://scenes/pion_j2.tscn")
	var genpion = loadpion.instance()
	add_child(genpion)
	get_node("pion_j2").position.x = get_node("boutons/col6").rect_position.x


func _on_col7_pressed():
	var loadpion = load("res://scenes/pion_j2.tscn")
	var genpion = loadpion.instance()
	add_child(genpion)
	get_node("pion_j2").position.x = get_node("boutons/col7").rect_position.x
