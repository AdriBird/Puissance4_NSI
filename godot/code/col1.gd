extends TextureButton

var loadpion = load("res://scenes/pion_j2.tscn")
signal pos

func _on_col1_pressed():
	print("première étape")
	var pion_pawn = loadpion.instance()
	self.rect_position.x += 30
	var pos_pion = self.rect_position.x
	pion_pawn.start(pos_pion)
	add_child(pion_pawn)
	print("deuxième étape")
	emit_signal("pos")
	
