g_flag = True
print("関数実行前フラグ: " + str({g_flag}))


def func(flag):
    global g_flag
    print("現在のフラグ: " + str({g_flag}))
    print("フラグ反転！")
    g_flag = not flag
    print("現在のフラグ: " + str({g_flag}))


func(g_flag)
print("関数実行後フラグ: " + str({g_flag}))
