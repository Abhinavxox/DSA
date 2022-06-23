package Binary_tree;
import java.util.Scanner;

public class QN1{
    
    static Node root;
    static class Node {
        String value;
        Node left;
        Node right;
    
        Node(String value) {
            this.value = value;
            right = null;
            left = null;
        }
    }


public static void main(String[] args) {

    creation_bianry();
    System.out.print("Inorder Traversal : ");
    inorder(root);
    System.out.println(" ");
    System.out.println(root.value);
    System.out.print("Preorder Traversal : ");
    preorder(root);
    System.out.println(" ");
    System.out.print("Postorder Traversal : ");
    postorder(root);
    System.out.println(" ");

}
 static Node creation_bianry(){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter value :  ");
    String d = sc.next();
    Node temp = new Node(d);
    if(d.equals("-1")){
        return null;
    }
    System.out.print("In left ");
    temp.left=creation_bianry();
    System.out.print("In right ");
    temp.right=creation_bianry();
    root = temp;
    return root;
 }


 static void preorder(Node root){
    if(root==null)
    {
        return;
    }
    else{    
        System.out.print(root.value +" "); 
        preorder(root.left);
        preorder(root.right);
    }
}

static void postorder(Node root)
{
    if(root==null)
    {
        return;
    }
    else{
        postorder(root.left);
        postorder(root.right);
        System.out.print(root.value +" ");
    }
}

static  void inorder(Node root){
    if(root==null)
    {
        return;
    }
    else
    {
        inorder(root.left);
        System.out.print(root.value +" ");
        inorder(root.right);
       
    }}

}