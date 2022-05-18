import json
import pandas as pd
from tabulate import tabulate

cols = ["Age",
        "Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10",
        "Q11", "Q12", "Q13", "Q14", "Q15", "Q16", "Q17", "Q18", "Q19", "Q20",
        "Q21", "Q22", "Q23", "Q24", "Q25", "Q26", "Q27", "Q28", "Q29", "Q30",
        "Q31", "Q32", "Q33", "Q34",
        "Gender", "ID", "Student", "AnsSE", "AnsIA", "AnsHAPPY"]


def create_df(filename="part_of_data.json"):
    df = pd.DataFrame()
    for column in cols:
        df[column] = ""

    f = open(filename, "r")
    data = json.loads(f.read())
    print()
    for i in data:
        temp_list = []

        temp_list.append(data[i][" respondent"]["Age"].strip())
        iter_data = iter(data[i][" respondent"]["Answers1"])
        for j in iter_data:
            temp_list.append(j)
        temp_list.append(data[i][" respondent"]["Gender"].strip())
        temp_list.append(data[i][" respondent"]["ID"])
        temp_list.append(data[i][" respondent"]["Student"])

        temp_list.append(data[i][" samoocena"]["AnsSE"])
        temp_list.append(data[i][" uzaleznienie"]["AnsIA"])
        temp_list.append(data[i][" zadowolenie"]["AnsHAPPY"])

        del(temp_list[1])
        df.loc[len(df)] = temp_list
    return df


def clear_data():
    df = create_df()
    df = df[(df.AnsIA <= 135) & (df.AnsIA >= 30)]
    df = df[(df.AnsSE <= 39) & (df.AnsSE >= 11)]
    df = df[(df.AnsHAPPY <= 15) & (df.AnsHAPPY >= 5)]
    df = df.loc[~((df["Age"] == "0-15") & (df["Student"] == False)), :]
    addicted = 0
    semi_addicted = 0
    not_addicted = 0

    confident = 0
    semi_confident = 0
    not_confident = 0

    happy = 0
    semi_happy = 0
    not_happy = 0

    for x in df['AnsIA'].tolist():  # Uzaleznienie
        if x >= 97:
            addicted += 1
        elif 97 > x >= 64:
            semi_addicted += 1
        else:
            not_addicted += 1

    for x in df['AnsSE'].tolist():  # pewnosc siebie
        if x >= 25:
            confident += 1
        elif 25 > x >= 18:
            semi_confident += 1
        else:
            not_confident += 1

    for x in df['AnsHAPPY'].tolist():  # zadowolenie
        if x >= 11:
            happy += 1
        elif 11 > x >= 8:
            semi_happy += 1
        else:
            not_happy += 1

    num_of_rows = len(df)
    add = round((addicted / num_of_rows * 100), 2)
    sadd = round((semi_addicted / num_of_rows * 100), 2)
    nadd = round((not_addicted / num_of_rows * 100), 2)
    conf = round((confident / num_of_rows * 100), 2)
    sconf = round((semi_confident / num_of_rows * 100), 2)
    nconf = round((not_confident / num_of_rows * 100), 2)
    hpy = round((happy / num_of_rows * 100), 2)
    shpy = round((semi_happy / num_of_rows * 100), 2)
    nhpy = round((not_happy / num_of_rows * 100), 2)
    answers = [["addicted", addicted, add],
               ["semi addicted", semi_addicted, sadd],
               ["not addicted", not_addicted, nadd],
               ["confident", confident, conf],
               ["semi confident", semi_confident, sconf],
               ["not confident", not_confident, nconf],
               ["happy", happy, hpy],
               ["semi happy", semi_happy, shpy],
               ["not happy", not_happy, nhpy]]
    print(tabulate(answers, headers=["Classification", "Number of answers", "% of group"]))
    print()

    return df


def scores():
    df = clear_data()
    desc_df = df.describe()
    count = desc_df.iloc[0].values
    top = desc_df.iloc[2].values
    freq = desc_df.iloc[3].values
    answers = []
    for i in range(len(freq)):
        x = round((freq[i]/count[i]*100), 2)
        temp_ans = [cols[i], f"{x}%", top[i]]
        answers.append(temp_ans)
    del(answers[-5])
    print(tabulate(answers, headers=["Question", "% of answers", "Top answer"]))
    print()

    data = [
           ["Happy + Confident + Addicted", len(df[(df.AnsHAPPY >= 11) & (df.AnsSE >= 25) & (df.AnsIA >= 97)])],
           ["Happy + Confident + !Addicted", len(df[(df.AnsHAPPY >= 11) & (df.AnsSE >= 25) & (df.AnsIA <= 64)])],
           ["Happy + Addicted", len(df[(df.AnsHAPPY >= 11) & (df.AnsIA >= 97)])],
           ["!Happy + Addicted", len(df[(df.AnsHAPPY <= 8) & (df.AnsIA >= 97)])],
           ["Confident + Addicted", len(df[(df.AnsSE >= 25) & (df.AnsIA >= 97)])],
           ["!Confident + Addicted", len(df[(df.AnsSE <= 18) & (df.AnsIA <= 64)])],
    ]
    print(tabulate(data, headers=["Dependency", "Count"]))
    print()



def mfa():  # most frequent answers
    df = clear_data()
    list_of_answers = []

    for col in df.columns:
        if col == "ID":
            continue
        top_values = df[col].mode()
        list_of_answers.append(top_values)
    for i in range(len(list_of_answers)):
        list_of_answers[i] = str(list_of_answers[i])
        list_of_answers[i] = list_of_answers[i][:-14]
        list_of_answers[i] = list_of_answers[i].split("\n")
        for j in range(len(list_of_answers[i])):
            list_of_answers[i][j] = list_of_answers[i][j][1:].strip()

    print(list_of_answers)
    return list_of_answers


if __name__ == "__main__":
    scores()
    # mfa()
