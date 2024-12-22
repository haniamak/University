
namespace WebApplication5.Data
{
    public interface IDapperRepository<T> : IDisposable
    {
        int? Insert(T item);
        int Update(T item);
        int Delete(int item);
        IEnumerable<T> GetAll();
        T GetById(int id);
    }
}
