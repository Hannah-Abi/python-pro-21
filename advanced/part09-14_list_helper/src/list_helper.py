# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        frequence_no = {}
        for item in my_list:
            if item not in frequence_no:
                frequence_no[item] = 1
            else:
                frequence_no[item] += 1
        most_common = my_list[0]
        most_frequence = 1
        for k, v in frequence_no.items():
            if v >= most_frequence:
                most_frequence = v
                most_common = k
        return most_common

    @classmethod
    def doubles(cls, my_list: list):
        frequence_no = {}
        for item in my_list:
            if item not in frequence_no:
                frequence_no[item] = 1
            else:
                frequence_no[item] += 1
        count = 0
        for v in frequence_no.values():
            if v >= 2:
                count += 1
        return count
if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
    print(ListHelper.greatest_frequency([1,1,2]))