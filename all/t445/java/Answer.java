package org.real.temp;

import org.apache.commons.math3.linear.Array2DRowRealMatrix;
import org.apache.commons.math3.linear.RealMatrix;

public class Answer {

    public static RealMatrix createRotMatrix(double angleDeg, String axis) {
        double radians = Math.toRadians(angleDeg);

        switch(axis.toUpperCase()) {
            case "X":
                return new Array2DRowRealMatrix(new double[][]{
                    {1, 0, 0},
                    {0, Math.cos(radians), -Math.sin(radians)},
                    {0, Math.sin(radians), Math.cos(radians)}
                });
            case "Y":
                return new Array2DRowRealMatrix(new double[][]{
                    {Math.cos(radians), 0, Math.sin(radians)},
                    {0, 1, 0},
                    {-Math.sin(radians), 0, Math.cos(radians)}
                });
            case "Z":
                return new Array2DRowRealMatrix(new double[][]{
                    {Math.cos(radians), -Math.sin(radians), 0},
                    {Math.sin(radians), Math.cos(radians), 0},
                    {0, 0, 1}
                });
            default:
                throw new IllegalArgumentException("Invalid axis: " + axis);
        }
    }

}