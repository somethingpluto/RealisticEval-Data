package org.real.temp;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

import org.junit.Test;

public class Tester {

    @Test
    public void testIsCppHeaderFile_HFile() {
        assertTrue(isCppHeaderFile("example.h"));
    }

    @Test
    public void testIsCppHeaderFile_HppFile() {
        assertTrue(isCppHeaderFile("example.hpp"));
    }

    @Test
    public void testIsCppHeaderFile_NonHeaderFile() {
        assertFalse(isCppHeaderFile("example.txt"));
    }

    @Test
    public void testIsCppHeaderFile_NoExtension() {
        assertFalse(isCppHeaderFile("example"));
    }

    @Test
    public void testIsCppHeaderFile_CFile() {
        assertFalse(isCppHeaderFile("example.c"));
    }
}