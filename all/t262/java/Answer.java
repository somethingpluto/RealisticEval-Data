package org.real.temp;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Answer {

    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static List<Double> averageOfLevels(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }

        List<Double> result = new ArrayList<>();
        Queue<Pair<TreeNode, Integer>> queue = new LinkedList<>();
        queue.offer(new Pair<>(root, 0));

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            double currentLevelSum = 0;
            int currentLevelCount = 0;

            for (int i = 0; i < levelSize; i++) {
                Pair<TreeNode, Integer> pair = queue.poll();
                TreeNode node = pair.getKey();
                int level = pair.getValue();

                currentLevelSum += node.val;
                currentLevelCount++;

                if (node.left != null) {
                    queue.offer(new Pair<>(node.left, level + 1));
                }
                if (node.right != null) {
                    queue.offer(new Pair<>(node.right, level + 1));
                }
            }

            // Calculate the average for the current level
            double levelAverage = currentLevelSum / currentLevelCount;
            result.add(levelAverage);
        }

        return result;
    }

    public static void main(String[] args) {
        // Example usage
        TreeNode root = new TreeNode(3,
                new TreeNode(9),
                new TreeNode(20, new TreeNode(15), new TreeNode(7)));
        List<Double> averages = averageOfLevels(root);
        System.out.println(averages);
    }
}

// Utility class to hold pairs of TreeNode and Integer
class Pair<K, V> {
    private K key;
    private V value;

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public K getKey() {
        return key;
    }

    public V getValue() {
        return value;
    }
}