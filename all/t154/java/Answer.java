import java.util.ArrayList;
import java.util.List;

class GitDiffChange {
    private String diff;
    private String code;

    public GitDiffChange(String diff, String code) {
        this.diff = diff;
        this.code = code;
    }

    // Getters and setters (or use Lombok for brevity)
    public String getDiff() {
        return diff;
    }

    public void setDiff(String diff) {
        this.diff = diff;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
}

class GitDiffFile {
    private String oldPath;
    private String newPath;
    private List<GitDiffChange> changes;
    private String newFileMode;
    private String deletedFileMode;
    private String index;

    public GitDiffFile(String oldPath, String newPath) {
        this.oldPath = oldPath;
        this.newPath = newPath;
        this.changes = new ArrayList<>();
        this.newFileMode = null;
        this.deletedFileMode = null;
        this.index = null;
    }

    // Getters and setters (or use Lombok for brevity)
    public String getOldPath() {
        return oldPath;
    }

    public String getNewPath() {
        return newPath;
    }

    public List<GitDiffChange> getChanges() {
        return changes;
    }

    public String getNewFileMode() {
        return newFileMode;
    }

    public void setNewFileMode(String newFileMode) {
        this.newFileMode = newFileMode;
    }

    public String getDeletedFileMode() {
        return deletedFileMode;
    }

    public void setDeletedFileMode(String deletedFileMode) {
        this.deletedFileMode = deletedFileMode;
    }

    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }
}

public class GitDiffParser {

    /**
     * Parses a string containing the contents of a Git diff and returns a list of objects with details of each file's changes.
     *
     * @param diffText The Git diff text to parse.
     * @return A list of objects representing the diff for each file.
     */
    public static List<GitDiffFile> parseGitDiff(String diffText) {
        String[] diffLines = diffText.split("\n");
        List<GitDiffFile> fileDiffs = new ArrayList<>();
        GitDiffFile currentFile = null;

        for (String line : diffLines) {
            if (line.startsWith("diff --git a/")) {
                // When a new file diff starts, push the current file diff to the list
                if (currentFile != null) {
                    fileDiffs.add(currentFile);
                }

                // Extract the old and new paths from the diff line
                String[] paths = line.split(" ");
                String oldPath = paths[2].substring(2); // Removing 'a/'
                String newPath = paths[3].substring(2); // Removing 'b/'

                currentFile = new GitDiffFile(oldPath, newPath);
            } else if (line.startsWith("new file mode")) {
                if (currentFile != null) {
                    currentFile.setNewFileMode(line.split(" ")[3]);
                }
            } else if (line.startsWith("deleted file mode")) {
                if (currentFile != null) {
                    currentFile.setDeletedFileMode(line.split(" ")[3]);
                }
            } else if (line.startsWith("index")) {
                if (currentFile != null) {
                    currentFile.setIndex(line.split(" ")[1]);
                }
            } else if (line.startsWith("@@")) {
                // Start of a hunk; add it to the changes list
                if (currentFile != null) {
                    currentFile.getChanges().add(new GitDiffChange(line, null));
                }
            } else if (currentFile != null && (line.startsWith("+") || line.startsWith("-") || line.startsWith(" "))) {
                // Line additions, deletions, or context
                currentFile.getChanges().add(new GitDiffChange(null, line));
            }
        }

        // Push the last file diff after the loop ends
        if (currentFile != null) {
            fileDiffs.add(currentFile);
        }

        return fileDiffs;
    }
}