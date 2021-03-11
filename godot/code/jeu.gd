extends Node2D

#var loadpion = load("res://scenes/pion_j2.tscn")

func _ready():
	pass

#func _on_col1_pressed():
#	var dup_pion = get_node("pion_j2").duplicate()
#	get_tree().get_root().add_child(dup_pion)
#	Global.posi_pion = get_node("boutons/col1").rect_position.x - 30
#	#get_node("pion_j2").position.x = get_node("boutons/col1").rect_position.x + 30


#func _on_col2_pressed():
#	get_tree().get_root().add_child(loadpion.instance())
#	Global.posi_pion = get_node("boutons/col2").rect_position.x - 50
#	#get_node("pion_j2").position.x = get_node("boutons/col2").rect_position.x + 30
#
#
#func _on_col3_pressed():
#	get_tree().get_root().add_child(loadpion.instance())
#	Global.posi_pion = get_node("boutons/col3").rect_position.x - 70
#	#get_node("pion_j2").position.x = get_node("boutons/col3").rect_position.x + 30
#
#
#func _on_col4_pressed():
#	get_tree().get_root().add_child(loadpion.instance())
#	Global.posi_pion = get_node("boutons/col4").rect_position.x - 90
#	#get_node("pion_j2").position.x = get_node("boutons/col4").rect_position.x + 30
#
#
#func _on_col5_pressed():
#	get_tree().get_root().add_child(loadpion.instance())
#	Global.posi_pion = get_node("boutons/col5").rect_position.x - 110
#	#get_node("pion_j2").position.x = get_node("boutons/col5").rect_position.x + 30
#
#
#func _on_col6_pressed():
#	get_tree().get_root().add_child(loadpion.instance())
#	Global.posi_pion = get_node("boutons/col6").rect_position.x - 130
#	#get_node("pion_j2").position.x = get_node("boutons/col6").rect_position.x + 30
#
#
#func _on_col7_pressed():
#	get_tree().get_root().add_child(loadpion.instance())
#	Global.posi_pion = get_node("boutons/col7").rect_position.x - 150
#	#get_node("pion_j2").position.x = get_node("boutons/col7").rect_position.x + 30


func _on_col1_pos():
	print("ok1")
#	var timer = Timer.new()
#	timer.set_wait_time(1)
	yield(get_tree().create_timer(0.1), "timeout")
	print("ok2")
	get_node("boutons/col1").rect_position.x -= 30
