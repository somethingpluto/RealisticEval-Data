package org.real.temp;

public class Answer {

    static class TreeNode {
        int value;
        TreeNode left;
        TreeNode right;

        public TreeNode(int value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }

        public TreeNode(int value, TreeNode left, TreeNode right) {
            this.value = value;
            this.left = left;
            this.right = right;
        }
    }

    static class BinaryTree {
        TreeNode root;

        public BinaryTree(TreeNode root) {
            this.root = root;
        }

        public BinaryTree() {
            this(null);
        }

        public List<Integer> preorderTraversal(TreeNode node, List<Integer> result) {
            if (result == null) {
                result = new ArrayList<>();
            }
            if (node != null) {
                result.add(node.value);
                preorderTraversal(node.left, result);
                preorderTraversal(node.right, result);
            }
            return result;
        }

        public List<Integer> inorderTraversal(TreeNode node, List<Integer> result) {
            if (result == null) {
                result = new ArrayList<>();
            }
            if (node != null) {
                inorderTraversal(node.left, result);
                result.add(node.value);
                inorderTraversal(node.right, result);
            }
            return result;
        }

        public List<Integer> postorderTraversal(TreeNode node, List<Integer> result) {
            if (result == null) {
                result = new ArrayList<>();
            }
            if (node != null) {
                postorderTraversal(node.left, result);
                postorderTraversal(node.right, result);
                result.add(node.value);
            }
            return result;
        }

        public List<Integer> iterativePreorder() {
            if (root == null) {
                return Collections.emptyList();
            }
            List<Integer> result = new ArrayList<>();
            Stack<TreeNode> stack = new Stack<>();
            stack.push(root);
            while (!stack.isEmpty()) {
                TreeNode node = stack.pop();
                if (node != null) {
                    result.add(node.value);
                    if (node.right != null) {
                        stack.push(node.right);
                    }
                    if (node.left != null) {
                        stack.push(node.left);
                    }
                }
            }
            return result;
        }

        public List<Integer> iterativeInorder() {
            List<Integer> result = new ArrayList<>();
            Stack<TreeNode> stack = new Stack<>();
            TreeNode current = root;
            while (!stack.isEmpty() || current != null) {
                while (current != null) {
                    stack.push(current);
                    current = current.left;
                }
                current = stack.pop();
                result.add(current.value);
                current = current.right;
            }
            return result;
        }

        public List<Integer> iterativePostorder() {
            if (root == null) {
                return Collections.emptyList();
            }
            List<Integer> result = new ArrayList<>();
            Stack<TreeNode> stack = new Stack<>();
            stack.push(root);
            while (!stack.isEmpty()) {
                TreeNode node = stack.pop();
                result.add(0, node.value);
                if (node.left != null) {
                    stack.push(node.left);
                }
                if (node.right != null) {
                    stack.push(node.right);
                }
            }
            return result;
        }
    }

    public static void main(String[] args) {
        // Example usage
        TreeNode root = new TreeNode(1,
                new TreeNode(2, new TreeNode(4), new TreeNode(5)),
                new TreeNode(3));
        
        BinaryTree tree = new BinaryTree(root);
        System.out.println(tree.preorderTraversal(root, null));
        System.out.println(tree.inorderTraversal(root, null));
        System.out.println(tree.postorderTraversal(root, null));
        System.out.println(tree.iterativePreorder());
        System.out.println(tree.iterativeInorder());
        System.out.println(tree.iterativePostorder());
    }
}