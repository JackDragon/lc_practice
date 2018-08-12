def split_n_max(sentence, n):
    if n < 1:
        return []
    ret_list = []
    start_of_word = 0
    prev_word_len = None
    for i in range(len(sentence)):
        # print(sentence[i])
        if sentence[i] == " " or i == len(sentence) - 1:
            # print("Found space")
            if i - start_of_word > n - 1:
                return []
            else:
                if i < len(sentence) - 1:
                    cur_word = sentence[start_of_word:i]
                else:
                    cur_word = sentence[start_of_word:i + 1]

                print(prev_word_len)
                if prev_word_len and prev_word_len + i - start_of_word < n:
                    # we are adding to previous word
                    ret_list[-1] = ret_list[-1] + " " + cur_word
                    prev_word_len += i - start_of_word
                else:
                    # we add to new word
                    # print("Appending  ]

                    sentence[start_of_word:i + 1])
                    ret_list.append(cur_word)
                    prev_word_len = i - start_of_word + 1
                    start_of_word = i + 1
    return ret_list


print(split_n_max("Hi, I'm Jack", 4))
# > ["Hi,", "I'm", "Jack"]

print(split_n_max("Hi, I'm Jack Jack Nowhere Is Cooki", 8))

# def bad_transfer(src_account, dst_account, amount):
#     src_cash = src_account.cash # DB read
#     dst_cash = dst_account.cash # DB read
#     if src_cash < amount:
#         raise InsufficientFunds
#     src_account.cash = src_cash - amount # DB write
#     src_account.send_src_transfer_email()
#     dst_account.cash = dst_cash + amount # DB write
#     dst_account.send_dst_transfer_email()
d