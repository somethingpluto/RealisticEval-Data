def format_post_count(count: int) -> str:
    """
    Formats the post count into a human-readable string.

    :param count: The number of posts.
    :return: A formatted string indicating the number of posts.
    """
    if count == 0:
        return "No Posts"
    else:
        post_count = str(count).zfill(2)  # Ensure at least two digits
        post_word = "Post" if count == 1 else "Posts"  # Singular or plural
        return f"{post_count} {post_word}"  # Correctly formatted string
