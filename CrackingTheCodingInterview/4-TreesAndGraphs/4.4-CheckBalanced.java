// Implement a function to check if a binary tree is balanced. For the purposes of this question, 
// a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

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
	public static boolean checkBalanced(TreeNode root) {
		return isBalanced(root, 0);
	}

	private static boolean isBalanced(TreeNode node, int difference) {
		if (node.left != null && node.right != null) {
			return isBalanced(node.left, difference) && isBalanced(node.right, difference);
		}
		if (difference > 1) {
			return false;
		}
		if (node.left != null) {
			return isBalanced(node.left, difference + 1);
		}
		if (node.right != null) {
			return isBalanced(node.right, difference + 1);
		}
		return true;
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

		System.out.println(checkBalanced(root));
    }
}