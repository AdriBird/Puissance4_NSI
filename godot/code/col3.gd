extends TextureButton


# Declare member variables here. Examples:
# var a = 2
# var b = "text"

var loadpion = load("res://scenes/pion_j2.tscn")
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_col3_pressed():
	var pion_pawn = loadpion.instance()
	var pos_pion = self.rect_global_position
	pion_pawn.start(pos_pion)
	add_child(pion_pawn)
