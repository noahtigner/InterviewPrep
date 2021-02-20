// Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth 
// (e.g., if you have a tree with depth D, you'll have D linked lists)

import java.util.ArrayList;

// Binary Tree
class TreeNode {
	TreeNode left;
	TreeNode right;
	int data;

	public TreeNode(int data) {
		this.left = null;
		this.right = null;
		this.data = data;
	}
}

// For linked lists of data at each depth
class DepthNode {
	DepthNode next;
	int data;

	public DepthNode(int data) {
		this.data = data;
		this.next = null;
	}
}

class QueueNode {
	QueueNode next;
	TreeNode treeNode;

	public QueueNode(TreeNode treeNode) {
		this.treeNode = treeNode;
		this.next = null;
	}
}

class Queue {
	QueueNode first;
	QueueNode last;

	public Queue() {
		this.first = null;
		this.last = null;
	}

	public void enqueue(TreeNode treeNode) {
		QueueNode node = new QueueNode(treeNode);
		if (this.first == null) {
			this.first = node;
		}
		if (this.last != null) {
			this.last.next = node;
		}
		this.last = node;
	}

	public TreeNode dequeue() {
		if (this.first == null) {
			return null;
		}
		TreeNode node = this.first.treeNode;
		this.first = this.first.next;
		return node;
	}

	public boolean isEmpty() {
		return this.first == null;
	}

	public int length() {
		if (this.isEmpty()) {
			return 0;
		}
		int count = 0;
		QueueNode node = this.first;
		while (node != null) {
			count++;
			node = node.next;
		}
		return count;
	}
}

class Main {

    // time: O(n), space: O(n)
	public static ArrayList<DepthNode> listOfDepths(TreeNode root) {
		ArrayList<DepthNode> depthsList = new ArrayList<DepthNode>();
		int i = 0; // tree level
		int levelSize = 0; // nodes in tree level

		// Level Order Traversal (BFS)
		Queue queue = new Queue();
		queue.enqueue(root);
		while (!queue.isEmpty()) {
			levelSize = queue.length();
			while (levelSize > 0) {
				TreeNode tnode = queue.dequeue();
				DepthNode dnode = new DepthNode(tnode.data);

				if (depthsList.size() == i) {
					depthsList.add(dnode);
				}
				else {
					DepthNode temp = depthsList.get(i);
					while (temp.next != null) {
						temp = temp.next;
					}
					temp.next = dnode;
				}

				if (tnode.left != null) {
					queue.enqueue(tnode.left);
				}
				if (tnode.right != null) {
					queue.enqueue(tnode.right);
				}
				levelSize--;
			}
			i++;
		}
		return depthsList;
	}

    public static void main(String[] args) {
        TreeNode root = new TreeNode(5);
		root.left = new TreeNode(3);
		root.right = new TreeNode(7);
		root.left.left = new TreeNode(2);
		root.left.right = new TreeNode(4);
		root.right.left = new TreeNode(6);
		root.right.right = new TreeNode(8);

		ArrayList<DepthNode> depthList = listOfDepths(root);
		for(int i = 0; i < depthList.size(); i++) {
			DepthNode node = depthList.get(i);
			while (node != null) {
				System.out.print(node.data + ", ");
				node = node.next;
			}
			System.out.println("");
		}
    }
}