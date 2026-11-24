extends GutTest


func test_addition() -> void:
	assert_eq(2 + 2, 4, "Addition should return four")


func test_string_comparison() -> void:
	assert_eq("GRID", "GRID", "Strings should match")


func test_boolean_value() -> void:
	assert_true(true, "Boolean value should be true")
