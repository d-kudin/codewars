def generate_hashtag(s):
    list1 = s.title().strip().split()
    final_s = f"#{''.join(list1)}"
    if len(final_s) > 140 or len(s) == 0 or len(final_s) == 0:
        return False
    else:
        return final_s
​