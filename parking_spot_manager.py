class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    def __init__(self, name, city, district, ptype, longitude, latitude):
        """ 생성자 초기 값을 입력
        Args:
            name : 자원명 문자열 값
            city : 시도 문자열 값
            district : 시군구 문자열 값
            ptype : 주차장유형 문자열 값
            longitude : 경도 실수 값
            latitude : 위도 실수 값
        """
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
        """ __item[keyword] 값을 반환하기 위한 함수 """
        return self.__item[keyword]


# version#2
def str_list_to_class_list(str_list):
    """ parking_spot 클래스 객체의 리스트로 변환 후 반환 """
    list = []  # 객체 리스트 선언
    for i in str_list:
        temp = i.split(',')  # 각 데이터는 쉼표(,)로 구분되어 있다고 했으므로, ','를 기준으로 split해서 parsing한다.
        list.append(parking_spot(temp[1], temp[2], temp[3], temp[4], temp[5], temp[6]))
        # 문자열의 첫 번째는 [순번]이기 때문에 순번인 temp[0]를 제외하고 temp[1]부터 list에 넣기 시작한다.
    return list  # 객체 리스트 반환


def print_spots(spots):  # spots을 매개변수로 받는다.
    print(f"---print elements({len(spots)})---")  # 총 spots의 개수를 출력하고
    for spot in spots: print(spot)  # 각 spot의 세부 정보에 대해 출력한다.
    return


# version#3

# 각각 name, city, district, ptype, locations을 기준으로 데이터를 분석하여 추려내는 함수
def filter_by_name(spots, name):
    """
    parking_spot 클래스 객체의 리스트(spots)와 키워드를 매개변수로 받아, 리스트함축 기능을 사용하여 데이터를 필터링한 후 생성된 새로운 리스트 반환
    리스트 함축 기능을 사용하기 위해 [i for ~~]과 같은 구문을 구성하였고 그 값을 바로 리턴할 수 있도록 구성
    name 뿐만 아니라 city, district, ptype의 경우도 동일.
    """
    return [i for i in spots if name in i.get('name')]


def filter_by_city(spots, city):
    return [i for i in spots if city in i.get('city')]


def filter_by_district(spots, district):
    return [i for i in spots if district in i.get('district')]


def filter_by_ptype(spots, ptype):
    return [i for i in spots if ptype in i.get('ptype')]


def filter_by_location(spots, locations):
    # 위치정보에 대한 튜플인 location은 순서대로 min_lat, max_lat, min_long, max_long을 포함
    min_lat, max_lat, min_long, max_long = locations
    """
       위의 함수들과 차이가 있다면 튜플의 값과 클래스 객체의 리스트 값을 비교하여 리스트 함축을 진행한다는 것이다.
    """
    return [i for i in spots if min_lat < i.get('latitude') < max_lat and min_long < i.get('longitude') < max_long]


# version#4
def sort_by_keyword(spots, keyword):
    """
        spots과 keyword를 매개변수를 받아 정렬을 수행.
        정렬기준의 자료형은 문자열이며, parking_spot 객체가 저장하고 잇는 딕셔너리의 key값과 동일한 목록을 지원

        내장함수 sorted를 이용했으며, 추가적으로 sorted의 비교기준을 정하는 key 매개변수의 인수는 lambda 함수를 이용해 구현.
    """
    return sorted(spots, key=lambda i: i.get(keyword))


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
