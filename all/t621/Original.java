// must test, written by copilot
public boolean isInCheck(Square[][] board){
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 8; j++){
            Square square = board[i][j];
            if(square.getPiece() != null && square.getPiece().isWhite != isWhite){
                for (Square s: square.getPiece().getSquaresSeen()) {
                    if(s.getPiece() instanceof King && s.getPiece().isWhite == isWhite){
                        return true;
                    }
                }
            }
        }
    }
    return false;
}