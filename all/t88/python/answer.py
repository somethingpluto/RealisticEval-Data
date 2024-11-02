def is_cron_between_2_and_4_am(cron_expression):
    parts = cron_expression.split(' ')
    hour_part = parts[1]

    # 检查小时部分
    hours = set()

    for part in hour_part.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            hours.update(range(start, end + 1))
        elif part == '*':
            return False  # 通配符，表示每个小时
        else:
            hours.add(int(part))

    # 只检查是否包含 2 或 3
    return 2 in hours or 3 in hours