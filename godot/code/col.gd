extends TextureButton

var loadpion = load("res://scenes/pion_j2.tscn")


func _ready():
	pass

func _pressed():
	var pion_pawn = loadpion.instance()
	Global.tour += 1
	#self.rect_position.x += 30
	var pos_pion = self.rect_global_position
	pion_pawn.start(pos_pion, Global.tour)
	add_child(pion_pawn)
	
