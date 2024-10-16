package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testFormatPostCount_SinglePost() {
        assertEquals("01 Post", formatPostCount(1));
    }

    @Test
    public void testFormatPostCount_TwoPosts() {
        assertEquals("02 Posts", formatPostCount(2));
    }

    @Test
    public void testFormatPostCount_TenPosts() {
        assertEquals("10 Posts", formatPostCount(10));
    }

    @Test
    public void testFormatPostCount_NinetyNinePosts() {
        assertEquals("99 Posts", formatPostCount(99));
    }

    @Test
    public void testFormatPostCount_FivePosts() {
        assertEquals("05 Posts", formatPostCount(5));
    }
    }