extends RigidBody2D


var my_pos = Vector2(0,0)
var couleur_dico = {"rouge": Color(0.94043, 0, 0), "jaune": Color(0.94043, 0.778872, 0.011021), "vert": Color(0, 0.694118, 0.094118), "violet": Color(0.560784, 0, 0.980392)} 

func _ready():
	self.global_position = my_pos + Vector2(30,80)
	self.scale = Vector2(1,1)
	$Sprite.scale = Vector2(0.38,0.38)
	$CollisionShape2D.scale = Vector2(0.9,0.95)
	
func _process(delta):
	#print(self.position.y)
#	self.position.x = Global.posi_pion
#	print(get_linear_velocity().y)
	if get_linear_velocity().y <= 20 and get_linear_velocity().y >= -20:
		if $verif_velocity.time_left == 0:
			$verif_velocity.set_wait_time(1)
			$verif_velocity.start()
			#print("timer lancé")
#			yield($verif_velocity, "timeout")
	else:
		#print("timer arrêté")
		$verif_velocity.stop()

func start(pos_pion, tour):
	if tour %2 == 1:
		self.modulate = couleur_dico["vert"]
	else:
		self.modulate = couleur_dico["violet"]
	my_pos = pos_pion

	
func _on_verif_velocity_timeout():
#	if get_linear_velocity().y <= 1 and get_linear_velocity().y >= -1:
	set_linear_velocity(Vector2(0,0))
	set_mode(1)
#	if get_mode() == 1:
#		print("mode changé")
	set_pause_mode(1)
#	if get_pause_mode() == 1:
#		print("la pause à marché")
#	if get_pause_mode() == 0:
#		print("si tu vois ce print c'est que le pause mode n'a pas marché")
