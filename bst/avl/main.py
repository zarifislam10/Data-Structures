from avl_node import AVLNode
from avl import AVL

def main():
    # Create a sample sequence of numbers to insert
    # This replaces the file reading from the Java version
    test_sequences = [
        [1, 2, 3, 4],
        [1, 2, 4, 3],
        [1, 3, 2, 4],
        [1, 3, 4, 2],
        [1, 4, 2, 3],
        [1, 4, 3, 2]
    ]
    
    for sequence in test_sequences:
        avl = AVL()
        print(f"\nInserting sequence: {sequence}")
        
        # Insert each number in the sequence
        for num in sequence:
            node = AVLNode(num)
            avl.insert(node)
        
        # Print the tree in pre-order traversal
        print("Pre-order traversal:", end=' ')
        avl.print_avl()
        print()  # New line after each tree

if __name__ == "__main__":
    main() 