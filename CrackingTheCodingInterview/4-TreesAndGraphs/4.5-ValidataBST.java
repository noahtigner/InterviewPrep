// Implement a function to check if a binary tree is a BST.

class TreeNode {
	int data;
	TreeNode left;
	TreeNode right;

	public TreeNode(int data) {
		this.data = data;
		this.left = null;
		this.right = null;
	}
}

class Main {

    // time: O(n), space: O(1)
	public static boolean validateBST(TreeNode root) {
		return isBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
	}

	private static boolean isBST(TreeNode node, int low, int high) {
		if (node == null) {
			return true;
		}
		if (node.data <= low || node.data >= high) {
			return false;
		}
		return isBST(node.left, low, node.data) && isBST(node.right, node.data, high);
	}

    public static void main(String[] args) {
        TreeNode root = new TreeNode(5);
		root.left = new TreeNode(3);
		root.right = new TreeNode(7);
		root.left.left = new TreeNode(2);
		root.left.right = new TreeNode(4);
		root.right.left = new TreeNode(6);
		root.right.right = new TreeNode(8);
		root.right.right.right = new TreeNode(18);

		System.out.println(validateBST(root));
    }
}