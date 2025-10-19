package algorithms;

import javax.swing.*; // zeby miec wszystkie componenty
import java.awt.*; // boarderlayout - poodzielane kreskami pola

public class DrawBST extends JPanel {
  private BST<String> bst;
  private int rozmiar = 800;

  public DrawBST(BST<String> bst) {
    this.bst = bst;
  }

  @Override
  protected void paintComponent(Graphics g) {
    setBounds(250, 50, rozmiar, rozmiar);
    setBackground(Color.WHITE);
    super.paintComponent(g);
    drawTree((Graphics2D)g, rozmiar/2, 10, bst.root, rozmiar/20);
  }

  private void drawTree(Graphics2D g, int x, int y, BST<String>.Node node, int depth) {
    g.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
    if (node != null) {
      g.drawString(node.value.toString(), x, y);
      if (node.right != null) {
        int x_r = x + rozmiar/20;
        int y_r = y + rozmiar/20;
        g.drawLine(x, y, x_r, y_r);
        drawTree(g, x_r, y_r, node.right, depth / 2);
      }

      if (node.left != null) {
        int x_l = x - rozmiar/20;
        int y_l = y + rozmiar/20;
        g.drawLine(x, y, x_l, y_l);
        drawTree(g, x_l, y_l, node.left, depth / 2);
      }
    }
  } 
}