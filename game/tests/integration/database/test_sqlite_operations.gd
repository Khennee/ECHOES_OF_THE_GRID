extends GutTest

var _database: SQLite


func before_each() -> void:
	_database = SQLite.new()
	_database.path = ":memory:"

	assert_true(_database.open_db())

	assert_true(
		_database.query("CREATE TABLE components (id INTEGER PRIMARY KEY, name TEXT NOT NULL);")
	)


func after_each() -> void:
	if is_instance_valid(_database):
		_database.close_db()
		_database = null


func test_insert_record() -> void:
	var success: bool = _database.query("INSERT INTO components (id, name) VALUES (1, 'Core');")

	assert_true(success)

	_database.query("SELECT * FROM components;")

	assert_eq(_database.query_result.size(), 1)


func test_select_record() -> void:
	_database.query("INSERT INTO components VALUES (1, 'Core');")

	var success: bool = _database.query("SELECT name FROM components WHERE id = 1;")

	assert_true(success)
	assert_eq(_database.query_result.size(), 1)

	if _database.query_result.size() == 1:
		assert_eq(_database.query_result[0]["name"], "Core")


func test_update_record() -> void:
	_database.query("INSERT INTO components VALUES (1, 'Core');")

	var success: bool = _database.query(
		"UPDATE components SET name = 'Repaired Core' WHERE id = 1;"
	)

	assert_true(success)

	_database.query("SELECT name FROM components WHERE id = 1;")

	assert_eq(_database.query_result.size(), 1)

	if _database.query_result.size() == 1:
		assert_eq(_database.query_result[0]["name"], "Repaired Core")


func test_delete_record() -> void:
	_database.query("INSERT INTO components VALUES (1, 'Core');")

	var success: bool = _database.query("DELETE FROM components WHERE id = 1;")

	assert_true(success)

	_database.query("SELECT * FROM components;")

	assert_eq(_database.query_result.size(), 0)


func test_parameter_binding() -> void:
	var component_name: String = "Runner's Core"

	var success: bool = _database.query_with_bindings(
		"INSERT INTO components (id, name) VALUES (?, ?);", [1, component_name]
	)

	assert_true(success)

	_database.query("SELECT name FROM components WHERE id = 1;")

	assert_eq(_database.query_result.size(), 1)

	if _database.query_result.size() == 1:
		assert_eq(_database.query_result[0]["name"], component_name)


func test_transaction_commit() -> void:
	assert_true(_database.query("BEGIN TRANSACTION;"))
	assert_true(_database.query("INSERT INTO components VALUES (1, 'Core');"))
	assert_true(_database.query("COMMIT;"))

	_database.query("SELECT * FROM components;")

	assert_eq(_database.query_result.size(), 1)


func test_transaction_rollback() -> void:
	assert_true(_database.query("BEGIN TRANSACTION;"))
	assert_true(_database.query("INSERT INTO components VALUES (1, 'Core');"))
	assert_true(_database.query("ROLLBACK;"))

	_database.query("SELECT * FROM components;")

	assert_eq(_database.query_result.size(), 0)
