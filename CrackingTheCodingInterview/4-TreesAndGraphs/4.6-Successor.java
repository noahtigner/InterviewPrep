// Write an algorithm to find the "next" node (i.e., in-order sccuessor) of a given node in a bst.
// You may assume each node has a link to its parents.

class TreeNode<E> {
    E data;
    TreeNode left, right, parent;

    public TreeNode(E data) {
        this.data = data;
        this.left = null;
        this.right = null;
        this.parent = null;
    }
}

class Main {

    public static TreeNode successor(TreeNode node) {
        if (node == null) {
            return null;
        }
        if (node.right != null) {
            return leftMostChild(node.right);
        }
        return firstRightParent(node);
    }

    private static TreeNode leftMostChild(TreeNode node) {
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }

    private static TreeNode firstRightParent(TreeNode node) {
        TreeNode current = node;
        TreeNode parent = node.parent;
        
        while (parent != null  && parent.left != current) {
            current = parent;
            parent = parent.parent;
        }
        return parent;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode<Integer>(40);

        root.left = new TreeNode<Integer>(20);
        root.right = new TreeNode<Integer>(60);
        root.left.parent = root;
        root.right.parent = root;

        root.left.left = new TreeNode<Integer>(10);
        root.left.right = new TreeNode<Integer>(30);
        root.right.left = new TreeNode<Integer>(50);
        root.right.right = new TreeNode<Integer>(70);
        root.left.left.parent = root.left;
        root.left.right.parent = root.left;
        root.right.left.parent = root.right;
        root.right.right.parent = root.right;

        root.left.left.left = new TreeNode<Integer>(5);
        root.left.left.right = new TreeNode<Integer>(15);
        root.left.left.left.parent = root.left.left;
        root.left.left.right.parent = root.left.left;

        TreeNode successor = successor(root.left.left.right);
        if (successor != null) { System.out.println(successor.data); }
    }
} 