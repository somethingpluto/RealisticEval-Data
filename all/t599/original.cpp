#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#define SIZE 1024

/*
 * To get the indexes the formula is:
 * - parent index = (index − 1)/2
 * - left child = 2 ∗ index + 1
 * - right child = 2 ∗ index + 2 
 */

struct Heap {
    int elements[SIZE];
    size_t current;
} typedef Heap;

void add(Heap* heap, int val);
void max_heapify(Heap* heap);
void swap(Heap* heap, int first_idx, int second_idx);
void print(Heap* heap);
int index_of(Heap* heap, int val);
bool delete(Heap* heap, int val);
bool contains(Heap* heap, int val);

/// Inserts a new element inside the heap
///
/// # Warnings
/// 
/// This function can potentially fail in the case
/// a value is inserted when the heap is full
void add(Heap* heap, int val) {
    if (heap->current + 1 == SIZE) {
        printf( 
            "Couldn't add anymore elemets, the length \
             of the heap exceeds the maximum size %d",
            SIZE
         );
         return;
    } else {
        heap->elements[heap->current] = val;
        heap->current++;
        max_heapify(heap);
    }
}

/// "Normalizes" an `Heap` into it's specified type of heap
/// checking if each elemet respects its properties
void max_heapify(Heap* heap) {
    int idx = heap->current - 1;
    // (idx -1) / 2] is the parent idx
    while (idx > 0 && heap->elements[idx] > heap->elements[(idx - 1) / 2]) {
        swap(heap, idx, (idx -1) / 2);
        idx = (idx -1) / 2;
    }
}

/// Swaps a child and its parent on the heap given their indexes
///
/// # Params
/// 
/// - `heap` the `Heap*` we are referring to
/// - `child_idx` the index of the child to swap
/// - `parent_idx` the index of the parent to swap
void swap(Heap* heap, int child_idx, int parent_idx) {
    int tmp = heap->elements[child_idx];
    heap->elements[child_idx] = heap->elements[parent_idx];
    heap->elements[parent_idx] = tmp;
}

/// Returns an index of a given value in the heap
/// 
/// # Params
/// 
/// - `heap` the `Heap*` we are referring to
/// - `val` an `int` representing the value of which we are trying to 
/// find the index 
/// 
/// # Returns
/// 
/// An `int` representing the index of the value if it was found, if  
/// the value is not found the fucnction returns `-1`
int index_of(Heap* heap, int val) {
    for (size_t i = 0; i < heap->current; i++) {
        if (heap->elements[i] == val) {
            return i;
        }
    }
    return -1;
    
}

/* 
 * So the algorithm works like this, we check for the index of the val
 * if the index isn't found return early, else save the index of the left
 * and right child. Then swap the value of the element to remove with the last
 * element on the heap, null the previously last element and check if any of the
 * new children break the heap rule, IF THEY DO then swap the parent with the
 * smallest of them
 */
/// Deletes an element from the heap and re normalizes it 
/// if any element break its properties
///
/// # Params
/// 
/// - `heap` the `Heap*` we are referring to
/// - `val` an `int` representing the value we are deleting
///
/// # Returns
///
/// A `bool` flag stating if the value was found or not
bool delete(Heap* heap, int val) { 
    int idx = index_of(heap, val);
    if (idx < 0) {
        return false;
    }
    // remove it
    heap->current--;
    heap->elements[idx] = heap->elements[heap->current];

    // reset or free it
    heap->elements[heap->current] = 0;

    // save its children indexes
    int left = (2 * idx) + 1;
    int right = (2 * idx) + 2;
    
    while (left < heap->current && 
        ((heap->elements[idx] < heap->elements[left]) ||
        (heap->elements[idx] < heap->elements[right]))
    ) {
        if (heap->elements[left] > heap->elements[right]) {// the left one is the bigger one
            swap(heap, left, idx);
            idx = left;
            left = (2 * idx) + 1;
            right = (2 * idx) + 2;
        } else { // the right one is the bigger one
            swap(heap, right, idx);
            idx = right;
            left = (2 * idx) + 1;
            right = (2 * idx) + 2;
        }
    }
    return true;
}

/* 
 * The following algorithm is specifically designed for a min-heap.
 * To tailor the algorithm for a max-heap the two comparison operations in 
 * the else if condition within the inner while loop should be flipped. 
 */
/// Checks for a value in the heap
/// 
/// # Params
/// 
/// - `heap` the `Heap*` we are referring to
/// - `val` an `int` representing the value we are checking for
/// 
/// # Returns
/// 
/// A `bool` flag stating if the value was found or not
bool contains(Heap* heap, int val) {
    // initialize the various indexes and the number of nodes
    int start_node = 0;
    int end_node = 0;
    int nodes = 1;
    int count = 0;

    // all of this part is just index arithmetic
    // it might look difficult but it's not too hard
    // to understand
    while (start_node < heap->current) {
        start_node = nodes - 1;
        end_node = start_node + nodes;
        count = 0;
        while (start_node < heap->current && start_node < end_node) {
            // basically if the element at the current index
            // is not the one searched and for each node in this
            // level is bigger than the parent and less than the child
            // the element can't be in the heap
            if (val == heap->elements[start_node]) {
                return true;
            } else if (val < heap->elements[(start_node - 1) / 2] 
                    && val > heap->elements[start_node]) {
                count++;
            }
            start_node++;
        }
        if (count == nodes) {
            return false;
        }
        nodes *= 2;
    }
    return false;
}

/// Prints the whole heap in an array like manner
void print(Heap* heap) {
    printf("[ ");
    for (size_t i = 0; i < sizeof(heap->elements) && heap->elements[i] != 0; i++) { 
        // i'm printing while it is not 0 but uninitialized values could 
        // be random numbers too
        printf("%d ", heap->elements[i]);
    }
    printf("]\n");
}

// some random testing generated by chatGPT
int main() {
    // Allocate memory for the heap dynamically
    Heap *myHeap = (Heap *)malloc(sizeof(Heap));

    myHeap->current = 0; // Initialize heap

    // Test adding elements to the heap
    add(myHeap, 10);
    add(myHeap, 20);
    add(myHeap, 15);
    add(myHeap, 7);
    add(myHeap, 25);

    printf("Heap after adding elements: ");
    print(myHeap);

    // Test deleting elements from the heap
    delete(myHeap, 15);
    printf("Heap after deleting 15: ");
    print(myHeap);

    // Test contains function
    int val_to_check = 7;
    if (contains(myHeap, val_to_check)) {
        printf("%d is in the heap.\n", val_to_check);
    } else {
        printf("%d is not in the heap.\n", val_to_check);
    }

    val_to_check = 100; // Value not in the heap
    if (contains(myHeap, val_to_check)) {
        printf("%d is in the heap.\n", val_to_check);
    } else {
        printf("%d is not in the heap.\n", val_to_check);
    }

    // Free dynamically allocated memory
    free(myHeap);

    return 0;
}