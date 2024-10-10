// Define the TreeNode class
function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

// Define the averageOfLevels function
var averageOfLevels = function(root) {
  if (!root) return [];

  let queue = [root];
  let result = [];

  while(queue.length > 0){
    let sum = 0;
    let count = queue.length;

    for(let i=0; i<count; i++){
      let current = queue.shift();
      sum += current.val;

      if(current.left) queue.push(current.left);
      if(current.right) queue.push(current.right);
    }

    result.push(sum/count);
  }

  return result;
};