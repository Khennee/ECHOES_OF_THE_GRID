extends Control


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	$BackgroundMusic.play()


func button_sfx() -> void:
	$ButtonSFX.play(0.3)
	await get_tree().create_timer(0.35).timeout
	$ButtonSFX.stop()


func _on_start_button_pressed() -> void:
	button_sfx()
	print("Game Started!")


func _on_settings_button_pressed() -> void:
	button_sfx()
	print("Settings Opened!")


func _on_quit_button_pressed() -> void:
	button_sfx()
	get_tree().quit()
