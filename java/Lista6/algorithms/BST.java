package algorithms;

public class BST<T extends Comparable<T>> implements Dictionary<T> {
  BST() {
    this.root = null;
  }
  public class Node { // ZROBIC PUBLIC DO TESTOW W MAIN
    Node left, right;
    T value;

    Node(T value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }

  }

  public Node root; // korzeń drzewa BST
  // opakowanie dla metod słownikowych zdefiniowanych w węzłach...

  private boolean searchRecursive(Node node, T elem) {
    if (node == null) {
      return false;
    }
    int compare = elem.compareTo(node.value);
    if (compare == 0) {
      return true;
    }
    if (compare > 0) {
      return searchRecursive(node.right, elem);

    } else {
      return searchRecursive(node.left, elem);
    }
  }

  @Override
  public boolean search(T elem) {
    return searchRecursive(root, elem);
  }

  private Node addRecursive(Node node, T elem) {
    if (node == null) {
      return new Node(elem);
    }

    if (search(elem) == true) {
      throw new IllegalArgumentException("Element do wstawienia jest juz w drzewie.");
    }
    int compare = elem.compareTo(node.value);
    if (compare > 0) {
      node.right = addRecursive(node.right, elem);
    } else {
      node.left = addRecursive(node.left, elem);
    }
    return node;
  }

  @Override
  public void insert(T elem) {
    if (elem == null) {
      throw new IllegalArgumentException("Wstawiany element musi miec wartosc");
    }
    root = addRecursive(root, elem);
  }

  private Node removeRecursive(Node node, T elem) {
    if (node == null) {
      return null;
    }
    int compare = elem.compareTo(node.value);
    if (compare > 0) {
      node.right = removeRecursive(node.right, elem);
    }
    else if (compare < 0) {
      node.left = removeRecursive(node.left, elem);
    } else {

      if (node.right == null) {
        return node.left;
      }
      if (node.left == null) {
        return node.right;
      }
      node.value = minimumNode(node.right).value;
      node.right = removeRecursive(node.right, node.value);
    }
    return node;
  }

  @Override
  public void remove(T elem) {
    root = removeRecursive(root, elem);
  }

  private Node minimumNode(Node node) {
    Node temp = node;
    while (temp.left != null) {
      temp = temp.left;
    }
    return temp;
  }

  @Override
  public T min() {
    if (root == null) {
      throw new IllegalStateException("Nie ma elementu minimalnego - drzewo jest puste.");
    }
    return minimumNode(root).value;
  }

  private Node maximumNode(Node node) {
    Node temp = node;
    while (temp.right != null) {
      temp = temp.right;
    }
    return temp;
  }

  @Override
  public T max() {
    if (root == null) {
      throw new IllegalStateException("Nie ma elementu maksymalnego - drzewo jest puste.");
    }
    return maximumNode(root).value;
  }

  @Override
  public int size() {
    return sizeRecursive(root);
  }

  private int sizeRecursive(Node node) {
    if (node == null) {
      return 0;
    }
    return 1 + sizeRecursive(node.left) + sizeRecursive(node.right);
  }
  @Override
  public void clear() {
    root = null;
  }
  /* 
  public static void main(String[] args){

		BST<Integer> b = new BST<>();
		b.insert(5);
    b.insert(2);
    b.insert(12);
    b.insert(1);
    b.insert(10);

    b.size();

    b.remove(4);	
    System.out.println(b.toString());
    b.size();
    b.search(3);
    b.min();
    b.max();

    b.clear();
    System.out.println(b.toString());
}*/

}