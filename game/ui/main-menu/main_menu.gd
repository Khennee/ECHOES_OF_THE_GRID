extends Control


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass


func _on_start_button_pressed() -> void:
	print("Game Started!")


func _on_settings_button_pressed() -> void:
	print("Settings Opened!")


func _on_quit_button_pressed() -> void:
	get_tree().quit()
