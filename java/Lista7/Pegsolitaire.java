import java.util.ArrayList;

class Pegsolitaire {

  class Move {
    int from;
    int hole;
    int to;

    Move(int from, int hole, int to) {
      this.from = from;
      this.hole = hole;
      this.to = to;
    }

    public String toString() {
      return ("(" + this.from + ", " + this.hole + "," + this.to + ")");
    }
  }

  ArrayList<ArrayList<Integer>> grid;
  ArrayList<Move> moveList;
  ArrayList<ArrayList<ArrayList<Integer>>> unsuccesfulGrid;

  Pegsolitaire(ArrayList<ArrayList<Integer>> grid) {
    this.grid = grid;
    moveList = new ArrayList<>();
    unsuccesfulGrid = new ArrayList<>();
  }

  private void printOutput() {
    for(Move move : moveList) {
      System.out.println(move.toString());
    }
  }

  private void displayGrid() {
    for(ArrayList<Integer> line : grid) {
      for(int i : line) {
        if(i == -1) {
          System.out.print("- ");
        }
        else {
          System.out.print(Integer.toString(i) + " ");
        }
      }
      System.out.println();
    }
  }

  private void makeMove(Move move) {
    grid.get(move.from/7).set(move.from % 7, 0);
    grid.get(move.hole/7).set(move.hole % 7, 0);
    grid.get(move.to/7).set(move.to % 7, 0);
    moveList.add(move);
  } 
  private void undoeMove(Move move) {
    grid.get(move.from/7).set(move.from % 7, 1);
    grid.get(move.hole/7).set(move.hole % 7, 1);
    grid.get(move.to/7).set(move.to % 7, 0);
    moveList.remove(moveList.size() - 1);
  } 

  
}