extends Control

const TOTAL_SLIDES: int = 23
var current_slide: int = 1

@onready var story_image: TextureRect = $StoryImage


func _ready() -> void:
	show_slide()


func show_slide() -> void:
	var image_path = "res://assets/cutscenes/opening/%02d.png" % current_slide
	story_image.texture = load(image_path)


func next_slide() -> void:
	if current_slide < TOTAL_SLIDES:
		current_slide += 1
		show_slide()
	else:
		finished_cutscene()


func skip_slide() -> void:
	finished_cutscene()


func _on_next_button_pressed() -> void:
	next_slide()


func _on_skip_button_pressed() -> void:
	skip_slide()


func finished_cutscene() -> void:
	print("Cutscene finished")
