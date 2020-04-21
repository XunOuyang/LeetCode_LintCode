class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        """
        if not preorder:
            return None
        preorder.sort()
        i = len(preorder)//2
        root.left = self.bstFromPreorder(preorder[:i])
        root.right = self.bstFromPreorder(preorder[i+1:])
        return root             
        """
        
        
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = bisect.bisect(preorder, preorder[0])
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
      
