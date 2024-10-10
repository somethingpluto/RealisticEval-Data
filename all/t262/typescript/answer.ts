interface TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
}

function averageOfLevels(root: TreeNode | null): number[] {
  if (!root) return [];

  let queue: TreeNode[] = [root];
  let result: number[] = [];

  while(queue.length > 0){
    let sum: number = 0;
    let count: number = queue.length;

    for(let i = 0; i < count; i++){
      let node: TreeNode = queue.shift()!;
      sum += node.val;

      if(node.left) queue.push(node.left);
      if(node.right) queue.push(node.right);
    }

    result.push(sum / count);
  }

  return result;
}