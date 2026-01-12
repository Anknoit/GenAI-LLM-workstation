char_list = [
    "adaw3r233t4w634gwgw",
    "rfewftf3243f",
    "ewf325r32tfgv2ewgf",
    "tfgew",
    "gwegwe32432",
]

common_list = []
alpha_list = []
num_list = []


def string_classifier(char_list):
    for i in char_list:
        print(i, len(i))
        print(i.isalnum())
        if i.isalnum():
            for j in i:
                if j.isalpha():
                    alpha_list.append(j)
                elif j.isnumeric():
                    num_list.append(j)
    print(num_list)
    print(alpha_list)

    # print(common_list, len(common_list))


string_classifier(char_list)
