def wrap_text(x, y):
    return str(y + x + y)


# result = wrap_text(
#     wrap_text(
#         wrap_text(
#             'new message', 
#             '###'
#         ),
#         "==="
#     ),
#     "---"
# )

pounds = wrap_text('new message', "###")
equals = wrap_text(pounds, "===")
hyphens = wrap_text(equals, "---")
result = hyphens

print(result)