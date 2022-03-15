my_list = [
    'a', 'a', 1, 2, 3, 'b', 'b',
    'a', 5, 'a', 6, 'd', 'd'
]

print(
    max(
        set(
            my_list
        ),
        key=my_list.count
    )
)
