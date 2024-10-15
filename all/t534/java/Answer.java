package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    /**
     * Removes the first occurrence of a specified element from a list.
     *
     * @param list - The list from which to remove the element.
     * @param element - The element to remove from the list.
     * @return A new list with the element removed, or the original list if the element is not found.
     */
    public static <T> List<T> removeElementInArray(List<T> list, T element) {
        List<T> newList = new ArrayList<>();
        
        for (T item : list) {
            if (!item.equals(element)) {
                newList.add(item); // Add elements that are not the target element
            }
        }
        
        return newList;
    }
}