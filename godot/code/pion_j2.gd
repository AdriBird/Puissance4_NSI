extends RigidBody2D


	
func _process(delta):
	print(self.position.y)
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

func start(pos_pion):
	print("ça marche")
	self.position.y = 140
	self.position.x = pos_pion

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
