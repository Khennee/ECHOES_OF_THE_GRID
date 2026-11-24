extends GutTest

const TEST_DATABASE_PATH: String = "user://eotg_test_persistence.db"


func before_each() -> void:
	_remove_test_database()


func after_each() -> void:
	_remove_test_database()


func _remove_test_database() -> void:
	if FileAccess.file_exists(TEST_DATABASE_PATH):
		var absolute_path: String = ProjectSettings.globalize_path(TEST_DATABASE_PATH)

		assert_eq(DirAccess.remove_absolute(absolute_path), OK)


func test_database_persistence() -> void:
	var database: SQLite = SQLite.new()
	database.path = TEST_DATABASE_PATH

	if not database.open_db():
		fail_test("Failed to open test database")
		return

	assert_true(database.query("CREATE TABLE components (id INTEGER PRIMARY KEY, name TEXT);"))

	assert_true(database.query("INSERT INTO components VALUES (1, 'Core');"))

	database.close_db()

	var reopened_database: SQLite = SQLite.new()
	reopened_database.path = TEST_DATABASE_PATH

	if not reopened_database.open_db():
		fail_test("Failed to reopen test database")
		return

	assert_true(reopened_database.query("SELECT * FROM components;"))
	assert_eq(reopened_database.query_result.size(), 1)

	if reopened_database.query_result.size() == 1:
		assert_eq(reopened_database.query_result[0]["name"], "Core")

	reopened_database.close_db()
