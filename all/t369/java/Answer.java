package org.real.temp;

public class Answer {
    private static final int N = 8;
    private int[] board = new int[N];
    private boolean solved = false;

    public void eightQueens() {
        if (solve(0)) {
            printSolution();
        } else {
            System.out.println("No solution");
        }
    }

    private boolean solve(int row) {
        if (row == N) {
            solved = true;
            return true;
        }

        for (int col = 0; col < N; col++) {
            if (isSafe(row, col)) {
                board[row] = col;
                if (solve(row + 1)) {
                    return true;
                }
                board[row] = -1; // Backtrack
            }
        }

        return false;
    }

    private boolean isSafe(int row, int col) {
        for (int i = 0; i < row; i++) {
            if (board[i] == col || Math.abs(board[i] - col) == Math.abs(i - row)) {
                return false;
            }
        }
        return true;
    }

    private void printSolution() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i] == j) {
                    System.out.print("Q ");
                } else {
                    System.out.print(". ");
                }
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Answer answer = new Answer();
        answer.eightQueens();
    }
}