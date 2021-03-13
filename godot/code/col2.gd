extends TextureButton


var loadpion = load("res://scenes/pion_j2.tscn")

func _on_col2_pressed():
	var pion_pawn = loadpion.instance()
	var pos_pion = self.rect_global_position
	pion_pawn.start(pos_pion)
	add_child(pion_pawn)
