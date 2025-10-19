package algorithms;

import javax.swing.*; // zeby miec wszystkie componenty

import java.awt.*; // boarderlayout - poodzielane kreskami pola
import java.awt.event.*;

public class App extends JFrame {
  private BST<String> bst;
  private DrawBST drawBst;

  public static void main(String[] args) {
    SwingUtilities.invokeLater(new Runnable() {
      @Override
      public void run() {
        new App();
      }
    });
  }

  public App() {
    bst = new BST<>();
    drawBst = new DrawBST(bst);
    UI();
  }

  private void UI() {
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // do klikania x do wyjscia
    setSize(1200, 900);
    
    JPanel mainPanel = new JPanel();
    mainPanel.setBackground(Color.CYAN);
    mainPanel.setBounds(10, 10, 200, 600);
    add(mainPanel);

    JTextField inputField = new JTextField(15); // do wpisywania nazw nodeow
    inputField.setBounds(30, 30, 100, 40);
    mainPanel.add(new JLabel("Value: "));
    mainPanel.add(inputField);

    JButton insertButton = new JButton("Insert");
    insertButton.setBounds(10, 400 , 50, 50);
    insertButton.addActionListener(new ActionListener() {
      @Override
      public void actionPerformed(ActionEvent e) {
        String value = inputField.getText();
        bst.insert(value);
        drawBst.repaint();
      }
    });
    mainPanel.add(insertButton);

    // Przycisk do usuwania
    JButton removeButtton = new JButton("Remove");
    removeButtton.setBounds(10, 500 , 50, 50);
    removeButtton.addActionListener(new ActionListener() {
      @Override
      public void actionPerformed(ActionEvent e) {
        String value = inputField.getText();
        bst.remove(value);
        drawBst.repaint();
      }
    });
    mainPanel.add(removeButtton);
    mainPanel.add(drawBst);
    
    setVisible(true);
  }

}