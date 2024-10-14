def format_post_count(count: int) -> str:
    """
    Formats the post count into a human-readable string.

    The function formats the number of posts into a two-digit string
    followed by "Post" or "Posts" based on the count.

    For example:
        - Input: 3  Output: "02 Posts"
        - Input: 1  Output: "01 Post"

    Args:
        count (int): The number of posts.

    Returns:
        str: A formatted string indicating the number of posts.
             The string will be in the format "XX Post" or "XX Posts",
             where XX is the count formatted as a two-digit number.
    """