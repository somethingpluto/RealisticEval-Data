package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;

public class Tester {
    @Test
    public void testValidColors() {
        assertEquals("\u001b[38;2;255;87;51m", hexToAnsi("#FF5733"));
        assertEquals("\u001b[38;2;0;255;0m", hexToAnsi("#00FF00"));
        assertEquals("\u001b[38;2;0;0;255m", hexToAnsi("#0000FF"));
    }
    @Test
    public void testBlackAndWhite() {
        assertEquals("\u001b[38;2;0;0;0m", hexToAnsi("#000000"));  // Black
        assertEquals("\u001b[38;2;255;255;255m", hexToAnsi("#FFFFFF"));  // White
    }

}