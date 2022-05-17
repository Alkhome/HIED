import json
import pandas as pd

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
    #TODO decide on the values
    # df = df[(df.AnsSE < 40) & (df.AnsSE > 10)]
    # df = df[(df.AnsIA < 40) & (df.AnsIA > 10)]
    # df = df[(df.AnsHAPPY < 40) & (df.AnsHAPPY > 10)]
    # #TODO add condition that deletes if student and age 0-15
    #print(df)
    return df

def mfa():  # most frequent answer
    df = clear_data()
    # list_of_answers = []
    # for column in cols:
    #     if column == "ID":
    #         continue
    #     list_of_answers.append(df[column].mode())
    # print(list_of_answers)
    list_of_answers = []

    for col in df.columns:
        if col == "ID":
            continue
        top_values = df[col].mode()
        list_of_answers.append(top_values)
    #pd.concat(list_of_answers, axis=1)
    #print(list_of_answers)
    for i in range(len(list_of_answers)):
        list_of_answers[i] = str(list_of_answers[i])
        list_of_answers[i] = list_of_answers[i][:-14]
        list_of_answers[i] = list_of_answers[i].split("\n")
        for j in range(len(list_of_answers[i])):
            list_of_answers[i][j] = list_of_answers[i][j][1:].strip()

    print(list_of_answers)
    return list_of_answers

def show_data():
    raise NotImplementedError


if __name__ == "__main__":
    #clear_data()
    mfa()
    pass
