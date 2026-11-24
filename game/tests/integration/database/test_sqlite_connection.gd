extends GutTest


func test_sqlite_class_available() -> void:
	assert_true(ClassDB.class_exists("SQLite"), "SQLite GDExtension should be registered")


func test_open_database() -> void:
	var database = SQLite.new()
	database.path = ":memory:"

	var opened: bool = database.open_db()

	assert_true(opened, "SQLite should open an in-memory database")

	if opened:
		database.close_db()


func test_execute_query() -> void:
	var database = SQLite.new()
	database.path = ":memory:"

	if not database.open_db():
		fail_test("Failed to open SQLite database")
		return

	var success: bool = database.query("SELECT 1 AS result;")

	assert_true(success, "SQLite should execute a query")

	if success:
		assert_eq(database.query_result.size(), 1)

		if database.query_result.size() == 1:
			assert_eq(database.query_result[0]["result"], 1)

	database.close_db()
