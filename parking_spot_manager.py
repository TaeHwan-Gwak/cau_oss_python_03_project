class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    def __init__(self, name, city, district, ptype, longitude, latitude):
        """ 생성자 초기 값을 입력 """
        self.__item = {
            'name': name,  # 문자열
            'city': city,  # 문자열
            'district': district,  # 문자열
            'ptype': ptype,  # 문자열
            'longitude': float(longitude),  # 실수
            'latitude': float(latitude),  # 실수
        }

    def __str__(self):
        item = self.__item
        s = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

    def get(self, keyword='name'):  # 기본 인수는 'name' 으로 지정.
        return self.__item[keyword]


def str_list_to_class_list(str_list):
    """ parking_spot 클래스 객체의 리스트로 변환 후 반환 """
    list = []  # 객체 리스트 선언
    for i in str_list:
        temp = i.split(',')  # 각 데이터는 쉼표(,)로 구분되어 있다고 했으므로, ','를 기준으로 split해서 parsing한다.
        list.append(parking_spot(temp[1], temp[2], temp[3], temp[4], temp[5], temp[6]))
    return list  # 객체 리스트 반환


def print_spots(spots):  # spots을 매개변수로 받는다.
    print(f"---print elements({len(spots)})---")  # 총 spots의 개수를 출력하고
    for spot in spots: print(spot)  # 각 spot의 세부 정보에 대해 출력한다.
    return


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)

    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)
