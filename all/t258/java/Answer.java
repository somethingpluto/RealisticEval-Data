package org.real.temp;

import java.nio.charset.Charset;
import java.util.Arrays;

public class Answer {

    public static Object[] extractCharacterBits(byte[] byteArray, String charToFind, Charset charset) {

        try {
            // Convert byte array to string using specified charset
            String str = new String(byteArray, charset);

            // Get index of character
            int pos = str.indexOf(charToFind);

            if(pos == -1) return null; // Character not found

            // Get bit representation of character
            byte[] bits = Arrays.copyOfRange(byteArray, pos, pos + 1);

            return new Object[]{pos, bits};

        } catch (Exception e) {
            System.out.println(e.getMessage());
            return null;
        }
    }

}