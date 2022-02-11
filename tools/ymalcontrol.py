import yaml


def get_yaml_data(filedir):
    with open(filedir, "r") as f:
        fo = yaml.load(f, Loader=yaml.FullLoader)
        cases = []
        for one in fo:
            cases.append([one["data"], one["resq"]])
        return cases


if __name__ == '__main__':
    logincases = get_yaml_data("../data/logincase.yaml")
    print(logincases)