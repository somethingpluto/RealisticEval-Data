from music21 import pitch


def adjust_to_c_major(note_name):
    c_major_scale = ["C", "D", "E", "F", "G", "A", "B"]

    # 检查 note_name 是否有效
    try:
        given_pitch = pitch.Pitch(note_name)
    except pitch.PitchException:
        # 如果无效，则返回默认音符
        return "C4"

    if given_pitch.name in c_major_scale:
        return note_name

    # 检查最近有效音符
    for direction in (1, -1):
        adjusted_pitch = given_pitch.transpose(direction)
        if adjusted_pitch.name in c_major_scale:
            return adjusted_pitch.nameWithOctave

    return note_name  # 可选，处理错误或提供默认音符 "C4"


# 示例调整一个音符
note = "F#4"
adjusted_note = adjust_to_c_major(note)
print(f"调整后的音符 {note} 是 {adjusted_note}")
