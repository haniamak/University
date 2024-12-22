using System.ComponentModel.DataAnnotations.Schema;
using Microsoft.Data.SqlClient;
using Microsoft.Extensions.Configuration;
using Dapper;
using System.ComponentModel.DataAnnotations;


namespace WebApplication3
{
    [Table("Person")]
    public class Person
    {
        [Key]
        public int Id { get; set; }
        public string Name { get; set; }
        public string Surname { get; set; }
    }



    public interface IDapperRepository<T> : IDisposable
    {
        //IEnumerable<T> Get(string query, object parameters);
        int? Insert(T item);
        int Update(T item);
        int Delete(int item);
        IEnumerable<T> GetAll();
        //IEnumerable<T> Get(string query, object parameters = null);
        T GetById(int id);
    }

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
            return _connection.QuerySingleOrDefault<T>($"SELECT * FROM {typeof(T).Name}s WHERE Id = @Id", new { Id = id });
        }

        public void Dispose()
        {
            _connection.Dispose();
        }
        //public IEnumerable<T> GetAll()
        //{
        //    return _connection.Query<T>($"SELECT * FROM {typeof(T).Name}s");
        //}
        /*
        public IEnumerable<T> Get(string query, object parameters)
        {
            return this._connection.Query<T>(query, parameters);
        }*/
        public IEnumerable<T> GetAll()
        {
            return _connection.Query<T>($"SELECT * FROM {typeof(T).Name}");
        }
        /*
        public IEnumerable<T> Get(string query, object parameters)
        {
            return this._connection.Query<T>(query, parameters);
        }
        
        public int Delete(T t)
        {
            return this._connection.Delete(t);
        }
        public int? Insert(T t)
        {
            return this._connection.Insert(t);
        }
        public int Update(T t)
        {
            return this._connection.Update(t);
        }*/
        public int? Insert(T entity)
        {
            return _connection.Execute($"INSERT INTO {typeof(T).Name}s VALUES (@entity)", entity);
        }

        public int Update(T entity)
        {
            return _connection.Execute($"UPDATE {typeof(T).Name}s SET VALUES (@entity) WHERE Id = @Id", entity);
        }
        public int Delete(int id)
        {
            return _connection.Execute($"DELETE FROM {typeof(T).Name}s WHERE Id = @Id", new { Id = id });
        }
    }
}
