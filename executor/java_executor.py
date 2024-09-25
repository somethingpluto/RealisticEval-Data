import re

JAVA_RUN_ENV = "../envs/java/src"


class JavaExecutor:
    def __init__(self, model_name):
        self._env_path = JAVA_RUN_ENV
        self.model_name = model_name

    def single_run(self, code: str, test_code: str):
        #
        with open(f"{JAVA_RUN_ENV}/main/java/org/real/temp/Temp.java", "w", encoding="utf8") as code_file:
            code_file.write("package org.real.temp;\n")
            cleared_code, is_class = self._clear_code(code)
            if not is_class:
                code_file.write("public class Temp {")
                code_file.write(cleared_code)
                code_file.write("}")
            else:
                code_file.write(cleared_code)
            code_file.flush()
        # 写入test文件
        with open("../envs/java/src/test/java/org/rel/temp/TestTemp.java", "w", encoding="utf8") as test_code_file:
            pass

    def _clear_code(self, code):
        code_arr = code.split("\n")
        cleared_code_arr = []
        is_class = False
        for line in code_arr:
            if line.startswith("package"):
                continue
            if line.startswith("public class"):
                line = re.sub(r'public class \w+', 'public class Temp', line)
                is_class = True
            cleared_code_arr.append(line)
        cleared_code = "\n".join(cleared_code_arr)
        return cleared_code, is_class

    def _clear_test_code(self, test_code) -> str:
        test_code_arr = test_code.split("\n")
        cleared_code_arr = []
        for line in test_code_arr:
            if line.startswith("package"):
                line = "package org.rel.temp;"
        return ""


if __name__ == '__main__':
    code = """import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * Given a set of points and a query point, this class finds the K nearest neighbors to the query point.
 * The algorithm efficiently handles large datasets, and the output includes the coordinates of these neighbors.
 */
public class KNearestNeighbors {

    public static class Point {
        public double x;
        public double y;

        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }

        public double distance(Point other) {
            return Math.sqrt(Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));
        }
    }

    /**
     * Find the K nearest neighbors to the query point.
     *
     * @param points Array of points from which to find the nearest neighbors.
     * @param queryPoint The point to which the nearest neighbors are found.
     * @param k The number of nearest neighbors to find.
     * @return An array containing the k nearest neighbors.
     */
    public static Point[] findKNearestNeighbors(Point[] points, Point queryPoint, int k) {
        // Priority queue to maintain the k nearest points
        PriorityQueue<Point> maxHeap = new PriorityQueue<>(k, new Comparator<Point>() {
            @Override
            public int compare(Point p1, Point p2) {
                // Compare distances to the query point
                double dist1 = p1.distance(queryPoint);
                double dist2 = p2.distance(queryPoint);
                return Double.compare(dist2, dist1); // max-heap based on distance
            }
        });

        for (Point point : points) {
            maxHeap.offer(point);
            if (maxHeap.size() > k) {
                maxHeap.poll(); // Remove the farthest point if we exceed k
            }
        }

        // Collect the k nearest neighbors into an array
        Point[] nearestNeighbors = new Point[k];
        for (int i = k - 1; i >= 0; i--) {
            nearestNeighbors[i] = maxHeap.poll();
        }

        return nearestNeighbors;
    }

    public static void main(String[] args) {
        Point[] points = {
            new Point(1, 2),
            new Point(2, 3),
            new Point(3, 1),
            new Point(5, 4),
            new Point(2, 1)
        };
        Point queryPoint = new Point(2, 2);
        int k = 3;

        Point[] nearestNeighbors = findKNearestNeighbors(points, queryPoint, k);
        for (Point neighbor : nearestNeighbors) {
            System.out.println("Neighbor: (" + neighbor.x + ", " + neighbor.y + ")");
        }
    }
}
"""
    java_executor = JavaExecutor(model_name="test")
    java_executor.single_run(code, "")
