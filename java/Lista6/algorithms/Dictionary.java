package algorithms;

public interface Dictionary<T extends Comparable<T>> {

    public boolean search(T elem);

    public void insert(T elem);

    public void remove(T elem);

    public T min();

    public T max();
    
    public int size();

    public void clear();

    
       
}