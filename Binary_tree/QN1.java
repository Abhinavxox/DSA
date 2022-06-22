package Binary_tree;

import java.util.Scanner;

public class QN1 {
	//create a binary tree
	
	public static void main(String[] args) {
		createTree();
		System.out.println("The preorder is: ");
		preorder(root);
	}
	
    static class Node {
        int value;
        Node left;
        Node right;
    
        Node(int value) {
            this.value = value;
            right = null;
            left = null;
        }
    }

    
    static Scanner sc = new Scanner(System.in);
//    static Node mainroot;
    static Node root ;
//    static int counter = 0;
        static Node createTree() {
            System.out.println("Enter the data");
            System.out.println("**Enter -1 if you want to go back or end");
            int data = sc.nextInt();
            
            if(data==-1) {
                return root;
            }
            
            root = new Node(data);
//            if(counter==0) {
//             mainroot = root;
//            }
//            counter++;
            System.out.println("Where do you want its child left or right or up?(0 or 1 or -1)");
            int pointer = sc.nextInt();

            String flag = "";
            if(pointer==0) {
                flag = "left";
                root.left = createTree();
            }
            else if(pointer==1) {
                flag = "right";
                root.right = createTree();
            }
            else if(pointer==-1) {
            	return root;
            }

            if(root.left==null || root.right==null){
                if(flag.equals("left")){
                    System.out.println("Where do you want its child right or up?(0 or 1)");
                    int pointer1 = sc.nextInt();
                    if(pointer1==0){
                        root.right = createTree();
                    }
                    else{
                        return root;
                    }
                }
                else{
                    System.out.println("Where do you want its child left or up?(0 or 1)");
                    int pointer2 = sc.nextInt();
                    if(pointer2==0){
                        root.left = createTree();
                    }
                    else{
                        return root;
                    }
                }
            }
            return root;
    }
	
		public static void preorder(Node root) {
		    if(root !=  null) {
		   //Visit the node by Printing the node data  
		      System.out.printf("%d ",root.value);
		      preorder(root.left);
		      preorder(root.right);
		    }
		  }
	

}
