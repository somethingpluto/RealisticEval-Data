package org.real.temp;

import java.text.SimpleDateFormat;
import java.util.Date;

public class Answer {
    public static String getTime() {
        SimpleDateFormat formatter = new SimpleDateFormat("hh:mm a");
        Date currentDate = new Date();
        return formatter.format(currentDate);
    }

    public static void main(String[] args) {
        System.out.println(getTime());
    }
}