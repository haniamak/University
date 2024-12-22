using WebApplication5.Models;
using Microsoft.Data.SqlClient;
using Microsoft.Extensions.Configuration;
using Dapper;

namespace WebApplication5.Data
{
	public class DapperRepository<T> : IDapperRepository<T>
	{
		IConfiguration _configuration;
		SqlConnection _connection;
		public DapperRepository(IConfiguration configuration)
		{
			_configuration = configuration;
			var connectionString = _configuration["ConnectionStrings:DefaultConnection"];
			_connection = new SqlConnection(connectionString);
		}

        public T GetById(int id)
        {
            string tableName = typeof(T).Name;
            string sql = $"SELECT * FROM {tableName} WHERE Id = @Id";
            return _connection.QuerySingleOrDefault<T>(sql, new { Id = id });
        }

        public void Dispose()
		{
			_connection.Dispose();
		}

		public IEnumerable<T> GetAll()
		{
			return _connection.Query<T>($"SELECT * FROM {typeof(T).Name}");
		}

        public int? Insert(T entity)
        {
            // Pobranie właściwości klasy T i utworzenie dynamicznego zapytania SQL
            var properties = typeof(T).GetProperties()
                .Where(p => p.Name != "Id") // Zakładamy, że "Id" jest autoinkrementowane
                .Select(p => p.Name);

            var columnNames = string.Join(", ", properties); // np. "Name, Age, Grade"
            var parameterNames = string.Join(", ", properties.Select(p => "@" + p)); // np. "@Name, @Age, @Grade"

            var tableName = typeof(T).Name; // Zakładamy, że nazwa klasy odpowiada nazwie tabeli

            var sql = $"INSERT INTO {tableName} ({columnNames}) VALUES ({parameterNames});";

            return _connection.Execute(sql, entity); // Wykonanie zapytania
        }


        public int Update(T entity)
        {
            // Get all properties of the entity, excluding "Id".
            var properties = typeof(T).GetProperties()
                .Where(p => p.Name != "Id")
                .Select(p => p.Name);

            // Generate the SET clause dynamically.
            var setClause = string.Join(", ", properties.Select(p => $"{p} = @{p}"));

            // Get the table name (assuming it matches the class name).
            var tableName = typeof(T).Name;

            // Build the SQL query.
            var sql = $"UPDATE {tableName} SET {setClause} WHERE Id = @Id";

            // Execute the query.
            return _connection.Execute(sql, entity);
        }
        public int Delete(int id)
        {
            var tableName = typeof(T).Name;
            var sql = $"DELETE FROM {tableName} WHERE Id = @Id";
            return _connection.Execute(sql, new { Id = id });
        }

    }
}
